"""Integration tests for the full research workflow using FastAPI TestClient."""

import io
import pytest
from unittest.mock import patch, MagicMock

from fastapi.testclient import TestClient

from app.main import app
from app.routers.projects import _projects
from app.routers.workflow import _workflow_states, _engine


@pytest.fixture(autouse=True)
def clear_state():
    """Clear in-memory state before each test."""
    _projects.clear()
    _workflow_states.clear()
    yield
    _projects.clear()
    _workflow_states.clear()


@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)


@pytest.fixture
def mock_ai():
    """Mock AI service on the existing engine instance to avoid external API calls."""
    mock_service = MagicMock()
    mock_service.analyze_problem.return_value = (
        "Problema identificado: Alta rotacion de personal en la empresa "
        "debido a falta de incentivos y clima laboral inadecuado."
    )
    mock_service.suggest_instruments.return_value = (
        "1. Encuesta de satisfaccion laboral\n"
        "2. Entrevista con empleados actuales y antiguos\n"
        "3. Revision de indicadores de RRHH"
    )
    mock_service.refine_problem.return_value = (
        "1. La ausencia de programas de incentivos genera alta rotacion de personal.\n"
        "2. El clima laboral inadecuado provoca insatisfaccion y desercion laboral.\n"
        "3. La falta de desarrollo profesional limita la retencion del talento humano."
    )
    mock_service.generate_research_questions.return_value = (
        "Pregunta principal: Como influye la falta de incentivos laborales "
        "en la rotacion de personal en empresas medianas?"
    )
    mock_service.validate_coherence.return_value = (
        "COHERENTE: Los datos presentados son consistentes y logicamente articulados."
    )
    mock_service.generate_chapter.return_value = (
        "Capitulo generado con formato APA 7. El contenido sigue la estructura "
        "metodologica establecida en las fases anteriores."
    )

    # Patch the ai_service on the module-level engine instance
    original_ai_service = _engine.ai_service
    _engine.ai_service = mock_service
    yield mock_service
    _engine.ai_service = original_ai_service


