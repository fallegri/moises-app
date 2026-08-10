import { render, screen } from '@testing-library/react'
import { describe, it, expect } from 'vitest'
import App from '../App'

describe('App', () => {
  it('renders the home page with app title', () => {
    render(<App />)
    expect(screen.getByText('Asistente de Investigacion')).toBeInTheDocument()
  })

  it('renders the hero heading', () => {
    render(<App />)
    expect(screen.getByText('Asistente de Investigacion Cientifica')).toBeInTheDocument()
  })

  it('renders the new project button', () => {
    render(<App />)
    expect(screen.getByText('Nuevo Proyecto')).toBeInTheDocument()
  })

  it('renders feature cards', () => {
    render(<App />)
    expect(screen.getByText('Identificacion del Problema')).toBeInTheDocument()
    expect(screen.getByText('Guia Paso a Paso')).toBeInTheDocument()
    expect(screen.getByText('Documentos APA 7')).toBeInTheDocument()
  })
})