class TestHealthEndpoint:
    """Test health check endpoint."""

    def test_health_returns_200(self, client):
        """Health endpoint should return healthy status."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"


class TestFullWorkflow:
    """Integration tests for the complete research workflow."""

    def test_create_project(self, client):
        """Test creating a new research project."""
        response = client.post("/projects/", json={"title": "Investigacion sobre rotacion laboral"})
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Investigacion sobre rotacion laboral"
        assert "id" in data

    def test_full_workflow_create_and_submit(self, client, mock_ai):
        """Test the full workflow: create project -> submit input -> get analysis."""
        # Step 1: Create project
        response = client.post("/projects/", json={"title": "Test Research"})
        assert response.status_code == 200
        project_id = response.json()["id"]

        # Step 2: Get workflow status (initializes workflow)
        response = client.get(f"/workflow/{project_id}/status")
        assert response.status_code == 200
        status = response.json()
        assert status["current_phase"] == "problem_identification"
        assert len(status["current_tasks"]) > 0

        # Step 3: Submit problem description
        response = client.post(
            f"/workflow/{project_id}/submit-input",
            json={
                "text": "En mi empresa hay una alta rotacion de personal. "
                "En los ultimos 6 meses se han ido 20 de 50 empleados."
            },
        )
        assert response.status_code == 200
        result = response.json()
        assert result["phase"] == "problem_identification"
        assert "result" in result
        assert "identified_problem" in result["result"]

    def test_workflow_advance_through_phases(self, client, mock_ai):
        """Test advancing through multiple workflow phases."""
        # Create project
        response = client.post("/projects/", json={"title": "Multi-phase Test"})
        project_id = response.json()["id"]

        # Initialize workflow
        client.get(f"/workflow/{project_id}/status")

        # Phase 1: Problem Identification
        client.post(
            f"/workflow/{project_id}/submit-input",
            json={"text": "Situacion problematica en la educacion rural"},
        )

        # Validate coherence
        response = client.post(f"/workflow/{project_id}/validate")
        assert response.status_code == 200
        assert response.json()["is_coherent"] is True

        # Advance to next phase
        response = client.post(f"/workflow/{project_id}/advance")
        assert response.status_code == 200
        assert response.json()["new_phase"] == "instrument_suggestion"

        # Phase 2: Instrument Suggestion
        client.post(
            f"/workflow/{project_id}/submit-input",
            json={"text": "Datos de encuestas recopilados"},
        )

        # Validate and advance
        client.post(f"/workflow/{project_id}/validate")
        response = client.post(f"/workflow/{project_id}/advance")
        assert response.status_code == 200
        assert response.json()["new_phase"] == "problem_refinement"

        # Phase 3: Problem Refinement
        client.post(
            f"/workflow/{project_id}/submit-input",
            json={"text": "Resultados de investigacion preliminar"},
        )

        # Validate and advance
        client.post(f"/workflow/{project_id}/validate")
        response = client.post(f"/workflow/{project_id}/advance")
        assert response.status_code == 200
        assert response.json()["new_phase"] == "research_question"

    def test_workflow_cannot_advance_without_validation(self, client, mock_ai):
        """Test that workflow cannot advance without coherence validation."""
        # Create project and submit first input
        response = client.post("/projects/", json={"title": "Validation Test"})
        project_id = response.json()["id"]
        client.get(f"/workflow/{project_id}/status")

        # Mock incoherent response for this test
        mock_ai.validate_coherence.return_value = "INCOHERENTE: Los datos no son consistentes."

        # Submit input
        client.post(
            f"/workflow/{project_id}/submit-input",
            json={"text": "Datos inconsistentes"},
        )

        # Try to advance - should fail because coherence not validated
        response = client.post(f"/workflow/{project_id}/advance")
        assert response.status_code == 400
        assert "coherence validation failed" in response.json()["detail"]

    def test_select_problem_formulation(self, client, mock_ai):
        """Test selecting a problem formulation in the refinement phase."""
        # Create project and get to refinement phase
        response = client.post("/projects/", json={"title": "Formulation Test"})
        project_id = response.json()["id"]
        client.get(f"/workflow/{project_id}/status")

        # Phase 1 - submit and advance
        client.post(
            f"/workflow/{project_id}/submit-input",
            json={"text": "Problema observado"},
        )
        client.post(f"/workflow/{project_id}/validate")
        client.post(f"/workflow/{project_id}/advance")

        # Phase 2 - submit and advance
        client.post(
            f"/workflow/{project_id}/submit-input",
            json={"text": "Datos adicionales"},
        )
        client.post(f"/workflow/{project_id}/validate")
        client.post(f"/workflow/{project_id}/advance")

        # Now in problem_refinement - submit data
        client.post(
            f"/workflow/{project_id}/submit-input",
            json={"text": "Resultados de campo"},
        )

        # Try to select an option (no refined problems stored yet, should get error)
        response = client.post(
            f"/workflow/{project_id}/select-option",
            json={"option_index": 0},
        )
        # Will return 400 because refined_problems list is empty in this mock
        assert response.status_code == 400


class TestFileUpload:
    """Tests for file upload functionality."""

    def test_upload_markdown_file(self, client):
        """Test uploading a markdown file to knowledge base."""
        content = b"# Test Research Paper\n\nThis is test content about methodology."
        response = client.post(
            "/knowledge/upload",
            files={"file": ("test_paper.md", content, "text/markdown")},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["filename"] == "test_paper.md"
        assert data["extracted_text_length"] > 0

    def test_upload_unsupported_file_type(self, client):
        """Test uploading an unsupported file type."""
        content = b"binary content"
        response = client.post(
            "/knowledge/upload",
            files={"file": ("test.pdf", content, "application/pdf")},
        )
        assert response.status_code == 400
        assert "Unsupported file type" in response.json()["detail"]

    def test_upload_text_file(self, client):
        """Test uploading a plain text file."""
        content = b"Contenido de investigacion sobre educacion en zonas rurales."
        response = client.post(
            "/knowledge/upload",
            files={"file": ("research.txt", content, "text/plain")},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["extracted_text_length"] > 0


class TestKnowledgeBase:
    """Tests for knowledge base search."""

    def test_search_knowledge_base(self, client):
        """Test searching the knowledge base."""
        response = client.get("/knowledge/search", params={"q": "metodologia"})
        assert response.status_code == 200
        data = response.json()
        assert "results" in data
        assert "query" in data
        assert data["query"] == "metodologia"

    def test_search_empty_query(self, client):
        """Test searching with an empty query."""
        response = client.get("/knowledge/search", params={"q": ""})
        assert response.status_code == 400

    def test_list_knowledge_documents(self, client):
        """Test listing all knowledge base documents."""
        response = client.get("/knowledge/documents")
        assert response.status_code == 200
        data = response.json()
        assert "documents" in data
        assert "total" in data


class TestDocumentGeneration:
    """Tests for document generation endpoint."""

    def test_generate_document(self, client):
        """Test generating an APA 7 document."""
        # First create a project
        response = client.post("/projects/", json={"title": "Document Test"})
        project_id = response.json()["id"]

        # Generate a document
        response = client.post(
            f"/documents/{project_id}/generate/introduccion",
            json={
                "content": "Este capitulo presenta la introduccion de la investigacion.",
                "author": "Investigador Test",
                "references": [
                    "Sampieri, R. (2014). Metodologia de la investigacion.",
                    "Vara-Horna, A. (2012). Siete pasos para una tesis.",
                ],
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert data["chapter"] == "introduccion"
        assert data["size_bytes"] > 0

    def test_download_generated_document(self, client):
        """Test downloading a generated document."""
        # Create project and generate document
        response = client.post("/projects/", json={"title": "Download Test"})
        project_id = response.json()["id"]

        client.post(
            f"/documents/{project_id}/generate/antecedentes",
            json={
                "content": "Capitulo de antecedentes de la investigacion.",
                "author": "Test Author",
            },
        )

        # Download the document
        response = client.get(f"/documents/{project_id}/download/antecedentes")
        assert response.status_code == 200
        assert "application/vnd.openxmlformats" in response.headers["content-type"]

    def test_download_nonexistent_document(self, client):
        """Test downloading a document that doesn't exist."""
        response = client.post("/projects/", json={"title": "No Doc Test"})
        project_id = response.json()["id"]

        response = client.get(f"/documents/{project_id}/download/capitulo_x")
        assert response.status_code == 404

    def test_generate_document_nonexistent_project(self, client):
        """Test generating a document for a non-existent project."""
        response = client.post(
            "/documents/nonexistent-id/generate/intro",
            json={"content": "test"},
        )
        assert response.status_code == 404

    def test_list_project_documents(self, client):
        """Test listing documents for a project."""
        # Create project and generate a document
        response = client.post("/projects/", json={"title": "List Test"})
        project_id = response.json()["id"]

        client.post(
            f"/documents/{project_id}/generate/marco_teorico",
            json={"content": "Marco teorico de la investigacion."},
        )

        response = client.get(f"/documents/{project_id}/list")
        assert response.status_code == 200
        data = response.json()
        assert len(data["documents"]) == 1
        assert data["documents"][0]["chapter"] == "marco_teorico"


class TestProjectsCRUD:
    """Integration tests for project CRUD operations."""

    def test_create_and_list_projects(self, client):
        """Test creating multiple projects and listing them."""
        client.post("/projects/", json={"title": "Project 1"})
        client.post("/projects/", json={"title": "Project 2"})

        response = client.get("/projects/")
        assert response.status_code == 200
        projects = response.json()
        assert len(projects) == 2

    def test_get_project_by_id(self, client):
        """Test getting a specific project."""
        response = client.post("/projects/", json={"title": "Single Project"})
        project_id = response.json()["id"]

        response = client.get(f"/projects/{project_id}")
        assert response.status_code == 200
        assert response.json()["title"] == "Single Project"

    def test_get_nonexistent_project(self, client):
        """Test getting a project that doesn't exist."""
        response = client.get("/projects/nonexistent-id")
        assert response.status_code == 404

    def test_update_project(self, client):
        """Test updating a project title."""
        response = client.post("/projects/", json={"title": "Original Title"})
        project_id = response.json()["id"]

        response = client.put(
            f"/projects/{project_id}", json={"title": "Updated Title"}
        )
        assert response.status_code == 200
        assert response.json()["title"] == "Updated Title"

    def test_delete_project(self, client):
        """Test deleting a project."""
        response = client.post("/projects/", json={"title": "To Delete"})
        project_id = response.json()["id"]

        response = client.delete(f"/projects/{project_id}")
        assert response.status_code == 200

        response = client.get(f"/projects/{project_id}")
        assert response.status_code == 404
