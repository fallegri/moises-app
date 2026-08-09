<!-- Página 1 -->

# Joe Suzuki

# Statistical

# Learning

# with Math

# and Python

# 100 Exercises for Building Logic

---

<!-- Página 2 -->

# Statistical Learning with Math and Python

---

<!-- Página 3 -->

# Joe Suzuki

# Statistical Learning

# with Math and Python

# 100 Exercises for Building Logic

---

<!-- Página 4 -->

Joe Suzuki Graduate School of Eng Sci Osaka University Toyonaka, Osaka, Japan

ISBN 978-981-15-7876-2 ISBN 978-981-15-7877-9 (eBook) https://doi.org/10.1007/978-981-15-7877-9

© The Editor(s) (if applicable) and The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2021 This work is subject to copyright. All rights are solely and exclusively licensed by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed. The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use. The publisher, the authors, and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, expressed or implied, with respect to the material contained herein or for any errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This Springer imprint is published by the registered company Springer Nature Singapore Pte Ltd. The registered company address is: 152 Beach Road, #21-01/04 Gateway East, Singapore 189721, Singapore

---

<!-- Página 5 -->

# Preface

I am currently with the Statistics Laboratory at Osaka University, Japan. I often meet with data scientists who are engaged in machine learning and statistical analyses for research collaborations and introducing my students to them. I recently found out that almost all of them think that (mathematical) logic rather than knowledge and experience is the most crucial ability for grasping the essence in their jobs. Our necessary knowledge is changing every day and can be obtained when needed. However, logic allows us to examine whether each item on the Internet is correct and follow any changes; without it, we might miss even chances. In 2016, I started teaching statistical machine learning to the undergraduate students of the Mathematics Department. In the beginning, I was mainly teaching them what (statistical) machine learning (ML) is and how to use it. I explained the procedures of ML, such as logistic regression, support vector machines, k-means clustering, etc., by showing figures and providing intuitive explanations. At the same time, the students tried to understand ML by guessing the details. I also showed the students how to execute the ready-made functions in several R packages without showing the procedural details; at the same time, they understood how to use the R packages as black boxes. However, as time went by, I felt that this manner of teaching should be changed. In other non-ML classes, I focus on making the students consider extending the ideas. I realized that they needed to understand the essence of the subject by mathematically considering problems and building programs. I am both a mathematician and an R/Python programmer and notice the importance of instilling logic inside each student. The basic idea is that the students see that both theory and practice meet and that using logic is necessary. I was motivated to write this book because I could not find any other book that was inspired by the idea of “instilling logic” in the field of ML. The closest comparison is “Introduction to Statistical Learning: with Application in R” (ISLR) by Gareth James, Daniela Witten, Trevor Hastie, and Robert Tibshirani (Springer), which is the most popular book in this field. I like this book and have used it for the aforementioned class. In particular, the presentation in the book is splendid (abundant figures and intuitive explanations). I followed this style when

v

---

<!-- Página 6 -->

vi Preface

writing this book. However, ISLR is intended for a beginner audience. Compared with ISLR, this book (SLMP) focuses more on mathematics and programming, although the contents are similar: linear regression, classification, information criteria, regularizations, decision trees, support vector machine, and unsupervised learning. Another similar book is “The Elements of Statistical Learning” (ESL) by Trevor Hastie, Robert Tibshirani, and Jerome Friedman (Springer), which provides the most reliable knowledge on statistical learning. I often use it when preparing for my classes. However, the volume of information in ESL is large, and it takes at least 500–1000 h to read it through, although I do recommend reading the book. My book, SLMP, on the other hand, takes at most 100 h, depending on the reader’s baseline ability, and it does not assume the reader has any knowledge of ML. After reading SLMP, it takes at most 300–500 h to read through ESL because the reader will have enough logic to easily understand ESL. ESL contains many equations and procedures but no programming codes. In this sense, SLMP focuses on both mathematics and programming more than ISLR and ESL. I sincerely wish that the reader of SLMP will develop both logic and statistical learning knowledge.

What Makes SLMP Unique?

I have summarized the features of this book as follows.

1. Developing logic To grasp the essence of the subject, we mathematically formulate and solve each ML problem and build those programs. The SLMP instills “logic” in the minds of the readers. The reader will acquire both the knowledge and ideas of ML, so that even if new technology emerges, they will be able to follow the changes smoothly. After solving the 100 problems, most of the students would say “I learned a lot.” 2. Not just a story If programming codes are available, you can immediately take action. It is unfortunate when an ML book does not offer the source codes. Even if a package is available, if we cannot see the inner workings of the programs, all we can do is input data into those programs. In SLMP, the program codes are available for most of the procedures. In cases where the reader does not understand the math, the codes will help them understand what it means. 3. Not just a how-to book: an academic book written by a university professor This book explains how to use the package and provides examples of executions for those who are not familiar with them. Still, because only the inputs and outputs are visible, we can only see the procedure as a black box. In this sense, the reader will have limited satisfaction because they will not be able to obtain

---

<!-- Página 7 -->

Preface vii

the essence of the subject. SLMP intends to show the reader the heart of ML and is more of a full-fledged academic book. 4. Solve 100 exercises: problems are improved with feedback from university students The exercises in this book have been used in university lectures and have been refined based on feedback from students. The best 100 problems were selected. Each chapter (except the exercises) explains the solutions, and you can solve all of the exercises by reading the book. 5. Self-contained All of us have been discouraged by phrases such as “for the details, please refer to the literature XX.” Unless you are an enthusiastic reader or researcher, nobody will seek out those references. In this book, we have presented the material in such a way that consulting external references is not required. Additionally, the proofs are simple derivations, and the complicated proofs are given in the appendices at the end of each chapter. SLMP completes all discussions, including the appendices. 6. Readers’ pages: questions, discussion, and program files The reader can ask any question on the book’s Facebook page (https://bayesnet. org/books). Additionally, all programs and data can be downloaded from http:// bitbucket.org/prof-joe (thus, you do not have to copy the programs from the book). 7. Linear algebra One of the bottlenecks in learning ML and statistics is linear algebra. Except for books for researchers, a few books assume the reader has knowledge of linear algebra, and most books cannot go into the details of this subject. Therefore, SLMP contains a summary of linear algebra. This summary is only 17 pages and is not just an example, but it provides all the proofs. If you already know linear algebra, then you can skip it. However, if you are not confident in the subject, you can read in only one day.

How to Use This Book

Each chapter consists of problems, their explanation (body), and an appendix (proof, program). You can start reading the body and solve the problem. Alternatively, you might want to solve the 100 exercises first and consult the body if necessary. Please read through the entire book until the end. When used in a lecture, I recommend that the teacher organizes the class into 12, 90 min lectures (or a 1000 min course) as follows: 3 lectures for Chap. 1, 2 lectures for Chap. 6, and 1 lecture for each of the other chapters. You may ask the students to complete the 100 exercises. If you read the text carefully, you will be able to answer any of their questions. I think that the entire book can be fully read in about 12 lectures total.

---

<!-- Página 8 -->

viii Preface

Acknowledgments

The author wishes to thank Yuske Inaoka, Tianle Yang, Ryosuke Shinmura, Junichi Maruyama, and Kazuya Morishita for checking the manuscript. This English book is largely based on the Japanese book published by Kyoritsu Shuppan Co., Ltd, in 2020. The author would like to thank Kyoritsu Shuppan Co., Ltd, for their generosity. The author also appreciates Ms. Mio Sugino, Springer, for preparing the publication and providing advice on the manuscript.

Osaka, Japan Joe Suzuki May 2021

---

<!-- Página 9 -->

# Contents

1 Linear Algebra .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 1 1.1 Inverse Matrix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 1 1.2 Determinant.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 3 1.3 Linear Independence . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 6 1.4 Vector Spaces and Their Dimensions . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 8 1.5 Eigenvalues and Eigenvectors . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 11 1.6 Orthonormal Bases and Orthogonal Matrix .. . . .. . . . . . . . . . . . . . . . . . . . 12 1.7 Diagonalization of Symmetric Matrices . . . . . . . .. . . . . . . . . . . . . . . . . . . . 13 Appendix: Proofs of Propositions .. . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 15

2 Linear Regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 19 2.1 Least Squares Method.. . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 19 2.2 Multiple Regression .. . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 22 2.3 Distribution of ˆβ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 25 2.4 Distribution of the RSS Values . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 26 2.5 Hypothesis Testing for ˆβ j  = 0. . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 29 2.6 Coefficient of Determination and the Detection of Collinearity . . . 35 2.7 Confidence and Prediction Intervals .. . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 39 Appendix: Proofs of Propositions .. . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 42 Exercises 1–18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 43

3 Classification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 53 3.1 Logistic Regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 53 3.2 Newton–Raphson Method . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 56 3.3 Linear and Quadratic Discrimination.. . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 61 3.4 k-Nearest Neighbor Method . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 65 3.5 ROC Curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 66 Exercises 19–31 .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 69

4 Resampling .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 77 4.1 Cross-Validation .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 77 4.2 CV Formula for Linear Regression .. . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 81

ix

---

<!-- Página 10 -->

x Contents

4.3 Bootstrapping .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 85 Appendix: Proofs of Propositions .. . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 89 Exercises 32–39 .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 90

5 Information Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 95 5.1 Information Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 95 5.2 Efficient Estimation and the Fisher Information Matrix .. . . . . . . . . . . 100 5.3 Kullback–Leibler Divergence.. . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 103 5.4 Derivation of Akaike’s Information Criterion.. .. . . . . . . . . . . . . . . . . . . . 105 Appendix: Proofs of Propositions .. . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 107 Exercises 40–48 .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 110

6 Regularization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 115 6.1 Ridge .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 115 6.2 Subderivative . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 117 6.3 Lasso .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 121 6.4 Comparing Ridge and Lasso . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 124 6.5 Setting the λ Value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 126 Exercises 49–56 .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 127

7 Nonlinear Regression.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 133 7.1 Polynomial Regression .. . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 133 7.2 Spline Regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 136 7.3 Natural Spline Regression . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 140 7.4 Smoothing Spline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 144 7.5 Local Regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 148 7.6 Generalized Additive Models .. . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 153 Appendix: Proofs of Propositions .. . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 155 Exercises 57–68 .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 161

8 Decision Trees . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 171 8.1 Decision Trees for Regression .. . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 171 8.2 Decision Tree for Classification . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 180 8.3 Bagging .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 185 8.4 Random Forest . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 187 8.5 Boosting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 189 Exercises 69–74 .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 193

9 Support Vector Machine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 199 9.1 Optimum Boarder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 199 9.2 Theory of Optimization . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 202 9.3 The Solution of Support Vector Machines . . . . . .. . . . . . . . . . . . . . . . . . . . 205 9.4 Extension of Support Vector Machines Using a Kernel . . . . . . . . . . . . 209 Appendix: Proofs of Propositions .. . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 216 Exercises 75–87 .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 217

---

<!-- Página 11 -->

Contents xi

10 Unsupervised Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 227 10.1 K-means Clustering .. . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 227 10.2 Hierarchical Clustering . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 232 10.3 Principle Component Analysis . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 239 Appendix: Program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 247 Exercises 88–100 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 248

Index . . . . . . . . .. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . . . . . . . . . . . . . . . . . . 255

---

<!-- Página 12 -->

## Chapter 1

# Linear Algebra

Abstract Linear algebra is the basis of logic constructions in any science. In this chapter, we learn about inverse matrices, determinants, linear independence, vector spaces and their dimensions, eigenvalues and eigenvectors, orthonormal bases and orthogonal matrices, and diagonalizing symmetric matrices. In this book, to understand the essence concisely, we define ranks and determinants based on the notion of Gaussian elimination and consider linear spaces and their inner products within the range of the Euclidean space and the standard inner product. By reading this chapter, the readers should solve the reasons why.

1.1 Inverse Matrix

n m×n First, we consider solving the problem Ax = b w.r.t. x ∈ Rfor A ∈ R, b ∈ mm×n m×(n+1) R. We refer to A ∈ Rand [A|b] ∈ Ras a coefficient matrix and an extended coefficient matrix, respectively. We write A ∼ B when A can be m×n transformed into B ∈ Rvia the three elementary row operations below:

Operation 1 divides one whole row by a nonzero constant. Operation 2 exchanges two rows. Operation 3 adds one row multiplied by a constant to another row. { { [ ] 2x + 3y = 8x = 12 3 8 Example 1⇐⇒is equivalent to∼ x + 2y = 5 y = 2 1 2 5 [ ] 1 0 1 . 0 1 2 ⎧ ⎨2x − y + 5z = −1{ x + 3z = 1 Example 2y + z = 3⇐⇒is equivalent to ⎩y + z = 3 x + 3z = 1 ⎡⎤⎡⎤ 2 −1 5 −11 0 3 1 ⎣0 1 1 3⎦ ∼⎣0 1 1 3⎦. 1 0 3 10 0 0 0

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 20211 J. Suzuki, Statistical Learning with Math and Python, https://doi.org/10.1007/978-981-15-7877-9_1

---

<!-- Página 13 -->

2 1 Linear Algebra

⎧⎡⎤ { ⎨2x − y + 5z = 02 −1 5 x + 3z = 0 Example 3y + z = 0⇐⇒is equivalent to⎣0 1 1⎦ ⎩y + z = 0 x + 3z = 01 0 3 ⎡⎤ 1 0 3 ∼⎣0 1 1⎦. 0 0 0

We refer to the first nonzero element in each of the nonzero rows as the main element of the row and the matrix satisfying the following conditions as the canonical form:

- All-zero rows are positioned in the lowest rows. - The main element is one unless the row is all zeros. - The lower the row, the closer to the right the position of the main element is. - For each column, all but the main elements are zero.

Example 4 The following matrices are in the canonical form in which 1© is the main element: ⎡⎤⎡⎤⎡⎤ 0 1© 3 0 21© 0 1 4 0 −10 1© 0 0 2 3 ⎣0 0 0 1© 1⎦,⎣0 1© 7 −4 0 1⎦,⎣0 0 0 0 0 0⎦, 0 0 0 0 00 0 0 0 1© 30 0 0 0 0 0 ⎡⎤ 0 0 1© 0 2 0 ⎣0 0 0 0 0 1©⎦ . 0 0 0 0 0 0

m×n For an arbitrary A ∈ R, the canonical form is unique, which will be proven at the end of Sect. 1.3. We refer to any procedure computing the canonical form based on the three above operations as Gaussian elimination. In particular, we refer to the number of main elements in matrix A as the rank of A (i.e., rank(A)). From the definition, the rank of A does not exceed the minimum of m, n. n×n n×n If matrix A ∈ Ris square and its canonical form is the unit matrix I ∈ R, n×n then we say that A is nonsingular. For square matrices A, B ∈ R, if [A|I ] ∼ [I |B], then the extended coefficient matrix [I |B] is the canonical form of [A|I ]. In such a case, we say that either A or B is the inverse matrix of the other and write −1 −1 A= B and B= A. The relation [A|I ] ∼ [I |B] implies that AX = I ⇐⇒ n×n B = X. In fact, if we write X = [x1, . . . , x n], B = [b1, . . . , b n] ∈ R, then the n relation implies that Ax i = e i ⇐⇒ b i = x i for i = 1, . . . , n, where e i ∈ Ris the unit vector in which the i-th element is one and the other elements are zero. ⎡⎤ 1 2 1 Example 5 For matrix A =⎣2 3 1⎦, we have 1 2 2

⎡⎤⎡⎤ 1 2 1 1 0 01 0 0 −4 2 1 ⎣2 3 1 0 1 0⎦ ∼⎣0 1 0 3 −1 −1⎦ . 1 2 2 0 0 10 0 1 −1 0 1

---

<!-- Página 14 -->

1.2 Determinant 3

⎡⎤ 1 2 1 If we look at the left half on both sides, we can see that⎣2 3 1⎦ ∼ 1 2 2 ⎡⎤ 1 0 0 ⎣⎦, which means that A is nonsingular. Therefore, we can write 0 1 0 0 0 1

⎡⎤−1⎡⎤ 1 2 1−4 2 1 ⎣⎦=⎣⎦ 2 3 13 −1 −1 1 2 2−1 0 1

⎡⎤−1⎡⎤ −4 2 11 2 1 ⎣⎦=⎣⎦ , 3 −1 −12 3 1 −1 0 11 2 2

and we have the following relation: ⎡⎤⎡⎤⎡⎤ 1 2 1−4 2 11 0 0 ⎣⎦⎣⎦ =⎣⎦ . 2 3 13 −1 −10 1 0 1 2 2−1 0 10 0 1

∗ n n On the other hand, although the solution x = xof Ax = b with x ∈ Rand b ∈ R −1∗ can be obtained by Ab, we may obtain via [A|b] ∼ [I |x], which means we find ∗−1 x = x, without computing A.

1.2 Determinant

We define the determinant det(A) for a square matrix A as follows. If the canonical form is not the unit matrix, which means that A is singular, we set det(A) := 0. If A is the unit matrix I , then we set det(A) = 1. Suppose that A is nonsingular and is not the unit matrix. If we repeatedly apply the third elementary row operation, we obtain a matrix such that each row and each column contain exactly one nonzero element. Then, if we repeat the second operation, we obtain a diagonal matrix. Finally, if we repeat the third operation, then we obtain the unit matrix. When computing the determinant det(A), we execute the reverse procedure from the unit matrix A = I to the original A:

Step 1 Multiply det(A) by αi if the i-th row is multiplied by αi . Step 2 Multiply det(A) by −1 if the i  = j rows are exchanged.

---

<!-- Página 15 -->

4 1 Linear Algebra

Step 3 Do not change det(A) if the j -th row multiplied by β j is subtracted from the i-th row.

We define det(A) as the final obtained value after executing the three steps. Let m be how many times we implement Step 2 (multiplying by −1). Then, we have ∏ m n det(A) = (−1) αi . i=1 n×n Proposition 1 For a matrix A ∈ R, A is nonsingular ⇐⇒ rank(A) = n ⇐⇒ det(A)  = 0.

Example 6 If an all-zero row appears, which means that the determinant is zero, we may terminate the procedure. For the matrix below, the determinant is six because we exchange the rows once at the beginning. ⎡⎤⎡⎤⎡⎤⎡⎤ 0 1 11 0 41 0 41 0 0 ⎣⎦ ∼⎣⎦ ∼⎣⎦ ∼⎣⎦ . 0 −1 50 −1 50 −1 50 −1 0 1 0 40 1 10 0 60 0 6

In the following example, since an all-zero row appears during Gaussian elimina- tion, the determinant is zero. ⎡⎤⎡⎤⎡⎤ 2 −1 52 −1 52 0 6 ⎣⎦ ∼⎣⎦ ∼⎣⎦ . 0 1 10 1 10 1 1 1 0 30 1/2 1/20 0 0

In general, for a 2 × 2 matrix, if a  = 0, we have ∣∣ ∣∣∣∣ ∣a b∣∣a b∣ ∣∣=∣∣= ad − bc, bc ∣ ∣ ∣∣ c d0 d − ∣∣ a

and even if a = 0, the determinant is ad − bc. ∣∣∣∣ ∣0 b∣∣c d∣ ∣∣= −∣∣= −bc. ∣ ∣ ∣ ∣ c d0 b

Therefore, ad − bc  = 0 is the condition for A to be nonsingular, and from [ ][ ][ ] a b1d −b1 0 · =, c dad − bc−c a0 1

we have [ ]−1[ ] a b1d −b = . c dad − bc−c a

---

<!-- Página 16 -->

1.2 Determinant 5

On the other hand, for 3 × 3 matrices, if a  = 0 and ae  = bd, we have ∣∣ ∣a b c∣ ∣∣∣∣ ∣a b c∣∣∣ ∣∣∣bdcd∣ ∣∣∣0 e − f − ∣ d e f= ∣∣∣a a∣ ∣∣ ∣∣ g h i∣bgcg∣ ∣0 h − i − ∣ a a ∣()∣ ∣bcd∣ ∣a 0 c − ·f − ∣ ∣e − bd/a a∣ ∣∣ ∣bdcd∣ =∣0 e − f − ∣ ∣∣ a a ∣()∣ ∣∣ ∣cgh − bg/acd∣ ∣0 0 i − − f − ∣ a e − bd/aa ∣∣ ∣a 0 0∣ ∣∣ ∣∣ ∣∣ ae − bd ∣∣ =∣0 0∣ ∣a ∣ ∣∣ ∣aei + bfg + cdh − ceg − bdi − af h∣ ∣0 0 ∣ ae − bd = aei + bfg + cdh − ceg − bdi − af h .

Even if either a = 0 or ae = bd holds, we can see that the determinant is aei + bfg + cdh − ceg − bdi − af h.

Proposition 2 For square matrices A and B of the same size, we have det(AB) = T det(A) det(B) and det(A ) = det(A).

T For the proof, see the Appendix at the end of this chapter. The equation det(A ) = det(A) in Proposition 2 means that we may apply the following rules to obtain the determinant det(A):

′ Step 2Multiply det(A) by −1 if the i  = j columns are exchanged. ′ Step 3Do not change det(A) if the j -th column multiplied by β j is subtracted from the i-th columns.

Example 7 (Vandermonde’s Determinant) ∣∣ ∣1 a. . . a n−1∣ ∣1 1∣∏ ∣... .∣n(n−1)/2 ∣... . .∣= (−1) (a i − a j ). (1.1) . . . ∣∣ ∣n−1∣1≤i<j ≤n 1 a n . . . a n

---

<!-- Página 17 -->

6 1 Linear Algebra

In fact, if n = 1, both sides are one, and the claim holds. If we assume the claim for n = k − 1, then for n = k, the left-hand side of (1.1) is

∣∣ ∣1 a. . . a k−2a k−1∣ ∣1 1 1∣ ∣k−2k−2k−1k−1∣ ∣0 a2 − a1 . . . a − a a − a ∣ k 1 k 1 ∣∣ ∣... ..∣ ∣.. .. . . .. ..∣ ∣∣ ∣k−2k−2k−1k−1∣ 0 ak − a1 . . . a − a a − a k 1 k 1 ∣∣ ∣∣ 1 0 . . . 0 0 ∣∣ ∣k−2k−1∣ ∣0 a2 − a1 . . . (a2 − a1)a 2 (a2 − a1)a 2∣ =∣....∣ ∣. ∣ ... .. ∣. . . . .∣ ∣∣ ∣k−2k−1∣ 0 ak − a1 . . . (ak − a1)a (ak − a1)a k k ∣∣∣∣ ∣k−2∣∣k−2∣ ∣a2 − a1 . . . (a2 − a1)a 2∣∣1 a2 . . . a 2∣ ∣∣∣∣ .. .... . =∣... .∣= (a2 − a1) . . . (ak − a1)∣... . .∣ ∣. .∣∣. . .∣ ∣∣∣∣ ∣k−2∣∣k−2∣ ak − a1 . . . (ak − a1)a 1 ak . . . a kk ∏ k−1(k−1)(k−2)/2 = (−1) (a1 − a2) . . . (a1 − ak ) · (−1) (ai − aj ), 2≤i<j ≤k

where the left-hand side is obtained by subtracting the first row from the other rows. The first equation is obtained by subtracting the (j − 1)-th column multiplied by a1 from the j -th column for j = k, k − 1, . . . , 2. The third equation is obtained by dividing the rows by constants and multiplying the determinant by the same constants. The last transformation is due to the assumption of induction, and this value coincides with the right-hand side of (1.1). Thus, from induction, we have (1.1).

1.3 Linear Independence

m×n m For a matrix A ∈ Rwith column vectors a1, . . . , a n ∈ R, if the solution of n Ax = 0 is only x = 0 ∈ R, we say that a1, . . . , a n are linearly independent; otherwise, we say that they are linearly dependent. Given a set of vectors, we refer to any instance of linear independence or dependence as a linear relation. If A ∼ B, we can see that the linear relations among the column vectors in A and B are equivalent.

---

<!-- Página 18 -->

1.3 Linear Independence 7

Example 8 For A = [a1, a2, a3, a4, a5] and B = [b1, b2, b3, b4, b5], A ∼ B means Ax = 0 ⇐⇒ Bx = 0. ⎡⎤⎡⎤⎡⎤⎡⎤⎡⎤ 111−2−1 ⎢⎥⎢⎥⎢⎥⎢⎥⎢⎥ 123−4−4 ⎢⎥⎢⎥⎢⎥⎢⎥⎢⎥ a1 =, a2 =, a3 =, a4 =, a5 =, ⎣⎦ ⎣⎦ ⎣⎦ ⎣⎦ ⎣⎦ 30−317 0−12−10

⎡⎤⎡⎤ 1 1 1 −2 −11 0 −1 0 2 ⎢⎥⎢⎥ 1 2 3 −4 −40 1 2 0 −1 ⎢⎥⎢⎥ ∼, ⎣3 0 −3 1 7⎦ ⎣0 0 0 1 1⎦ 0 −1 −2 −1 00 0 0 0 0

⎫⎧ a1, a2, a4 are linearly independent⎬⎨b1, b2, b4 are linearly independent a3 = −a1 + 2a2⇐⇒b3 = −b1 + 2b2 ⎭ ⎩ a5 = 2a1 − a2 + a4b5 = 2b1 − b2 + b4.

We interpret the rank as the maximum number of linearly independent columns in the matrix. m If a1, . . . , a n ∈ Rare linearly independent, none of them can be expressed by ∑ any linear combination of the others. If we can express them as a i = x j a j j  =i ∑ n for some i, we would have Ax = x i a i = 0, which means that there exists i=1 n x ∈ Rsuch that x i  = 0. On the other hand, if they are linearly dependent, such an ∑ x i  = 0 that Ax = 0 exists, and we write a i = (−x j /x i )a j . Moreover, even j  =i if we define a vector a r+1 by a linear combination a1, . . . , a r , then a1, . . . , a r , a r+1 m×n n×l are linearly dependent. Thus, if we right-multiply A ∈ Rby a matrix B ∈ R, where B is on the right, then we obtain a matrix AB whose column vectors are ∑∑ nn a b , . . . , a b , which means that the rank (the number of linearly i=1 i i,1i=1 i i,l independent vectors) does not exceed the rank of A, i.e., rank(AB) ≤ rank(A). When a matrix B is obtained from elementary row operations applied to matrix A, the number of linearly independent row vectors in B does not exceed that in A. Similarly, because A can be obtained from B via elementary row operations, the numbers of linearly independent row vectors are equal, which holds even when B is the canonical form of A. On the other hand, all nonzero rows in the canonical form are linearly independent, and the number of such vectors is the same as that of the main elements. Therefore, the rank is the number of linearly independent row T vectors in A as well. Thus, A and its transpose A share the same rank. Moreover, l×m the matrix BA obtained by multiplying B ∈ Rfrom right by A has the same T T T T rank as (BA) = A B , which means that rank(BA) does not exceed rank(A ), which is equal to rank(A). We summarize the above discussion as follows.

---

<!-- Página 19 -->

8 1 Linear Algebra

m×n n×l Proposition 3 For A ∈ Rand B ∈ R, we have

rank(AB) ≤ min{rank(A), rank(B)}

T rank(A ) = rank(A) ≤ min{m, n}. [ ][ ][ ][ ] 2 31 01 21 0 Example 9 From A =∼, B =∼, and AB = 1 20 11 20 0 [ ][ ] 5 101 0 ∼, the ranks of A, B, and AB are 2, 1, and 1, respectively. 3 60 0 ⎡⎤ 0 1© 3 0 2 Example 10 The rank of⎣0 0 0 1© 1⎦ is two and does not exceed three 0 0 0 0 0 and five.

Finally, we show that the canonical form is unique. Suppose that A ∼ B and that the i-th columns of A and B are a i and b i , respectively. Since a linear relation that is true in A is true in B as well, if a j is linearly independent of the vectors, so is b j . Suppose further that B is in the canonical form. If the number of independent vectors on the left is k − 1, i.e., b j is the k-th row, then b k should be e k, the column vector such that the k-th element is one, and the other elements are zero. Otherwise, the k- th row of the canonical form is a zero vector, or a column vector that is right from b j becomes e k , which contradicts that B is in the canonical form. On the other hand, if ∑∑∑ a j can be written as ri a i , then b j should be written as ri b i = ri e i , i<j i<j i<j which means that b j is a column vector whose i-th element is the coefficient ri in a j . In any case, given A, the canonical form B is unique.

1.4 Vector Spaces and Their Dimensions

n We refer to any subset V of Rsuch that { x, y ∈ V ⇒ x + y ∈ V (1.2) a ∈ R, x ∈ V ⇒ ax ∈ V

n as a linear subspace of R. We may similarly define a subspace of V .

n Example 11 Let V be the subset of Rsuch that the last element of x ∈ V is equal to the sum of the other elements. Since we can see that

n−1n−1n−1 ∑∑∑ x, y ∈ V ⇒ x n =x i , y n =y i ⇒ x n +y n =(x i +y i ) ⇒ x +y ∈ V i=1i=1i=1

---

<!-- Página 20 -->

1.4 Vector Spaces and Their Dimensions 9

and

n−1n−1 ∑∑ x ∈ V ⇒ x n =x i ⇒ ax n =ax i ⇒ ax ∈ V , i=1i=1

n V satisfies (1.2) and is a subspace of R. For example, for a subset W of V such T that the first element is zero, W := {[x1, . . . , x n]∈ V |x1 = 0} satisfies (1.2), and W is a subspace of V .

n 1 In the following, we refer to any subspace of Rsolely as a vector space. Any vector in the vector space can be expressed as a linear combination of a finite 3 number of vectors. For example, an arbitrary x = [x1, x2, x3] ∈ Rcan be written ∑ 3T T T as x = x i e i using e1 := [1, 0, 0], e2 := [0, 1, 0], e3 := [0, 0, 1]. We i=1 refer to a linearly independent subset {a1, . . . , a r } of V any element in V that can be expressed as a linear combination of a1, . . . , a r as a basis of V , and the number r of elements in {a1, . . . , a r } to as the dimension of V . Although the basis of the V is not unique, the dimension of any basis is equal. Thus, the dimension of V is unique.

Example 12 The set of vectors V that are linear combinations of a1, . . . , a5 in Example 8 satisfies (1.2) and constitutes a vector space. Since a1 , a2 , and a4 are linearly independent and a3 and a5 can be expressed by linear combinations of these vectors, each element v in V can be expressed by specifying x1, x2, x4 ∈ R in x1a1 + x2a2 + x4a4 , but there exists a v ∈ V that cannot be expressed by specifying x1, x2 ∈ R and x2, x4 ∈ R in x1a1 + x2a2 and x2a2 + x4a4 , respectively. On the other hand, if we specify x1, x2, x3, x4 ∈ R in x1a1 + x2a2 + a3x3 + x4a4 , then from

x1a1 + x2a2 + a3x3 + x4a4 = x1a1 + x2a2 + x3(−a1 + 2a2) + x4a4

= (x1 − x3)a1 + (x2 + 2x3)a2 + x4a4 ,

there is more than one way to express v = a2 , such as (x1, x2, x3, x4) = (0, 1, 0, 0), (1, −1, 1, 0). Therefore, {a1, a2, a4} is a basis, and the dimension of ′′′ the vector space is three. In addition, {a, a, a4}, such that a= a1 + a2 and 121 ′ a= a1 − a2, a4 , is a basis as well. In fact, because of 2 ⎡⎤⎡⎤ 2 0 −21 0 0 ⎢⎥⎢⎥ ′′3 −1 −40 1 0 [a, a, a4] =⎢⎥∼⎢⎥, 12⎣⎦ ⎣⎦ 3 3 10 0 1 −1 1 −10 0 0

they are linearly independent.

1 In general, any subset V that satisfies (1.2) is said to be a vector space with scalars in R.

---

<!-- Página 21 -->

10 1 Linear Algebra

n m Let V and W be subspaces of Rand R, respectively. We refer to any map 2 m×n V x → Ax ∈ W as the linear map w.r.t. A ∈ R. For example, the image {Ax | x ∈ V } and the kernel {x ∈ V | Ax = 0} are subspaces W and V , respectively. On the other hand, the image can be expressed as a linear combination of the columns in A and its dimension coincides with the rank of A (i.e., the number of linearly independent vectors in A).

Example 13 For the matrix A in Example 8 and vector space V , each element of which can be expressed by a linear combination of a1, . . . , a5 , the vectors in the image can be expressed by a linear combination of a1 , a2 , and a4 . ⎡⎤ x1 ⎡⎤⎢⎥⎡⎤ 1 0 −1 0 2⎢x2⎥0 ⎢⎥ Ax = 0 ⇐⇒⎣0 1 2 0 −1⎦⎢x3⎥=⎣0⎦ ⎢⎥ 0 0 0 1 1⎣x4⎦0 x5 ⎡⎤⎡⎤⎡⎤⎡⎤ x1x3 − 2x51−2 ⎢⎥⎢⎥⎢⎥⎢⎥ ⎢x2⎥⎢−2x3 + x5⎥⎢−2⎥⎢1⎥ ⎢⎥⎢⎥⎢⎥⎢⎥ ⇐⇒⎢x3⎥=⎢x3⎥= x3⎢1⎥+ x5⎢0⎥. ⎢⎥⎢⎥⎢⎥⎢⎥ ⎣x4⎦⎣−x5⎦⎣0⎦⎣−1⎦ x5x501 ⎧⎡⎤ ⎪1 ⎪ ⎪ ⎪⎢⎥ ⎪−2 ⎨⎢⎥ ⎢⎥ The image and kernel are {c1a1 + c2a2 + c4a4 | c1, c2, c4 ∈ R} andc3⎢1⎥ ⎪⎢⎥ ⎪ ⎪⎣0⎦ ⎪ ⎪ ⎩ 0 ⎡⎤⎫ −2⎪⎪ ⎪ ⎢⎥⎪ ⎪ ⎢1⎥⎬ ⎢⎥ +c5⎢0⎥| c3, c5 ∈ R, respectively, and they are the subspaces of V (three ⎢⎥⎪ ⎪ ⎣−1⎦⎪⎪ ⎪ ⎭ 1 5 dimensions) and W = R(two dimensions), respectively.

n m Proposition 4 Let V and W be subspaces of Rand R, respectively. The image m×n and kernel of the linear map V → W w.r.t. A ∈ Rare subspaces of W and V , respectively, and the sum of the dimensions is n. The dimension of the image coincides with the rank of A.

For the proof, see the Appendix at the end of this chapter.

2 In general, for vector spaces V and W , we say that f : V → W is a linear map if f (x + y) = f (x) + f (y), where x, y ∈ V , f (ax) = af (x), a ∈ R, and x ∈ V .

---

<!-- Página 22 -->

1.5 Eigenvalues and Eigenvectors 11

1.5 Eigenvalues and Eigenvectors

n×nn For a matrix A ∈ R, if there exist 0  = x ∈ Cand λ ∈ C such that Ax = λx, we refer to x  = 0 as the eigenvector of eigenvalue λ. In general,

the solution of (A − λI )x = 0 is only x = 0 ⇐⇒ det(A − λI )  = 0.

Combined with Proposition 1, we have the following proposition.

Proposition 5 λ is an eigenvalue of A ⇐⇒ det(A − λI ) = 0

In this book, we only consider matrices for which all the eigenvalues are real. In n×n general, if the eigenvalues of A ∈ Rare λ1, . . . , λn, they are the solutions of the eigenpolynomial det(A − tI ) = (λ1 − t) . . . (λn − t) = 0, and if we substitute in t = 0, we have det(A) = λ1 . . . λn.

Proposition 6 The determinant of a square matrix is the product of its eigenvalues.

n In general, for each λ ∈ R, the subset V λ := {x ∈ R| Ax = λx} constitutes a n subspace of R(the eigenspace of λ):

x, y ∈ V λ ⇒ Ax = λx, Ay = λy ⇒ A(x + y) = λ(x + y) ⇒ x + y ∈ V λ

x ∈ V λ , a ∈ R ⇒ Ax = λx, a ∈ R ⇒ A(ax) = λ(ax) ⇒ ax ∈ V λ . ⎡⎤ 7 12 0 2 Example 14 For A =⎣−2 −3 0⎦, from det(A−tI ) = 0, we have (t −1)(t − 2 4 1 3) = 0. ⎡⎤⎡⎤ 6 12 01 2 0 When t = 1, we have A − tI =⎣−2 −4 0⎦ ∼⎣0 0 0⎦, and a basis 2 4 00 0 0 ⎡⎤⎡⎤ 20 of its kernel consists of⎣−1⎦ and⎣0⎦ . 01 ⎡⎤⎡⎤ 4 12 01 3 0 When t = 3, we have A − tI =⎣−2 −6 0⎦ ∼⎣1 2 −1⎦ , and a 2 4 −20 0 0 ⎡⎤ 3 basis of its kernel consists of⎣−1⎦. Hence, we have 1

⎧⎡⎤⎡⎤⎫⎧⎡⎤⎫ ⎨20⎬⎨3⎬ W1 =c1⎣−1⎦ + c2⎣0⎦ | c1, c2 ∈ R, W3 =c3⎣−1⎦ | c3 ∈ R. ⎩⎭ ⎩⎭ 011

---

<!-- Página 23 -->

12 1 Linear Algebra

⎡⎤ 1 3 2 Example 15 For A =⎣0 −1 0⎦, from det(A − tI ) = 0, we have (t + 1 2 0 ⎡⎤⎡⎤ 2 3 21 0 1 2 1)(t − 2) = 0. When t = −1, we have A − tI =⎣0 0 0⎦ ∼⎣0 1 0⎦, 1 2 10 0 0 ⎡⎤ −1 and a basis of its kernel consists of⎣0⎦. When t = 2, we have A − tI = 1 ⎡⎤⎡⎤⎡⎤ −1 3 21 0 −22 ⎣0 −3 0⎦ ∼⎣0 1 0⎦, and a basis of its kernel consists of⎣0⎦. 1 2 −20 0 01 Hence, we have ⎧⎡⎤⎫⎧⎡⎤⎫ ⎨−1⎬⎨2⎬ W−1 =c1⎣0⎦ | c1 ∈ R, W2 =c2⎣0⎦ | c2 ∈ R. ⎩⎭ ⎩⎭ 11

n×n If we obtain a diagonal matrix by multiplying a square matrix A ∈ Rby a nonsingular matrix and its inverse from left and right, respectively, then we say that A is diagonalizable.

Example 16 If we write the matrix that arranges the eigenvectors in Example 14 ⎡⎤⎡⎤ 2 0 31 0 0 −1 as P =⎣−1 0 −1⎦, then we have P AP =⎣0 1 0⎦. 0 1 10 0 3 As in Example 14, if the sum of the dimensions of the eigenspaces is n, we can diagonalize matrix A. On the other hand, as in Example 15, we cannot diagonalize A. In fact, each column vector of P should be an eigenvector. If the sum of the dimensions of the eigenspaces is less than n, we cannot choose linearly independent columns of P .

1.6 Orthonormal Bases and Orthogonal Matrix

∑ 3 T n We define the inner product and norm of a vector space V as u v = u i vi and i=1 √ T ‖u‖ = u u, respectively, for u, v ∈ V . If a basis u1, . . . , u n of V is orthogonal (the inner product of each pair is zero), the norms are ones; we say that they

3 ′′ In general, we say that the map (·, ·) is an inner product of V if (u + u, v) = (u, v) + (u, v), ′ (cu, v) = c(u, v), (u, v) = (u, v), and u  = 0 ⇒ (u, u) > 0 for u, v ∈ V , where c ∈ R.

---

<!-- Página 24 -->

1.7 Diagonalization of Symmetric Matrices 13

constitute an orthonormal basis. For an arbitrary linear independent v1, . . . , vn ∈ V , we construct an orthonormal basis u1, . . . , u n of V such that the subspaces that contain u1, . . . , u i and v1, . . . , vi coincide for i = 1, . . . , n.

Example 17 (Gram–Schmidt Orthonormal Basis) We construct an orthonormal basis u1, . . . , u i such that

{α1v1 + . . . + αi vi |α1, . . . , αi ∈ R} = {β1u1 + . . . + β i u i |β1, . . . , β i ∈ R} ⎡⎤⎡⎤ 11 for each i = 1, . . . , n: Suppose we are given v1 =⎣1⎦ , v2 =⎣3⎦ , and v3 = 01 ⎡⎤⎡⎤ 21 11 ⎣−1⎦. Then, the orthonormal basis consists of u= = √⎣1⎦, 1 ‖v1‖ 2 10 ⎡⎤⎡⎤⎡⎤ 11−1′ 41v ′2 v= v2 − (v2, u1)u1 =⎣3⎦ − √· √⎣1⎦ =⎣1⎦, u2 = = 2 ′ 2 2‖v2‖ 101 ⎡⎤ −1 1 √⎣1⎦ 3 1 ⎡⎤⎡⎤⎡⎤ 21−1 11−21 ′ v= v3 −(v3, u1)u1 −(v3, u2)u2 =⎣−1⎦− √· √⎣1⎦− √· √⎣1⎦ = 3 2 23 3 101 ⎡⎤⎡⎤ 11 51 ⎣−1⎦, and u= √⎣−1⎦. 3 66 22

We say a square matrix such that the columns are orthonormal. For an orthogonal n×nT matrix P ∈ R, P P is the unit matrix. Therefore,

T −1 P = P . (1.3)

T If we take the determinants on both sides, then det(P ) det(P ) = 1. From det(P ) = T det(P ), we have det(P ) = ±1. On the other hand, we refer to the linear map T T T T V x → P x ∈ V as an orthogonal map. Since (P x) (P y) = x P P y = x y, x, y ∈ V , an orthogonal map does not change the inner product of any pairs in V .

1.7 Diagonalization of Symmetric Matrices

n×n In this section, we assume that square matrix A ∈ Ris symmetric. We say that a square matrix is an upper-triangular matrix if the (i, j )-th elements are zero for all i > j . Then, we have the following proposition.

---

<!-- Página 25 -->

14 1 Linear Algebra

Proposition 7 For any square matrix A, we can obtain an upper-triangular matrix −1 P AP by multiplying it from right using an orthogonal matrix P .

For the proof, see the Appendix at the end of this chapter. −1−1T T T −1T If we note that P AP is symmetric because (P AP ) = P A (P ) = −1 P AP , from (1.3), Proposition 7 claims that diagonalization and triangulation are obtained using the orthogonal matrix P . In the following, we claim a stronger statement. To this end, we note the following proposition.

Proposition 8 For a symmetric matrix, any eigenvectors in different eigenspaces are orthogonal.

In fact, for eigenvalues λ, μ ∈ R of A, where x ∈ V λ and y ∈ V μ, we have

T T T T T T T T λx y = (λx) y = (Ax) y = x A y = x Ay = x (μy) = μx y .

T In addition, because λ  = μ, we have x y = 0. As we have seen before, a matrix A being diagonalizable is equivalent to the sum n of the dimensions of the eigenspaces. Thus, if we choose the basis of each eigenspace to be orthogonal, all n vectors will be orthogonal.

−1 Proposition 9 For a symmetric matrix A and an orthogonal matrix P , the P AP is diagonal with diagonal elements equal to the eigenvalues of A. ⎡⎤⎧⎡⎤⎡⎤ 1 2 −1⎨2−1 Example 18 The eigenspaces of⎣2 −2 2⎦ arec1⎣1⎦ + c2⎣0⎦ ⎩ −1 2 101 ⎧⎡⎤⎫ ⎨1⎬ | c1, c2 ∈ R} andc3⎣−2⎦ | c3 ∈ R. ⎩⎭ 1 Then, we orthogonalize the basis of the two-dimensional eigenspace. For P = ⎡√√√⎤⎡⎤ 2/5 −1/30 1/62 0 0 √√√ ⎣1/5 2/30 −2/6⎦, we have P −1AP =⎣0 2 0⎦. √√ 0 5/30 1/60 0 −4

In addition, from the discussion thus far, we have the following proposition. Proposition 10 For a symmetric matrix A of size n, the three conditions below are equivalent:

m×n T 1. A matrix B ∈ Rexists such that A = B B. T n 2. x Ax ≥ 0 for an arbitrary x ∈ R. 3. All the eigenvalues of A are nonnegative.

T T T T 2 In fact, 1. ⇒ 2. because A = B B ⇒ x Ax = x B Bx = ‖Bx‖, T T T 2 2. ⇒ 3. because x Ax ≥ 0 ⇒ 0 ≤ x Ax = x λx = λ‖x‖, and 3. ⇒ 1. √√√√ −1T T because λ1, . . . , λn ≥ 0 ⇒ A = P DP = P DDP = (DP ) DP ,

---

<!-- Página 26 -->

Appendix: Proofs of Propositions 15

√ where D and D are the diagonal matrices whose elements are λ1, . . . , λn and √√ λ1, . . . , λn, respectively. In this book, we refer to the matrices that satisfy the three equivalent conditions in Proposition 10 and the ones whose eigenvalues are positive as to nonnegative definite and positive definite matrices, respectively.

Appendix: Proof of Propositions

Proposition 2 For square matrices A and B of the same size, we have det(AB) = T det(A) det(B) and det(A ) = det(A).

Proof For Steps 1, 2, and 3, we multiply the following matrices from left:

V i (α): a unit matrix where the (i, i)-th element has been replaced with α. U i,j : a unit matrix where the (i, i), (j, j )-th and (i, j ), (j, i)-th elements have been replaced by zero and one, respectively. Wi,j (β): a unit matrix where the (i, j )-th zero (i  = j ) has been replaced by −β.

n×n Then, for B ∈ R,

det(V i (α)B) = α det(B), det(U i,j B) = − det(B), det(Wi,j (β)B) = det(B) . (1.4)

Since

det(V i (α)) = α, det(U i,j ) = −1, det(Wi,j (β)) = 1 (1.5)

holds, if we write matrix A as the product E1, . . . , E r of matrices of the three types, then we have

det(A) = det(E1) . . . det(E r ) .

det(AB) = det(E1 · E2 . . . E r B) = det(E1) det(E2 . . . E r B) = . . .

= det(E1) . . . det(E r ) det(B) = det(A) det(B).

T On the other hand, since matrices V i (α) and U i,j are symmetric and Wi,j (β) = Wj,i (β), we have a similar equation to (1.4) and (1.5). Hence, we have

T TTTT det(A ) = det(E r . . . E ) = det(E r ) . . . det(E ) = det(E1) . . . det(E r ) = det(A) . 1 1



---

<!-- Página 27 -->

16 1 Linear Algebra

n m Proposition 4 Let V and W be subspaces of Rand R, respectively. The image m×n and kernel of the linear map V → W w.r.t. A ∈ Rare subspaces of W and V , respectively, and the sum of the dimensions is n. The dimension of the image coincides with the rank of A.

Proof Let r and x1, . . . , x r ∈ V be the dimension and basis of the kernel, respectively. We add x r+1, . . . , x n, which are linearly independent of them, so that x1, . . . , x r , x r+1, . . . , x n are the bases of V . It is sufficient to show that Ax r+1, . . . , Ax n are the bases of the image. First, since x1, . . . , x r are vectors in the kernel, we have Ax1 = . . . = Ax r = 0. ∑ n For an arbitrary x = b j x j with b r+1, . . . , b n ∈ R, the image can be expressed j =1 ∑ n as Ax = j =r+1 b j Ax j , which is a linear combination of Ax r+1, . . . , Ax n. Then, our goal is to show that

n ∑ b i Ax i = 0 ⇒ b r+1, . . . , b n = 0 . (1.6) i=r+1 ∑∑ nn If A b i x i = 0, then b i x i is in the kernel. Therefore, there exist i=r+1 i=r+1 ∑∑∑ nrn b1, . . . , b r such that b i x i = − b i x i , which means that b i x i = i=r+1 i=1 i=1 0. However, we assumed that x1, . . . , x n are linearly independent, which means that b1 = . . . = b n = 0, and Proposition (1.6) is proven. 

Proposition 7 For any square matrix A, we can obtain an upper-triangular matrix −1 P AP by multiplying it, using an orthonormal matrix P .

Proof We prove the proposition by induction. For n = 1, since the matrix is scalar, the claim holds. From the assumption of induction, for an arbitrary ˜B ∈ (n−1)×(n−1) R, there exists an orthogonal matrix ˜Q such that ⎡⎤ ˜λ∗ 2 −1 ⎢⎥ ˜Q˜B ˜Q =. . , ⎣.⎦ 0 ˜λn

where ∗ represents the nonzero elements and ˜λ2, . . . , ˜λn are the eigenvalues of ˜B. n×n For a nonsingular matrix A ∈ Rwith eigenvalues λ1, . . . , λn, allowing multiplicity, let u1 be an eigenvector of eigenvalue λ1 and R an orthogonal matrix such that the first column is u1 . Then, we have Re1 = u1 and Au1 = λ1u1 , where T n e1 := [1, 0, . . . , 0]∈ R. Hence, we have

−1−1−1−1 RARe1 = RAu1 = λ1Ru1 = λ1RRe1 = λ1e1,

and we may express [ ] −1λ1 b RAR =, 0 B

---

<!-- Página 28 -->

Appendix: Proofs of Propositions 17

(n−1)×1 where b ∈ R[1 × (n − 1)] and 0 ∈ R. Note that R and A are nonsingular, so is B. [ ] 1 0 We claim that P = Ris an orthogonal matrix, where Q is an 0 Q (n−1)×(n−1)T orthogonal matrix that diagonalizes B ∈ R. In fact, QQ is a unit [ ][ ] 1 01 0 T T matrix, so is P P =R R. Note that the eigenvalues of B are 0 Q0 Q λ2, . . . , λn of A:

n ∏ −1 (λi − λ) = det(A − λIn ) = det(RAR − λIn ) = (λ1 − λ) det(B − λIn−1) , i=1

where In is a unit matrix of size n. −1 Finally, we claim that A is diagonalized by multiplying P and P from left and right, respectively: [ ][ ][ ] [ ] [ ] −11 0−11 01 0λ1 b1 0 P AP =RAR= −1−1 0 Q0 Q0 Q0 B0 Q ⎡⎤ λ1 ∗ [ ] ⎢λ⎥ λ1 bQ⎢2⎥ ==⎢⎥, −1. 0 QBQ⎣. .⎦ λn

which completes the proof. 

---

<!-- Página 29 -->

## Chapter 2

# Linear Regression

Abstract Fitting covariate and response data to a line is referred to as linear regression. In this chapter, we introduce the least squares method for a single covariate (single regression) first and extend it to multiple covariates (multiple regression) later. Then, based on the statistical notion of estimating parameters from data, we find the distribution of the coefficients (estimates) obtained via the least squares method. Thus, we present a method for estimating a confidence interval of the estimates and for testing whether each of the true coefficients is zero. Moreover, we present a method for finding redundant covariates that may be removed. Finally, we consider obtaining a confidence interval of the response of new data outside of the dataset used for the estimation. The problem of linear regression is a basis of consideration in various issues and plays a significant role in machine learning. .

2.1 Least Squares Method

Let N be a positive integer. For given data (x1, y1), . . . , (x N , y N ) ∈ R × R, we obtain the intercept β0 and slope β1 via the least squares method. More precisely, ∑ N2 we minimize the sum L := (y i − β0 − β1x i )of the squared distances (y i − i=1 2 β0 − β1x i )between (x i , y i ) and (x i , β0 + x i β1) over i = 1, · · · , N (Fig. 2.1). Then, by partially differentiating L by β0, β1 and letting them be zero, we obtain the following equations:

N ∑ ∂L = −2(y i − β0 − β1x i ) = 0 (2.1) ∂β0 i=1

N ∑ ∂L = −2x i (y i − β0 − β1x i ) = 0, (2.2) ∂β1 i=1

where the partial derivative is calculated by differentiating each variable and regarding the other variables as constants. In this case, β0 and β1 are regarded as constants when differentiating L by β1 and β0 , respectively.

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 202119 J. Suzuki, Statistical Learning with Math and Python, https://doi.org/10.1007/978-981-15-7877-9_2

---

<!-- Página 30 -->

20 2 Linear Regression

Fig. 2.1 Obtain β0 and β1 y that minimize ∑n 2 i=1(yi − β1xi − β0)via the least squares method Line y = β x + β (xi, β xi + β )

Distance |yi − β xi − β |

(xi, yi)

x0

N ∑ 2 By solving Eqs. (2.1)–(2.2) when(x i − ¯x)= 0, i.e., i=1

x1 = · · · = x N is not true (2.3)

we obtain

N ∑ (x i − ¯x)(y i − ¯y) i=1 ˆβ=(2.4) 1 N ∑ 2 (x i − ¯x) i=1 ˆβ= ¯y − ˆβ¯x , (2.5) 0 1

NN 1∑1∑ where ¯x := x i and ¯y := y i . We used the variables ˆβ0 and ˆβ1 instead NN i=1i=1 of β0 and β1 , which means that they are not the true values but rather estimates obtained from data. If we divide both sides of Eq. (2.1) by −2N, we obtain (2.5). To show (2.4), we center the data as follows:

˜x1 := x1 − ¯x, . . . , ˜x N := x N − ¯x, ˜y1 := y1 − ¯y, . . . , ˜y N := y N − ¯y,

and obtain the slope ( ˆβ1 ) first. Even if we shift all the points by ( ¯x, ¯y) in the directions of X and Y , the slope remains the same, but the line goes through the origin. Note that once x1, . . . , x N , y1, . . . , y N are centered, then we have

NN ∑∑ 11 ˜x i = ˜y i = 0 NN i=1i=1

---

<!-- Página 31 -->

2.1 Least Squares Method 21

Fig. 2.2 Instead of (2.4), we BEFORE center the data at the4 AFTER beginning and obtain the 3 slope via (2.6) first and obtain the intercept later via the 2 arithmetic means ¯x, ¯y and the relation in (2.5)1y

0

-1

-2

-2 -1 0 1 2 x

and

NN 1∑1∑ ˜y i − β1˜x i = 0 , NN i=1i=1

which means that the intercept becomes zero with the new coordinates. From the centered x1, . . . , x N and y1, . . . , y N , we obtain ˆβ1 ; if we substitute β0 = 0 into (2.2), unless ˜x1 = · · · = ˜x N = 0, we obtain

N ∑ ˜x i ˜y i i=1 ˆβ=. (2.6) 1 N ∑ 2 ˜xi i=1

The estimate (2.6) is obtained after centering w.r.t. x1, . . . , x N and y1, . . . , y N , and if we return to the values before the centering by

x1 := ˜x1 + ¯x, . . . , x N := ˜x N + ¯x, y1 := ˜y1 + ¯y, . . . , y N := ˜y N + ¯y ,

we obtain (2.4). Finally, from ˆβ1 and the relation in (2.5), we obtain the intercept ˆβ= ¯y − ˆβ¯x. 0 1 ′ Example 19 Figure 2.2 shows the two lines l and lgenerated via the Python program below. l is obtained from the N pairs of data and the least squares method, ′ and lis obtained by shifting l so that it goes through the origin.

---

<!-- Página 32 -->

22 2 Linear Regression

def min_sq(x,y): x_bar,y_bar=np.mean(x),np.mean(y) beta_1=np.dot(x-x_bar,y-y_bar)/np.linalg.norm(x-x_bar)**2 beta_0=y_bar-beta_1*x_bar return [beta_1,beta_0]

N=100# Data generation a=np.random.normal(loc=2,scale=1,size=N)# randomly generate the coefficients of the line b=randn(1)# randomly generate the points surrounding the line x=randn(N) y=a*x+b+randn(N)

a1,b1=min_sq(x,y)# estimating coefficients xx=x-np.mean(x);yy=y-np.mean(y)# centering a2,b2=min_sq(xx,yy)

(1.7865393047324676, 1.067565008452225e-16)

x_seq=np.arange(-5,5,0.1) y_pre=x_seq*a1+b1 yy_pre=x_seq*a2+b2

plt.scatter(x,y,c="black")# plots of the points plt.axhline(y=0,c="black",linewidth=0.5) plt.axvline(x=0,c="black",linewidth=0.5) plt.plot(x_seq,y_pre,c="blue",label="Before")# the line before centering plt.plot(x_seq,yy_pre,c="orange",label="After")# the line after centering plt.legend(loc="upper left")

In the program, by using x_seq with intercept a and slope b , we get y_pre and yy_pre , and the X-axis y = 0, and the Y-axis x = 0 by the commands plt.axvline(x=0), plt.axhline(y=0), and abline(v=0), respec- tively. The function min_sq defined in the program returns the intercept b and slope a from the least squares methods.

2.2 Multiple Regression

We extend the regression problem for a single covariate (p = 1) to the one for multiple covariates (p ≥ 1). To this end, we formulate the least squares method for single regression with matrices. If we define ⎡⎤⎡⎤ y11 x1[ ] ⎢.⎥⎢..⎥β0 y :=⎣.⎦ , X :=⎣..⎦ , β :=, (2.7) .. . β1 y N1 x N

---

<!-- Página 33 -->

2.2 Multiple Regression 23

N ∑ 2 then for L :=(y i − β0 − x i β1), we have i=1

2 L = ‖y − Xβ‖

and ⎡⎤ ∂L ⎢∂β⎥ 0T ∇L :=⎢⎥= −2X (y − Xβ) . (2.8) ⎣∂L⎦ ∂β1

By examining (2.8), we see that the elements on the right-hand side of (2.8) are ⎡⎤ N ∑ ⎢−2(y i − β0 − β1x i )⎥ ⎢⎥ ⎢i=1⎥ , (2.9) ⎢N⎥ ∑ ⎣⎦ −2x i (y i − β0 − β1x i ) i=1

which means that (2.9) expresses (2.1) and (2.2). For multiple regression (p ≥ 1), we may extend the formulation in (2.7) to the one below: ⎡⎤⎡⎤ ⎡⎤β0 1 x1,1 · · · x1,p y1 ⎢⎥⎢⎥ β ⎢.⎥⎢⎥⎢1⎥ y :=⎣.⎦ , X :=⎢... .⎥, β :=⎢.⎥, .... .. ⎣. . . .⎦ ⎣.⎦ y N 1 x N,1 · · · x N,pβ p

Even if we extend this formulation, (2.8) still holds. In fact, if we let x i,0 = 1, i = 1, . . . , N, (2.9) is extended to ⎡⎤ Np ∑∑ ⎢−2(y i −β j x i,j )⎥ ⎢⎥ ⎢i=1j =0⎥ ⎢⎥ ⎢N∑p∑⎥ ⎢⎥ ⎢−2x i,1(y i −β j x i,j )⎥ T ⎢⎥ − 2X (y − Xβ) =i=1j =0. (2.10) ⎢⎥ ⎢⎥ . ⎢.⎥ ⎢.⎥ ⎢Np⎥ ⎢∑∑⎥ ⎣⎦ −2x i,p (y i −β j x i,j ) i=1j =0

T T Since (2.10) being zero means that X Xβ = X y, we have the following statement:

---

<!-- Página 34 -->

24 2 Linear Regression

T (p+1)×(p+1) Proposition 11 When a matrix X X ∈ Ris invertible, we have

ˆβ = (X T X)−1X T y . (2.11)

Example 20 The following is a Python program that estimates the intercept and slope via the least squares method: based on (2.11) for N = 100 random data points with β0 = 1, β1 = 2, β2 = 3, and i ∼ N(0, 1).

n=100; p=2 beta=np.array([1,2,3]) x=randn(n,2) y=beta[0]+beta[1]*x[:,0]+beta[2]*x[:,1]+randn(n) X=np.insert(x,0,1,axis=1)# adding the all one vector in the leftmost column np.linalg.inv(X.T@X)@X.T@y# estimate the beta

array([1.08456582, 1.91382258, 2.98813678])

T We may notice that the matrix X X is not invertible under each of the following conditions:

1. N < p + 1. 2. Two columns in X coincide.

In fact, when N < p + 1, from Proposition 3, we have

T rank(X X) ≤ rank(X) ≤ min{N, p + 1} = N < p + 1 ,

T which means from Proposition 1 that X X is not invertible. On the other hand, when two columns in X coincide, from Proposition 3, we have

T rank(X X) ≤ rank(X) < p + 1 ,

T which means that, from Proposition 1, X X is not invertible as well. T Moreover, we see that the ranks of X X and X coincide. In fact, for an arbitrary p+1 z ∈ R,

T T T 2 X Xz = 0 ⇒ z X Xz = 0 ⇒ ‖Xz‖= 0 ⇒ Xz = 0

and

T Xz = 0 ⇒ X Xz = 0,

T which means that the kernels of X X and X coincide. Since the numbers of columns T of X X and X are equal, so are the dimensions of their images (see Proposition 4). On the other hand, from Proposition 4, since the image dimensions are the ranks T T of the matrices, the ranks of X X and X are equal. N×(p+1) In the following section, we assume that the rank of X ∈ Ris p + 1. In particular, if p = 1, the condition in (2.3) is equivalent to rank(X) = 1 < 2 = p+1.

---

<!-- Página 35 -->

2.3 Distribution of ˆβ 25

ˆ 2.3 Distribution of β

N We assume that the responses y ∈ Rhave been obtained from the covariates N×(p+1) p+1 X ∈ Rmultiplied by the (true) coefficients β ∈ Rplus some noise N  ∈ R, which means that y fluctuates only because of the randomness in . Thus, we let

y = Xβ +  , (2.12)

where the true β is unknown and different from the estimate ˆβ. We have estimated ˆβ via the least squares method from the N pairs of data (x, y), . . . , (x , y ) ∈ 11N N p p R× R, where x i ∈ Ris the row vector consisting of p values excluding the leftmost one in the i-th row of X. Moreover, we assume that each element 1, . . . , N in the random variable  is independent of the others and follows the Gaussian distribution with mean zero and 2 variance σ . Therefore, the density function is

2  i 1− 2 fi (i ) = √e2σ 2 2πσ

2 for i = 1, . . . , N, which we write as i ∼ N(0, σ ). We may express the distributions of 1, . . . , N by

T N  ∏− 1 2 f () =fi (i ) = e2σ , 2N/2 (2πσ ) i=1

2 which we write as  ∼ N(0, σ I ), where I is a unit matrix of size N. In general, we have the following statement:

Proposition 12 Two Gaussian random variables are independent if and only if their covariance is zero.

For the proof, see the Appendix at the end of this chapter. If we substitute (2.12) into (2.11), we have

ˆβ = (X T X)−1X T (Xβ + ) = β + (X T X)−1X T  . (2.13)

The estimate ˆβ of β depends on the value of  because N pairs of data (x1, y1), . . . , (x N , y N ) randomly occur. In fact, for the same x1, . . . , x N , if we again generate (y1, . . . , y N ) randomly according to (2.12) only, the fluctuations (1, . . . , N ) are different. The estimate ˆβ is obtained based on the N pairs of N randomly generated data points. On the other hand, since the average of  ∈ R T −1T is zero, the average of  multiplied from left by the constant matrix (X X)X is

---

<!-- Página 36 -->

26 2 Linear Regression

zero. Therefore, from (2.13), we have

E[ ˆβ] = β. (2.14)

In general, we say that an estimate is unbiased if its average coincides with the true value. Moreover, both ˆβ and its average β consist of p + 1 values. In this case, in 2 addition to each variance V ( ˆβ i ) = E( ˆβ i − β i ), i = 0, 1, . . . , p, the covariance σi,j := E( ˆβ i − β i )( ˆβ j − β j ) can be defined for each pair i  = j . We refer to the matrix consisting of σi,j in the i-th row and j -th column as to the covariance matrix ˆ of β, which can be computed as follows. From (2.13), we have ⎡⎤ 2 ( ˆβ0 − β0)( ˆβ0 − β0)( ˆβ1 − β1) · · · ( ˆβ0 − β0)( ˆβ p − β p ) ⎢ˆˆˆ2 ˆˆ⎥ ( β− β)( β− β) ( β− β)· · · ( β− β)( β − β ) ⎢1 10 01 11 1p p ⎥ E⎢...⎥ . ⎣... . .⎦ . . . 2 ( ˆβ p − β p )( ˆβ0 − β0) ( ˆβ p − β p )( ˆβ1 − β1) · · · ( ˆβ p − β p ) ⎡⎤ ˆβ− β 0 0 ⎢ˆ⎥ β− β ⎢1 1⎥ = E⎢.⎥[ ˆβ0 − β0, ˆβ1 − β1, . . . , ˆβ p − β p] ⎣..⎦ ˆβ − β p p

T T −1T T −1T T = E( ˆβ − β)( ˆβ − β) = E(X X)X {(X X)X }

T −1T T T −1 2T −1 = (X X)X E X(X X)= σ (X X),

T 2 for which we have determined that the covariance matrix of  is E = σ I . Hence, we have

ˆβ ∼ N(β, σ 2(X T X)−1) . (2.15)

2.4 Distribution of the RSS Values

In this subsection, we derive the distribution of the squared loss by substituting 2 β = ˆβ into L = ‖y − Xβ‖when we fit the data to a line. To this end, we explore 1 T −1T N×N the properties of the matrix H := X(X X)X ∈ R. The following are easy to derive but useful in the later part of this book:

2 T −1T T −1T T −1T H = X(X X)X · X(X X)X = X(X X)X = H

2 2 (I − H )= I − 2H + H = I − H

T −1T H X = X(X X)X · X = X.

1 We often refer to this matrix as the hat matrix.

---

<!-- Página 37 -->

2.4 Distribution of the RSS Values 27

Moreover, if we set ˆy := X ˆβ, then from (2.11), we have ˆy = X ˆβ = T −1T X(X X)X y = Hy, and

y − ˆy = (I − H )y = (I − H )(Xβ + ) = (X − H X)β+(1 − H ) = (I −H ).

(2.16)

We define

2 T T 2T RSS := ‖y − ˆy‖= {(I − H )}(I − H ) =  (I − H ) =  (I − H ) .

(2.17)

The following proposition is useful for deriving the distribution of the RSS values:

Proposition 13 The eigenvalues of H and I − H are only zeros and ones, and the dimensions of the eigenspaces of H and I − H with eigenvalues one and zero, respectively, are both p+1, while the dimensions of the eigenspaces of H and I −H with eigenvalues of zero and one, respectively, are both N − p − 1.

For the proof, see the Appendix at the end of this chapter. Since I −H is a real symmetric matrix, from Proposition 9, we can diagonalize it T by an orthogonal matrix P to obtain the diagonal matrix P (I −H )P . Additionally, since the N − p − 1 and p + 1 eigenvalues out of the N eigenvalues are ones and zeros, respectively, without loss of generality, we may put ones for the first N −p−1 elements in the diagonal matrix:

T P (I − H )P = diag(1, . . . , 1, 0, . . . , 0) . ︸ ︷︷ ︸︸ ︷︷ ︸ N−p−1p+1

N T Thus, if we define v = P  ∈ R, then from  = P v and (2.17), we have

T T T T T T RSS =  (I − H ) = (P v)(I − H )P v = v P (I − H )P v ⎡⎤ ⎡⎤ 1 0 · · · · · · · · · 0 ⎢⎥v1 ⎢. . ..⎥⎢⎥ ⎢0 . 0 · · · · · · .⎥⎢.⎥ ⎢⎥⎢..⎥ ⎢.⎥⎢⎥ ⎢.⎥⎢⎥ ⎢. 0 1 0 · · · 0⎥⎢vN−p−1⎥ = [v1, . . . , vN−p−1, vN−p , . . . , vn]⎢⎥⎢⎥ ⎢...⎥⎢v⎥ ⎢.. .. 0 0 · · · ..⎥⎢N−p⎥ ⎢⎥⎢.⎥ ⎢.....⎥⎢.⎥ ⎢..... . .⎥⎣.⎦ ⎣. . . . . .⎦ vN 0 · · · 0 · · · · · · 0

N−p−1 ∑ 2 =v i i=1

T for v = [v1, . . . , vN ].

---

<!-- Página 38 -->

28 2 Linear Regression

N−p−1 Let w ∈ Rbe the first N − p − 1 elements of v. Then, since the average of v is E[P ] = 0, we have E[w] = 0; thus,

T T T T 2 T 2 Evv = EP (P ) = P E P = P σ ˜I P = σ ˜I ,

where ˜I is a diagonal matrix such that the first N − p − 1 and last p + 1 diagonal T elements are ones and zeros, respectively. Hence, the covariance matrix is Eww = 2 σ I , where I is a unit matrix of size N − p − 1. For the Gaussian distributions, the independence of variables is equivalent to the covariance matrix being a diagonal matrix (Proposition 12); we have

RSS 2 ∼ χ, (2.18) 2 N−p−1 σ

22 where we denote by χ, which is a χdistribution with m degrees of freedom, i.e., m the distribution of the squared sum of m independent standard Gaussian random variables.

2 Example 21 For each degree of freedom up to m for the χdistribution, we depict the probability density function in Fig. 2.3.

x=np.arange(0,20,0.1) for i in range(1,11): plt.plot(x,stats.chi2.pdf(x,i),label=’{}’.format(i)) plt.legend(loc=’upper right’)

0.81 2 3 4 0.6 5 6 7 0.4 8 9 dchisq(x, i) 10 0.2

0.0 0 5 10 15 20 x

2 Fig. 2.3 χdistributions with 1 to 10 degrees of freedom

---

<!-- Página 39 -->

2.5 Hypothesis Testing for ˆβ j  = 0 29

ˆ 2.5 Hypothesis Testing for βj  = 0

In this section, we consider whether each of the ˆβ j , j = 0, 1, . . . , p, is zero or not based on the data. p Without loss of generality, we assume that the values of x1, . . . , x N ∈ R(row p+1 vectors) and β ∈ Rare fixed. However, due to fluctuations in the N random variables 1, . . . , N , we may regard that the values

T T y1 = β0 + x1[β1, . . . , β p ]+ 1 , . . . , y N = β0 + x N [β1, . . . , β p]+ N

occurred by chance (Fig. 2.4). In fact, if we observe y1, · · · , y N again, since the randomly occurring 1, . . . , N are not the same, the y1, · · · , y N are different from the previous ones. In the following, although the value of β j is unknown for each j = 0, 1, . . . , p, we construct a test statistic T that follows a t distribution with N − p − 1 degrees of freedom as defined below when we assume β j = 0. If the actual value of T is rare under the assumption β j = 0, we decide that the hypothesis β j = 0 should be rejected. What we mean by a t distribution with m degrees of freedom is that the √ distribution of the random variable T := U/V /m such that U ∼ N(0, 1), 22 V ∼ χ(the χdistribution of degree of freedom m), and U and V are independent. m For each degree of freedom up to m, we depict the graph of the probability density function of the t distribution as in Fig. 2.5. The t distribution is symmetric, its center is at zero, and it approaches the standard Gaussian distribution as the number of degrees of freedom m grows.

Example 22 We allow the degrees of freedom of the t distribution to vary and compare these distributions with the standard Gaussian distribution.

1.4

1.0 beta.1

0.6

0.6 0.8 1.0 1.2 1.4 beta.0

Fig. 2.4 We fix p = 1, N = 100, and x1, . . . , xN ∼ N(2, 1), generate 1, . . . ,  N ∼ N(0, 1), and estimate the intercept β0 and slope β1 from x1, . . . , xN and y1 = x1+1+1, . . . , yN = xN +1+ N . We repeat the procedure one hundred times and find that the ( ˆβ0, ˆβ1) values are different

---

<!-- Página 40 -->

30 2 Linear Regression

Fig. 2.5 t distributions with Degrees of Freedom in the t Distribution 1 to 10 degrees of freedom. The thick line shows the0.51 standard Gaussian2 distribution3 0.4 4 5 6 0.3 7 8 0.29 10

0.1

0.0 -10 -5 0 5 10

Fig. 2.6 Acceptance and rejection regions for hypothesis testing0.6 1 − α ACCEPT 0.4 dnorm 0.2 α/ 2 α/2 REJECTREJECT 0.0

-6 -4 -2 0 2 4 6 x

x=np.arange(-10,10,0.1) plt.plot(x,stats.norm.pdf(x,0,1),label="Normal ",c="black",linewidth=1) for i in range(1,11): plt.plot(x,stats.t.pdf(x,i),label=’{}’.format(i),linewidth=0.8) plt.legend(loc=’upper right’) plt.title("changes of t distribution by degree of freedom")

Text(0.5, 1.0, ’changes of t distribution by degree of freedom’)

The hypothesis test constructed here is to set the significance level (e.g., α = 0.01, 0.05) and to reject the null hypothesis if the value of T is outside of the range that occurs with probability 1 − α as in Fig. 2.6. More precisely, if T is either too large or too small so that the probability is within α/2 from both extremes, we reject the null hypothesis β j = 0. If β j = 0 is true, since T ∼ tN−p−1 , it is rare that T will be far from the center. We estimate σ in (2.12) and the standard deviation of ˆβ j by √ RSS ˆσ := N − p − 1

---

<!-- Página 41 -->

2.5 Hypothesis Testing for ˆβ j  = 0 31

and √ SE( ˆβ j ) := ˆσ Bj ,

T −1 respectively, where Bj is the j -th diagonal element of (X X).

Example 23 For p = 1, since ⎡⎤⎡⎤ [ ] 1 x11 ¯x T 1 · · · 1⎢..⎥⎢N∑⎥ X X =⎣..⎦ = N⎣1⎦ , . .2 x1 · · · x N¯x x, i 1 x NN i=1

the inverse is ⎡⎤ N ∑ 1 2 1 T −1 ⎢xi − ¯x⎥ (X X)= ⎣N⎦ , Ni=1 ∑ 2 (x i − ¯x)− ¯x 1 i=1

which means that

N 1∑ 2 x i N i=11 B0 =and B1 = . NN ∑∑ 22 (x i − ¯x)(x i − ¯x) i=1i=1

T −1 2 2 For B = (X X), Bσ is the covariance matrix of ˆβ, and Bj σ is the variance of ˆβ . Thus, we may regard Bˆσ 2 as an estimate of Bσ 2 . For β= 1 and β= 1, we j j j 0 1 estimate ˆβ0 and ˆβ1 from N = 100 data points. We repeated the process 100 times and plotted them in Fig. 2.4.

N=100; p=1 iter_num=100 for i in range(iter_num): x=randn(N)+2# mean=2, var=1 e=randn(N) y=x+1+e b_1,b_0=min_sq(x,y) plt.scatter(b_0,b_1) plt.axhline(y=1.0,c="black",linewidth=0.5) plt.axvline(x=1.0,c="black",linewidth=0.5) plt.xlabel(’beta_0’) plt.ylabel(’beta_1’)

Text(0, 0.5, ’beta_1’)

---

<!-- Página 42 -->

32 2 Linear Regression

Because ¯x is positive, the correlation between ˆβ0 and ˆβ1 is negative. In the following, we show

ˆβ − β j j t = ∼ tN−p−1. (2.19) SE( ˆβ j )

To this end, from the definition of the t distribution, we have √ ˆβ − β ˆβ − β RSS/σ 2 j jj j = √/. SE( ˆβ j ) Bj σ N − p − 1

Thus, from (2.15)–(2.18), we have

ˆβ − β RSS j j2 U := √∼ N(0, 1) and V := ∼ χ. 2 N−p−1 Bj σ σ

Hence, it remains to be shown that U and V are independent. In particular, since RSS depends only on y − ˆy, it is sufficient to show that y − ˆy and ˆβ − β are independent. To this end, if we note that

T T −1T T ( ˆβ − β)(y − ˆy) = (X X)X  (I − H ) ,

T 2 from E = σ I and H X = X, we have

T E( ˆβ − β)(y − ˆy) = 0 .

Since both y − ˆy = (I − H ) and ˆβ − β follow Gaussian distributions, zero covariance between them means that they are independent (Proposition 12), which completes the proof.

Example 24 We wish to perform a hypothesis test for a null hypothesis H0 : β j = 0 and its alternative H1 : β j  = 0. For p = 1 and using

ˆβ − 0 j t = ∼ tN−p−1 SE( ˆβ j )

under H0 , we construct the following procedure in which the function ∫ x stats.t.cdf(x,m) returnsfm (t)dt, where fm is the probability density −∞ function of a t distribution with m degrees of freedom. We compare the output with the output obtained via the lm function in the R environment.

---

<!-- Página 43 -->

2.5 Hypothesis Testing for ˆβ j  = 0 33

N=100 x=randn(N); y=randn(N) beta_1,beta_0=min_sq(x,y) RSS=np.linalg.norm(y-beta_0-beta_1*x)**2 RSE=np.sqrt(RSS/(N-1-1)) B_0=(x.T@x/N)/np.linalg.norm(x-np.mean(x))**2 B_1=1/np.linalg.norm(x-np.mean(x))**2 se_0=RSE*np.sqrt(B_0) se_1=RSE*np.sqrt(B_1) t_0=beta_0/se_0 t_1=beta_1/se_1 p_0=2*(1-stats.t.cdf(np.abs(t_0),N-2)) p_1=2*(1-stats.t.cdf(np.abs(t_1),N-2))

beta_0,se_0,t_0,p_0# intercept

(-0.007650428118828838, 0.09826142188565655, -0.0778579016262494, 0.9380998328599441)

beta_1,se_1,t_1,p_1# coefficient

(0.03949448841467844, 0.10414969655462533, 0.37920886686370736, 0.7053531714456662)

In Python we usually use scikit-learn.

from sklearn import linear_model

reg=linear_model.LinearRegression() x=x.reshape(-1,1)# we need to indicate the size of the arrangement in sklearn y=y.reshape(-1,1)# If we set one of the dimensions and set the other to -1, it will automatically adjust itself. reg.fit(x,y)# execution

LinearRegression(copy_X=True,fit_intercept=True,n_jobs=None, normalize=False)

reg.coef_,reg.intercept_# coefficient; beta_1, intercept; beta_0

(array([[0.03949449]]), array([-0.00765043]))

Now let us use a module called statsmodels to see the details of the results: add all 1’s to the left column of X.

import statsmodels.api as sm

---

<!-- Página 44 -->

34 2 Linear Regression

X=np.insert(x,0,1,axis=1) model=sm.OLS(y,X) res=model.fit() print(res.summary())

OLS Regression Results ============================================================================== Dep. Variable: y R-squared: 0.001 Model: OLS Adj. R-squared: -0.009 Method: Least Squares F-statistic: 0.1438 Date: Wed, 12 Feb 2020 Prob (F-statistic): 0.705 Time: 14:27:19 Log-Likelihood: -139.12 No. Observations: 100 AIC: 282.2 Df Residuals: 98 BIC: 287.5 Df Model: 1 Covariance Type: nonrobust ============================================================================== coef std err t P>|t| [0.025 0.975] ------------------------------------------------------------------------------ const -0.0077 0.098 -0.078 0.938 -0.203 0.187 x1 0.0395 0.104 0.379 0.705 -0.167 0.246 ============================================================================== Omnibus: 1.015 Durbin-Watson: 2.182 Prob(Omnibus): 0.602 Jarque-Bera (JB): 0.534 Skew: -0.086 Prob(JB): 0.766 Kurtosis: 3.314 Cond. No. 1.06 ==============================================================================

Here, we have RSS = 1.072 (df = N − p − 1 = 98), and the coefficient of determination is 0.02232. For the definition of the adjusted coefficient of determination, see Sect. 2.6.

Example 25 We repeat the estimation ˆβ1 in Example 24 one thousand times (r = 1000) to construct the histogram of ˆβ1/SE(β1). In the following procedure, we compute the quantity beta_1/se_1, and accumulate them as a vector of size r in T. First, we generate the data that follow the null hypothesis β_1 = 0 (Fig. 2.7, left).

N=100; r=1000 T=[] for i in range(r): x=randn(N); y=randn(N) beta_1,beta_0=min_sq(x,y) pre_y=beta_0+beta_1*x# the predicted value of y RSS=np.linalg.norm(y-beta_0-beta_1*x)**2 RSE=np.sqrt(RSS/(N-1-1)) B_0=(x.T@x/N)/np.linalg.norm(x-np.mean(x))**2 B_1=1/np.linalg.norm(x-np.mean(x))**2 se_1=RSE*np.sqrt(B_1) T.append(beta_1/se_1)

plt.hist(T,bins=20,range=(-3,3),density=True) x=np.linspace(-4,4,400) plt.plot(x,stats.t.pdf(x,98)) plt.title("the null hypothesis holds.") plt.xlabel(’the value of t’) plt.ylabel(’probability density’)

---

<!-- Página 45 -->

2.6 Coefficient of Determination and the Detection of Collinearity 35

NOT under H(βj = 0.1)under H: βj = 0 0 0

0.4

0.4 0.3 0.3 0.2 0.2

0.1 0.1

Probability Density Function0.0Probability Density Function0.0 -3 -1 1 3-2 0 2 4 tt

Fig. 2.7 Distribution of ˆβ1/SE( ˆβ1) under the null hypothesis β1 = 0 (left) and under β1 = 0.1 (Right)

Text(0, 0.5, ’probability density’)

Next, we generate data that do not follow the null hypothesis (β1 = 0.1) and esti- mate the model with them, replacing y=randn(N) with y=0.1*x+randn(N) (Fig. 2.7, Right).

2.6 Coefficient of Determination and the Detection of Collinearity

N×N In the following, we define a matrix W ∈ Rsuch that all the elements are 1/N. N 1∑ N Thus, all the elements of Wy ∈ Rare ¯y = y i for y1, . . . , y N ∈ R. N i=1 As we have defined the residual sum of squares as

2 2 2 RSS = ‖ ˆy − y‖= ‖(I − H )‖= ‖(I − H )y‖,

we define the explained sum of squares

2 2 2 ESS := ‖ ˆy − ¯y‖= ‖ ˆy − Wy‖= ‖(H − W )y‖

---

<!-- Página 46 -->

36 2 Linear Regression

and the total sum of squares

2 2 TSS := ‖y − ¯y‖= ‖(I − W )y‖.

If RSS is much less than T SS, we may regard that linear regression is suitable for the data. For the three measures, we have the relation

TSS = RSS + ESS. (2.20)

Since we have H X = X and the elements in the leftmost column of X are all ones, any all one vector multiplied by a constant is an eigenvector of eigenvalues of one, which means that H W = W . Thus, we have

(I − H )(H − W ) = 0. (2.21)

If we square both sides of (I − W )y = (I − H )y + (H − W )y, from (2.21), we 2 2 2 have ‖(I − W )y‖= ‖(I − H )y‖+ ‖(H − W )y‖. Moreover, we can show that RSS and ESS are independent. To this end, we notice that the covariance matrix between (I − H ) and (H − W )y = (H − W )Xβ + (H − W ) is equal to that of N (I − H ) and (H − W ). In fact, (H − W )Xβ ∈ Rdoes not fluctuate and is not random. Thus, we may remove it when we compute the covariance matrix. Then, T from (2.21), the covariance matrix E(I − H ) (H − W ) is a zero matrix. Because RSS and ESS follow Gaussian distributions, they are independent (Proposition 12). We refer to

2 ESSRSS R= = 1 − TSS TSS

as to the coefficient of determination. As we will see later, for single regression 2 (p = 1), the value of Rcoincides with the square of the sample-based correlation coefficient

N ∑ (x i − ¯x)(y i − ¯y) i=1 ˆρ :=√. √ NN √∑∑ √ 22 (x i − ¯x)(y i − ¯y) i=1i=1

In this sense, the coefficient of determination expresses (nonnegative) correlation between the covariates and response. In fact, for p = 1, from ˆy = ˆβ0 + ˆβ1x and N ∑ 2 2 (2.5), we have ˆy − ¯y = ˆβ1(x − ¯x). Hence, from (2.4) and ‖x − ¯x‖=(x i − ¯x) i=1

---

<!-- Página 47 -->

2.6 Coefficient of Determination and the Detection of Collinearity 37

N ∑ 2 2 and ‖y − ¯y‖=(y i − ¯y), we have i=1

⎧⎫2 NN ⎪∑⎪∑ ⎪⎪2 ⎪(x − ¯x)(y − ¯y)⎪(x − ¯x) ⎪i i ⎪i ⎪⎪ 22⎨⎬ ESSˆβ‖x − ¯x‖i=1i=1 1 = = 2 TSS ‖y − ¯y‖⎪⎪N∑⎪⎪N∑ ⎪2⎪2 ⎪⎪ ⎪(x i − ¯x)⎪(y i − ¯y) ⎩⎭ i=1i=1 { }2 N ∑ (x i − ¯x)(y i − ¯y) i=12 == ˆρ. NN ∑∑ 22 (x i − ¯x)(y i − ¯y) i=1i=1

We sometimes use a variant of the coefficient of determination (the adjusted coefficient of determination) such that RSS and TSS are divided by N − p − 1 and N − 1, respectively:

RSS/(N − p − 1) 1 − . (2.22) TSS/(N − 1)

If p is large, the adjusted coefficient of determination is smaller than the non- adjusted counterpart. For the regular coefficient of determination, the larger the number of covariates, the better the line fits the data. However, for adjustment covariates, unnecessary covariates that are not removed are penalized.

Example 26 We construct a function to obtain the coefficient of determination and calculate it for actual data.

def R2(x,y): n=x.shape[0] xx=np.insert(x,0,1,axis=1) beta=np.linalg.inv(xx.T@xx)@xx.T@y y_hat=xx@beta y_bar=np.mean(y) RSS=np.linalg.norm(y-y_hat)**2 TSS=np.linalg.norm(y-y_bar)**2 return 1-RSS/TSS

N=100; m=2 x=randn(N,m) y=randn(N) R2(x,y)

0.03530233580996256

---

<!-- Página 48 -->

38 2 Linear Regression

# If it is "one" variable, R^2 is the square of the correlation. x=randn(N,1) y=randn(N) R2(x,y)

0.033782723309598084

xx=x.reshape(N) np.corrcoef(xx,y)

array([[1. , 0.18380077], [0.18380077, 1. ]])

np.corrcoef(xx,y)[0,1]**2# The square of the correlation

0.033782723309598084

While the coefficient of determination expresses how well the covariates explain the response variable, it takes a maximum value of one. We also use VIFs (variance inflation factors), which measures the redundancy of each covariate when the other covariates are present:

1 V I F := , 2 1 − R X j |X−j

2 where Ris the coefficient of determination when the j -th variable is the X j |X−j N×p N response and the other p − 1 variables are covariates in X ∈ R(y ∈ Ris not used when the VIF is computed). The larger the VIF, the better the covariate is explained by the other covariates, which means that the j -th covariate is redundant. The minimum value of VIF is one, and we say that the collinearity of a covariate is strong when its VIF value is large.

Example 27 We installed the Python library sklearn, and computed the VIF for the Boston dataset.

from sklearn.datasets import load_boston

boston=load_boston() x=boston.data x.shape

(506, 13)

def VIF(x): p=x.shape[1]

---

<!-- Página 49 -->

2.7 Confidence and Prediction Intervals 39

values=[] for j in range(p): S=list(set(range(p))-{j}) values.append(1/(1-R2(x[:,S],x[:,j]))) return values

VIF(x)

array([1.79219155, 2.29875818, 3.99159642, 1.07399533, 4.39371985, 1.93374444, 3.10082551, 3.95594491, 7.48449634, 9.00855395, 1.79908405, 1.34852108, 2.94149108])

2.7 Confidence and Prediction Intervals

p+1 Thus far, we have showed how to obtain the estimate ˆβ of β ∈ R. In other words, 2 from (2.19), we obtain the confidence interval of ˆβ as follows:

β i = ˆβ i ± tN−p−1(α/2)SE( ˆβ i )

for i = 0, 1, . . . , p, where tN−p−1(α/2) is the t-statistic such that α/2 = ∫ ∞ f (u)du for the probability density function f . t In this section, we also wish to obtain the confidence interval of x∗ ˆβ for another p+1 point x∗ ∈ R(a row vector whose first element is one), which is different from the x1, . . . , x N used for estimation. Then, the average and variance of x∗ ˆβ are E[x∗ ˆβ] = x∗E[ ˆβ] and

T2T −1T V [x∗ ˆβ] = x∗V ( ˆβ)x = σ x∗(X X)x , ∗ ∗

2 respectively, where σ is the variance of i , i = 1, . . . , N. As we derived before, if we define √ √ ˆT −1T ˆσ := RSS/(N − p − 1), SE(x∗ β) := ˆσx∗(X X)x ∗ ,

then we can show that

x∗ ˆβ − x∗βx∗ ˆβ − x∗β C : = = √ T −1T SE(x∗ ˆβ) ˆσ x∗(X X)x ∗ √ // x∗ ˆβ − x∗βRSS = √(N − p − 1) T −1T2 σ x∗(X X)x σ ∗

follows a t distribution with N − p − 1 degrees of freedom. In fact, the numerator RSS 2 follows the N(0, 1) distribution, and follows a χdistribution. More- 2 N−p−1 σ

2 ˆˆ We write ξ − γ ≤ ξ ≤ ˆξ + γ as ξ = ˆξ ± γ , where ξ is an unbiased estimator of ξ .

---

<!-- Página 50 -->

40 2 Linear Regression

The t Distribution with 0.3 Dezgree of Freedom N − p − 1 Confident Interval C 0.2 Prediction Interval P RejectReject 0.1 0.005 0.005 0.0 Probability Density Function -4 -2 0 2 4 Values of C,P

Fig. 2.8 The confidence and prediction intervals are obtained based on the fact that those intervals are the ranges with probability 1 − α, excluding the tails, where we set α = 0.01

over, as we derived before, RSS and ˆβ − β are independent. Thus, the proof of C ∼ tN−p−1 is completed. On the other hand, if we need to consider the noise  as well as the estimated x∗ ˆβ in the evaluation, we consider the variance in the difference between x∗ ˆβ and y∗ := x∗β + :

2T −1T2 V [x∗ ˆβ − (x∗β + )] = V [x∗( ˆβ − β)] + V [] = σ x∗(X X)x + σ . ∗

Similarly, we can derive the following: √ // x∗ ˆβ − y∗x∗ ˆβ − y∗RSS P := = √(N −p−1) ∼ tN−p−1. 2 SE(x∗ ˆβ − y∗) σ (1 + x∗(X T X)−1x T)σ ∗

Hence, with probability α, we obtain the confidence and prediction intervals, respectively, as follows (Figs. 2.8 and 2.9): √ T −1T x∗β = x∗ ˆβ ± tN−p−1(α/2) ˆσx∗(X X)x ∗ √ T −1T y∗ = x∗ ˆβ ± tN−p−1(α/2) ˆσ1 + x∗(X X)x . ∗

Example 28 We do not just fit the points to a line via the least squares method; we also draw the confidence interval that surrounds the line and the prediction interval that surrounds both the fitted line and the confidence interval.

N=100; p=1 X=randn(N,p) X=np.insert(X,0,1,axis=1) beta=np.array([1,1]) epsilon=randn(N) y=X@beta+epsilon

---

<!-- Página 51 -->

2.7 Confidence and Prediction Intervals 41

Fig. 2.9 The line obtained via the least squares method.3 The confidence andPrediction Interval prediction intervals are shown2 by the solid and dashed lines, 1Confidence Interval respectively. In general, the prediction interval lies outside0 y of the confidence interval Confidence Interval -1

-2 Prediction Interval -3

-10 -5 0 5 10 x

# definiton of f(x) and g(x) U=np.linalg.inv(X.T@X) beta_hat=U@X.T@y RSS=np.linalg.norm(y-X@beta_hat)**2 RSE=np.sqrt(RSS/(N-p-1)) alpha=0.05

def f(x,a):## a=0 means confidence , a=1 means prediction x=np.array([1,x]) # stats.t.ppf(0.975,df=N-p-1) # The point at which the cumulative probability is 1 - alpha /2 range=stats.t.ppf(0.975,df=N-p-1)*RSE*np.sqrt(a+x@U@x.T) lower=x@beta_hat-range upper=x@beta_hat+range return ([lower,upper])

# example stats.t.ppf(0.975,df=1)# the point Corresponding to p

12.706204736432095

x_seq=np.arange(-10,10,0.1) # Confidence interval lower_seq1=[]; upper_seq1=[] for i in range(len(x_seq)): lower_seq1.append(f(x_seq[i],0)[0]); upper_seq1.append(f(x_seq[i],0)[1]) # prediction interval lower_seq2=[]; upper_seq2=[] for i in range(len(x_seq)): lower_seq2.append(f(x_seq[i],1)[0]); upper_seq2.append(f(x_seq[i],1)[1]) # Predicted value by regression yy=beta_hat[0]+beta_hat[1]*x_seq

---

<!-- Página 52 -->

42 2 Linear Regression

plt.xlim(np.min(x_seq),np.max(x_seq)) plt.ylim(np.min(lower_seq1),np.max(upper_seq1)) plt.plot(x_seq,yy,c="black") plt.plot(x_seq,lower_seq1,c="blue") plt.plot(x_seq,upper_seq1,c="red") plt.plot(x_seq,lower_seq2,c="blue",linestyle="dashed") plt.plot(x_seq,upper_seq2,c="red",linestyle="dashed") plt.xlabel("x") plt.ylabel("y")

Text(0, 0.5, ’y’)

Appendix: Proofs of Propositions

Proposition 12 Two Gaussian random variables are independent if and only if their covariance is zero.

22 Proof Let X ∼ N(μ X , σ ) and Y ∼ N(μ Y , σ ), and let E[·] be the expectation X Y operation. If we let

E(X − μ X )(Y − μ Y ) ρ := √√(2.23) 22 E(X − μ X )E(Y − μ Y )

and define the independence of X andY by the property fX (x)fY (y) = fXY (x, y) for all x, y ∈ R, where {} 11 2 fX (x) = √exp− (x − μ X ) 2 2πσX2σ X {} 11 2 fY (y) = √exp− (y − μ Y ) 2 2πσY2σ Y 1 fXY (x, y) = √ 2 2πσX σY1 − ρ {[ ( )2( ) ( ) 1x − μ Xx − μ Xy − μ Y × exp− − 2ρ 2 2(1 − ρ)σXσXσY ]} ( )2 x − μ X +, σX

---

<!-- Página 53 -->

Exercises 1–18 43

then ρ = 0 ⇒ fXY (x, y) = fX (x)fY (y). On the other hand, if fXY (x, y) = fX (x)fY (y), then we can write the numerator of ρ in (2.23) as follows: ∫ ∫ ∞∞ (x − μ X )(y − μ Y )fXY (x, y)dxdy −∞−∞ ∫ ∫ ∞∞ =(x − μ X )fX (x)dx(y − μ Y )fY (y)dy −∞−∞ = 0 ,

which means that ρ = 0 ⇐ fXY (x, y) = fX (x)fY (y). 

Proposition 13 The eigenvalues of H and I − H are only zeros and ones, and the dimensions of the eigenspaces of H and I − H with eigenvalues one and zero, respectively, are both p+1, while the dimensions of the eigenspaces of H and I −H with eigenvalues of zero and one, respectively, are both N − p − 1.

T −1T Proof Using Proposition 4, from H = X(X X)X and rank(X) = p + 1, we have

T −1 rank(H ) ≤ min{rank(X(X X)), rank(X)} ≤ rank(X) = p + 1 .

On the other hand, from Proposition 4 and H X = X, rank(X) = p + 1, we have

rank(H ) ≥ rank(H X) = rank(X) = p + 1 .

Therefore, we have rank(H ) = p + 1. Moreover, from H X = X, the columns of X are the basis of the image of H and the eigenvectors of H for an eigenvalue of one. Since the dimension of the image of H is p + 1, the dimension of the kernel is N − p − 1 (the eigenspace of an eigenvalue of zero). Moreover, for an arbitrary p+1 x ∈ R, we have (I − H )x = 0 ⇐⇒ H x = x and (I − H )x = x ⇐⇒ H x = 0, which means that the eigenspaces of H and I − H for eigenvalues of zero and one are the same as the eigenspaces of I − H and H for eigenvalues one and zero, respectively. 

Exercises 1–18

1. For a given x1, . . . , x N , y1, . . . , y N ∈ R, let ˆβ0, ˆβ1 be the β0, β1 ∈ R that N ∑ 2 minimizes L :=(y i − β0 − β1x i ). Show the following equations, where i=1 NN 1∑1∑ ¯x and ¯y are defined by x i and y i . NN i=1i=1

---

<!-- Página 54 -->

44 2 Linear Regression

(a) ˆβ0 + ˆβ1 ¯x = ¯y (b) Unless x1 = . . . = x N ,

N ∑ (x i − ¯x)(y i − ¯y) i=1 ˆβ= 1 N ∑ 2 (x i − ¯x) i=1

∂L∂L Hint: Item (a) is obtained from = 0. For (b), substitute (a) into = ∂β0∂β1 N ∑ −2x i (y i − β0 − β1x i ) = 0 and eliminate β0 . Then, solve it w.r.t. β1 first and i=1 obtain β0 later. 2. We consider the line l with the intercept ˆβ0 and slope ˆβ1 obtained in Problem 1. ′ Find the intercept and slope of the shifted line lfrom the data x1 − ¯x, . . . , x N − ¯x and y1 − ¯y, . . . , y N − ¯y. How do we obtain the intercept and slope of l from those ′ of the shifted line l? ′ 3. We wish to visualize the relation between the lines l, lin Problem 2. Fill Blanks (1) and (2) below and draw the graph.

def min_sq(x,y):# function for finding the intercept and coefficient of the least-squares x_bar,y_bar=np.mean(x),np.mean(y) beta_1=np.dot(x-x_bar,y-y_bar)/np.linalg.norm(x-x_bar)**2 beta_0=y_bar-beta_1*x_bar return [beta_1,beta_0]

N=100 a=np.random.normal(loc=2,scale=1)# mean, variance, size b=randn(1)# coefficient x=randn(N) y=a*x+b+randn(N)

a1,b1=min_sq(x,y)# estimating xx=x-# blank(1) # yy=y-# blank(2) # a2,b2=min_sq(xx,yy)# estimating after centering

(1.7865393047324676, 1.067565008452225e-16)

x_seq=np.arange(-5,5,0.1) y_pre=x_seq*a1+b1 yy_pre=x_seq*a2+b2 plt.scatter(x,y,c="black") plt.axhline(y=0,c="black",linewidth=0.5) plt.axvline(x=0,c="black",linewidth=0.5) plt.plot(x_seq,y_pre,c="blue",label="before centering") plt.plot(x_seq,yy_pre,c="orange",label="after centering") plt.legend(loc="upper left")

---

<!-- Página 55 -->

Exercises 1–18 45

m×m 4. Let m, n be positive integers. Suppose that the matrix A ∈ Rcan be written T n×m by A = B B for some B ∈ R.

m (a) Show that Az = 0 ⇐⇒ Bz = 0 for arbitrary z ∈ R. Hint: Use Az = 0 ⇒ T T 2 z B Bz = 0 ⇒ ‖Bz‖= 0. (b) Show that the ranks of A and B are equal. Hint: Because the kernels of A and B are equal so are the dimensions (ranks) of the images.

N×(p+1) In the following, the leftmost column of X ∈ Rconsists of all ones.

T 5. For each of the following cases, show that X X is not invertible:

(a) N < p + 1. (b) N ≥ p + 1 and different columns are equal in X.

N×(p+1) In the following, the rank of X ∈ Ris p + 1.

p+1 2 6. We wish to obtain β ∈ Rthat minimizes L := ‖y − Xβ‖from X ∈ √ √ N √∑ N×(p+1)N √ 2T R, y ∈ R, where ‖ · ‖ denoteszfor z = [z1, · · · , zN ]. i i=1 (a) Let x i,j be the (i, j )-th element of X. Show that the partial derivative of L = ⎛⎞2 Np ∑∑ 1 ⎝y −x β ⎠w.r.t. β is the j -th element of −X T y + X T Xβ. i i,j jj 2 i=1j =0 N ∑ T T Hint: The j -th element of X y isx i,j y i , the (j, k)-th element of X X is i=1 NpN ∑∑∑ T x i,j x i,k , and the j -th element of X Xβ isx i,j x i,k β k . i=1k=0i=1 ∂L p+1 (b) Find β ∈ Rsuch that = 0. In the sequel, we write the value by ˆβ. ∂β

7. Suppose that the random variable ˆβ is obtained via the procedure in Problem 6, N×(p+1) N where we assume that X ∈ Ris given and y ∈ Ris generated by p+1 2 Xβ +  with unknown constants β ∈ Rand σ > 0 and random variable 2  ∼ N(0, σ I ).

T −1T (a) Show ˆβ = β + (X X)X . (b) Show that the average of ˆβ coincides with β, i.e., ˆβ is an unbiased estimator. T 2T −1 (c) Show that the covariance matrix of ˆβ is E( ˆβ − β)( ˆβ − β) = σ (X X).

T −1T N×N 8. Let H := X(X X)X ∈ Rand ˆy := X ˆβ. Show the following equations:

2 (a) H = H , 2 (b) (I − H )= I − H , (c) H X = X,

---

<!-- Página 56 -->

46 2 Linear Regression

(d) ˆy = Hy, (e) y − ˆy = (I − H ), 2 T (f) ‖y − ˆy‖=  (I − H ).

9. Prove the following statements:

(a) The dimension of the image, rank, of H is p + 1. Hint: We assume that the rank of X is p + 1. (b) H has eigenspaces of eigenvalues of zero and one, and their dimensions are N − p − 1 and p + 1, respectively. Hint: The number of columns N in H is the sum of the dimensions of the image and kernel. (c) I − H has eigenspaces of eigenvalues of zero and one, and their dimensions p+1 are p + 1 and N − p − 1, respectively. Hint: For an arbitrary x ∈ R, we have (I − H )x = 0 ⇐⇒ H x = x and (I − H )x = x ⇐⇒ H x = 0.

T 10. Using the fact that P (I − H )P becomes a diagonal matrix such that the first N − p − 1 and last p + 1 diagonal elements are ones and zeros, respectively, for an orthogonal P , show the following: ∑ T N−p−12 (a) RSS :=  (I − H ) = v, where v := P . Hint: Because P i=1 i T −1T is orthogonal, we have P P = I . Substitute  = P v = P v into the T definition of RSS and find that the diagonal elements of P (I − H )P are the N eigenvalues. In particular, I − H has N − p − 1 and p + 1 eigenvalues of zero and one, respectively. T 2 T T T (b) Evv = σ ˜I . Hint: Use Evv = P (E )P . 2 2 (c) RSS/σ ∼ χ N−p−1 2 (the χdistribution with N − p − 1 degrees of freedom). Hint: Find the statistical properties from (a) and (b).

Use the fact that the independence of Gaussian random variables is equivalent to the covariance matrix of them being diagonal, without proving it. T T 11. (a) Show that E( ˆβ − β)(y − ˆy) = 0. Hint: Use ( ˆβ − β)(y − ˆy) = T −1T T T 2 (X X)X  (I − H ) and E = σ I . T −1 (b) Let B0, . . . , Bp be the diagonal elements of (X X). Show that ( ˆβ i − √ 2 β i )/(Bi σ ) and RSS/σ are independent for i = 0, 1, . . . , p. Hint: Since RSS is a function of y − ˆy, the problem reduces to independence between y − ˆy and ˆβ − β. Because they are Gaussian, it is sufficient to show that the covariance is zero.√ RSS (c) Let ˆσ :=(the residual standard error, an estimate of σ ), and N − p − 1 √ SE( ˆβ i ) := ˆσ Bi (an estimate of the standard error of ˆβ i ). Show that

ˆβ − β i i ∼ tN−p−1, i = 0, 1, . . . , p SE( ˆβ i )

(the t distribution with N − p − 1 degrees of freedom). Hint: Derive

---

<!-- Página 57 -->

Exercises 1–18 47

√ // ˆβ − β ˆβ − β RSS i ii i = √(N − p − 1) 2 SE( ˆβ i ) σ Biσ

and show that the right-hand side follows a t distribution. (d) When p = 1, find B0 and B1 , letting (x1,1, . . . , x N,1) = (x1, . . . , x N ). Hint: Derive ⎡⎤ N ∑ 1 2 1 T −1 ⎢xi − ¯x⎥ (X X)= ⎣N⎦ . Ni=1 ∑ 2 (x i − ¯x)− ¯x 1 i=1

Use the fact that independence of Gaussian random variables U1, . . . , U m, V1, . . . , V N is equivalent to a covariance matrix of size m × n being a diagonal matrix, without proving it. 12. We wish to test the null hypothesis H0 : β i = 0 versus its alternative H1 : β i  = 0. For p = 1, we construct the following procedure using the fact that under H0 ,

ˆβ − 0 i t = ∼ tN−p−1 , SE( ˆβ i ) ∫ ∞ where the function stats.t.cdf(x,m) returns the value offm (t)dt, x where fm is the probability density function of a t distribution with m degrees of freedom.

N=100 x=randn(N); y=randn(N) beta_1,beta_0=min_sq(x,y) RSS=np.linalg.norm(y-beta_0-beta_1*x)**2 RSE=np.sqrt(RSS/(N-1-1)) B_0=(x.T@x/N)/np.linalg.norm(x-np.mean(x))**2 B_1=1/np.linalg.norm(x-np.mean(x))**2 se_0=RSE*np.sqrt(B_0) se_1=RSE*np.sqrt(B_1) t_0=beta_0/se_0 t_1=beta_1/se_1 p_0=2*(1-stats.t.cdf(np.abs(t_0),N-2)) p_1=2*(1-stats.t.cdf(np.abs(t_1),N-2)) beta_0,se_0 ,t_0 ,p_0#intercept beta_1,se_1,t_1,p_1# coefficient

Examine the outputs using the stats_model package and linear_model function in the Python language.

from sklearn import linear_model

---

<!-- Página 58 -->

48 2 Linear Regression

reg=linear_model.LinearRegression() x=x.reshape(-1,1)# we need to indicate the size of the arrangement in sklearn y=y.reshape(-1,1)# If we set one of the dimensions and set the other to -1, it will automatically adjust itself. reg.fit(x,y)# execute reg.coef_,reg.intercept_# coefficient; beta_1, intercept; beta_0

import statsmodels.api as sm

X=np.insert(x,0,1,axis=1) model=sm.OLS(y,X) res=model.fit() print(res.summary())

13. The following procedure repeats estimating ˆβ1 one thousand times (r = 1000) and draws a histogram of ˆβ1/SE(β1), where beta_1/se_1 is computed each time from the data, and they are accumulated in the vector T of size r.

N=100; r=1000 T=[] for i in range(r): x=randn(N); y=randn(N) beta_1,beta_0=min_sq(x,y) pre_y=beta_0+beta_1*x# the predicted value of y RSS=np.linalg.norm(y-beta_0-beta_1*x)**2 RSE=np.sqrt(RSS/(N-1-1)) B_0=(x.T@x/N)/np.linalg.norm(x-np.mean(x))**2 B_1=1/np.linalg.norm(x-np.mean(x))**2 se_1=RSE*np.sqrt(B_1) T.append(beta_1/se_1) plt.hist(T,bins=20,range=(-3,3),density=True) x=np.linspace(-4,4,400) plt.plot(x,stats.t.pdf(x,1)) plt.title("the null hypothesis holds") plt.xlabel(’the value of t’) plt.ylabel(’probability density’)

Replace y=randn(N) with y=0.1*x+randn(N) and execute it. Further- more, explain the difference between the two graphs. N ∑ 1 N×N 14. Suppose that each element of W ∈ Ris 1/N, thus ¯y = y i = Wy N i=1 T for y = [y1, · · · , y N ].

(a) Show that H W = W and (I − H )(H − W ) = 0. Hint: Because each column of W is an eigenvector of eigenvalue one in H , we have H W = W . 2 2 2 (b) Show that ESS := ‖ ˆy − ¯y‖= ‖(H − W )y‖and T SS := ‖y − ¯y‖= 2 ‖(I − W )y‖. 2 2 (c) Show that RSS = ‖(I − H )‖= ‖(I − H )y‖and ESS are independent Hint: The covariance matrix of (I − H ) and (H − W )y is that of (I − H )

---

<!-- Página 59 -->

Exercises 1–18 49

T and (H − W ). Evaluate the covariance matrix E(I − H ) (H − W ). Then, use (a). 2 2 2 (d) Show that ‖(I − W )y‖= ‖(I − H )y‖+ ‖(H − W )y‖, i.e., T SS = RSS + ESS. Hint: (I − W )y = (I − H )y + (H − W )y.

N×p In the following, we assume that X ∈ Rdoes not contain a vector of size N of all ones in the leftmost column.

N×p N 15. Given X ∈ Rand y ∈ R, we refer to

ESSRSS 2 R= = 1 − T SS T SS

as to the coefficient of determination. For p = 1, suppose that we are given T x = [x1, . . . , x N ].

(a) Show that ˆy − ¯y = ˆβ1(x − ¯x). Hint: Use ˆy i = ˆβ0 + ˆβ1x i and Problem 1(a). ˆβ2‖x − ¯x‖2 2 1 (b) Show that R= . 2 ‖y − ¯y‖ 2 (c) For p = 1, show that the value of Rcoincides with the square of the N ∑ 2 2 correlation coefficient. Hint: Use ‖x − ¯x‖=(x i − ¯x)and Problem 1(b). i=1 (d) The following function computes the coefficient of determination:

def R2(x,y): n=x.shape[0] xx=np.insert(x,0,1,axis=1) beta=np.linalg.inv(xx.T@xx)@xx.T@y y_hat=xx@beta y_bar=np.mean(y) RSS=np.linalg.norm(y-y_hat)**2 TSS=np.linalg.norm(y-y_bar)**2 return 1-RSS/TSS N=100; m=2; x=randn(N,m); y=randn(N); R2(x,y)

Let N=100 and m=1, and execute x=randn(N); y=randn(N); R2(x,y); np.corrcoef(x,y)^2.

16. The coefficient of determination expresses how well the covariates explain the response variable, and its maximum value is one. When we evaluate how redundant a covariate is when the other covariates are present, we often use VIFs (variance inflation factors)

1 V I F := , 2 1 − R X j |X−j

2 where Ris the coefficient of determination of the j -th covariate in X j |X−j N×p N X ∈ Rgiven the other p − 1 covariates (y ∈ Ris not used). The larger the VIF value, the better the covariate is explained by the other covariates (the

---

<!-- Página 60 -->

50 2 Linear Regression

minimum value is one), which means that the collinearity is strong. Install the sklearn.datasets and compute the VIF values for each variable in the Boston dataset by filling the blank. (Simply execute the following).

from sklearn.datasets import load_boston

boston=load_boston() p=x.shape[1]; values=[] for j in range(p): S=list(set(range(p))-{j}) values.append(# blank #) values

p+1 17. We can compute the prediction value x∗ ˆβ for each x∗ ∈ R(the row vector whose first value is one), using the estimate ˆβ.

2T −1T (a) Show that the variance of x∗ ˆβ is σ x∗(X X)x . Hint: Use V ( ˆβ) = ∗ 2T −1 σ (X X). √ TT −1T (b) If we let SE(x ˆβ) := ˆσ x∗(X X)x , show that ∗ ∗

x∗ ˆβ − x∗β ∼ tN−p−1 , SE(x∗ ˆβ) √ where ˆσ = RSS/(N − p − 1). (c) The actual value of y can be expressed by y∗ := x∗β + . Thus, the variance 2 of y∗ − x∗ ˆβ is σ larger. Show that

x∗ ˆβ − y∗ √∼ tN−p−1 . T −1T ˆσ 1 + x∗(X X)x ∗

18. From Problem 17, we have √ TTT −1 x ∗ ˆβ ± tN−p−1(α/2) ˆσx ∗ (X X)x∗

√ TT −1 y∗ ± tN−p−1(α/2) ˆσ1 + x ∗ (X X)x∗

(the confidence and prediction intervals, respectively), where f is the t distribu- tion with N − p − 1 degrees of freedom. tN−p−1(α/2) is the t-statistic such that ∫ ∞ α/2 = f (u)du. Suppose that p = 1. We wish to draw the confidence and t prediction intervals in red and blue, respectively, for x∗ ∈ R. For the confidence interval, we expressed the upper and lower limits by red and blue solid lines, respectively, executing the procedure below. For the prediction interval, define the function g(x) and overlay the upper and lower dotted lines in red and blue on the same graph.

---

<!-- Página 61 -->

Exercises 1–18 51

N=100; p=1 X=randn(N,p) X=np.insert(X,0,1,axis=1) beta=np.array([1,1]) epsilon=randn(N) y=X@beta+epsilon

# definition of f(x) and g(x) U=np.linalg.inv(X.T@X) beta_hat=U@X.T@y RSS=(y-X@beta_hat).T@(y-X@beta_hat) RSE=np.sqrt(RSS/(N-p-1)) alpha=0.05 def f(x): x=np.array([1,x]) # stats.t.ppf(0.975,df=N-p-1) # the point at which the cumulative probability is 1-alpha/2_ range=stats.t.ppf(0.975,df=N-p-1)*RSE*np.sqrt(x@U@x.T) lower=x@beta_hat-range upper=x@beta_hat+range return ([lower,upper])

x_seq=np.arange(-10,10,0.1) lower_seq1=[]; upper_seq1=[] for i in range(len(x_seq)): lower_seq1.append(f(x_seq[i],0)[0]) upper_seq1.append(f(x_seq[i],0)[1]) yy=beta_hat[0]+beta_hat[1]*x_seq

plt.xlim(np.min(x_seq),np.max(x_seq)) plt.ylim(np.min(lower_seq1),np.max(upper_seq1)) plt.plot(x_seq,yy,c="black") plt.plot(x_seq,lower_seq1,c="blue") plt.plot(x_seq,upper_seq1,c="red") plt.plot(x_seq,lower_seq2,c="blue",linestyle="dashed") plt.plot(x_seq,upper_seq2,c="red",linestyle="dashed") plt.xlabel("x") plt.ylabel("y")

---

<!-- Página 62 -->

## Chapter 3

# Classification

Abstract In this chapter, we consider constructing a classification rule from covari- ates to a response that takes values from a finite set such as ±1, figures 0, 1, · · · , 9. For example, we wish to classify a postal code from handwritten characters and to make a rule between them. First, we consider logistic regression to minimize the error rate in the test data after constructing a classifier based on the training data. The second approach is to draw borders that separate the regions of the responses with linear and quadratic discriminators and the k-nearest neighbor algorithm. The linear and quadratic discriminations draw linear and quadratic borders, respectively, and both introduce the notion of prior probability to minimize the average error probability. The k-nearest neighbor method searches the border more flexibly than the linear and quadratic discriminators. On the other hand, we take into account the balance of two risks, such as classifying a sick person as healthy and classifying a healthy person as unhealthy. In particular, we consider an alternative approach beyond minimizing the average error probability. The regression method in the previous chapter and the classification method in this chapter are two significant issues in the field of machine learning.

3.1 Logistic Regression

We wish to determine a decision rule from p covariates to a response that takes two p values. More precisely, we derive the map x ∈ R→ y ∈ {−1, 1} from the data p (x1, y1), . . . , (x N , y N ) ∈ R× {−1, 1} that minimizes the error probability.

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 202153 J. Suzuki, Statistical Learning with Math and Python, https://doi.org/10.1007/978-981-15-7877-9_3

---

<!-- Página 63 -->

54 3 Classification

Fig. 3.1 As the value of β Logistic Curve increases, the probability of y = 1 increases1.00 0.2 monotonically and changes 0.5 greatly from approximately 01 0.8 to approximately 1 near2 10 x = 0 ) x | 0.6 = 1 Y ( 0.4 P

0.2

0.0 -10 -5 0 5 10 x

p In this section, we assume that for x ∈ R(row vector), the probabilities of β+xβ e 01 1 y = 1 and y = −1 are expressed by and , respectively, 1 + e β0+xβ 1 + e β0+xβ p for some β0 ∈ R and β ∈ Rand write the probability of y ∈ {−1, 1} as

1 −y(β+xβ) 1 + e0

(logistic regression). To roughly explain the function (the sigmoid function), we draw the graph for p = 1, β0 = 0, β > 0, and y = 1:

1 f (x) = , x ∈ R . −(β+xβ) 1 + e0

Example 29 We ran the following program, and the graph is shown in Fig. 3.1:

def f(x): return np.exp(beta_0+beta*x)/(1+np.exp(beta_0+beta*x))

beta_0=0 beta_seq=np.array([0,0.2,0.5,1,2,10]) x_seq=np.arange(-10,10,0.1) plt.xlabel("x") plt.ylabel("P(Y=1|x)") plt.title("logistic curve") for i in range(beta_seq.shape[0]): beta=beta_seq[i] p=f(x_seq) plt.plot(x_seq,p,label=’{}’.format(beta)) plt.legend(loc=’upper left’)

1 p+1 p In this chapter, instead of β ∈ R, we separate the slope β ∈ Rand the intercept β0 ∈ R.

---

<!-- Página 64 -->

3.1 Logistic Regression 55

From

−(β+xβ) e0 ′ f (x) = β ≥ 0 −(β+xβ) 2 (1 + e0)

−(β0+xβ)−(β0+xβ) ′′2 e[1 − e] f (x) = −β, −(β+xβ) 3 (1 + e0)

we see that f (x) is increasing monotonically and is convex and concave when x < −β0/β and x > −β0/β, respectively; they change at x=0, when β0 = 0. p In the following, from the observations (x1, y1), . . . , (x N , y N ) ∈ R× {−1, 1}, N ∏1 by maximizing the likelihood(maximum likelihood), or mini- 1 + e−y i (β0+x i β) i=1 mizing the negative log-likelihood:

N ∑ −y (β+x β) l(β0, β) =log(1 + vi ), vi = ei 0i , i = 1, . . . , N, i=1

p we obtain the estimate β0 ∈ R, β ∈ R.

Example 30 If the observations are

i 1 2 3 · · · 25 xi 71.2 29.3 42.3 · · · 25.8 yi −1 −1 1 · · · 1

(p = 1, N = 25), the likelihood to be maximized is

111 · · 1 + exp(β0 + 71.2β1) 1 + exp(β0 + 29.3β1) 1 + exp(−β0 − 42.3β1) 1 · · · . 1 + exp(−β0 − 25.8β1)

Note that the observations are known, and we determine β0, β1 so that the likelihood is maximized.

However, for logistic regression, unlike for linear regression, no formula to obtain the estimates of the coefficients exists.

---

<!-- Página 65 -->

56 3 Classification

3.2 Newton–Raphson Method

When we solve the equations such as the partial derivatives of l(β0, β) being zero, the Newton–Raphson method is often used. To understand the essence, briefly, we consider the purest example of the use of the Newton–Raphson method. Suppose that we solve f (x) = 0 with

2 f (x) = x− 1 .

We set an initial value x = x0 and draw the tangent that goes through the point (x0, f (x0)). If the tangent crosses the x-axis (y = 0) at x = x1 , then we again draw the tangent that intersects the point (x1, f (x1)). If we repeat the process, the sequence x0, x1, x2, . . . approaches the solution of f (x) = 0. In general, because ′ the tangent line is y − f (x i ) = f (x i )(x − x i ), the intersection with y = 0 is

f (x i ) x i+1 := x i − (3.1) ′ f (x i )

for i = 0, 1, 2, · · · . If more than one solution exists, the solution obtained by the convergence may depend on the initial value of x0 . In the current case, if we set x0 = −2, the solution converges to x = −1. In addition, we need to decide when the cycle should be terminated based on some conditions, such as the size of |x i+1 − x i | and the number of repetitions.

Example 31 For x0 = 4, we run the following Python program to obtain the graph in Fig. 3.2. The program repeats the cycle ten times.

def f(x): return x**2-1 def df(x): return 2*x

x_seq=np.arange(-1,5,0.1) f_x=f(x_seq) plt.plot(x_seq,f_x) plt.axhline(y=0,c="black",linewidth=0.5) plt.xlabel("x") plt.ylabel("f(x)") x=4 for i in range(10): X=x; Y=f(x)# X,Y before updating x=x-f(x)/df(x)# x after updating y=f(x)# y after updating plt.plot([X,x],[Y,0],c="black",linewidth=0.8) plt.plot([X,X],[Y,0],c="black",linestyle="dashed",linewidth=0.8) plt.scatter(x,0,c="red")

---

<!-- Página 66 -->

3.2 Newton–Raphson Method 57

20

15 ) (x f 10

5

0

-1 0 1 2 3 4 5 x

Fig. 3.2 The Newton–Raphson method: starting from x0 = 4, the tangent that goes through (x0, f (x0)) and crosses the x-axis at x1 , and the tangent that goes through (x1, f (x1)) and crosses the x-axis at x2 , and so on. The sequence is obtained by the recursion x1 = x0 − ′′ f (x0)/f (x0), x2 = x1 − f (x1)/f (x1), . . .. The points in the sequence are marked in red

The Newton–Raphson method can even be applied to two variables and two equations: for { f (x, y) = 0 , g(x, y) = 0

we can see that (3.1) is extended to

⎡⎤−1 ∂f (x, y)∂f (x, y) [ ][ ][ ] xx⎢∂x∂y⎥f (x, y) ←−⎢⎥, (3.2) ⎣⎦ yy∂g(x, y)∂g(x, y)g(x, y) ∂x∂y ⎡⎤ ∂f (x, y)∂f (x, y) ⎢⎥ ∂x∂y ⎢⎥ where the matrixis called a Jacobian matrix. ⎣∂g(x, y)∂g(x, y)⎦ ∂x∂y

2 2 Example 32 For f (x, y) = x+ y− 1 and g(x, y) = x + y, if we start searching the solution from (x, y) = (3, 4), the execution is as follows:

def f(z): return z[0]**2+z[1]**2-1 def dfx(z): return 2*z[0] def dfy(z): return 2*z[1] def g(z): return z[0]+z[1]

---

<!-- Página 67 -->

58 3 Classification

def dgx(z): return 1 def dgy(z): return 1

z=np.array([3,4])# initial value for i in range(10): J=np.array([[dfx(z),dfy(z)],[dgx(z),dgy(z)]]) z=z-np.linalg.inv(J)@np.array([f(z),g(z)]) z

array([-0.70710678, 0.70710678])

p Then, we apply the same method to the problem of finding β0 ∈ R and β ∈ R such that ∇l(β0, β) = 0:

2−1 (β0, β) ← (β0, β) − {∇l(β0, β)} ∇l(β0, β) ,

∂f p+1 2 where ∇f (v) ∈ Ris a vector such that the i-th element is , and ∇f (v) ∈ ∂vi 2 ∂f (p+1)×(p+1) Ris a square matrix such that the (i, j )-th element is . In the ∂vi ∂vj p p+1 following, for ease of notation, we write (β0, β) ∈ R × Ras β ∈ R. If we differentiate the negative log-likelihood l(β0, β) and if we let vi = −y (β+x β)p+1 ei 0i , i = 1, . . . , N, the vector ∇l(β0, β) ∈ Rsuch that the j -th element ∂l(β0, β) T is , j = 0, 1, . . . , p, can be expressed by ∇l(β0, β) = −X u with ∂β j ⎡⎤ y1v1 ⎢1 + v⎥ 1 ⎢⎥ ⎢.⎥ u =., ⎢.⎥ ⎣y N vN⎦ 1 + vN

p+1 where β0 is regarded as the 0th element, and the i-th row of X is [1, x i ] ∈ R. If 22 we note y i = ±1, i.e., y= 1, the matrix ∇l(β0, β) such that the (j, k)-th element i 2 ∂l(β0, β) 2T is , j, k = 0, 1, . . . , p, can be expressed by ∇l(β0, β) = X W X with ∂β j β k ⎡⎤ v1 · · · 0 ⎢(1 + v1)2 ⎥ ⎢⎥ .. . W =⎢.. . .⎥. ⎢. .⎥ ⎣v⎦ N 0 · · · (1 + vN )2

---

<!-- Página 68 -->

3.2 Newton–Raphson Method 59

Using such W and u, the update rule can be written as

T −1T β ← β + (X W X)X u .

−1N In addition, if we introduce the variable z := Xβ + W u ∈ R, the formula becomes simpler:

T −1T β ← (X W X)X W z .

Example 33 We wrote a Python program that solves ∇l(β0, β) = 0 and executed it for the following data.

N=1000; p=2 X=randn(N,p) X=np.insert(X,0,1,axis=1) beta=randn(p+1) y=[] prob=1/(1+np.exp(X@beta)) for i in range(N): if (np.random.rand(1)>prob[i]): y.append(1) else : y.append(-1) # Data generation ends here beta# check

array([ 0.79985659, -1.31770628, -0.23553563])

# likelihood estimation beta=np.inf gamma=randn(p+1)# initial value of beta print (gamma) while (np.sum((beta-gamma)**2)>0.001): beta=gamma s=X@beta v=np.exp(-s*y) u=(y*v)/(1+v) w=v/((1+v)**2) W=np.diag(w) z=s+u/w gamma=np.linalg.inv(X.T@W@X)@X.T@W@z print (gamma)

[-1.00560507 0.44039528 -0.89669456] [ 1.73215544 -1.89462271 1.11707796] [-0.25983643 -0.38933759 -1.10645012] [ 0.81463839 -1.04443553 0.39176123] [ 0.7458049 -1.3256336 -0.08413818] [ 0.79163801 -1.41592785 -0.09332545] [ 0.7937899 -1.4203184 -0.09373029]

We found that the results were almost correct. For some cases, the maximum likelihood solution cannot be obtained even if we apply the Newton–Raphson method. For example, if the observations satisfy

---

<!-- Página 69 -->

60 3 Classification

p y i (β0 + x i β) ≥ 0, (x i , y i ) ∈ R× R, i = 1, . . . , N, then the maximum likelihood estimate of logistic regression cannot be obtained. In fact, the terms in the exponent part of

N ∏1 1 + exp{−y i (β0 + x i β)} i=1

can be all negative, which means that the exponent can diverge to −∞ if we multiply β0 and β by 2. Thus, the likelihood can approach one by choosing some β0 and β. Even if we do not meet such conditions, if p is large compared to N, the possibility of the parameter being infinitely large increases.

Example 34 For p = 1, we estimated the coefficients ˆβ0, ˆβ1 of logistic regression using the training data with N/2 samples and predicted the response of the covariate values in the N/2 test data.

# data genetration n=100 x=np.concatenate([randn(n)+1,randn(n)-1],0) y=np.concatenate([np.ones(n),-np.ones(n)],0) train=np.random.choice(2*n,int(n),replace=False)# indices for training data test=list(set(range(2*n))-set(train))# indices for test data X=np.insert(x[train].reshape(-1,1),0,1,axis=1) Y=y[train] # All 1 columns are added to the left of x

# The value may not converge with some initial value of gamma , so we may perform several times. p=1 beta=[0,0]; gamma=randn(p+1) print (gamma) while (np.sum((beta-gamma)**2)>0.001): beta=gamma s=X@beta v=np.exp(-s*Y) u=(Y*v)/(1+v) w=v/((1+v)**2) W=np.diag(w) z=s+u/w gamma=np.linalg.inv(X.T@W@X)@X.T@W@z print (gamma)

[0.20382031 0.19804102] [0.17521272 1.13479347] [0.29020473 1.72206578] [0.38156063 2.04529677] [0.40773631 2.1233337 ] [0.40906736 2.12699164]

def table_count(m,u,v): n=u.shape[0] count=np.zeros([m,m]) for i in range(n):

---

<!-- Página 70 -->

3.3 Linear and Quadratic Discrimination 61

count[int(u[i]),int(v[i])]+=1 return (count)

ans=y[test]# answer pred=np.sign(gamma[0]+x[test]*gamma[1])# predicted value ans=(ans+1)/2# Change from -1,1 to 0,1. pred=(pred+1)/2# Change from -1,1 to 0,1. table_count(3,ans, pred)

array([[41., 9.], [ 5., 45.]])

We set up a data frame with the pairs of covariate and response values and divided the N = 2n data into training and test sets of size n. The finally obtained values of y are the correct values, and we predicted each of the y values based on the estimates of β0 and β1 and whether each of the zs is positive or negative. The table expresses the numbers of correct and incorrect answers, and the correct rate in this experiment was (41 + 45)/100 = 0.86.

3.3 Linear and Quadratic Discrimination

p As before, we find the map x ∈ R→ y ∈ {−1, 1} to minimize the error p probability, given the observations x1, . . . , x N ∈ R, y1, . . . , y N ∈ {−1, 1}. In this p section, we assume that the distributions of x ∈ Rgiven y = ±1 are N(μ±1, ±1) and write the probability density functions by {} 11 T −1 f±1(x) = √exp− (x − μ±1) (x − μ±1). (3.3) p ±1 (2π) det 2

In addition, we introduce the notion of prior probabilities of events: we assume that the probabilities of responses y = ±1 are known before seeing the covariates x, which we term the prior probability. For example, we may estimate the probability of the response being π±1 from the ratio of the two from y1, . . . , y N in the training data. On the other hand, we refer to

π±1f±1(x) π1f1(x) + π−1f−1(x)

as the posterior probability of y = ±1 given x. We can minimize the error probability by estimating y = 1 if

π1f1(x)π−1f−1(x) ≥ , π1f1(x) + π−1f−1(x) π1f1(x) + π−1f−1(x)

---

<!-- Página 71 -->

62 3 Classification

which is equivalent to

π1f1(x) ≥ π−1f−1(x) , (3.4)

and y = −1 otherwise. The procedure assumes that f±1 follows a Gaussian distribution and that the expectation μ±1 and covariance matrix ±1 are known, and that π±1 is known. For actual situations, we need to estimate these entities from the training data. The principle of maximizing the posterior probability is applied not only to the binary case (K = 2) but also to the general case K ≥ 2, where K is the number of values that the response takes. The probability that response y = k given covariates x is P (y = k|x) for k = 1, . . . , K. If we estimate y = ˆk, then the probability of the ∑ estimate being correct is 1 − P (y = k|x) = P (y = ˆk|x). Thus, choosing a k = ˆk k that maximizes the posterior probability P (y = ˆk|x) as ˆk minimizes the average error probability when the prior probability is known. In the following, assuming K = 2 for simplicity, we see the properties at the border between y = ±1 when we maximize the posterior probability:

T −1T −1det 1π1 −(x − μ1) (x − μ1) + (x − μ−1) (x − μ−1) = log − 2 log , 1 −1 det −1π−1

where the equation is obtained from (3.3) and (3.4). In general, the border is a func- T −1T −1 tion of the quadratic forms x x and x x of x (quadratic discrimination). 1 −1

In particular, when 1 = −1 , if we write them as , the border becomes a surface (a line when p = 2), which we call linear discrimination. In fact, the terms T −1T −1 x x = x x are canceled out, and the border becomes 1 −1

π T −1T−1T−11 2(μ1 − μ−1) x − (μ 1 μ1 − μ −1 μ−1) = −2 log , π−1

or more simply,

μ+ μπ T −11 −11 (μ1 − μ−1) (x − ) = − log . 2 π−1

μ1 + μ−1 Thus, if π1 = π−1 , then the border is x = . 2 If π±1 and f±1 are unknown, we need to estimate them from the training data.

Example 35 For artificially generated data, we estimated the averages and covari- ances of covariates x for a response y = ±1, and drew the border.

# True parameters mu_1=np.array([2,2]); sigma_1=2; sigma_2=2; rho_1=0 mu_2=np.array([-3,-3]); sigma_3=1; sigma_4=1; rho_2=-0.8

---

<!-- Página 72 -->

3.3 Linear and Quadratic Discrimination 63

# generate data based on true parameters n=100 u=randn(n); v=randn(n) x_1=sigma_1*u+mu_1[0]; y_1=(rho_1*u+np.sqrt(1-rho_1**2)*v)*sigma_2+mu_1[1] u=randn(n); v=randn(n) x_2=sigma_3*u+mu_2[0]; y_2=(rho_2*u+np.sqrt(1-rho_2**2)*v)*sigma_4+mu_2[1]

# estimate the parameters from the data mu_1=np.average((x_1,y_1),1); mu_2=np.average((x_2,y_2),1) df=np.array([x_1,y_1]); mat=np.cov(df,rowvar=1); inv_1=np.linalg.inv(mat); de_1=np.linalg.det(mat)# df=np.array([x_2,y_2]); mat=np.cov(df,rowvar=1); inv_2=np.linalg.inv(mat); de_2=np.linalg.det(mat)#

# substitute the parameters into the distribution formula def f(x,mu,inv,de): return(-0.5*(x-mu).T@inv@(x-mu)-0.5*np.log(de)) def f_1(u,v): return f(np.array([u,v]),mu_1,inv_1,de_1) def f_2(u,v): return f(np.array([u,v]),mu_2,inv_2,de_2)

# generate contour data # draw a boundary line where this value is 0 pi_1=0.5; pi_2=0.5 u=v=np.linspace(-6,6,50) m=len(u) w=np.zeros([m,m]) for i in range(m): for j in range(m): w[i,j]=np.log(pi_1)+f_1(u[i],v[j])-np.log(pi_2)-f_2(u[i],v[j])

# plotting Boundaries and Data plt.contour(u,v,w,levels=0,colors=[’black’]) plt.scatter(x_1,y_1,c="red") plt.scatter(x_2,y_2,c="blue")

We show the covariates for each response and the generated border in Fig. 3.3 (Right). If the covariance matrices are equal, we change the lines marked with "#" as follows:

# Linear Discrimination (Figure 2 . 3 left) (if we assume the variance is equal) # modify the lines marked with # as follows xx=np.concatenate((x_1-mu_1[0],x_2-mu_2[0]),0).reshape(-1,1) yy=np.concatenate((y_1-mu_1[1],y_2-mu_2[1]),0).reshape(-1,1) df=np.concatenate((xx,yy),1)# data was merged vertically. mat=np.cov(df,rowvar=0)# rowvar=0 because of the vertical direction inv_1=np.linalg.inv(mat) de_1=np.linalg.det(mat) inv_2=inv_1; de_2=de_1 w=np.zeros([m,m]) for i in range(m): for j in range(m): w[i,j]=np.log(pi_1)+f_1(u[i],v[j])-np.log(pi_2)-f_2(u[i],v[j]) plt.contour(u,v,w,levels=0,colors=[’black’]) plt.scatter(x_1,y_1,c="red") plt.scatter(x_2,y_2,c="blue")

---

<!-- Página 73 -->

64 3 Classification

66

44 22

00

-2-2 1 1

1 -6-6 -6 -4 -2 0 2 4 6-6 -4 -2 0 2 4 6

Fig. 3.3 Linear Discrimination (Left) and Quadratic Discrimination (Right): The border is a line if the covariance matrices are equal; otherwise, it is a quadratic (elliptic) curve. In the former case, if the prior probabilities and the covariance matrices are equal, then the border is the vertical bisector of the line connecting the centers

We show the output in Fig. 3.3 (Left).

Example 36 (Fisher’s Iris Dataset) Even when the response takes more than two values, we can choose the response with the maximum posterior probability. Fisher’s Iris dataset contains four covariates (the petal length, petal width, sepal length, and sepal width), and the response variable can be three species of irises (Iris setosa, Iris virginica, and Iris versicolor). Each of the three species contains 50 samples (N = 150, p = 4). We construct the classifier via quadratic discrimination and evaluate it using the test dataset that are different from the training data.

from sklearn.datasets import load_iris

iris=load_iris() iris.target_names x=iris.data y=iris.target n=len(x) train=np.random.choice(n,int(n/2),replace=False) test=list(set(range(n))-set(train)) # estimate parameter X=x[train,:] Y=y[train] mu=[] covv=[] for j in range(3): xx=X[Y==j,:] mu.append(np.mean(xx,0)) covv.append(np.cov(xx,rowvar=0))

# Definitions of distributions which we substitute the estimated parameters def f(w,mu,inv,de): return -0.5*(w-mu).T@inv@(w-mu)-0.5*np.log(de) def g(v,j): return f(v,mu[j],np.linalg.inv(covv[j]),np.linalg.det(covv[j]))

---

<!-- Página 74 -->

3.4 k-Nearest Neighbor Method 65

z=[] for i in test: z.append(np.argsort([-g(x[i,],0),-g(x[i,],1),-g(x[i,],2)])[0]) table_count(3,y[test],z)

array([[27., 0., 0.], [ 0., 20., 4.], [ 0., 0., 24.]])

If the prior probabilities of the three species are not equal, for example, if those of Iris setosa, Iris virginica, and Iris versicolor are 0.5, 0.25, and 0.25, respectively, then, we add the logarithm of the prior probabilities to the variables a,b,c in the program.

3.4 k-Nearest Neighbor Method

The k-nearest neighbor method does not require constructing a specific rule from p the training data (x1, y1), . . . , (x N , y N ) ∈ R×(finite set). Suppose that given new p data x∗ ∈ R, x i , i ∈ S, are the k training data such that the distances between x i and x∗ are the smallest, where S is a subset of {1, · · · , n} of size k. The k-nearest neighbor method predicts the response y∗ of x∗ by the majority of y i , i ∈ S.). For example, suppose that N = 5, p = 1 and that the data are given as below. If k = 3 and x∗ = 1.6, then S = {3, 4, 5} and the majority class is y∗ = 0. If k = 2 and x∗ = −2.2, then S = {1, 2}. However, in that case, the majority is not unique. Then, we remove one element from S. Because x1 = −2.1 is close to x∗ = −2.2, we set S = {2} and y∗ = −1.

xi −2.1 −3.7 1.3 0.4 1.5 yi −1 1 0 0 1

For example, we may construct the following procedure for the k-nearest neighbor method that uses a tie-breaking rule, the m−1 responses among the closest m − 1 responses are compared when the majority among the closest m responses are not unique:

def knn_1(x,y,z,k): x=np.array(x); y=np.array(y) dis=[] for i in range(x.shape[0]): dis.append(np.linalg.norm(z-x[i,])) S=np.argsort(dis)[0:k]# k indices which The distance is close u=np.bincount(y[S])# count the number m=[i for i, x in enumerate(u) if x==max(u)]# index of high frequent # Processing of the brakings (if the frequency is more than 2) while (len(m)>1): k=k-1 S=S[0:k] u=np.bincount(y[S]) m=[i for i, x in enumerate(u) if x==max(u)]# index of high frequent return m[0]

---

<!-- Página 75 -->

66 3 Classification

If there is more than one majority class, we remove the i ∈ S such that the distance between x j and x∗ is the largest among x j , j ∈ Sj and continue to find the majority. If S contains exactly one element, eventually, we identify the majority class. For multiple x∗s, we may extend the above procedure to the following:

# generalize def knn(x,y,z,k): w=[] for i in range(z.shape[0]): w.append(knn_1(x,y,z[i,],k)) return w

We find that the smaller k, the more sensitive the border is to the training data.

Example 37 (Fisher’s Iris Dataset)

from sklearn.datasets import load_iris

iris=load_iris() iris.target_names x=iris.data y=iris.target n=x.shape[0] train=np.random.choice(n,int(n/2),replace=False) test=list(set(range(n))-set(train)) w=knn(x[train,],y[train],x[test,],k=3) table_count(3,y[test],w)

array([[25., 0., 0.], [ 0., 26., 4.], [ 0., 1., 19.]])

3.5 ROC Curves

Although maximizing the posterior probability is valid in many cases in the sense of minimizing the error probability, however, we may want to improve an alternative performance even if we lose the merit of minimizing the error probability. For example, during credit card screening, less than 3% of applicants have problems. In this case, if all the applications are approved, an error rate of 3% is attained. However, in that case, the card company claims that there are risks and rejects at least 10% of the applications. In cancer screening, although only 3% of people have cancer, more than 20% of people who have been screened are diagnosed with cancer. Considering a sick person as healthy is riskier than treating a healthy person as unhealthy. If a doctor does not want to take responsibility, he may judge more people as having cancer. In other words, depending on the balance between the risk of mistakenly considering a healthy person as sick (type I error) and the risk of assuming a sick

---

<!-- Página 76 -->

3.5 ROC Curves 67

Table 3.1 Examples of types I and II errors Type I Error Type II Error Quality control Identify good products asIdentify defective products as defectivegood Medical diagnosis Identify healthy people as sick Identify sick people as healthy Criminal investigation Identify the criminal as not aTreat noncriminals as criminals criminal Entrance exams Reject excellent students Allow inferior students to enter

person as healthy (type II error) (Table 3.1), the criterion for judgment differs. In other words, it is necessary to consider the optimality of each of the ways of balancing the risks. We use terms such as true positives, false positives, false negatives, and true negatives as defined below.

Sick Healthy Treating as sick True Positive False Positive Treating as healthy False Negative True Negative

The rates of the type I and type II errors are α and β, respectively, the power and false positive rate are defined as follows:

T P Power = = 1 − β T P + F N F P F alse P ositive Rate = = α. F P + T N

For each false positive rate (α), consider maximizing the power 1 − β (the Neyman–Pearson criterion ). In that case, there are countless ways of testing depending on how to balance the two values. The curve with the false positive rate on the horizontal axis and the power on the vertical axis is called the receiver operating characteristic (ROC) curve. The higher the curve goes to the upper-left corner of the plot, that is, the larger the area under the ROC curve (AUC, maximum of 1), the better the test performs.

Example 38 Let f1(x) and f0(x) be the distributions for a measurement x of people with a disease and healthy people, respectively. For each positive θ , the decision was made to determine whether the person had the symptom if

f1(x) ≥ θ . f0(x)

---

<!-- Página 77 -->

68 3 Classification

Fig. 3.4 The ROC curveROC Curve shows all the performances of the test for acceptable false1.0 positives

0.8

0.6 AUC= 0.9304883 0.4 True Positive

0.2

0.0 0.0 0.2 0.4 0.6 0.8 1.0 False Positive

In the following, the distributions of sick and healthy people are N(1, 1) and N(−1, 1), respectively, and the ROC curve is shown in Fig. 3.4:

N_0=10000; N_1=1000 mu_1=1; mu_0=-1# Sick :1 , Normal :0 var_1=1; var_0=1 x=np.random.normal(mu_0,var_0,N_0) y=np.random.normal(mu_1,var_1,N_1) theta_seq=np.exp(np.arange(-10,100,0.1)) U=[]; V=[] for i in range(len(theta_seq)): u=np.sum((stats.norm.pdf(x,mu_1,var_1)/stats.norm.pdf(x,mu_0,var_0))> theta_seq[i])/N_0 # Treat a person who are not sick as sick v=np.sum((stats.norm.pdf(y,mu_1,var_1)/stats.norm.pdf(y,mu_0,var_0))> theta_seq[i])/N_1 # Treating a sick person as sick U.append(u); V.append(v)

AUC=0# estimate the area for i in range(len(theta_seq)-1): AUC=AUC+np.abs(U[i+1]-U[i])*V[i]

plt.plot(U,V) plt.xlabel("False Positive") plt.ylabel("True Positive") plt.title("ROC curve") plt.text(0.3,0.5,’AUC={}’.format(AUC),fontsize=15)

Text(0.3, 0.5, ’AUC=0.9301908000000001’)

---

<!-- Página 78 -->

Exercises 19–31 69

Exercises 19–31

p p 19. We assume that there exist β0 ∈ R and β ∈ Rsuch that for x ∈ R, β0+xβ e 1 the probabilities of Y = 1 and Y = −1 are and , β+xβ β+xβ 1 + e 01 + e 0 respectively. Show that the probability of Y = y ∈ {−1, 1} can be written 1 as . −y(β+xβ) 1 + e0 1 20. For p = 1 and β > 0, show that the function f (x) = is −(β+xβ) 1 + e0 monotonically increasing for x ∈ R and convex and concave in x < −β0/β and x > −β0/β, respectively. How does the function change as β increases? Execute the following to answer this question:

def f(x): return np.exp(beta_0+beta*x)/(1+np.exp(beta_0+beta*x))

beta_0=0 beta_seq=np.array([0,0.2,0.5,1,2,10]) x_seq=np.arange(-10,10,0.1) plt.xlabel("x") plt.ylabel("P(Y=1|x)") plt.title("logistic curve") for i in range(beta_seq.shape[0]): beta=beta_seq[i] p=f(x_seq) plt.plot(x_seq,p,label=’{}’.format(beta)) plt.legend(loc=’upper left’)

p 21. We wish to obtain the estimates of β0 ∈ R and β ∈ Rby maximizing N ∏1 the likelihood, or equivalently, by minimizing the negated 1 + e−y i (β0+x i β) i=1 logarithm

N ∑ −y i (β0+x i β) l(β0, β) =log(1 + vi ), vi = e i=1

p from observations (x1, y1), . . . , (x N , y N ) ∈ R× {−1, 1} (maximum likeli- hood). Show that l(β0, β) is convex by obtaining the derivative ∇l(β0, β) and 22 the second derivative ∇l(β0, β). Hint: Let ∇l(β0, β) and ∇l(β0, β) be the ∂l column vector of size p + 1 such that the j -th element is and the matrix of ∂β j 2 ∂l size (p + 1) × (p + 1) such that the (j, k)-th element is , respectively. ∂β j ∂β k Simply show that the matrix is nonnegative definite. To this end, show that 2T T ∇l(β0, β) = X W X. If W is diagonal, then it can be written as W = U U ,

---

<!-- Página 79 -->

70 3 Classification

where the diagonal elements of U are the square roots of W , which means 2T ∇l(β0, β) = (U X) U X. 22. Solve the following equations via the Newton–Raphson method by constructing a Python program:

2 ′ (a) For f (x) = x− 1, set x = 2 and repeat the recursion x ← x − f (x)/f (x) 100 times. 2 2 (b) For f (x, y) = x+ y− 1, g(x, y) = x + y, set (x, y) = (1, 2) and repeat the recursion 100 times. ⎡⎤−1 ∂f (x, y)∂f (x, y) [ ][ ][ ] xx⎢∂x∂y⎥f (x, y) ←−⎢⎥ ⎣⎦ yy∂g(x, y)∂g(x, y)g(x, y) ∂x∂y

Hint: Define the procedure and repeat it one hundred times.

def f(z): return z[0]**2+z[1]**2-1 def dfx(z): return 2*z[0] def dfy(z): return 2*z[1] def g(z): return z[0]+z[1] def dgx(z): return 1 def dgy(z): return 1 z=np.array([1,2])# initial value

p 23. We wish to solve ∇l(β0, β) = 0, (β0, β) ∈ R × Rin Problem 21 via the Newton–Raphson method using the recursion

2−1 (β0, β) ← (β0, β) − {∇l(β0, β)} ∇l(β0, β) ,

p+1 2(p+1)×(p+1) where ∇f (v) ∈ Rand ∇f (v) ∈ Rare the vector such that ∂f the i-th element is and the square matrix such that the (i, j )-th element is ∂vi 2 ∂f , respectively. In the following, for ease of notation, we write (β0, β) ∈ ∂vi ∂vj p p+1 R × Rby β ∈ R. Show that the update rule can be written as

T −1T βnew ← (X W X)X W z , (3.5)

p+1 T (p+1)×(p+1) where u ∈ Rsuch that ∇l(βold) = −X u and W ∈ Rsuch 2T −1 that ∇l(βold) = X W X, z ∈ R is defined by z := Xβold + W u, and T X W X is assumed to be nonsingular. Hint: The update rule can be written as T −1T βnew ← βold + (X W X)X u.

---

<!-- Página 80 -->

Exercises 19–31 71

24. We construct a procedure to solve Problem 23. Fill in blanks (1)(2)(3), and examine that the procedure works.

N=1000; p=2 X=randn(N,p) X=np.insert(X,0,1,axis=1) beta=randn(p+1) y=[] prob=1/(1+np.exp(X@beta)) for i in range(N): if (np.random.rand(1)>prob[i]): y.append(1) else : y.append(-1) # # Data generation ends here beta# check

array([ 0.79985659, -1.31770628, -0.23553563])

# # likelihood estimation beta=np.inf gamma=randn(p+1)# print (gamma) while (np.sum((beta-gamma)**2)>0.001): beta=gamma s=X@beta v=np.exp(-s*y) u=# blank(1) # w=# blank(2) # W=np.diag(w) z=# blank(3) # gamma=np.linalg.inv(X.T@W@X)@X.T@W@z print (gamma)

p 25. If the condition y i (β0 + x i β) ≥ 0, (x i , y i ) ∈ R× R, i = 1, . . . , N is met, we cannot obtain the parameters of logistic regression via maximum likelihood. Why? 26. For p = 1, we wish to estimate the parameters of logistic regression from N/2 training data and to predict the responses of the N/2 test data that are not used as the training data. Fill in the blanks and execute the program.

# data genetration n=100 x=np.concatenate([randn(n)+1,randn(n)-1],0) y=np.concatenate([np.ones(n),-np.ones(n)],0) train=np.random.choice(2*n,int(n),replace=False)# indices for training data test=list(set(range(2*n))-set(train))# indices for test data X=np.insert(x[train].reshape(-1,1), 0, 1, axis=1) Y=y[train] # All 1 columns are added to the left of x

# The value may not converge with some initial value of gamma, so we may perform severaltimes. p=1 beta=[0,0]; gamma=randn(p+1)

---

<!-- Página 81 -->

72 3 Classification

print (gamma) while (np.sum((beta-gamma)**2)>0.001): beta=gamma s=X@beta v=np.exp(-s*Y) u=(Y*v)/(1+v) w=v/((1+v)**2) W=np.diag(w) z=s+u/w gamma=np.linalg.inv(X.T@W@X)@X.T@W@z print (gamma)

def table_count(m,u,v): n=u.shape[0] count=np.zeros([m,m]) for i in range(n): # blank(1) #+=1 return (count)

ans=y[test]# answer pred=# blank(2) # ans=(ans+1)/2# change from -1,1, to 0,1. pred=(pred+1)/2# change from -1,1, to 0,1. table_count(3,ans,pred)

Hint: For prediction, see whether β0 + xβ1 is positive or negative. 27. In linear discrimination, let π k be the prior probability of Y = k for k = 1, . . . , m (m ≥ 2), and let fk (x) be the probability density function of the p p p covariates x ∈ Rgiven response Y = k with mean μ k ∈ Rand covariance p×pp matrix k ∈ R. We consider the set Sk,l of x ∈ Rsuch that

π k fk (x)π l fl (x) = KK ∑∑ π j fj (x)π j fj (x) j =1j =1

for k, l = 1, . . . , m, k  = l.

p (a) Show that when π k = π l , Sk,l is the set of x ∈ Ron the quadratic surface

det T −1T −1k −(x − μ k ) (x − μ k ) + (x − μ l ) (x − μ l ) = log . k l det l

p (b) Show that when k = l (= ), Sk,l is the set of x ∈ Ron the surface T p a x +b = 0 with a ∈ Rand b ∈ R and express a, b using μ k , μ l , , π k , π l . (c) When π k = π l and k = l , show that the surface of (b) is x = (μ k + μ l )/2.

28. In the following, we wish to estimate distributions from two classes and draw a boundary line that determines the maximum posterior probability. If the covariance matrices are assumed to be equal, how do the boundaries change? Modify the program.

---

<!-- Página 82 -->

Exercises 19–31 73

# True parameters mu_1=np.array([2,2]); sigma_1=2; sigma_2=2; rho_1=0 mu_2=np.array([-3,-3]); sigma_3=1; sigma_4=1; rho_2=-0.8

# generate data based on true parameter n=100 u=randn(n); v=randn(n) x_1=sigma_1*u+mu_1[0]; y_1=(rho_1*u+np.sqrt(1-rho_1**2)*v)*sigma_2+mu_1[1] u=randn(n); v=randn(n) x_2=sigma_3*u+mu_2[0]; y_2=(rho_2*u+np.sqrt(1-rho_2**2)*v)*sigma_4+mu_2[1]

# estimate the parameters from the data mu_1=np.average((x_1,y_1),1); mu_2=np.average((x_2,y_2),1) df=np.array([x_1,y_1]); mat=np.cov(df,rowvar=1); inv_1=np.linalg.inv(mat); de_1=np.linalg.det(mat)# df=np.array([x_2,y_2]); mat=np.cov(df,rowvar=1); inv_2=np.linalg.inv(mat); de_2=np.linalg.det(mat)#

# substitute the parameters into the distribution formula def f(x,mu,inv,de): return(-0.5*(x-mu).T@inv@(x-mu)-0.5*np.log(de)) def f_1(u,v): return f(np.array([u,v]),mu_1,inv_1,de_1) def f_2(u,v): return f(np.array([u,v]),mu_2,inv_2,de_2)

# generate contour data # draw a boundary line where this value is 0 pi_1=0.5; pi_2=0.5 u=v=np.linspace(-6,6,50) m=len(u) w=np.zeros([m,m]) for i in range(m): for j in range(m): w[i,j]=np.log(pi_1)+f_1(u[i],v[j])-np.log(pi_2)-f_2(u[i],v[j]) # plotting Boundaries and Data plt.contour(u,v,w,levels=1,colors=[’black’]) plt.scatter(x_1,y_1,c="red") plt.scatter(x_2,y_2,c="blue")

Hint: Modify the lines marked with #. 29. Even in the case of three or more values, we can select the class that maximizes the posterior probability. From four covariates (length of sepals, width of sepals, length of petals, and width of petals) of Fisher’s iris data, we wish to identify the three types of irises (Setosa, Versicolor, and Virginica) via quadratic discrimination. Specifically, we learn rules from training data and evaluate them with test data. Assuming N = 150 and p = 4, each of the three irises contains 50 samples, and the prior probability is expected to be equal to 1/3. If we find that the prior probabilities of Setosa, Versicolor, and Virginica irises are 0.5, 0.25, 0.25, how should the program be changed to determine the maximum posterior probability?

---

<!-- Página 83 -->

74 3 Classification

from sklearn.datasets import load_iris

iris=load_iris() iris.target_names x=iris.data y=iris.target n=len(x) train=np.random.choice(n,int(n/2),replace=False) test=list(set(range(n))-set(train)) # estimate parameter X=x[train,:] Y=y[train] mu=[] covv=[] for j in range(3): xx=X[Y==j,:] mu.append(np.mean(xx,0)) covv.append(np.cov(xx,rowvar=0))

# Definitions of distributions which we substitute the estimated parameters def f(w,mu,inv,de): return -0.5*(w-mu).T@inv@(w-mu)-0.5*np.log(de) def g(v,j): return f(v,mu[j],np.linalg.inv(covv[j]),np.linalg.det(covv[j]))

z=[] for i in test: a=g(x[i,],0); b=g(x[i,],1); c=g(x[i,],2) if a<b: if b<c: z.append(2) else: z.append(1) else: z.append(0) u=y[test] count=np.zeros([3,3]) for i in range(int(n/2)): count[u[i],z[i]]+=1 count

30. In the k-nearest neighbor method, we do not construct a specific rule from p training data (x1, y1), . . . , (x N , y N ) ∈ R×(finite set). Suppose that given a new data x∗, x i , i ∈ S are the k training data such that the distances between x i and x∗ are the smallest, where S is a subset of {1, . . . , n} of size k. The k- nearest neighbor method predicts the response y∗ of x∗ by majority voting of y i , i ∈ S. If there is more than one majority, we remove the i ∈ S such that the distance between x j and x∗ is the largest among x j , j ∈ Sj and continue to find the majority. If S contains exactly one element, we obtain the majority. The following process assumes that there is one test data, but the method can be extended to cases where there is more than one test data. Then, apply the method to the data in Problem 29.

---

<!-- Página 84 -->

Exercises 19–31 75

def knn_1(x,y,z,k): x=np.array(x); y=np.array(y) dis=[] for i in range(x.shape[0]): dis.append(np.linalg.norm(z-x[i,],ord=2)) S=np.argsort(dis)[0:k]# k indices which The distance is close u=np.bincount(y[S])# count the number m=[i for i, x in enumerate(u) if x==max(u)]# index of high frequent # Processing of the brakings (if the frequency is more than 2) while (len(m)>1): k=k-1 S=S[0:k] u=np.bincount(y[S]) m=[i for i, x in enumerate(u) if x==max(u)]# index of high frequent return m[0]

31. Let f1(x) and f0(x) be the distributions for a measurement x of people with a disease and those without the disease, respectively. For each positive θ, the decision that the person had the symptoms was determined according to whether

f1(x) ≥ θ . f0(x)

In the following, we suppose that the distributions of sick and healthy people are N(1, 1) and N(−1, 1), respectively. Fill in the blank and draw the ROC curve.

N_0=10000; N_1=1000 mu_1=1; mu_0=-1# Sick :1, Normal :0 var_1=1; var_0=1 x=np.random.normal(mu_0,var_0,N_0) y=np.random.normal(mu_1,var_1,N_1) theta_seq=np.exp(np.arange(-10,100,0.1)) U=[]; V=[] for i in range(len(theta_seq)): u=np.sum((stats.norm.pdf(x,mu_1,var_1)/stats.norm.pdf(x,mu_0,var_0))> theta_seq[i])/N_0# Treat a person who are not sick as sick v=## blank ## U.append(u); V.append(v)

AUC=0# estimate the are for i in range(len(theta_seq)-1): AUC=AUC+np.abs(U[i+1]-U[i])*V[i]

plt.plot(U,V) plt.xlabel("False Positive") plt.ylabel("True Positive") plt.title("ROC curve") plt.text(0.3,0.5,’AUC={}’.format(AUC),fontsize=15)

---

<!-- Página 85 -->

## Chapter 4

# Resampling

Abstract Generally, there is not only one statistical model that explains a phe- nomenon. In that case, the more complicated the model, the easier it is for the statistical model to fit the data. However, we do not know whether the estimation result shows a satisfactory (prediction) performance for new data different from those used for the estimation. For example, in the forecasting of stock prices, even if the price movements up to yesterday are analyzed so that the error fluctuations are reduced, the analysis is not meaningful if no suggestion about stock price movements for tomorrow is given. In this book, choosing a more complex model than a true statistical model is referred to as overfitting. The term overfitting is commonly used in data science and machine learning. However, the definition may differ depending on the situation, so the author felt that uniformity was necessary. In this chapter, we will first learn about cross-validation, a method of evaluating learning performance without being affected by overfitting. Furthermore, the data used for learning are randomly selected, and even if the data follow the same distribution, the learning result may be significantly different. In some cases, the confidence and the variance of the estimated value can be evaluated, as in the case of linear regression. In this chapter, we will continue to learn how to assess the dispersion of learning results, called bootstrapping.

4.1 Cross-Validation

As we attempted in the previous chapter, it makes sense to remove some of the N tuples for test instead of using them all for estimation. However, in that case, the samples used for estimation are reduced, and a problem occurs, such as the estimation accuracy deteriorating. Therefore, a method called (k-fold) cross-validation (CV) was devised. Assum- ing that k is an integer that divides N, 1/k of the data are used for the test, and the other 1 − 1/k of the data are used to estimate the model; we change the test data and estimate the model k times and evaluate it by the average (Table 4.1). The

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 202177 J. Suzuki, Statistical Learning with Math and Python, https://doi.org/10.1007/978-981-15-7877-9_4

---

<!-- Página 86 -->

78 4 Resampling

Table 4.1 Rotation in the cross-validation approach. Each group consists of N/k samples, which NN2NN are divided into k groups based on the sample ID: 1 ∼ , + 1 ∼ , . . . , (k − 2) + 1 ∼ k k k k NN (k − 1) , (k − 1) + 1 ∼ N k k Group 1 Group 2 · · · Group k − 1 Group k First Test Estimate · · · Estimate Estimate Second Estimate Test · · · Estimate Estimate ... .. ... .. . . . . . (k − 1)-th Estimate Estimate · · · Test Estimate k-th Estimate Estimate · · · Estimate Test

process of evaluating the prediction error of linear regression is as follows (function cv_linear).

def cv_linear(X,y,K): n=len(y); m=int(n/K) S=0 for j in range(K): test=list(range(j*m,(j+1)*m))# indices for test data train=list(set(range(n))-set(test))# indices for train data beta=np.linalg.inv(X[train,].T@X[train,])@X[train,].T@y[train] e=y[test]-X[test,]@beta S=S+np.linalg.norm(e)**2 return S/n

Example 39 We analyzed the variable selection results of the 10-fold cross- validation approach for linear regression. We assumed that the response depends only on X3, X4, X5 (and the intercept) among the p = 5 covariates X1, X2, X3, X4, X5 .

n=100; p=5 X=randn(n,p) X=np.insert(X,0,1,axis=1) beta=randn(p+1) beta[[1,2]]=0 y=X@beta+randn(n) cv_linear(X[:,[0,3,4,5]],y,10)

1.1001140673920566

cv_linear(X,y,10)

1.156169036077035

We evaluated the prediction error via cross-validation for the three cases such that the response depends on {X3, X4, X5} and {X1, X2, X3, X4, X5}, respectively. In the first and last cases, it is difficult to see the difference without repeating it. Therefore, the difference was compared 100 times (Fig. 4.1).

---

<!-- Página 87 -->

4.1 Cross-Validation 79

Fig. 4.1 The horizontal axisOverfitting is the prediction error when considering variable selection (some variables are not selected), and this case has a1.3 slightly smaller prediction error compared to the case where all the variables are 1.1 selected (vertical axis)

0.9

Square loss for all variables 0.7 0.8 0.9 1.0 1.1 1.2 1.3 Square loss for variables 4, 5, 6

n=100; p=5 X=randn(n,p) X=np.insert(X,0,1,axis=1) beta=randn(p+1); beta[[1,2]]=0 U=[]; V=[] for j in range(100): y=X@beta+randn(n) U.append(cv_linear(X[:,[0,3,4,5]],y,10)) V.append(cv_linear(X,y,10)) x_seq=np.linspace(0.7,1.5,100) y=x_seq plt.plot(x_seq,y,c="red") plt.scatter(U,V) plt.xlabel("The squared error in selecting variables 4, 5 and 6") plt.ylabel("The squared error in selecting all variables") plt.title("Over fitting by selecting too many variables")

Text(0.5, 1.0, ’Over fitting by selecting too many variables’)

As seen from Fig. 4.1, overfitting occurs when all the variables are used without performing variable selection.

Example 40 What k of k-fold CV is the best w.r.t. the prediction error depends on the data. Some believe that k = N is optimal. Additionally, k = 10 is often used, but there is no theoretical basis for this choice. We generated N datasets ten times and showed how the value changes depending on the value of k (see Fig. 4.2). It seems that the value of k should be at least ten.

n=100; p=5 plt.ylim(0.3,1.5) plt.xlabel("k") plt.ylabel("the values of CV") for j in range(2,11,1): X=randn(n,p) X=np.insert(X,0,1,axis=1) beta=randn(p+1)

---

<!-- Página 88 -->

80 4 Resampling

y=X@beta+randn(n) U=[]; V=[] for k in range(2,n+1,1): if n%k==0: U.append(k); V.append(cv_linear(X,y,k)) plt.plot(U,V)

Cross-validation (CV) is widely used in practical aspects of data science, as well as in variable selection in linear regression problems (e.g., 39). The problems introduced in Chap. 3 are as follows:

- In variable selection for logistic regression, the error rate is compared by CV to find the optimal combination of variables whose coefficients are not zero. - The error rate is compared by CV between linear discrimination and quadratic discrimination, and the better method is selected. - In the k-nearest neighbor method, the error rate of each k is compared by CV, and the optimal k is calculated (Fig. 4.3).

Fig. 4.2 How the predictionCV and k of k-fold error of CV changes with k. We simulated artificial data following the same distribution ten times. It can be confirmed that a specific k is not small CV

0.4 0.6 0.8 1.0 1.2 1.4

0 20 40 60 80 100 k

Fig. 4.3 10-fold Error Rate for each K cross-validation. We show how the error rate of the prediction changes with k in 0.08 the k-nearest neighbor method

0.04 Error Rate

0.00 2 4 6 8 10 K

---

<!-- Página 89 -->

4.2 CV Formula for Linear Regression 81

There are numerous ways to prevent overfitting other than CV (described later); however, CV is more advantageous in the sense that they can be applied more generally than CV.

Example 41 With 10-fold cross-validation, we evaluated how the error rate changes for each k in the k-nearest neighbor method for Fisher’s Iris dataset. The execution may take more than 10 min (we used the function knn defined in Chap. 3).

from sklearn.datasets import load_iris

iris=load_iris() iris.target_names x=iris.data y=iris.target n=x.shape[0] index=np.random.choice(n,n,replace=False)# rearrange x=x[index,] y=y[index]

U=[] V=[] top_seq=list(range(0,150,15)) for k in range(1,11,1): S=0 for top in top_seq: test=list(range(top,top+15)) train=list(set(range(150))-set(test)) knn_ans=knn(x[train,],y[train],x[test,],k=k) ans=y[test] S=S+np.sum(knn_ans!=ans) S=S/n U.append(k) V.append(S) plt.plot(U,V) plt.xlabel("K") plt.ylabel("error rate ") plt.title(" Assessment of error rate by CV ")

Text(0.5, 1.0, ’ Assessment of error rate by CV ’)

4.2 CV Formula for Linear Regression

In the case of k-fold CV, especially when k = N (LOOCV, leave-one-out cross- validation), it takes much time to execute because the data are divided into N groups. In the following, we describe a method of realizing fast CV in the case of linear regression, which is slightly complicated mathematically but is not limited to LOOCV.

---

<!-- Página 90 -->

82 4 Resampling

In the following, we consider k nonoverlapping subsets of {1, . . . , N}. In CV, one of the subsets is used as the test data, and the other k − 1 are training data. It is known that in linear regression, we have the formula to evaluate the squared 1 loss under cross-validation without actually executing k cycles of evaluations. In 2 N the following, by ‖a‖, we denote the squared sum of the N elements in a ∈ R.

Proposition 14 (J. Shao, 1993) If we divide {1, . . . , N} into nonoverlapping 2 subsets, the sum of the squared loss values evaluated by cross-validation is ∑ −12 ‖(I − H S )e S ‖, S

T −1TT −1T where for each subset S, H S := XS (X X)X is the matrix H = X(X X)X S that consists of the rows and columns in S, and e S is the vector e = y − X ˆβ that consists of the rows in S. In the following, based on the knowledge we have obtained thus far, we show why the proposition holds. We write the matrices that consist of the rows in S and N×(p+1) r×(p+1) (N−r)×(p+1) not in i  ∈ S of X ∈ Ras XS ∈ Rand X−S ∈ R, respectively, where r is the cardinality of S. Similarly, we define y S and y−S for N y ∈ R. Then, we have

N ∑∑∑ T TTTTT X X =x x j = x x j + x x j = X XS + X X−S (4.1) j j j S −S j =1j ∈Sj  ∈S

and

N ∑∑∑ T TTTTT X y =x j y j = x j y j + x j y j = X S y S + X −S y−S , (4.2) j =1j ∈Sj  ∈S

p+1 where x j ∈ Ris a row vector. Then, we note the following equation:

Proposition 15 (Sherman–Morrison–Woodbury) Let m, n ≥ 1. For A ∈ n×n n×m m×mm×n R, U ∈ R, C ∈ R, and V ∈ R, we have

−1 −1 −1−1 −1−1−1 (A + U CV )= A− AU (C+ V AU )V A. (4.3)

For the proof, see the Appendix at the end of this chapter.

1 Many books mention a restrictive formula valid only for LOOCV (k = N). This book addresses the general formula applicable to any k. 2 Linear Model Selection by Cross-Validation Jun Shao, Journal of the American Statistical Association Vol. 88, No. 422 (Jun., 1993), pp. 486–494.

---

<!-- Página 91 -->

4.2 CV Formula for Linear Regression 83

T T If we apply n = p + 1, m = r, A = X X, C = I , U = X , and V = −XS to S (4.3), we have

T−1 T −1 T −1T−1T −1 (X X−S )= (X X)+ (X X)X (I − H S )XS (X X). (4.4) −S S

The following statement assures the nonsingularity of I − H S .

T Proposition 16 Suppose that X X is a nonsingular matrix. Then, for each S ⊂ T {1, . . . , N}, if X X−S is invertible, so is I − H S . −S For the proof, see the Appendix at the end of this chapter. T−1T Thus, from (4.1), (4.2), and (4.4), the estimate ˆβ−S := (X X−S )X y−S −S −S obtained without using the data in S is as follows:

ˆβ= (X TX)−1(X T y − X Ty ) −S −S −S S S

T −1 T −1T−1T −1T T = {(X X)+ (X X)X (I − H S )XS (X X)}(X y − X y S ) S S T −1TT −1T−1 = ˆβ − (X X)X S y S + (X X)X S (I − H S )(XS ˆβ − H S y S )

T −1T−1 = ˆβ − (X X)X (I − H S ){(I − H S )y S − XS ˆβ + H S y S } S T −1T−1 = ˆβ − (X X)X (I − H S )e S , S

T −1T where ˆβ = (X X)X y is the estimate of β obtained using all data, and e S := y S − XS ˆβ is the loss of the data in S when we use the estimate ˆβ. We predict the data that belong to S based on the estimates ˆβ−S , and evaluate the residue y S − XS ˆβ−S :

T −1T−1 y S − XS ˆβ−S = y S − XS { ˆβ − (X X)X S (I − H S )e S }

T −1T−1 = y S − XS ˆβ + XS (X X)X (I − H S )e S S −1−1 = e S + H S (I − H S )e S = (I − H S )e S

and its squared sum. Thus, while the residue y S − XS ˆβ based on ˆβ obtained using all the data is e S , the residue y S − XS ˆβ−S based on ˆβ−S obtained using the data −1−1 excluding S is (I − H S )e S , which means that e S is multiplied by (I − H S ), which completes the proof of Proposition 14. T −1T When we obtain the prediction error, we compute H = X(X X)X and −1 e = (I − H )y in advance. We can obtain (1 − H S )e S for each S by removing some rows of e and some rows and columns of H , and can obtain the squared sum of them over all S. We construct the following efficient procedure based on Proposition 14:

def cv_fast(X,y,k): n=len(y) m=n/k H=X@np.linalg.inv(X.T@X)@X.T

---

<!-- Página 92 -->

84 4 Resampling

I=np.diag(np.repeat(1,n)) e=(I-H)@y I=np.diag(np.repeat(1,m)) S=0 for j in range(k): test=np.arange(j*m,(j+1)*m,1,dtype=int) S=S+(np.linalg.inv(I-H[test,:][:,test])@e[test]).T@np.linalg.inv(I-H [test,test])@e[test] return S/n

cv_fast(x,y,10)

0.04851318320309918

Example 42 For each k, we measured how much the execution time differs between the functions cv_fast and cv_linear .

# data generation n=1000; p=5 beta=randn(p+1) x=randn(n,p) X=np.insert(x,0,1,axis=1) y=X@beta+randn(n)

import time

U_l=[]; V_l=[]; U_f=[]; V_f=[] for k in range(2,n+1,1): if n%k==0: t1=time.time()# Time before processing cv_linear(X,y,k) t2=time.time()# Time after processing U_l.append(k); V_l.append(t2-t1) t1=time.time() cv_fast(X,y,k) t2=time.time() U_f.append(k); V_f.append(t2-t1) plt.plot(U_l,V_l,c="red",label="cv_linear") plt.plot(U_f,V_f,c="blue",label="cv_fast") plt.legend() plt.xlabel("k") plt.ylabel("execution time") plt.title("comparing between cv_fast and cv_linear")

Text(0.5, 1.0, ’comparing between cv_fast and cv_linear’)

The results are shown in Fig. 4.4. There is a large difference at N = 1000. The LOOCV of k = N takes the longest processing time, and the difference is large there. However, this difference is not so significant at N = 100 because the execution time itself is short. Additionally, since the function cv_fast is specialized for linear regression only, in other problems, a general CV procedure rather than cv_fast will be required.

---

<!-- Página 93 -->

4.3 Bootstrapping 85

Fig. 4.4 Comparison until cv.fast vs cv.linear N = 1000. It can be seen that the processing time of the0.5cv.linear function cv_fast is short for cv.fast each k0.4

0.3

0.2 Execution Time 0.1

0.0 0 200 400 600 800 1000 k

4.3 Bootstrapping

Section 2.7 shows the confidence intervals of the true parameter β and the response y∗ for each covariate x∗ in linear regression can be calculated from the observed data. However, it is not an exaggeration to say that it is rare to be able to do such things in general settings. To address this issue, we will outline the bootstrap method and its importance (Fig. 4.5).

Randomly Chosen 1 x8, y8, z8 x6, y6, z6 x2, y2, z2Randomly Chosen 2 x3, y3, z3x3, y3, z3 Originalx6, y6, z6x8, y8, z8 x1, y1, z1x1, y1, z1x1, y1, z1 x2, y2, z2x7, y7, z7x3, y3, z3 x3, y3, z3x, y, zx2, y2, z2 333 x4, y4, z4x3, y3, z3 x5, y5, z5x1, y1, z1 x6, y6, z6x2, y2, z2Randomly Chosen Last x7, y7, z7x2, y2, z2 x8, y8, z8x3, y3, z3 x3, y3, z3 x1, y1, z1 x7, y7, z7 x8, y8, z8 x1, y1, z1 x2, y2, z2

Fig. 4.5 Bootstrapping Multiple data frames of the same size are generated randomly and the dispersion of the estimated values is observed. Each piece of data in the newly created data frame must be included in the original data frame

---

<!-- Página 94 -->

86 4 Resampling

Suppose that for each row in the data frame, we can obtain an estimate of parameter α

ˆα = f (df1, · · · , dfN )

using a function f that estimates α from data df1, · · · , dfN . We consider N ran- domly chosen rows, allowing duplication, to obtain (dfi, . . . , dfi), i1, . . . , i N ∈ 1 N {1, . . . , N}. Then, we obtain another estimate of α:

ˆα1 = f (dfi, . . . , dfi). 1 N

We repeat the process r times to obtain the sequence of the estimates ˆα1, · · · , ˆαr and can obtain an unbiased estimate of variance of the estimates obtained by f . 2 Suppose we estimate the variance σ ( ˆα) by ⎧⎫ 2 r⎨r⎬ ∑∑ 11 2 ˆσ ( ˆα) := ˆαh − ˆαf, r − 1⎩ r⎭ h=1f =1

the following procedure realizes the notion of bootstrap given a function f to estimate, and it evaluates the performance of function f .

def bt(df,f,r): m=df.shape[0] org=f(df,np.arange(0,m,1)) u=[] for j in range(r): index=np.random.choice(m,m,replace=True) u.append(f(df,index)) return {’original’:org,’bias’:np.mean(u)-org,’stderr’:np.std(u, ddof=1)}

The function bt returns the estimate org estimated from the original data frame, the difference bias between org and the arithmetic mean of the r estimates, and the standard error stderr of the estimates. The values of the bias and standard error depend on the choice of function f .

Example 43 For N data points (x1, y1), . . . , (x N , y N ) w.r.t. variables X and Y , we 3 estimate

V (Y ) − V (X) α := , V (X) + V (Y ) − 2Cov(X, Y )

3 In a portfolio, for two brands X and Y , the quantity of X and Y is often estimated.

---

<!-- Página 95 -->

4.3 Bootstrapping 87

where V (·) and Cov(·, ·) are the variance and covariance of the variables. Suppose that ⎡⎤ { }2 NN 1∑1∑ 22 v:= ⎣x− x i⎦ x i N − 1N i=1i=1 ⎡⎤ { }2 NN 1∑1∑ 22 v:= ⎣y− y i⎦ y i N − 1N i=1i=1 [ { } { }] NNN ∑∑∑ 11 c xy := x i y i − x iy i, N − 1N i=1i=1i=1

we estimate α by

22 vy − vx ˆα := 22 v+ v− 2c xy x y

Then, we evaluate the variance via bootstrapping to examine how reliable the estimate ˆα is (i.e., how close it is to α).

Portfolio=np.loadtxt("Portfolio.csv",delimiter=",",skiprows=1) def func_1(data,index): X=data[index,0]; Y=data[index,1] return (np.var(Y, ddof=1)-np.var(X, ddof=1))/(np.var(X, ddof=1)+np.var(Y, ddof=1)-2*np.cov(X,Y)[0,1]) bt(Portfolio,func_1,1000)

{’original’: 0.15330230333295436, ’bias’: 0.0063149270038345695, ’stderr’: 0.17757037146622828}

If a method for evaluating the estimation error is available, we do not have to assess it by bootstrapping, but for our purposes, let us compare the two to see how correctly bootstrapping performs.

Example 44 We estimated the intercept and slope in the file crime.txt many times by bootstrap, evaluated the dispersion of the estimated values, and compared them with the theoretical values calculated by the sm.OLS function. In the bootstrap estimation, func_2 estimates the intercept and two slopes when regressing the first variable to the third and fourth variables (j = 1, 2, 3) and evaluates its standard deviation.

from sklearn import linear_model

df=np.loadtxt("crime.txt",delimiter="\t") reg=linear_model.LinearRegression()

---

<!-- Página 96 -->

88 4 Resampling

X=df[:,[2,3]] y=df[:,0] reg.fit(X,y) reg.coef_

array([11.8583308 , -5.97341169])

for j in range(3): def func_2(data,index): X=data[index,2:4]; y=data[index,0] reg.fit(X,y) if j==0: return reg.intercept_ else: return reg.coef_[j-1] print (bt(df,func_2,1000))

{’original’: 621.4260363802889, ’bias’: 39.45710543185794, ’stderr’: 220.8724310716836} {’original’: 11.858330796711094, ’bias’: -0.4693174397369564, ’stderr’: 3.394059052591196} {’original’: -5.973411688164963, ’bias’: -0.2157575210725442, ’stderr’: 3.166476969985083}

import statsmodels.api as sm

n=X.shape[0] X=np.insert(X,0,1,axis=1) model=sm.OLS(y,X) res=model.fit() print(res.summary())

OLS Regression Results ============================================================================== Dep. Variable: y R-squared: 0.325 Model: OLS Adj. R-squared: 0.296 Method: Least Squares F-statistic: 11.30 Date: Mon, 10 Feb 2020 Prob (F-statistic): 9.84e-05 Time: 00:36:04 Log-Likelihood: -344.79 No. Observations: 50 AIC: 695.6 Df Residuals: 47 BIC: 701.3 Df Model: 2 Covariance Type: nonrobust ============================================================================== coef std err t P>|t| [0.025 0.975] ------------------------------------------------------------------------------ const 621.4260 222.685 2.791 0.008 173.441 1069.411 x1 11.8583 2.568 4.618 0.000 6.692 17.024 x2 -5.9734 3.561 -1.677 0.100 -13.138 1.191 ============================================================================== Omnibus: 14.866 Durbin-Watson: 1.581 Prob(Omnibus): 0.001 Jarque-Bera (JB): 16.549 Skew: 1.202 Prob(JB): 0.000255 Kurtosis: 4.470 Cond. No. 453. ==============================================================================

---

<!-- Página 97 -->

Appendix: Proofs of Propositions 89

The function func_2 finds the intercept and the slope of the third and fourth variables at i = 1, 2, 3, respectively. In this case, the standard deviation of the intercept and the slopes of the two variables almost match the theoretical values obtained as the output of the sm.OLS function. Even if it is a linear regression problem, if the noise does not follow a Gaussian distribution or is not independent, bootstrapping is still useful.

Appendix: Proof of Propositions

Proposition 15 (Sherman–Morrison–Woodbury) For m, n ≥ 1 and a matrix n×n n×m m×m m×n A ∈ R, U ∈ R, C ∈ R, V ∈ R, we have

−1 −1 −1−1 −1−1−1 (A + U CV )= A− AU (C+ V AU )V A(4.5)

Proof The derivation is due to the following:

−1 −1−1 −1−1−1 (A + U CV )(A− AU (C+ V AU )V A)

−1 −1 −1−1−1 = I + U CV A− U (C+ V AU )V A

−1−1 −1−1−1 −U CV AU (C+ V AU )V A

−1 −1−1 −1−1−1 = I + U CV A− U C · (C) · (C+ V AU )V A

−1−1 −1−1−1 −U C · V AU · (C+ V AU )V A

−1 −1 −1−1 −1−1−1 = I + U CV A− U C(C+ V AU )(C+ V AU )V A= I.



T Proposition 16 Suppose that X X is a nonsingular matrix. For each S ⊂ T {1, . . . , N}, if X X−S is a nonsingular matrix, so is I − H S . −S m×nn×m Proof For m, n ≥ 1, U ∈ R, and V ∈ R, we have [ ] [ ] [ ][ ] [ ] I 0I + U V UI 0I + U V UI 0 = V I0 I−V IV + V U V V U + I−V I [ ] I U =. 0 I + V U

Combined with Proposition 2, we have

det(I + U V ) = det(I + V U ) . (4.6)

---

<!-- Página 98 -->

90 4 Resampling

Therefore, from Proposition 2, we have

TT T det(X X−S ) = det(X X − X XS ) −S S T T −1T = det(X X) det(I − (X X)X S XS )

T T −1T = det(X X) det(I − XS (X X)X ) , S

T where the last transformation is due to (4.6). Hence, from Proposition 1, if X X−S −S T and X X are nonsingular, so is I − H S . 

Exercises 32–39

n×n n×m m×m 32. Let m, n ≥ 1. Show that for matrix A ∈ R, U ∈ R, C ∈ R, V ∈ m×n R,

−1 −1 −1−1 −1−1−1 (A + U CV )= A− AU (C+ V AU )V A(4.7)

(Sherman–Morrison–Woodbury). Hint: Continue the following:

−1 −1−1 −1−1−1 (A + U CV )(A− AU (C+ V AU )V A)

−1 −1 −1−1−1 = I + U CV A− U (C+ V AU )V A

−1−1 −1−1−1 −U CV AU (C+ V AU )V A

−1 −1−1 −1−1−1 = I + U CV A− U C · (C) · (C+ V AU )V A

−1−1 −1−1−1 −U C · V AU · (C+ V AU )V A.

(N−r)×(p+1) 33. Let S be a subset of {1, . . . , N} and write the matrices X ∈ R r×(p+1) that consist of the rows in S and the rows not in S as XS ∈ Rand (N−r)×(p+1) X−S ∈ R, respectively, where r is the number of elements in S. N Similarly, we divide y ∈ Rinto y S and y−S .

(a) Show

T−1 T −1 T −1T−1T −1 (X X−S )= (X X)+ (X X)X (I − H S )XS (X X), −S S

T −1T where H S := XS (X X)X is the matrix that consists of the rows and S T −1T columns in S of H = X(X X)X . Hint: Apply n = p + 1, m = r, T T A = X X, C = I , U = X , V = −XS to (4.3). S (b) For e S := y S − ˆy S with ˆy S = XS ˆβ, show the equation

ˆβ= ˆβ − (X T X)−1X T(I − H )−1e −S S S S

---

<!-- Página 99 -->

Exercises 32–39 91

T TTT TT Hint: From X X = X XS + X X−S and X y = X y S + X y−S , S −S S −S

ˆβ= {(X T X)−1 + (X T X)−1X T(I − H )−1X(X T X)−1}(X T y − X Ty ) −S S S S S S T −1T−1 = ˆβ − (X X)X (I − H S )(XS ˆβ − H S y S ) S T −1T−1 = ˆβ − (X X)X (I − H S ){(I − H S )y S − XS ˆβ + H S y S }. S

−1 34. By showing y S − XS ˆβ−S = (I − H S )e S , prove that the squared sum of the ∑ −12 2 groups in CV is ‖(I − H S )e S ‖, where ‖a‖denotes the squared sum of S N the elements in a ∈ R. 35. Fill in the blanks below and execute the procedure in Problem 34. Observe that the squared sum obtained by the formula and by the general cross-validation method coincide.

n=1000; p=5 X=np.insert(randn(n,p),0,1,axis=1) beta=randn(p+1).reshape(-1,1) y=X@beta+0.2*randn(n).reshape(-1,1) y=y[:,0]

# Conventional CV def cv_linear(X,y,K): n=len(y); m=int(n/K) S=0 for j in range(K): test=list(range(j*m,(j+1)*m))# indices for test data train=list(set(range(n))-set(test))# indices for train data beta=np.linalg.inv(X[train,].T@X[train,])@X[train,].T@y[train] e=y[test]-X[test,]@beta S=S+np.linalg.norm(e)**2 return S/n

# Fast CV def cv_fast(X,y,k): n=len(y) m=n/k H=X@np.linalg.inv(X.T@X)@X.T I=np.diag(np.repeat(1,n)) e=(I-H)@y I=np.diag(np.repeat(1,m)) S=0 for j in range(k): test=np.arange(j*m,(j+1)*m,1,dtype=int) S=S+(np.linalg.inv(I-H[test,test])@e[test]).T@np.linalg.inv(I-H[ test,test])@e[test] return S/n

---

<!-- Página 100 -->

92 4 Resampling

Moreover, we wish to compare the speeds of the functions cv_linear and cv_fast. Fill in the blanks below to complete the procedure and draw the graph.

import time

U_l=[]; V_l=[] for k in range(2,n+1,1): if n%k==0: t1=time.time()# time before processing cv_linear(X,y,k) t2=time.time()# time after processing U_l.append(k); V_l.append(t2-t1)

# some blanks #

plt.plot(U_l,V_l,c="red",label="cv_linear") plt.legend() plt.xlabel("k") plt.ylabel("execution time") plt.title("compairing between cv_fast and cv_linear")

Text(0.5, 1.0, ’compairing between cv_fast and cv_linear’)

36. How much the prediction error differs with k in the k-fold CV depends on the data. Fill in the blanks and draw the graph that shows how the CV error changes with k. You may use either the function cv_linear or cv_fast.

n=100; p=5 plt.ylim(0.3,1.5) plt.xlabel("k") plt.ylabel("values of CV") for j in range(2,11,1): X=randn(n,p) X=np.insert(X,0,1,axis=1) beta=randn(p+1) y=X@beta+randn(n) U=[]; V=[] for k in range(2,n+1,1): if n%k==0: # blank # plt.plot(U,V)

37. We wish to know how the error rate changes with K in the K-nearest neighbor method when 10-fold CV is applied for the Fisher’s Iris data set. Fill in the blanks, execute the procedure, and draw the graph.

from sklearn.datasets import load_iris

iris=load_iris() iris.target_names x=iris.data y=iris.target n=x.shape[0]

---

<!-- Página 101 -->

Exercises 32–39 93

order=np.random.choice(n,n,replace=False)# rearrange x=x[index,] y=y[index]

U=[] V=[] top_seq=list(range(0,135,15)) for k in range(1,11,1): S=0 for top in top_seq: test=# blank(1) # train=list(set(range(150))-set(test)) knn_ans=knn(x[train,],y[train],x[test,],k=k) ans=# blank(2) # S=S+np.sum(knn_ans!=ans) S=S/n U.append(k) V.append(S) plt.plot(U,V) plt.xlabel("K") plt.ylabel("error rate ") plt.title("Assessment of error rate by CV")

Text(0.5, 1.0, ’Assessment of error rate by CV’)

38. We wish to estimate the standard deviation of the quantity below w.r.t. X, Y based on N data. ⎧⎡⎤ { }2 ⎪N∑N∑ ⎪11 ⎪2 ⎪v:= ⎣X− X⎦ ⎪x i i ⎪ ⎪N − 1N ⎪ ⎪i=1i=1 ⎪ ⎪⎡⎤ ⎪{ }2 ⎨NN vy − vx1∑1∑ ,v:= ⎣Y 2− Y⎦ y i vx + vy − 2vxy⎪⎪N − 1i N ⎪i=1i=1 ⎪ ⎪ ⎪[ { } { }] ⎪NNN ⎪∑∑∑ ⎪11 ⎪ ⎪ ⎪vxy := Xi Yi − XiYi ⎩ N − 1N i=1i=1i=1

To this end, allowing duplication, we randomly choose N data in the data frame r times and estimate the standard deviation (Bootstrap). Fill in the blanks (1)(2) to complete the procedure and observe that it estimates the standard deviation.

def bt(df,f,r): m=df.shape[0] org=# blank(1) # u=[] for j in range(r): index=np.random.choice(# blank(2) #) u.append(f(df,index)) return {’original’:org,’bias’:np.mean(u)-org,’stderr’:np.std(u, ddof =1)}

---

<!-- Página 102 -->

94 4 Resampling

def func_1(data,index): X=data[index,0]; Y=data[index,1] return (np.var(Y, ddof=1)-np.var(X, ddof=1))/(np.var(X, ddof=1)+np. var(Y, ddof=1)-2*np.cov(X,Y)[0,1])

Portfolio=np.loadtxt("Portfolio.csv",delimiter=",",skiprows=1) bt(Portfolio,func_1,1000)

39. For linear regression, if we assume that the noise follows a Gaussian distribu- tion, we can compute the theoretical value of the standard deviation. We wish to compare the value with the one obtained by bootstrap. Fill in the blanks and execute the procedure. What are the three kinds of data that appear first?

from sklearn import linear_model

df=np.loadtxt("crime.txt",delimiter="\t") reg=linear_model.LinearRegression() X=df[:,[2,3]] y=df[:,0] reg.fit(X,y) reg.coef_

array([11.8583308 , -5.97341169])

for j in range(3): def func_2(data,index): X=data[index,2:4]; y=## blank ## reg.fit(X,y) if j==0: return reg.intercept_ else: return reg.coef_[j-1] print (bt(df,func_2,1000))

import statsmodels.api as sm

n=X.shape[0] X=np.insert(X,0,1,axis=1) model=sm.OLS(y,X) res=model.fit() print(res.summary())

---

<!-- Página 103 -->

## Chapter 5

# Information Criteria

Abstract Until now, from the observed data, we have considered the following cases:

- Build a statistical model and estimate the parameters contained in it. - Estimate the statistical model.

In this chapter, we consider the latter for linear regression. The act of finding rules from observational data is not limited to data science and statistics. However, many scientific discoveries are born through such processes. For example, the writing of the theory of elliptical orbits, the law of constant area velocity, and the rule of harmony in the theory of planetary motion published by Kepler in 1596 marked the transition from the dominant theory to the planetary motion theory. While the explanation by the planetary motion theory was based on countless theories based on philosophy and thought, Kepler’s law solved most of the questions at the time with only three laws. In other words, as long as it is a law of science, it must not only be able to explain phenomena (fitness), but it must also be simple (simplicity). In this chapter, we will learn how to derive and apply the AIC and BIC, which evaluate statistical models of data and balance fitness and simplicity.

5.1 Information Criteria

Information criterion is generally defined as an index for evaluating the validity of a statistical model from observation data. Akaike’s information criterion (AIC) and the Bayesian information criterion (BIC) are well known. An information criterion often refers to the evaluation of both how much the statistical model explains the data (fitness) and how simple the statistical model is (simplicity). AIC and BIC are standard except for the difference in how they are balanced. The same can be done with the cross-validation approach discussed in Chap. 4, which is superior to the information criteria in versatility but does not explicitly control the balance between fitness and simplicity. One of the most important problems in linear regression is to select some p p covariates based on N observations (x1, y1), . . . , (x N , y N ) ∈ R× R. The reason

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 202195 J. Suzuki, Statistical Learning with Math and Python, https://doi.org/10.1007/978-981-15-7877-9_5

---

<!-- Página 104 -->

96 5 Information Criteria

why there should not be too many covariates is that they overfit the data and try to explain the noise fluctuation by other covariates. Thus, we need to recognize the exact subset. p However, it is not easy to choose S ⊆ {1, . . . , p} from the 2subsets

{}, {1}, . . . , {p}, {1, 2}, . . . , {1, . . . , p}

p when p is large because 2increases exponentially with p. We express the fitness 1 and simplicity by the RSS value RSS(S) based on the subset S and the cardinality k(S) := |S| of S. Then, we have that { ′ ′ RSS(S) ≥ RSS(S) S ⊆ S⇒ ′ k(S) ≤ k(S),

RSS 2k which means that the larger the k = k(S), the smaller ˆσ = is, where k N RSSk := mink(S)=k RSS(S). The AIC and BIC are defined by

2 AI C := N log ˆσ + 2k (5.1) k 2 BI C := N log ˆσ k + k log N , (5.2)

and the coefficient of determination

RSSk 1 − T SS

increases monotonically with k and reaches its maximum value at k = p. However, the AIC and BIC values decrease before reaching the minimum at some 0 ≤ k ≤ p and increase beyond that point, where the k values that minimize the AIC and BIC are minimized are generally different. The adjusted coefficient of determination maximizes

RSSk /(N − k − 1) 1 − T SS/(N − 1)

at some 0 ≤ k ≤ p, which is often much larger than those of the AIC and BIC.

Example 45 The following data fields are from the Boston dataset in the Python sklearn package. We assume that the first thirteen variables and the last variable are covariates and a response, respectively. We construct the following procedure to find the set of covariates that minimizes the AIC. In particular, we execute itertools.combinations(range(p),k)

1 By |S|, we mean the cardinality of set S.

---

<!-- Página 105 -->

5.1 Information Criteria 97

Column # Variable Meaning of the variable 1 CRIM Per capita crime rate by town 2 ZN Proportion of residential land zoned for lots over 25,000 sq. ft. 3 INDUS Proportion of nonretail business acres per town 4 CHAS Charles River dummy variable (1 if the tract bounds the river; 0 otherwise) 5 NOX Nitric oxide concentration (parts per 10 million) 6 RM Average number of rooms per dwelling 7 AGE Proportion of owner-occupied units built prior to 1940 8 DIS Weighted distances to five Boston employment centers 9 RAD Index of accessibility to radial highways 10 TAX Full-value property tax rate per $10,000 11 PTRATIO Student–teacher ratio by town 2 12 B 1000(Bk − 0.63), where Bk is the proportion of black people by town 13 LSTAT % lower status of the population 14 MEDV Median value of owner-occupied homes in $1000s

( ) p to obtain a matrix of size k ×that has subsets {1, · · · , p} of size k in its k 2 columns to find the minimum value ˆσ over S such that |S| = k. k

from sklearn.linear_model import LinearRegression import itertools# enumerate combinations

res=LinearRegression()

def RSS_min(X,y,T): S_min=np.inf m=len(T) for j in range(m): q=T[j] res.fit(X[:,q],y) y_hat=res.predict(X[:,q]) S=np.linalg.norm(y_hat-y)**2 if S<S_min: S_min=S set_q=q return(S_min,set_q)

2 We compute N log ˆσ + 2k for S and find the value of k that minimizes it among k k = 0, 1, . . . , p.

from sklearn.datasets import load_boston

---

<!-- Página 106 -->

98 5 Information Criteria

boston=load_boston() X=boston.data[:,[0,2,4,5,6,7,9,10,11,12]] y=boston.target

n,p=X.shape AIC_min=np.inf for k in range(1,p+1,1): T=list(itertools.combinations(range(p),k)) # each column has combinations (k from p) S_min,set_q=RSS_min(X,y,T) AIC=n*np.log(S_min/n)+2*k## if AIC<AIC_min: AIC_min=AIC set_min=set_q print(AIC_min,set_min)

4770.415163216072 (0, 2, 3, 5, 7, 8, 9)

If we replace the line n*np.log(S.min)+2*k marked by ## with n*np.log(S.min)+k*np.log(N), then the quantity becomes the BIC. To maximize the adjusted coefficient of determination, we may update it as follows:

y_bar=np.mean(y) TSS=np.linalg.norm(y-y_bar)**2 D_max=-np.inf for k in range(1,p+1,1): T=list(itertools.combinations(range(p),k)) S_min,set_q=RSS_min(X,y,T) D=1-(S_min/(n-k-1))/(TSS/(n-1)) if D>D_max: D_max=D set_max=set_q print(D_max,set_max)

0.9999988717090253 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

For each k = 0, 1, . . . , p, we find the S that minimizes RSS(S) such that |S| = k for each k = 0, 1, . . . , p and compute the adjusted coefficient of determination from RSSk . Then, we obtain the maximum value of the adjusted coefficients of determination over k = 0, 1, . . . , p.

On the other hand, the BIC (5.2) is used as often as the AIC (5.1). The difference 2 is only in the balance between fitness log ˆσ and simplicity k. k We see that the schools with 200 and 100 points for English and math, respectively, on the entrance examination choose different applicants from the schools with 100 and 200 points for English and math, respectively. Similarly, the statistical models selected by the AIC and BIC are different. Since the BIC has a more significant penalty for the simplicity k, the selected k is smaller, and the chosen model is simpler than that chosen by the AIC. More importantly, the BIC converges to the correct model when the number of samples N is large (consistency), but the AIC does not. The AIC was developed

---

<!-- Página 107 -->

5.1 Information Criteria 99

Fig. 5.1 The BIC is largerChanges of AIC/BIC with # of Covariates than the AIC, but the BIC chooses a simpler model with AIC fewer variables than the AIC1850BIC

1800

1750 AIC/BIC 1700

1650

2 4 6 8 10 # of Covariates

to minimize the prediction error (Sect. 5.4). Even if the statistical model selected is incorrect, the squared error in the test data may be small for the finite number of samples N, which is an advantage of the AIC. It is essential to use the specific information criteria according to their intended purposes, and it is meaningless to discuss which one is superior to the other (Fig. 5.1).

Example 46

def IC(X,y,k): n,p=X.shape T=list(itertools.combinations(range(p),k)) S,set_q=RSS_min(X,y,T) AIC=n*np.log(S/n)+2*k BIC=n*np.log(S/n)+k*np.log(n) return {’AIC’:AIC,’BIC’:BIC}

AIC_seq=[]; BIC_seq=[] for k in range(1,p+1,1): AIC_seq.append(IC(X,y,k)[’AIC’]) BIC_seq.append(IC(X,y,k)[’BIC’]) x_seq=np.arange(1,p+1,1) plt.plot(x_seq,AIC_seq,c="red",label="AIC") plt.plot(x_seq,BIC_seq,c="blue",label="BIC") plt.xlabel(" the number of variables ") plt.ylabel("values of AIC/BIC") plt.title("changes of the number of variables and AIC and BIC") plt.legend()

---

<!-- Página 108 -->

100 5 Information Criteria

5.2 Efficient Estimation and the Fisher Information Matrix

Next, as preparation for deriving the AIC, it is deduced that the estimates of linear regression by the least squares method are a so-called efficient estimator that minimizes the variance among s. For this purpose, we define the Fisher information matrix to derive the Cramér–Rao inequality. p+1 Suppose that the observations x1, . . . , x N ∈ R(row vector) and y1, . . . , y N ∈ R have been generated by the realizations y i = x i β + β0 + e i , i = 1, . . . , N with 2p random variables e1, . . . , e N ∼ N(0, σ ) and unknown constants β0 ∈ R, β ∈ R, p+1 which we write as β ∈ R. In other words, the probability density function can be written as {} 11 2 f (y i |x i , β) := √exp− ‖y i − x i β‖ 2 2 2πσ 2σ ⎡⎤ ⎡⎤⎡⎤β0 x1y1 ⎢⎥ β ⎢.⎥N×(p+1) ⎢.⎥N ⎢1⎥p+1 X =⎣.⎦ ∈ R, y =⎣.⎦ ∈ R, β =⎢.⎥∈ R. ... ⎣⎦ . x Ny N β p

T −1T T In the least squares method, we estimated β by ˆβ = (X X)X y if X X is nonsingular (Proposition 11). p+1 We claim that ˆβ coincides with the β ∈ Rthat maximizes the likelihood

N ∏ L :=f (y i |x i , β). i=1

In fact, the log-likelihood is written by

N1 22 l := log L = − log(2πσ ) − ‖y − Xβ‖. 2 2 2σ

2 2 If σ > 0 is fixed, maximizing this value is equivalent to minimizing ‖y − Xβ‖. 2 Moreover, if we partially differentiate l w.r.t. σ , we have that

22 ∂lN‖y − Xβ‖ = − + = 0 . 2 2 22 ∂σ 2σ 2(σ )

T −1T Thus, using ˆβ = (X X)X y, we find that

1RSS 2 2 ˆσ := ‖y − X ˆβ‖= N N

---

<!-- Página 109 -->

5.2 Efficient Estimation and the Fisher Information Matrix 101

2 is the maximum likelihood estimate of σ . In Chap. 2, we derived ˆβ ∼ 2T −1 N(β, σ (X X)), which means that ˆβ is an unbiased estimator and the covariance 2T −1 matrix is σ (X X). In general, if the variance is minimized among the unbiased estimators, it is called an efficient estimator. In the following, we show that the estimate ˆβ is an efficient estimator. ∂l Let ∇l be the vector consisting of , j = 0, 1, . . . , p. We refer to the ∂β j covariance matrix J of ∇l divided by N as the Fisher information matrix. For N ∏ N f (y|x, β) :=f (y i |x i , β), we have i=1

N ∇f (y|x, β) ∇l = . f N (y|x, β)

Suppose that the order between the derivative w.r.t. β and the integral w.r.t. y can be ∫ 2 N switched. If we partially differentiate both sides of f (y|x, β)dy = 1 w.r.t. β, ∫ N we have that ∇f (y|x, β)dy = 0. On the other hand, we have that

∫ ∫ N ∇f (y|x, β) N N E∇l =f (y|x, β)dy =∇f (y|x, β)dy = 0 (5.3) N f (y|x, β)

and ∫ N 0 = ∇ ⊗ [E∇l] = ∇ ⊗(∇l)f (y|x, β)dy ∫∫ 2N N =(∇l)f (y|x, β)dy +(∇l){∇f (y|x, β)}dy

22 = E[∇l] + E[(∇l)] . (5.4)

In particular, (5.4) implies that

11 22 J = E[(∇l)] = − E[∇l] . (5.5) N N

Example 47 For linear regression, we analyze (5.5):

N ∑ 1 T ∇l = x i (y i − x i β) 2 σ i=1

2 In many practical situations, including linear regression, no problem occurs.

---

<!-- Página 110 -->

102 5 Information Criteria

N ∑ 11 2TT ∇l = − x x i = − X X 2i 2 σ σ i=1

N 1∑ T E[∇l] = x E(y i − x i β) = 0 2i σ i=1 ⎡⎤ NN 1∑∑ T TTT E[∇l)(∇l) ] = E⎣x (y i − x i β){x (y j − x i β)}⎦ 22 i j (σ ) i=1j =1

NN 1∑1∑ TT T2 = x E(y i − x i β)(y i − x i β) x i = x σ I x i 22i 22i (σ )(σ ) i=1i=1

N ∑ 1T1T = x i x i = X X 22 σ σ i=1

N ∑ 1 TT V [∇l] = x E(y i − x i β)(y i − x i β) x i 22i (σ ) i=1

N 1∑1 T2T = x σ I x i = X X. 22i 2 (σ )σ i=1

In general, we have the following statement.

Proposition 17 (Cramér–Rao Inequality) Any covariance matrix V ( ˜β) ∈ (p+1)×(p+1) Rw.r.t. an unbiased estimate is not below the inverse of the Fisher information matrix:

−1 V ( ˜β) ≥ (NJ ),

where an inequality between matrices ≥ 0 implies that the difference is nonnegative definite.

Note that the least squares estimate satisfies the equality part of the inequality. To this end, if we partially differentiate both sides of ∫ ˜β f N (y|x, β)dy = β i i

w.r.t. β j , we have the following equation: ∫{ ∂1, i = j ˜β f N (y|x, β)dy = i ∂β j0, i  = j.

---

<!-- Página 111 -->

5.3 Kullback–Leibler Divergence 103

If we write this equation in terms of its covariance matrix, we have that T E[ ˜β(∇l) ] = I , where I is a unit matrix of size (p+1). Moreover, from E[∇l] = 0 (5.3), we rewrite the above equation as

T E[( ˜β − β)(∇l) ] = I . (5.6)

Then, the covariance matrix of the vector of size 2(p + 1) that consists of ˜β − β and ∇l is [ ] ˜ V ( β) I . I NJ

Note that because both V ( ˜β) and J are covariance matrices, they are nonnegative definite. Finally, we claim that both sides of [ ][ ] [ ] [ ] −1 −1 V ( ˜β) − (NJ )0I −(NJ )V ( ˜β) II 0 = −1 0 NJ0 II NJ−(NJ )I

nT are nonnegative definite. In fact, for an arbitrary x ∈ R, if x Ax ≥ 0, for an n×mmT T arbitrary B ∈ R, and y ∈ R, we have that y B ABy ≥ 0, which means that −1 p+1 T V ( ˜β) − (NJ )is nonnegative definite (for x, y ∈ R, the inequality x {V ( ˜β) − −1T (NJ )}x + y NJy ≥ 0 should hold even if y = 0). This completes the proof of Proposition 17.

5.3 Kullback–Leibler Divergence

For probability density functions f, g ∈ R, we refer to ∫ ∞ f (x) D(f ‖g) :=f (x) log dx −∞g(x)

as to the Kullback–Leibler (KL) divergence, which is defined if the following condition is met: ∫∫ f (x)dx > 0 ⇒g(x)dx > 0 SS

for an arbitrary S ⊆ R. In general, since D(f ‖g) and D(g‖f ) do not coincide, the KL divergence is not a distance. However, D(f ‖g) ≥ 0 and is equal to zero if and only if f and g

---

<!-- Página 112 -->

104 5 Information Criteria

Fig. 5.2 y = x − 1 is beyond y = log x except x = 11.0 y = x − 1 y = log x 0.5 y 1 0.0

-0.5

0.5 1.0 1.5 2.0 2.5 3.0 x

coincide. In fact, we have from log x ≤ x − 1, x > 0 (Fig. 5.2) that ∫ ∫ ∫ ( ) ∞∞∞ f (x)g(x)g(x) f (x) log dx = −f (x) log dx ≥ −f (x)− 1dx −∞g(x) −∞f (x) −∞f (x) ∫ ∞ = −(g(x) − f (x))dx = 1 − 1 = 0 . −∞

In the following, we compute the KL divergence value D(β||γ ) of a parameter γ when the true parameter is β.

Proposition 18 For covariates x1, . . . , x N , if the responses are z1, . . . , zN , the N ∑ p+1 likelihood −log f (zi |x i , γ ) of γ ∈ Ris i=1

N111 2 2 T T T T log 2πσ + ‖z − Xβ‖− (γ − β) X (z − Xβ) + (γ − β) X X(γ − β) 2 2σ 2 σ 2 2σ 2 (5.7)

p+1 for an arbitrary β ∈ R.

For the proof, see the Appendix at the end of this chapter. We assume that z1, . . . , zN has been generated by f (z1|x1, β), . . . , f (zN |x N , β), where the true parameter is β. Then, the average of (5.7) w.r.t. Z1 = z1, . . . , Z N = zN is

N ∑N1 22 − E Zlog f (Z i |x i , γ ) = log(2πσ e) + ‖X(γ − β)‖(5.8) 2 2 2σ i=1

2 2 since the averages of z − Xβ and ‖z − Xβ‖are 0 and Nσ , respectively.

---

<!-- Página 113 -->

5.4 Derivation of Akaike’s Information Criterion 105

Moreover, the value of (5.8) can be written as

N∫ ∞ ∑ −f (z|x i , β) log f (z|x i , γ )dz . −∞ i=1

N∫ ∞ ∑ Sincef (z|x i , β) log f (z|x i , β)dz is a constant that does not depend on −∞ i=1 γ , we only need to choose a parameter γ so that the sum of Kullback–Leibler divergence

NN∫ ∞ ∑f (z|x, β)∑f (z|x, β)1 i i 2 E Zlog =f (z|xi , β) log dz = ‖X(γ − β)‖ f (z|xi , γ ) −∞f (z|xi , γ ) 2σ 2 i=1i=1 (5.9)

is minimized.

5.4 Derivation of Akaike’s Information Criterion

In general, the true parameters β are unknown and should be estimated. In the following, our goal is to choose a γ among the s so that (5.9) is minimized on average. N In general, for random variables U, V ∈ R, we have that

T 2 22 {E[U V ]}≤ E[‖U ‖]E[‖V ‖] (Schwarz’s inequality) .

In fact, in the quadratic equation w.r.t. t

2 22T 2 E(tU + V )= tE[‖U ‖] + 2tE[U V ] + E[‖V ‖] = 0,

at most one solution exists, so the determinant is not positive. If we let U = T −1 X(X X)∇l and V = X( ˜β − β), then we have

T 2 T −122 {E[( ˜β − β) ∇l]}≤ E‖X(X X)∇l‖E‖X( ˜β − β)‖. (5.10)

In the following, we use the fact that for matrices A = (a i,j ) and B = (b i,j ), if the ∑∑ products AB and BA are defined, then both traces are ij a i,j b j,i and coincide. Now, the traces of the left-hand and right-hand sides of (5.6) are

T T T trace{E[( ˜β − β)(∇l) ]} = trace{E[(∇l) ( ˜β − β)]} = E[( ˜β − β) (∇l)]

---

<!-- Página 114 -->

106 5 Information Criteria

and p + 1, which means that

T E[( ˜β − β) (∇l)] = p + 1 . (5.11)

Moreover, we have that {[]} T −12 T T −1T T −1 E‖X(X X)∇l‖= Etrace(∇l) (X X)X X(X X)∇l

T −1T = trace{(X X)E(∇l)(∇l) } T −1−2T −22 = trace{(X X)σ X X} = trace{σ I } = (p + 1)/σ . (5.12)

Thus, from (5.10), (5.11), and (5.12), we have that

22 E{‖X( ˜β − β)‖} ≥ (p + 1)σ

T −1T On the other hand, if we apply the least squares method: ˆβ = (X X)X y, we have that

2 T T E‖X( ˆβ − β)‖= E[trace ( ˆβ − β) X X( ˆβ − β)]

T 22 = trace (V [ ˆβ]X X) = trace (σ I ) = (p + 1)σ ,

and the equality holds. The goal of Akaike’s information criterion is to minimize the quantity

N1 2 log 2πσ + (p + 1) 2 2

obtained by replacing the second term of (5.8) with its average. In particular, for the problem of variable selection, the number of the covariates is not p, but any 0 ≤ k ≤ p. Hence, we choose the k that minimizes

2 N log σ + k . (5.13) k

22 Note that the value of σ := minσ (S) is unknown. For a subset S ⊆ k k(S)=k 22 {1, . . . , p} of covariates, some might replace σ (S) with ˆσ (S). However, the value 22 of log ˆσ (S) is smaller on average than log σ (S). In fact, we have the following proposition.

3 Proposition 19 Let k(S) be the cardinality of S. Then, we have that ( ) k(S) + 21 22 E[log ˆσ (S)] = log σ (S) − + O. 2 N N

3 By O(f (N)), we denote a function such that g(N)/f (N) is bounded.

---

<!-- Página 115 -->

Appendix: Proofs of Propositions 107

For the proof, see the Appendix at the end of this chapter. −2 Since, up to O(N), we have [] k + 2 22 Elog ˆσ k + = log σ k , N

k 22 the AIC replaces log σ k in (5.13) with log ˆσ k + and chooses the k that minimizes N

2 N log ˆσ + 2k . (5.14) k

Appendix: Proof of Propositions

Proposition 18 For covariates x1, . . . , x N , if the responses are z1, . . . , zN , the N ∑ p+1 likelihood −log f (zi |x i , γ ) of γ ∈ Ris i=1

N111 2 2 T T T T log 2πσ + ‖z − Xβ‖− (γ − β) X (z − Xβ) + (γ − β) X X(γ − β) 2 2σ 2 σ 2 2σ 2 (5.15)

p+1 for an arbitrary β ∈ R.

p+1 Proof In fact, for u ∈ R and x ∈ R, we have that

11 2 2 log f (u|x, γ ) = − log 2πσ − (u − xγ ) 2 2 2σ 2 2 (u − xγ )= {(u − xβ) − x(γ − β)}

2 T T T T = (u − xβ)− 2(γ − β) x (u − xβ) + (γ − β) x x(γ − β) 11 2 2 log f (u|x, γ ) = − log 2πσ − (u − xβ) 2 2 2σ 11 T T T T + (γ − β) x (u − xβ) − (γ − β) x x(γ − β) 2 2 σ 2σ

and, if we sum over (x, u) = (x1, z1), . . . , (x n , zn ), we can write

N ∑ N1 2 2 −log f (zi |x i , γ ) = log 2πσ + ‖z − Xβ‖ 2 2 2σ i=1 11 T T T T − (γ − β) X (z − Xβ) + (γ − β) X X(γ − β) , 2 2 σ 2σ

---

<!-- Página 116 -->

108 5 Information Criteria

N ∑ T 2 2T where we have used z = [z1, . . . , zN ]and ‖z − Xβ‖=(zi − x i β), X X = i=1 NN ∑∑ TT T x x i , X (z − Xβ) =x (zi − x i β).  i i i=1i=1 4 Proposition 19 Let k(S) be the cardinality of S. Then, we have ( ) k(S) + 21 22 E[log ˆσ (S)] = log σ (S) − + O. 2 N N

2 Proof Let m ≥ 1, U ∼ χ, V1, . . . , V m ∼ N(0, 1). For i = 1, . . . , m, we have that m {} ∫ ∫ 2 ∞∞ 22121(1 − 2t)v tV tv−v/2i−1/2 Ee i =e i √ei dv i =√exp− dv i = (1 − 2t) −∞2π −∞2π 2 ∫ ∞ tU t (v2+···+v2) 1−(v2+···+v2)/2 −m/2 Ee =e 1 m √e1 m dv1 · · · dv m = (1 − 2t), −∞2π

which means that for n = 1, 2, . . ., ∣ n t U d Ee ∣ n EU = ∣= m(m + 2) · · · (m + 2n − 2) , (5.16) n∣ dt t =0

2 t t U 2 where Ee = 1 + tE[U ] + E[U ] + · · · has been used. Moreover, from the 2 Taylor expansion, we have that []( )( ) 2 UU1U Elog = E− 1− E− 1+ · · · . (5.17) mm 2 m

2 If we let (5.16) for n = 1, 2, where EU = m and EU = m(m + 2), the first and second terms of (5.17) are zero and

111 2 22 2 − (EU − 2mEU + m) = − {m(m + 2) − 2m+ m} = − , 2 2 2m2mm

respectively.

4 By O(f (N)), we denote a function such that g(N)/f (N) is bounded.

---

<!-- Página 117 -->

Appendix: Proofs of Propositions 109

2 Next, we show that each term in (5.17) for n ≥ 3 is at most O(1/m). From the binomial theorem and (5.16), we have that

n( ) ∑ n nj n−j E(U − m) =EU (−m) j j =0 n( ) ∑ n−jnn−j =(−1) m m(m + 2) · · · (m + 2j − 2) . (5.18) j j =0

If we regard

n−j m m(m + 2) · · · (m + 2j − 2)

as a polynomial w.r.t. m, the coefficients of the highest and (n − 1)-th terms are one and 2{1 + 2 + · · · + (j − 1)} = j (j − 1), respectively. Hence, the coefficients of the n-th and (n − 1)-th terms in (5.18) are

n( )n( ) ∑∑ nn−j nj n−j n (−1) =(−1) 1= (−1 + 1) = 0 jj j =0j =0

and n( )n ∑∑n! nj j −2 (−1) j (j − 1) =(−1) j(n − j )!(j − 2)! j =0j =2 n−2( ) ∑ n − 2i = n(n − 1)(−1) = 0 , i i=0

respectively. Thus, we have shown that for n ≥ 3, ( )( ) n U1 E− 1= O. 2 m m

2 RSS(S)N ˆσ (S) 2 Finally, from = ∼ χand (5.17), if we apply m = 22N−k(S)−1 σ (S) σ (S) N − k(S) − 1, then we have that () ( )2 Nk(S) + 11 log = + O N − k(S) − 1 N − k(S) − 1 N − k(S) − 1

[()] / ( )( ) 22 ˆσ (S)σ 1111 Elog= − + O= − + O 22 N − k(S) − 1NN − k(S) − 1 NN N

---

<!-- Página 118 -->

110 5 Information Criteria

and []( )( ) 2 ˆσ (S)1k(S) + 11k(S) + 21 Elog = − − + O= − + O. 222 σ N N NN N



Exercises 40–48

In the following, we define

⎡⎤ ⎡⎤⎡⎤⎡⎤β 0 x1y1z1⎢⎥ ⎢⎥⎢⎥⎢⎥⎢β1⎥ .N×(p+1) .N .N p+1 X =⎢.⎥∈ R, y =⎢.⎥∈ R, z =⎢.⎥∈ R, β =⎢.⎥∈ R, ⎣.⎦ ⎣.⎦ ⎣.⎦ ⎢.⎥ ⎣.⎦ xNyNzN βp

T where x1, . . . , x N are row vectors. We assume that X X has an inverse matrix and denote by E[·] the expectation w.r.t. {} 2 1‖y i − x i β‖ f (y i |x i , β) := √exp− . 2 2 2πσ 2σ

N×(p+1) N 40. For X ∈ Rand y ∈ R, show each of the following:

2 p+1 (a) If the variance σ > 0 is known, the β ∈ Rthat maximizes l := N ∑ log f (y i |x i , β) coincides with the least squares solution. Hint: i=1

N1 22 l = − log(2πσ ) − ‖y − Xβ‖. 2 2 2σ

p+1 2 (b) If both β ∈ Rand σ > 0 are unknown, the maximum likelihood 2 estimate of σ is given by

1 2 2 ˆσ = ‖y − X ˆβ‖. N

2 Hint: If we partially differentiate l with respect to σ , we have

2 ∂lN‖y − Xβ‖ = − + = 0. 2 2 22 ∂σ 2σ 2(σ )

---

<!-- Página 119 -->

Exercises 40–48 111

(c) For probabilistic density functions f and g over R, the Kullback–Leibler divergence is nonnegative, i.e., ∫ ∞ f (x) D(f ‖g) :=f (x) log dx ≥ 0. −∞g(x) ∏ N N 41. Let f (y|x, β) := i=1 f (y i |x i , β). By showing (a) through (d), prove

11 2 2 J = E(∇l)= − E∇l. N N

N ∇f (y|x, β) (a) ∇l = ; N f (y|x, β) ∫ N (b)∇f (y|x, β)dy = 0; (c) E∇l = 0; 22 (d) ∇E[∇l] = E[∇l] + E[(∇l)].

p+1 42. Let ˜β ∈ Rbe an arbitrary unbiased estimate β. By showing (a) through (c), prove Cramer–Rao’s inequality

−1 V ( ˜β) ≥ (NJ ).

T (a) E[( ˜β − β)(∇l) ] = I . (b) The covariance matrix of the vector combining ˜β −β and ∇l of size 2(p +1) [ ] V ( ˜β) I . I NJ

(c) Both sides of [][] [] [] −1 −1 V ( ˜β) − (NJ )0I −(NJ )V ( ˜β) II 0 = −1 0 NJ0 II NJ−(NJ )I

are nonnegative definite.

2 2 43. By showing (a) through (c), prove E‖X( ˜β − β)‖≥ σ (p + 1).

T (a) E[( ˜β − β) ∇l] = p + 1; T −12 2 (b) E‖X(X X)∇l‖= (p + 1)/σ ; T 2 T −122 (c) {E( ˜β − β) ∇l}≤ E‖X(X X)∇l‖E‖X( ˜β − β)‖. Hint: For random m T 2 22 variables U, V ∈ R(m ≥ 1), prove {E[U V ]}≤ E[‖U ‖]E[‖V ‖] (Schwarz’s inequality).

---

<!-- Página 120 -->

112 5 Information Criteria

44. Prove the following statements:

(a) For covariates x1, . . . , x N , if we obtain the responses z1, . . . , zN , then the N ∑ p+1 likelihood −log f (zi |x i , γ ) of the parameter γ ∈ Ris i=1

N212 1T T 1T T log 2πσ + ‖z−Xβ‖− (γ −β) X (z−Xβ)+ (γ −β) X X(γ −β) 2 2σ 2 σ 2 2σ 2

p+1 for an arbitrary β ∈ R. (b) If we take the expectation of (a) w.r.t. z1, . . . , zN , it is

N1 22 log(2πσ e) + ‖X(γ − β)‖. 2 2 2σ

(c) If we estimate β and choose an estimate γ of β, the minimum value of (b) on average is

N1 2 log(2πσ e) + (p + 1), 2 2

and the minimum value is realized by the least squares method. (d) Instead of choosing all the p covariates, we choose 0 ≤ k ≤ p covariates from p. Minimizing

N1 2 log(2πσ e) + (k + 1) k 2 2

22 w.r.t. k is equivalent to minimizing N log σ + k w.r.t. k, where σ is the k k minimum variance when we choose k covariates.

45. By showing (a) through (f), prove ( )( ) 2 ˆσ (S)1k(S) + 11k(S) + 21 E log = − − + O= − + O. 2 22 σ N N NN N

2 Use the fact that the moment of U ∼ χis m

n EU = m(m + 2) · · · (m + 2n − 2)

without proving it. ( )( )2 UU1U (a) E log = E− 1− E− 1+ · · · m m 2 m ( )( )2 UU2 (b) E− 1= 0 and E− 1= . m m m

---

<!-- Página 121 -->

Exercises 40–48 113

n( ) ∑ n−jn (c)(−1) = 0. j j =0 n( ) ∑ n n−jnn−j (d) If we regard E(U −m) =(−1) m m(m+2) · · · (m+2j −2) j j =0 as a polynomial of degree m, the sum of the terms of degree n is zero. Hint: Use (c). (e) The sum of the terms of degree n−1 is zero. Hint: Derive that the coefficient of degree n − 1 is 2{1 + 2 + · · · + (j − 1)} = j (j − 1) for each j and that n( ) ∑ nj (−1) j (j − 1) = 0. j j =0 ( / )( ) 22 ˆσ (S)σ 11 (f) E log= − + O. 2 N − k(S) − 1NN N 46. The following procedure produces the AIC value. Fill in the blanks and execute the procedure.

from sklearn.linear_model import LinearRegression import itertools# # enumerate combinations

res=LinearRegression()

def RSS_min(X,y,T): S_min=np.inf m=len(T) for j in range(m): q=T[j] res.fit(X[:,q],y) y_hat=res.predict(X[:,q]) S=np.linalg.norm(y_hat-y)**2 if S<S_min: S_min=S set_q=q return(S_min,set_q)

from sklearn.datasets import load_boston

boston=load_boston() X=boston.data[:,[0,2,4,5,6,7,9,10,11,12]] y=boston.target

---

<!-- Página 122 -->

114 5 Information Criteria

n,p=X.shape AIC_min=np.inf for k in range(1,p+1,1): T=list(itertools.combinations(range(p),k)) # # each column has combinations (k from p) S_min,set_q=RSS_min(X,y,T) AIC=# blank(1) # if AIC<AIC_min: AIC_min=# blank(2) # set_min=# blank(3) # print(AIC_min,set_min)

47. Instead of AIC, we consider a criterion that minimizes the following quantity (Bayesian Information Criterion (BIC)):

2 N log ˆσ + k log N.

Replace the associated lines of the AIC procedure above, and name the function BIC. For the same data, execute BIC. Moreover, construct a procedure to choose the covariate set that maximizes

RSS/(N − k − 1) 2 AR:= 1 − T SS/(N − 1)

(adjusted coefficient of determination), and name the function AR2. For the same data, execute AR2. 48. We wish to visualize the k that minimizes AIC and BIC. Fill in the blanks and execute the procedure.

def IC(X,y,k): n,p=X.shape T=list(itertools.combinations(range(p),k)) S,set_q=RSS_min(X,y,T) AIC=# blank(1) # BIC=# blank(2) # return {’AIC’:AIC,’BIC’:BIC}

AIC_seq=[]; BIC_seq=[] for k in range(1,p+1,1): AIC_seq.append(# blank(3) #) BIC_seq.append(# blank(4) #) x_seq=np.arange(1,p+1,1) plt.plot(x_seq,AIC_seq,c="red",label="AIC") plt.plot(x_seq,BIC_seq,c="blue",label="BIC") plt.xlabel("the number of variables") plt.ylabel("values of AIC/BIC") plt.title("changes of the number of variables and AIC and BIC") plt.legend()

---

<!-- Página 123 -->

## Chapter 6

# Regularization

Abstract In statistics, we assume that the number of samples N is larger than the number of variables p. Otherwise, linear regression will not produce any least squares solution, or it will find the optimal variable set by comparing the information p criterion values of the 2subsets of the cardinality p. Therefore, it is difficult to estimate the parameters. In such a sparse situation, regularization is often used. In the case of linear regression, we add a penalty term to the squared error to prevent the coefficient value from increasing. When the regularization term is a constant λ times the L1 and L2 norms of the coefficient, the method is called lasso and ridge, respectively. In the case of lasso, as the constant λ increases, some coefficients become 0; finally, all coefficients become 0 when λ is infinity. In that sense, lasso plays a role of model selection. In this chapter, we consider the principle of lasso and compare it with ridge. Finally, we learn how to choose the constant λ.

6.1 Ridge

T N×(p+1) In linear regression, assuming that the matrix X X with X ∈ Ris T −1T nonsingular, we derive that ˆβ = (X X)X y minimizes the per-sample squared 2 N error ‖y − Xβ‖for y ∈ R. In the rest of this chapter, without loss of generality, we regularize only the slope, assuming that the intercept is zero and that X is in N×p N×(p+1) Rrather than in R. T Although it is unlikely in general settings that the matrix X X is singular, even if the determinant is too small, the confidence interval becomes large and an inconvenient situation occurs. To prevent such situations, letting λ ≥ 0 be a constant, we often use ridge to minimize the square error plus the squared norm of β multiplied by λ:

12 2 L := ‖y − Xβ‖+ λ‖β‖2. (6.1) N

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2021115 J. Suzuki, Statistical Learning with Math and Python, https://doi.org/10.1007/978-981-15-7877-9_6

---

<!-- Página 124 -->

116 6 Regularization

If we differentiate L by β, we obtain

2 T 0 = − X (y − Xβ) + 2λβ . N

T If X X + λI is nonsingular, we have

ˆβ = (X T X + NλI )−1X T y ,

T T where X X + NλI is nonsingular as long as λ > 0. In fact, since X X is non- negative definite, all the eigenvalues μ1, . . . , μ p are nonnegative (Proposition 10). T Hence, from Proposition 5, we obtain the eigenvalues of X X + NλI by

T det(X X + NλI − tI ) = 0 ⇒ t = μ1 + Nλ, . . . , μ p + Nλ > 0 .

Moreover, from Proposition 6, all the eigenvalues being positive means that the T T product det(X X +NλI ) is positive and that the matrix X X +NλI is nonsingular T p×p (Proposition 1), which is true for any p and N. If N < p, the rank of X X ∈ R is at most N (Proposition 3), and it is not nonsingular (Proposition 1). Therefore, we have

T λ > 0 ⇐⇒ X X + NλI is nonsingular.

For ridge, we implement the following procedure:

def ridge(x,y,lam=0):#lam stands for lambda X=copy.copy(x) n,p=X.shape X_bar=np.zeros(p) s=np.zeros(p) for j in range(p): X_bar[j]=np.mean(X[:,j]) for j in range(p): s[j]=np.std(X[:,j]) X[:,j]=(X[:,j]-X_bar[j])/s[j] y_bar=np.mean(y) y=y-y_bar beta=np.linalg.inv(X.T@X+n*lam*np.eye(p))@X.T@y for j in range(p): beta[j]=beta[j]/s[j] beta_0=y_bar-X_bar.T@beta return {’beta’:beta,’beta_0’:beta_0}

Example 48 We store the dataset (US Crime Data: https://web.stanford.edu/~hastie/StatLearnSparsity/data. html) as a text file crime.txt and apply ridge to find the relation between the response and covariates..

---

<!-- Página 125 -->

6.2 Subderivative 117

1 Response Total overall reported crime rate per 1 million residents 2 NA 3 Covariate Annual police funding in $/resident 4 Covariates % of people 25+ years with 4 yrs. of high school 5 Covariates % of 16- to 19-year-olds not in high school and not high school graduates 6 Covariates % of 18- to 24-year-olds in college 7 Covariates % of 18- to 24-year-olds in college

We execute the function ridge via the following procedure:

df=np.loadtxt("crime.txt",delimiter="\t") X=df[:,[i for i in range(2,7)]] p=X.shape[1] y=df[:,0] lambda_seq=np.arange(0,50,0.5) plt.xlim(0,50) plt.ylim(-7.5,15) plt.xlabel("lambda") plt.ylabel("beta") labels=[ "annual police funding in $resident","% of people 25 years+ with 4 yrs. of high school", "% of 16 to 19 year-olds not in highschool and not highschool graduates","% of 18 to 24 year-olds in college", "% of 18 to 24 year-olds in "]

for j in range(p): coef_seq=[] for l in lambda_seq: coef_seq.append(ridge(X,y,l)[’beta’][j]) plt.plot(lambda_seq,coef_seq,label="{}".format(labels[j])) plt.legend(loc="upper right")

We illustrate how the coefficients change as λ increases in Fig. 6.1.

6.2 Subderivative

We consider optimizing functions that cannot be differentiated. For example, when 3 we find the points x at which a variable function f such as f (x) = x− 2x + 1 is maximal and minimal, by differentiating f with respect to x, we can solve equation ′2 f (x) = 0. However, what if the absolute function is contained as in f (x) = x+ x + 2|x|? To this end, we extend the notion of differentiation. To begin, we assume that f is convex. In general, if f (αx +(1−α)y) ≤ αf (x)+ 1 (1 − α)f (y) for an arbitrary 0 < α < 1 and x, y ∈ R, we say that f is convex.

---

<!-- Página 126 -->

118 6 Regularization

Ridge: The Coefficients for each λ

40annual police funding in $/resident % of people 25 years+ with 4 yrs. of high school % of 16 to 19 year-olds not in highschool · · · % of 18 to 24 year-olds in college 20% of 18 to 24 year-olds in college

0β

-20

-40 0 20 40 60 80 100 λ

Fig. 6.1 Execution of Example 48. The coefficients β obtained via ridge shrink as λ increases

For example, f (x) = |x| is convex because

|αx + (1 − α)y| ≤ α|x| + (1 − α)|y| .

In fact, because both sides are nonnegative, if we subtract the square of the left from that of the right, we have 2α(1 − α)(|xy| − xy) ≥ 0. If a convex function f : R → R and x0 ∈ R satisfy

f (x) ≥ f (x0) + z(x − x0) (6.2)

for x ∈ R, we say that the set of such z ∈ R is the subderivative of f at x0 . If a 2 ′ convex f is differentiable at x0 , then z consists of one elementf (x0), which can be shown as follows. When a convex function f is differentiable at x0 , we have f (x) ≥ f (x0) + ′ f (x0)(x − x0). In fact, we see that the inequality

f (αx + (1 − α)x0) ≤ αf (x) + (1 − α)f (x0)

is equivalent to

f (x0 + α(x − x0)) − f (x0) f (x) − f (x0) ≥ (x − x0) . α(x − x0)

1 In this book, convexity always means convex below and does not mean concave (convex above). 2 ′′ In such a case, we do not express the subderivative as {f (x0)} but as f (x0).

---

<!-- Página 127 -->

6.2 Subderivative 119

f (x) = |x|

f (x) = −1 f (x) = 1

x 0 cannot be differentiated

Fig. 6.2 f (x) = |x| cannot be differentiated at the origin. The coefficients from both sides do not match

Then, regardless of x < x0 and x > x0 ,

f (x0 + α(x − x0)) − f (x0) α(x − x0)

′ approaches the same f (x0) as α → 0. However, we can show that when the convex function f is differentiable at x0 , the z that satisfies (6.2) does not exist, except ′ f (x0). In fact, in order for (6.2) to hold for x > x0 and x < x0 , we require f (x) − f (x0)f (x) − f (x0) ≥ z and ≤ z, respectively, which means that z is x − x0x − x0 no less than the left derivative at x0 and no more than the right derivative at x0 . Since f is differentiable at x = x0 , these values need to coincide. In this book, we consider only the case of f (x) = |x| and x0 = 0 (Fig. 6.2), and (6.2) becomes |x| ≥ zx for an arbitrary x ∈ R. Then, we can show that the subderivative is the interval [−1, 1]:

|x| ≥ zx , x ∈ R ⇐⇒ |z| ≤ 1 .

To demonstrate this result, suppose that |x| ≥ zx for an arbitrary x ∈ R. If the claim is true for x > 0 and for x < 0, we require z ≤ 1 and z ≥ −1, respectively. On the other hand, if −1 ≤ z ≤ 1, we have zx ≤ |z‖x| ≤ |x| for any x ∈ R.

Example 49 For the cases x < 0, x = 0, and x > 0, we obtain points x such that 2 2 f (x) = x− 3x + |x| and f (x) = x+ x + 2|x| are minimal. For x  = 0, we can differentiate the functions. Note that the subderivative of f (x) = |x| at x = 0 is [−1, 1]. For the first case { { 2 2 2 x− 3x + x, x ≥ 0x− 2x, x ≥ 0 f (x) = x− 3x + |x| == 2 2 x− 3x − x, x < 0 x− 4x, x < 0

⎧ ⎨2x − 2, x > 0 ′ f (x) =2x − 3 + [−1, 1] = −3 + [−1, 1] = [−4, −2]  0, x = 0 ⎩ 2x − 4 < 0, x < 0

---

<!-- Página 128 -->

120 6 Regularization

it is minimal at x = 1 (Fig. 6.3, left). For the second case { { 2 2 2 x+ x + 2x, x ≥ 0x+ 3x, x ≥ 0 f (x) = x+ x + 2|x| == 2 2 x+ x − 2x, x < 0 x− x, x < 0 ⎧ ⎨2x + 3 > 0, x > 0 ′ f (x) =2x + 1 + 2[−1, 1] = 1 + 2[−1, 1] = [−1, 3] 0, x = 0 ⎩ 2x − 1 < 0, x < 0

it is minimal at x = 0 (Fig. 6.3, right). The graphs are obtained via the following code:

x_seq=np.arange(-2,2,0.05) y=x_seq**2-3*x_seq+np.abs(x_seq) plt.plot(x_seq,y) plt.scatter(1,-1,c="red") plt.title("y=x^2-3x+|x|")

Text(0.5, 1.0, ’y=x^2-3x+|x|’)

y=x_seq**2+x_seq+2*np.abs(x_seq) plt.plot(x_seq,y) plt.scatter(0,0,c="red") plt.title("y=x^2+x+2|x|")

Text(0.5, 1.0, ’y=x^2+x+2|x|’)

2 2 y = x− 3x + |x|y = x+ x + 2|x| 10 8 8 10 12 6 6yy 44 22 0 0 -2 -1 0 1 2-2 -1 0 1 2 xx

2 Fig. 6.3 Neither can be differentiated at x = 0. The f (x) = x− 3x + |x| (left) and f (x) = 2 x+ x + 2|x| (right) are minimal at x = 1 and x = 0

---

<!-- Página 129 -->

6.3 Lasso 121

6.3 Lasso

In ridge, we minimize Eq. (6.1). Lasso also restrains the volume of β, but each coefficient becomes zero when λ exceeds a limit that depends on the coefficient. To examine the mechanism, we replace the second term (L2 norm) ‖β‖2 = √ 22 β+ · · · + βp in (6.1) with the L1 norm ‖β‖1 = |β1| + · · · + |β p|. For λ ≥ 0, we 1 formulate the problem as minimizing

1 2 L := ‖y − Xβ‖+ λ‖β‖1 . (6.3) 2N

Dividing the first term by two is not essential, and we may double λ if necessary. For simplicity, we first assume

N{ 1∑1, j = k x i,j x i,k =(6.4) N0, j  = k, i=1

N 1∑ and let sj := x i,j y i , which will make the derivation easier. N i=1 If we differentiate L with respect to β j , we obtain ⎧ () Np⎨1, β j > 0 ∑∑ 1 0 ∈ − x i,jy i −x i,k β k+ λ−1, β j < 0(6.5) N⎩ i=1k=1[−1, 1], β j = 0

because the subderivative of |x| at x = 0 is [−1, 1]. Since we have ⎧ ⎨−sj + β j + λ, β j > 0 0 ∈−sj + β j − λ, β j < 0 ⎩ −sj + β j + λ[−1, 1], β j = 0,

we may write the solution as ⎧ ⎨sj − λ, sj > λ β j =sj + λ, sj < −λ ⎩ 0, −λ ≤ sj ≤ λ,

where the right-hand side can be expressed as β j = Sλ (sj ) with the function ⎧ ⎨x − λ, x > λ Sλ (x) =x + λ, x < −λ ⎩ 0, −λ ≤ x ≤ λ.

---

<!-- Página 130 -->

122 6 Regularization

Fig. 6.4 The shape of Sλ (x) soft.th(lambda,x) for λ = 5 4 2 λ = 5 0

soft.th(5, x) -4 -2

-10 -5 0 5 10 x

We present the shape of Sλ (·) for λ = 5 in Fig. 6.4, where we execute the following code:

def soft_th(lam,x): return np.sign(x)*np.maximum(np.abs(x)-lam,0)

x_seq=np.arange(-10,10,0.1) plt.plot(x_seq,soft_th(5,x_seq)) plt.plot([-5,-5],[4,-4],c="black",linestyle="dashed",linewidth=0.8) plt.plot([5,5],[4,-4],c="black",linestyle="dashed",linewidth=0.8) plt.title("soft_th(lam,x)") plt.text(-1.5,1,’lambda=5’,fontsize=15)

Text(-1.5, 1, ’lambda=5’)

Finally, we remove assumption (6.4). However, relation (6.5) does not hold for ∑p this case. To this end, we replace y i − x i,j β j in (6.5) by ri,j − x i,j β j with the j =1 N ∑1∑ residue ri,j := y i − x i,k β k and by sj := ri,j x i,j in k =j N i=1 ⎧ N⎨1, β j > 0 1∑ 0 ∈ − x i,j (ri,j − x i,j β j ) + λ−1, β j < 0 N⎩ i=1[−1, 1], β j = 0.

Then, for fixed β j , we update β k for k  = j and repeat the process for j = 1, · · · , p. We further repeat the cycle until convergence. For example, we can construct the following procedure:

def lasso(x,y,lam=0): X=copy.copy(x) n,p=X.shape X_bar=np.zeros(p) s=np.zeros(p) for j in range(p): X_bar[j]=np.mean(X[:,j]) for j in range(p):

---

<!-- Página 131 -->

6.3 Lasso 123

s[j]=np.std(X[:,j]) X[:,j]=(X[:,j]-X_bar[j])/s[j] y_bar=np.mean(y) y=y-y_bar eps=1 beta=np.zeros(p); beta_old=np.zeros(p) while eps>0.001: for j in range(p): index=list(set(range(p))-{j}) r=y-X[:,index]@beta[index] beta[j]=soft_th(lam,r.T@X[:,j]/n) eps=np.max(np.abs(beta-beta_old)) beta_old=beta for j in range(p): beta[j]=beta[j]/s[j] beta_0=y_bar-X_bar.T@beta return {’beta’:beta,’beta_0’:beta_0}

Example 50 We apply the data in Example 48 to lasso.

df=np.loadtxt("crime.txt",delimiter="\t") X=df[:,[i for i in range(2,7,1)]] p=X.shape[1] y=df[:,0] lasso(X,y,20)

{’beta’: array([ 9.65900353, -2.52973842, 3.23224466, 0. , 0. ]), ’beta_0’: 452.208077876934}

lambda_seq=np.arange(0,200,0.5) plt.xlim(0,200) plt.ylim(-10,20) plt.xlabel("lambda") plt.ylabel("beta") labels=["annual police funding in resident","% of people 25 years+ with 4 yrs. of high school", "% of 16 to 19 year-olds not in highschool and not highschool graduates","% of 18 to 24 year-olds in college", "% of 18 to 24 year-olds in college"]

for j in range(p): coef_seq=[] for l in lambda_seq: coef_seq.append(lasso(X,y,l)[’beta’][j]) plt.plot(lambda_seq,coef_seq,label="{}".format(labels[j])) plt.legend(loc="upper right") plt.title("values of each coefficient for each lambda")

Text(0.5, 1.0, "values of each coefficient for each lambda")

lasso(X,y,3.3)

{’beta’: array([10.8009963 , -5.35880785, 4.59591339, 0.13291555, 3.83742115]), ’beta_0’: 497.4278799943754}

As shown in Fig. 6.5, the larger the λ is, the smaller the absolute value of the coefficients. We observe that each coefficient becomes zero when λ exceeds a

---

<!-- Página 132 -->

124 6 Regularization

Lasso: The Coeffieicnts for each λ

annual police funding in $/resident 40 % of people 25 years+ with 4 yrs. of · · · % of 16 to 19 year-olds not in · · · % of 18 to 24 year-olds in college % of 18 to 24 year-olds in college 20

0β

-20

-40 0 20 40 60 80 100 λ

Fig. 6.5 Execution of Example 50. Although the coefficients decrease as λ increases for lasso, each coefficient becomes zero for large λ, and the timing for the coefficients differs

threshold that depends on the coefficient and that the sets of nonzero coefficients depend on the value of λ. The larger the λ is, the smaller the set of nonzero coefficients.

6.4 Comparing Ridge and Lasso

If we compare Figs. 6.1 and 6.5, we find that the absolute values of ridge and lasso decrease as λ increases and that the values approach zero. However, in lasso, each of the coefficients diminishes when λ exceeds a value that depends on the coefficient, and the timing also depends on the coefficients; therefore, we must consider this property for model selection. Thus far, we have mathematically analyzed ridge and lasso. Additionally, we may wish to intuitively understand the geometrical meaning. Images such as those in Fig. 6.6 are often used to explain the difference between lasso and ridge. N×p Suppose that p = 2 and that X ∈ Rconsists of two columns x i,1 and x i,2 , i = 1, . . . , N. In the least squares method, we obtain β1 and β2 that minimize N ∑ 2 S :=(y i − β1x i,1 − β2x i,2). Let ˆβ1 and ˆβ2 be the estimates. Since i=1

NN ∑∑ x i,1(y i − ˆy i ) =x i,2(y i − ˆy i ) = 0 i=1i=1

---

<!-- Página 133 -->

6.4 Comparing Ridge and Lasso 125

with ˆy i = ˆβ1x i1 + ˆβ2x i2 and

y i − β1x i,1 − β2x i,2 = y i − ˆy i − (β1 − ˆβ1)x i,1 − (β2 − ˆβ2)x i,2

N ∑ 2 for arbitrary β1, β2 , the RSS(y i − β1x i,1 − β2x i,2)can be expressed as i=1

NN ∑∑ 22 (β1 − ˆβ1)x+2(β1 − ˆβ1)(β2 − ˆβ2)x i,1x i,2 i,1 i=1i=1

NN ∑∑ 222 +(β2 − ˆβ2)x+(y i − ˆy i ). (6.6) i,2 i=1i=1

If we let (β1, β2) := ( ˆβ1, ˆβ2), then we obtain the minimum value (= RSS). However, when p = 2, we may regard solving (6.1) and (6.3) in ridge and lasso 22′ as obtaining (β1, β2) that minimize (6.6) w.r.t. β+ β≤ C, |β1| + |β2| ≤ Cfor 1 2 ′ ′ constants C, C> 0, respectively, where the larger the C, C, the smaller the λ is, where we regard x i1, x i2, y i , ˆy i , i = 1, · · · , N, and ˆβ1, ˆβ2 as constants. The elliptic curve in Fig. 6.6(left) has center ( ˆβ1, ˆβ2), and each of the contours shares the same value of (6.6). If we expand the contours, then we eventually obtain a rhombus at some (β1, β2). Such a pair (β1, β2) is the solution of lasso. If the rhombus is smaller (if λ is larger), the elliptic curve is more likely to reach one of the four corners of the rhombus, which means that one of β1 and β2 becomes zero. However, as shown in Fig. 6.6(right), if we replace the rhombus with a circle (ridge), it is unlikely that one of β1 and β2 becomes zero.

LassoRidge 555444 1 1 444 333 333 222 y222y 1111 111111 000 000

-1-1-1-1-1-1 -1 0 1 2 3-1 0 1 2 3-1 0 1 2 3-1 0 1 2 3 4-1 0 1 2 3 4-1 0 1 2 3 4 xx

Fig. 6.6 The contours that share the center ( ˆβ1, ˆβ2) and the square error (6.6), where the rhombus ′ and circle are the constraints of the L1 regularization |β1| + |β2| ≤ Cand the L2 regularization 22 β+ β≤ C, respectively 1 2

---

<!-- Página 134 -->

126 6 Regularization

Fig. 6.7 In the green area,66 the solution satisfies either1 β1 = 0 or β2 = 0 when the1 44 center is ( ˆβ1, ˆβ2)

22

00

-2-2 -2 0 2 4 6-2 0 2 4 6

For simplicity, we consider a circle rather than an elliptic curve. In this case, if the solution ( ˆβ1, ˆβ2) of the least squares method is located somewhere in the green region in Fig. 6.7, either β1 = 0 or β2 = 0 is the solution. Specifically, if the rhombus is small (λ is large), even if ( ˆβ1, ˆβ2) remain the same, the area of the green region becomes large.

6.5 Setting the λ Value

When we apply lasso, sklearn.linear_model package Lasso is available. Thus far, we have constructed procedures from scratch to understand the principle. We may use the existing package in real applications. To set the λ value, we usually apply the cross-validation (CV) method in Chap. 3. Suppose that the CV is tenfold. For example, for each λ, we estimate β using nine groups and test the estimate using one group, and we execute this process ten times, changing the groups to evaluate λ. We evaluate all λ values and choose the best. If we input the covariates and response data to the function LassoCV, the package evaluates various values of λ and outputs the best one.

Example 51 We apply the data in Examples 48 and 50 to the function LassoCV to obtain the best λ. Then, for the best λ, we apply the usual lasso procedure to obtain β. The package outputs the evaluation (the squared error for the test data) and confidence interval for each λ (Fig. 6.8). The numbers on the top of the figure express how many variables are nonzero for the λ value.

from sklearn.linear_model import Lasso from sklearn.linear_model import LassoCV

Las=Lasso(alpha=20) Las.fit(X,y) Las.coef_

array([11.09067594, -5.2800757 , 4.65494282, 0.55015932, 2.84324295])

---

<!-- Página 135 -->

Exercises 49–56 127

5 5 5 5 5 5 5 5 4 4 3 3 3 3 3 3 2 1 1 1

110000

90000

70000 Mean-Squared Error

50000 0 1 2 3 4 5 log λ

Fig. 6.8 Using the function LassoCV, we obtain the evaluation for each λ (the squared error for the test data), marked as a red point. The vertical segments are the confidence intervals of the true coefficient values. log λmin = 3. (The optimum value is approximately λmin = 20). The numbers on the top of the figure 5, . . . , 5, 4, . . . , 4, 3, . . . , 3, 2, 2, 1, . . . , 1 indicate how many variables are nonzero

# The grid search for the value specified in alphas Lcv=LassoCV(alphas=np.arange(0.1,30,0.1),cv=10) Lcv.fit(X,y) Lcv.alpha_ Lcv.coef_

array([11.14516156, -4.87861992, 4.24780979, 0.63662582, 1.52576885])

Exercises 49–56

N×p N p 49. Let N, p ≥ 1. For X ∈ Rand y ∈ R, λ ≥ 0, we wish to obtain β ∈ R that minimizes

1 2 2 ‖y − Xβ‖+ λ‖β‖, 2 N √ ∑p 2 where for β = (β1, . . . , β p ), we denote ‖β‖2 :=β. Suppose N < p. j =1 j Show that such a solution always exists and that it is equivalent to λ > 0. Hint: In order to show a necessary and sufficient condition, both directions should be proved.

---

<!-- Página 136 -->

128 6 Regularization

50. (a) Suppose that a function f : R → R is convex and differentiable at x = x0 . Show that a z exists for an arbitrary x ∈ R such that f (x) ≥ f (x0) + z(x −x0) (subderivative) and that it coincides with the differential coefficient ′ f (x0) at x = x0 . (b) Show that −1 ≤ z ≤ 1 is equivalent to zx ≤ |x| for all x ∈ R. (c) Find the set of z defined in (a) for function f (x) = |x| and x0 ∈ R. Hint: Consider the cases x0 > 0, x0 < 0, and x0 = 0. 22 (d) Compute the subderivatives of f (x) = x−3x+|x| and f (x) = x+x+2|x| for each point, and find the maximal and minimal values for each of the two functions. 51. Write Python program soft_th(lam,x) of the function Sλ (x), λ > 0, x ∈ R defined by ⎧ ⎨x − λ, x > λ Sλ (x) :=0, |x| ≤ λ ⎩ x + λ, x < −λ,

and execute the following:

x_seq=np.arange(-10,10,0.1) plt.plot(x_seq,soft_th(5,x_seq)) plt.plot([-5,-5],[4,-4],c="black",linestyle="dashed",linewidth=0.8) plt.plot([5,5],[4,-4],c="black",linestyle="dashed",linewidth=0.8) plt.title("soft_th(lam,x)") plt.text(-1.5,1,’lambda=5’,fontsize=15)

52. We wish to find the β ∈ R that minimizes

N ∑ 1 2 L = (y i − x i β)+ λ|β|, 2N i=1

given (x i , y i ) ∈ R × R, i = 1, . . . , N, λ > 0, where we assume that ∑ 1N2 x1, . . . , x N have been scaled so that x= 1. Express the solution by Ni=1 i ∑ 1N z := x i y i and function Sλ (·). Ni=1 p 53. For p > 1 and λ > 0, we estimate the coefficients β0 ∈ R and β ∈ R p as follows: initially, we randomly give the coefficients β ∈ R. Then, we ( ) N ∑x r∑ i,j i,j update β j by Sλ, where ri,j := y i − x i,j β j . We repeat this N i=1k =j process for j = 1, . . . , p and repeat the cycle until convergence. The function lasso below is used to scale the sample-based variance to one for each of the p variables before estimation of (β0, β). Fill in the blanks and execute the procedure.

def lasso(x,y,lam=0):#lam stands for lambda X=copy.copy(x) n,p=X.shape

---

<!-- Página 137 -->

Exercises 49–56 129

X_bar=np.zeros(p) s=np.zeros(p) for j in range(p): X_bar[j]=np.mean(X[:,j]) for j in range(p): s[j]=np.std(X[:,j]) X[:,j]=(X[:,j]-X_bar[j])/s[j] y_bar=np.mean(y) y=y-y_bar eps=1 beta=np.zeros(p); beta_old=np.zeros(p) while eps>0.001: for j in range(p): index=list(set(range(p))-{j}) r=# blank(1) # beta[j]=# blank(2) # eps=np.max(np.abs(beta-beta_old)) beta_old=beta for j in range(p): beta[j]=beta[j]/s[j] beta_0=# blank(3) # return {’beta’:beta,’beta_0’:beta_0}

df=np.loadtxt("crime.txt",delimiter="\t") X=df[:,[i for i in range(2,7,1)]] p=X.shape[1] y=df[:,0]

lambda_seq=np.arange(0,200,0.5) plt.xlim(0,200) plt.ylim(-7.5,15) plt.xlabel("lambda") plt.ylabel("beta") labels=["annual police funding in resident","% of people 25 years+ with 4 yrs. of high school", "% of 16 to 19 year-olds not in highschool and not highschool graduates" ,"% of 18 to 24 year-olds in college", "% of 18 to 24 year-olds in college"]

for j in range(p): coef_seq=[] for l in lambda_seq: coef_seq.append(# blank(4) #) plt.plot(lambda_seq,coef_seq,label="{}".format(labels[j])) plt.legend(loc="upper right") plt.title("values of each coefficient for each lambda")

54. Transform Problem 53(lasso) into the setting in Problem 49(ridge) and execute it. Hint: Replace the line of eps and the while loop in the function lasso by

beta=np.linalg.inv(X.T@X+n*lam*np.eye(p))@X.T@y

and change the function name to ridge. Blank (4) should be ridge rather than lasso.

---

<!-- Página 138 -->

130 6 Regularization

55. Look up the meanings of Lasso and LassoCV and find the optimal λ and β for the data below. Which variables are selected among the five variables?

from sklearn.linear_model import Lasso

Las=Lasso(alpha=20) Las.fit(X,y) Las.coef_

array([132.15580773, -24.96440514, 19.26809441, 0. , 0. ])

# The grid search for the value specified in alphas Lcv=LassoCV(alphas=np.arange(0.1,30,0.1),cv=10) Lcv.fit(X,y) Lcv.alpha_ Lcv.coef_

Hint: The coefficients are displayed via Lcv.coef_. If a coefficient is nonzero, we consider it to be selected. 56. Given x i,1, x i,2, y i ∈ R, i = 1, . . . , N, let ˆβ1 and ˆβ2 be the β1 and β2 that N ∑ 2 minimize S :=(y i − β1x i,1 − β2x i,2)given ˆβ1x i,1 + ˆβ2x i,2 , ˆy i , (i = i=1 1, . . . , N). Show the following three equations:

(a)

NN ∑∑ x i,1(y i − ˆy i ) =x i,2(y i − ˆy i ) = 0 . i=1i=1

For arbitrary β1, β2 ,

y i − β1x i,1 − β2x i,2 = y i − ˆy i − (β1 − ˆβ1)x i,1 − (β2 − ˆβ2)x i,2 .

N ∑ 2 For arbitrary β1, β2 ,(y i − β1x i,1 − β2x i,2)can be expressed by i=1

NNN ∑∑∑ 2222 (β1 − ˆβ1)xi,1 +2(β1 − ˆβ1)(β2 − ˆβ2)xi,1xi,2 + (β2 − ˆβ2)xi,2 i=1i=1i=1

N ∑ 2 +(yi − ˆyi ). i=1

---

<!-- Página 139 -->

Exercises 49–56 131

NN ∑∑∑ 22N (b) We consider the casex=x= 1 and x i,1x i,2 = 0. In i,1 i,2 i=1 i=1i=1 the standard least squares method, we choose the coefficients as β1 = ˆβ1 and β2 = ˆβ2 . However, under the constraint that |β1| + |β2| is less than a constant, we choose (β1, β2) at which the circle with center ( ˆβ1, ˆβ2) and the smallest radius comes into contact with the rhombus. Suppose that we grow the radius of the circle with center ( ˆβ1, ˆβ2) until it comes into contact with the rhombus that connects (1, 0), (0, 1), (−1, 0), (0, −1). Show the region of the centers such that one of the coordinates ( ˆβ1 and ˆβ2) is zero. (c) What if the rhombus in (b) is replaced by a unit circle?

---

<!-- Página 140 -->

## Chapter 7

# Nonlinear Regression

Abstract For regression, until now we have focused on only linear regression, but in this chapter, we will consider the nonlinear case where the relationship between the covariates and response is not linear. In the case of linear regression in Chap. 2, if there are p variables, we calculate p + 1 coefficients of the basis that consists of p + 1 functions 1, x1, · · · , x p. This chapter addresses regression when the basis is general. For example, if the response is expressed as a polynomial of the covariate p x, the basis consists of 1, x, · · · , x . We also consider spline regression and find a basis. In that case, the coefficients can be found in the same manner as for linear regression. Moreover, we consider local regression for which the response cannot be expressed by a finite number of basis functions. Finally, we consider a unified framework (generalized additive model) and backfitting.

7.1 Polynomial Regression

We consider fitting the relation between the covariates and response to a polynomial from observed data (x1, y1), . . . , (x N , y N ) ∈ R × R. By a polynomial, we mean the function f : R → R that is determined by specifying the coefficients β0, β1, . . . , β p p 3 in β0 + β1x + · · · + β p x for p ≥ 1, such as f (x) = 1 + 2x − 4x. As we do in the least squares method, we assume that the coefficients β0, . . . , β p minimize

N ∑ p2 (y i − β0 − β1x i − · · · − β p x ). i i=1

jT By overlapping x i,j and x , if the matrix X X is nonsingular with i ⎡⎤ p 1 x1 · · · x 1 ⎢... .⎥ X =⎣... . .⎦ , . . . p 1 x N · · · x N

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2021133 J. Suzuki, Statistical Learning with Math and Python, https://doi.org/10.1007/978-981-15-7877-9_7

---

<!-- Página 141 -->

134 7 Nonlinear Regression

Fig. 7.1 We generated the p = 3 data by adding standardp = 5 Gaussian random values to ap = 7 sine curve and fit the data to polynomials of orders) x ( p = 3, 5, 7f

-3 -2 -1 0 1 2 3 x

T −1T we can check that ˆβ = (X X)X y is the solution. As in linear regression ˆf (x) = ˆβ+ ˆβx+ · · · + ˆβ x , from the obtained ˆβ, . . . , ˆβ , we construct an estimated 0 11 p p0p function

ˆf (x) = ˆβ+ ˆβx + · · · + ˆβ x p . 0 1p

Example 52 We generate N = 100 observed data by adding standard Gaussian random values to the sine function and fit them to polynomials of orders p = 3, 5, 7. We show the results in Fig. 7.1. The generation of polynomials is achieved via the following code:

def g(beta,u): S=0 for j in range(p+1):# length of beta = p+1 S=S+beta[j]*u**j return S

n=100; x=randn(n); y=np.sin(x)+randn(n) m=3 p_set=[3,5,7] col_set=["red","blue","green"] randn(3)*randn(3)**np.array([1,2,3])

array([ 0.07981705, -0.06213429, -0.01101873])

plt.scatter(x,y,s=20,c="black") plt.ylim(-2.5,2.5) x_seq=np.arange(-3,3,0.1) for i in range(m): p=p_set[i] X=np.ones([n,1]) for j in range(1,p+1): xx=np.array(x**j).reshape((n,1)) X=np.hstack((X,xx)) beta=np.linalg.inv(X.T@X)@X.T@y def f(u): return g(beta,u)

---

<!-- Página 142 -->

7.1 Polynomial Regression 135

plt.plot(x_seq,f(x_seq),c=col_set[i],label="p={}".format(p)) plt.legend(loc="lower right")

We can show that if no less than p +1 are different among x1, . . . , x N , the matrix T T X X is nonsingular. To examine this claim, since the ranks of X X and X are equal (see Sect. 2.2), it is sufficient to show that the determinant is not zero for the matrix N×(p+1) such that the p + 1 columns are contained in X ∈ R, which is true from the fact that, in Example 7, the determinant of the n × n Vandermonde’s matrix is not zero if a1, . . . , a n are different. Polynomial regression can be applied to more general settings. For f0 = 1 and T −1T f1, . . . , fp : R → R, we can compute ˆβ = (X X)X y as long as each of the columns in ⎡⎤ 1 f1(x1) · · · fp (x1) ⎢... .⎥ X =⎣... . .⎦ . . . 1 f1(x N ) · · · fp (x N )

is linearly independent. From the obtained ˆβ0, . . . , ˆβ p, we can construct

ˆf (x) = ˆβf(x) + ˆβf(x) + · · · + ˆβ f(x) , 0011p p

where we often assume f0(x) = 1.

2 Example 53 We then generate x ∼ N(0, π) and { −1 + , 2m − 1 ≤ |x| < 2m y =, m = 1, 2, . . . (7.1) 1 + , 2m − 2 ≤ |x| < 2m − 1

2 (Fig. 7.2), where  ∼ N(0, 0.2 ). We observe that the even functions f1(x) = 1, f2(x) = cos x, f3(x) = cos 2x, and f4(x) = cos 3x are better to fit than the odd functions f1(x) = 1, f2(x) = sin x, f3(x) = sin 2x, and f4(x) = sin 3x (Fig. 7.3) because we generated the observed data according to an even function with added noise.

Fig. 7.2 The graph of the function obtained by1 removing noise in (7.1). It is 3- 2- 1- 0 1 2 3 an even and cyclic function -1

---

<!-- Página 143 -->

136 7 Nonlinear Regression

Fig. 7.3 We generated data such that whether y is close to either −1 or 1 is based on whether x is even or odd when truncating it. Note that (7.1) is a cyclic and even function when removing the noise  (Fig. 7.2). We observe that cos nx, n = 1, 2, . . ., are better to fit than sin nx, n = 1, 2, . . . -4 -2 0 2 4

The procedure is implemented via the following code:

# Generating data close to an even function n=100 x=randn(n)*np.pi y=np.round(x)%2*2-1+randn(n)*0.2

# Write axes, etc. plt.scatter(x,y,s=20,c="black") plt.tick_params(labelleft=False) x_seq=np.arange(-8,8,0.2)

def f(x,g): return beta[0]+beta[1]*g(x)+beta[2]*g(2*x)+beta[3]*g(3*x)

# select 1, cosx ,cos2x and cos3x as basis X=np.ones([n,1]) for j in range(1,4): xx=np.array(np.cos(j*x)).reshape((n,1)) X=np.hstack((X,xx)) beta=np.linalg.inv(X.T@X)@X.T@y plt.plot(x_seq,f(x_seq,np.cos),c="red")

# select 1, sinx ,sin2x and sin3x as basis X=np.ones([n,1]) for j in range(1,4): xx=np.array(np.sin(j*x)).reshape((n,1)) X=np.hstack((X,xx)) beta=np.linalg.inv(X.T@X)@X.T@y plt.plot(x_seq,f(x_seq,np.sin),c="blue")

7.2 Spline Regression

In this section, we restrict the polynomials to those with an order at most three, such 3 2 3 as x+ x− 7, −8x− 2x + 1.

---

<!-- Página 144 -->

7.2 Spline Regression 137

We first note that if polynomials f and g of order p = 3 coincide with each other (j ) (j ) up to the second derivative at the point x∗ ∈ R: f (x∗) = g (x∗), j = 0, 1, 2, in ⎧ 3 ⎪∑ ⎪j ⎪ ⎪f (x) =β j (x − x∗) ⎪ ⎨ j =0 3 ⎪∑ ⎪ ⎪j ⎪g(x) =γ j (x − x∗) ; ⎪ ⎩ j =0

′ then, we have β j = γ j , j = 0, 1, 2. In fact, we see that f (x∗) = g(x∗), f (x∗) = ′′′′′ g(x∗), and f (x∗) = g(x∗) imply 2β2 = 2γ2 , β1 = γ1 , and β0 = γ0 , respectively. Hence, we have

3 f (x) − g(x) = (β3 − γ3)(x − x∗).

In the following, for K ≥ 1, we divide the line R at the knots −∞ = α0 < α1 < · · · < αK < αK+1 = ∞ and express the function f (x) as a polynomial fi (x) for each αi ≤ x ≤ αi+1 , where we assume that those K + 1 functions are continuous up to the second derivative at the K knots:

(j )(j ) f (αi ) = f (αi ), j = 0, 1, 2, i = 1, . . . , K (7.2) i−1i

(spline function). Note that there exists a constant γ i such that fi (x) = fi−1(x) + 3 γ i (x − αi )for each i = 1, 2, . . . , K + 1. In (7.2), there are 3K linear constraints for 4(K + 1) variables w.r.t. K + 1 cubic polynomials, each of which contains four coefficients, which means that there remain K + 4 degrees of freedom. We first arbitrarily determine the values 2 3 of β0, β1, β2, and β3 in f0(x) = β0 + β1x + β2x+ β3xfor α0 ≤ x ≤ α1 . Next, noting that for each i = 1, 2, . . . , K, the difference between fi and fi−1 3 is (x − αi )multiplied by a constant β i+3 , all the polynomials are determined by specifying β i+3 , i = 1, 2, . . . , K. We express the function f as follows: ⎧ 2 3 ⎪β0 + β1x + β2x+ β3x, α0 ≤ x ≤ α1 ⎪ ⎪ ⎪2 3 3 ⎪β0 + β1x + β2x+ β3x+ β4(x − α1), α1 ≤ x ≤ α2 ⎪⎪ ⎪2 3 3 3 ⎨β+ βx + βx+ βx+ β(x − α)+ β(x − α), α≤ x ≤ α 0 12341522 3 f (x) =.. ⎪.. ⎪. . ⎪ ⎪⎪ ⎪2 3 3 ⎪β0 + β1x + β2x+ β3x+ β4(x − α1) ⎪ ⎩ 3 3 +β5(x − α2)+ · · · + βK+3(x − αK ), αK ≤ x ≤ αK+1

K ∑ 2 3 3 = β0 + β1x + β2x+ β3x+βi+3(x − αi ), + i=1

---

<!-- Página 145 -->

138 7 Nonlinear Regression

where (x − αi )+ is the function that takes x − αi and zero for x > αi and for x ≤ αi , respectively. The method for choosing the coefficients β0, . . . , β K+3 is similar to the method we use for linear regression. Suppose we have observa- tions (x1, y1), . . . , (x N , y N ), where the sample points x1, . . . , x N and the knots α1, . . . , αK should not be confused. For the matrix ⎡⎤ 23333 1 x1 xx(x1 − α1)+ (x1 − α2)+ · · · (x1 − αK )+ 1 1 ⎢23333⎥ 1 xxx(x− α)(x− α)· · · (x− α) ⎢2 2 2 2 1+ 2 2+ 2 K +⎥ X =⎢........⎥, ⎣........⎦ . . . . . . . . 23333 1 x N xx(x N − α1)(x N − α2)· · · (x N − αK ) N N + + +

T we determine the β = [β0, . . . , β K+3]that minimizes

N ∑ 233332 {yi −β0−xi β1−xi β2−xi β3−(xi −α1)+β4−(xi −α2)+β5−· · ·−(xi −αK )+βK+3}. i=1

If the rank is K + 4, i.e., the K + 4 columns of X are linearly independent, then T T −1T X X is nonsingular, and we obtain the solution ˆβ = (X X)X y (Fig. 7.4).

Example 54 After generating data, we execute spline regression with K = 5, 7, 9 knots. We present the results in Fig. 7.5.

Spline Curve

2 fi−1(αi) = fi(αi) f0(α1) = f1(α1) 1 f(αi) = f(αi)f(α) = f(α) i−1i 011 1 f(αi) = f(αi)f0 (α1) = f1””(α1) i−1i fK−1(αK ) = fK (αK )) 0(x fK−1(αK ) = fK (αK )f fK−1(αK ) = fK (αK ) -1

-2α1 αi αK· · · · · ·

-4 -2 0 2 4 x

Fig. 7.4 In spline functions, the value and the first and second derivatives should coincide on the left and right of each knot

---

<!-- Página 146 -->

7.2 Spline Regression 139

K = 5 K = 7 K = 9

) x ( f

-4 -2 02 4 x

Fig. 7.5 Spline regression with K = 5, 7, 9 knots (Example 54)

n=100 x=randn(n)*2*np.pi y=np.sin(x)+0.2*randn(n) col_set=["red","green","blue"] K_set=[5,7,9] plt.scatter(x,y,c="black",s=10) plt.xlim(-5,5) for k in range(3): K=K_set[k] knots=np.linspace(-2*np.pi,2*np.pi,K) X=np.zeros((n,K+4)) for i in range(n): X[i,0]=1 X[i,1]=x[i] X[i,2]=x[i]**2 X[i,3]=x[i]**3 for j in range(K): X[i,j+4]=np.maximum((x[i]-knots[j])**3,0) beta=np.linalg.inv(X.T@X)@X.T@y def f(x): S=beta[0]+beta[1]*x+beta[2]*x**2+beta[3]*x**3 for j in range(K): S=S+beta[j+4]*np.maximum((x-knots[j])**3,0) return S u_seq=np.arange(-5,5,0.02) v_seq=[] for u in u_seq: v_seq.append(f(u)) plt.plot(u_seq,v_seq,c=col_set[k],label="K={}".format(K)) plt.legend()

---

<!-- Página 147 -->

140 7 Nonlinear Regression

7.3 Natural Spline Regression

In this section, we modify spline regression by replacing cubic curves with lines only for both ends x ≤ α1 and αK ≤ x (natural spline curve). Suppose we write the function f for x ≤ αK as follows: ⎧ ⎪β1 + β2x, α0 ≤ x ≤ α1 ⎪ ⎪ ⎪3 ⎪β+ βx + β(x − α), α≤ x ≤ α ⎪1 2311 2 ⎪ ⎪ ⎨.. .. . . f (x) = ⎪3 3 ⎪β1 + β2x + β3(x − α1)+ · · · + β K (x − αK−2), αK−2 ≤ x ≤ αK−1 ⎪ ⎪ ⎪3 ⎪β+ βx + β(x − α)+ · · · ⎪1 231 ⎪ ⎩3 3 +β K (x − αK−2)+ β K+1(x − αK−1), αK−1 ≤ x ≤ αK .

K+1 ∑ Since the second derivative at x = αK is zero, we have 6β j (αK −αj −2) = 0, j =3 and we obtain

K ∑α− α K j −2 β K+1 = −β j . (7.3) αK − αK−1 j =3

Then, if we find the values of β1, · · · , β K , we obtain the values of f (αK ) and ′′ f (αK ) and the line y = f (αK )(x − αK ) + f (αK ) for x ≥ αK (Fig. 7.6). Thus, the function f is obtained by specifying β1, . . . , β K .

Proposition 20 The function f (x) has K cubic polynomials h1(x) = 1, h2(x) = x, hj +2(x) = d j (x) − d K−1(x), j = 1, . . . , K − 2, as a basis, and if we define

γ1 := β1, γ2 := β2, γ3 := (αK − α1)β3, . . . , γ K := (αK − αK−2)β K

K ∑ for each β1, . . . , β K , then we can express f by f (x) =γ j hj (x), where we have j =1

33 (x − αj )+ − (x − αK )+ d j (x) = , j = 1, . . . , K − 1 . αK − αj

For the proof, see the Appendix at the end of this chapter.

---

<!-- Página 148 -->

7.3 Natural Spline Regression 141

Natural Spline Curve

6 fK−2(αK−1) = fK−1(αK−1) 4 f(αK−1) = f(αK−1)f0(α1) = f1(α1) K−2K−1 f(αK−1) = f(αK−1)f(α) = f(α)fK−1(αK ) = fK (αK ) 2K−2K−10111 f(α) = f(α) 0 = f1 (α1)K−1K K K f(αK ) = 0) 0K−1(x f

-2

-4 α1 αKαK−1 -6

-6 -4 -2 0 2 4 6 x

Fig. 7.6 In the natural spline curves, we choose the slope and intercept of the line for x ≤ α1 (two degrees of freedom) and the coefficients for αi ≤ x ≤ αi+1 (one degree of freedom for each i = 1, 2, . . . , K − 2). However, no degrees of freedom are left for αK−1 ≤ x ≤ αK because ′′ f (α) = 0. Moreover, for αK ≤ x, the slope and intercept are determined from the values of ′ f (αK ) and f (αK ), and no degrees of freedom are left as well

We can construct the corresponding Python code as follows:

def d(j,x,knots): K=len(knots) return (np.maximum((x-knots[j])**3,0)-np.maximum((x-knots[K-1])**3,0))/( knots[K-1]-knots[j])

def h(j,x,knots): K=len(knots) if j==0: return 1 elif j==1: return x else : return (d(j-2,x,knots)-d(K-2,x,knots))# Note that the way of counting in array is beginning 0.

If we are given observations (x1, y1), . . . , (x N , y N ), then we wish to determine 2 γ that minimizes ‖y − Xγ ‖with ⎡⎤ h1(x1) = 1 h2(x1) · · · hK (x1) ⎢⎥ h(x) = 1 h(x) · · · h(x) ⎢1222K 2⎥ X =⎢...⎥. (7.4) ⎣...⎦ . . · · · . h1(x N ) = 1 h2(x N ) · · · hK (x N )

---

<!-- Página 149 -->

142 7 Nonlinear Regression

T If the rank is K, i.e., the K columns in X are linearly independent, the matrix X X T −1T is nonsingular, and we obtain the solution ˆγ = (X X)X y.

Example 55 If K = 4, then we have h1(x) = 1, h2(x) = x, ⎧ ⎪0, x ≤ α1 ⎪ ⎪3 ⎪(x − α) ⎪1 ⎪, α≤ x ≤ α ⎪1 3 ⎨ α4 − α1 h3(x) = d1(x) − d3(x) = 33 ⎪(x − α1)(x − α3) ⎪ ⎪− , α≤ x ≤ α ⎪3 4 ⎪α− αα− α ⎪4 14 3 ⎪ ⎩ (α3 − α1)(3x − α1 − α3 − α4), α4 ≤ x

⎧ ⎪0, x ≤ α2 ⎪ ⎪3 ⎪(x − α) ⎪2 ⎪ ⎪, α2 ≤ x ≤ α3 ⎨ α4 − α2 h4(x) = d2(x) − d3(x) =33 ⎪(x − α2)(x − α3) ⎪ ⎪− , α3 ≤ x ≤ α4 ⎪ ⎪α− αα− α ⎪4 24 3 ⎪ ⎩ (α3 − α2)(3x − α2 − α3 − α4), α4 ≤ x.

Hence, the lines for x ≤ α1 and x ≥ α4 are

f (x) = γ1 + γ2x, x ≤ α1 f (x) = γ1 + γ2x + γ3(α3 − α1)(3x − α1 − α3 − α4)

+γ4(α3 − α2)(3x − α2 − α3 − α4), x ≥ α4.

Example 56 We compare the ordinary and natural spline curves (Fig. 7.7). By definition, the natural spline becomes a line at both ends, although considerable differences are observed near the points α1 and αK . The procedure is implemented according to the following code:

n=100 x=randn(n)*2*np.pi y=np.sin(x)+0.2*randn(n) K=11 knots=np.linspace(-5,5,K) X=np.zeros((n,K+4)) for i in range(n): X[i,0]=1 X[i,1]=x[i] X[i,2]=x[i]**2 X[i,3]=x[i]**3 for j in range(K): X[i,j+4]=np.maximum((x[i]-knots[j])**3,0) beta=np.linalg.inv(X.T@X)@X.T@y

---

<!-- Página 150 -->

7.3 Natural Spline Regression 143

K=6

Spline Natural Spline ) x ( , g ) x ( f

-6 -4 -2 0 2 4 6 x

K=11

Spline Natural Spline ) x ( , g ) x ( f

-6 -4 -2 0 2 4 6 x

Fig. 7.7 Comparison of the ordinary (blue) and natural (red) splines when K = 6 (left) and K = 11 (right) in Example 56. While the natural spline becomes a line for each of the both ends, they do not coincide inside the region, in particular, near the borders

def f(x): S=beta[0]+beta[1]*x+beta[2]*x**2+beta[3]*x**3 for j in range(K): S=S+beta[j+4]*np.maximum((x-knots[j])**3,0) return S

X=np.zeros((n,K)) X[:,0]=1 for j in range(1,K): for i in range(n): X[i,j]=h(j,x[i],knots) gamma=np.linalg.inv(X.T@X)@X.T@y

def g(x): S=gamma[0] for j in range(1,K): S=S+gamma[j]*h(j,x,knots) return S

---

<!-- Página 151 -->

144 7 Nonlinear Regression

u_seq=np.arange(-6,6,0.02) v_seq=[]; w_seq=[] for u in u_seq: v_seq.append(f(u)) w_seq.append(g(u)) plt.scatter(x,y,c="black",s=10) plt.xlim(-6,6) plt.xlabel("x") plt.ylabel("f(x),g(x)") plt.tick_params(labelleft=False) plt.plot(u_seq,v_seq,c="blue",label="spline ") plt.plot(u_seq,w_seq,c="red",label=" natural spline") plt.vlines(x=[-5,5],ymin=-1.5,ymax=1.5,linewidth=1) plt.vlines(x=knots,ymin=-1.5,ymax=1.5,linewidth=0.5,linestyle="dashed") plt.legend()

7.4 Smoothing Spline

Given observed data (x1, y1), . . . , (x N , y N ), we wish to obtain f : R → R that minimizes

N∫ ∞ ∑ 2 ′′2 L(f ) :=(y i − f (x i ))+ λ{f (x)}dx (7.5) −∞ i=1

(smoothing spline), where λ ≥ 0 is a constant determined a priori. Suppose x1 < · · · < x N . The second term in (7.5) penalizes the complexity of the function f , and ′′2 {f (x)}intuitively expresses how nonsmooth the function is at x. If f is linear, the value is zero, and if λ is small, although the curve meanders, the curve is easier to fit to the observed data. On the other hand, if λ is large, although the curve does not follow the observed data, the curve is smoother. First, we show that the optimal f is realized by the natural spline with knots x1, . . . , x N .

Proposition 21 (Green and Silverman, 1994) The natural spline f with knots x1, . . . , x N minimizes L(f ).

See the Appendix at the end of this chapter for the proof. Next, we obtain the coefficients γ1, . . . , γ N of such a natural spline f (x) = N ∑ γ i hi (x). Let G = (gi,j ) be the matrix with elements i=1 ∫ ∞ ′′′′ gi,j :=h(x)h(x)dx . (7.6) i j −∞

---

<!-- Página 152 -->

7.4 Smoothing Spline 145

Then, the second term in L(g) becomes

∫ ∫ NN ∞∞∑∑ ′′2′′′′ λ{f (x)}dx = λγ i h(x)γ j h(x)dx i j −∞−∞ i=1j =1 NN∫ ∞ ∑∑ ′′′′T = λγ i γ jh(x)h(x)dx = λγ Gγ . i j −∞ i=1j =1

Thus, by differentiating L(g) with respect to γ , as done to obtain the coefficients of ridge regression in Chap. 5, we find that the solution of

T −X (y − Xγ ) + λGγ = 0

is given by

T −1T ˆγ = (X X + λG)X y .

Because the proof of the following proposition is complicated, it is provided in the Appendix at the end of this chapter.

Proposition 22 The elements gi,j defined in (7.6) are given by () 2 (x N−1 − x j −2)12x N−1 + 6x j −2 − 18x i−2 +12(x N−1 − x i−2)(x N−1 − x j −2)(x N − x N−1) gi,j = (x N − x i−2)(x N − x j −2)

for x i ≤ x j , where gi,j = 0 for either i ≤ 2 or j ≤ 2.

For example, by means of the following procedure, we can obtain the matrix G from the knots x1 < · · · < x N .

def G(x): n=len(x) g=np.zeros((n,n)) for i in range(2,n): for j in range(i,n): g[i,j]=12*(x[n-1]-x[n-2])*(x[n-2]-x[j-2])*(x[n-1]-x[i-2])/(x[n -1]-x[i-2])/(x[n-1]-x[j-2])+(12*x[n-2]+6*x[j-2]-18*x[i-2])*(x[ n-2]-x[j-2])**2/(x[n-1]-x[i-2])/(x[n-1]-x[j-2]) g[j,i]=g[i,j] return g

Example 57 Computing the matrix G and ˆγ for each λ, we draw the smoothing spline curve. We observe that the larger the λ is, the smoother the curve (Fig. 7.8). The procedure is implemented via the following code:

---

<!-- Página 153 -->

146 7 Nonlinear Regression

Fig. 7.8 In smoothing spline, Smoothing Spline (N= 100) we specify a parameter λ that expresses the smoothness λ = 40 instead of knots. Forλ = 400 λ = 40, 400, 1000, weλ = 1000 observe that the larger the λ is, the more difficult it is to fit the curve to the observed data) x ( g

-5 0 5 x

# generating data n=100; a=-5; b=5 x=(b-a)*np.random.rand(n)+a# uniform distribution (-5,5) y=x-0.02*np.sin(x)-0.1*randn(n) index=np.argsort(x); x=x[index]; y=y[index]

# compute x X=np.zeros((n,n)) X[:,0]=1 for j in range(1,n): for i in range(n): X[i,j]=h(j,x[i],x) GG=G(x) lambda_set=[1,30,80] col_set=["red","blue","green"] plt.scatter(x,y,c="black",s=10) plt.title("smoothing splines (n=100)") plt.xlabel("x") plt.ylabel("g(x)") plt.tick_params(labelleft=False)

# smoothing splines when lambda=40, 400, 1000 for i in range(3): lam=lambda_set[i] gamma=np.linalg.inv(X.T@X+lam*GG)@X.T@y def g(u): S=gamma[0] for j in range(1,n): S=S+gamma[j]*h(j,u,x) return S u_seq=np.arange(-8,8,0.02) v_seq=[] for u in u_seq: v_seq.append(g(u)) plt.plot(u_seq,v_seq,c=col_set[i],label="lambda={}".format(lambda_set[i ])) plt.legend()

---

<!-- Página 154 -->

7.4 Smoothing Spline 147

In ridge regression, we obtain a matrix of size (p + 1) × (p + 1). However, for the current problem, we must compute the inverse of a matrix of size N × N, so we need an approximation because the computation is complex for large N. However, if N is not large, the value of λ can be determined by cross-validation. Proposition 14 applies when matrix X is given by (7.4) with K = N. In addition, T Proposition 15 applies when A is given by X X + λG. Thus, the predictive error of CV in Proposition 14 is given by ∑ −12 CV [λ] := ‖(I − H S [λ])e S ‖, S

T −1T where H S [λ] := XS (X X + λG)X . We construct the following procedure: S

def cv_ss_fast(X,y,lam,G,k): n=len(y) m=int(n/k) H=X@np.linalg.inv(X.T@X+lam*G)@X.T df=np.sum(np.diag(H)) I=np.eye(n) e=(I-H)@y I=np.eye(m) S=0 for j in range(k): test=np.arange(j*m,(j+1)*m) S=S+(np.linalg.inv(I-H[test,:][:,test])@e[test]).T@(np.linalg.inv(I- H[test,test])@e[test]) return {’score’:S/n,’df’:df}

Note that if we set λ = 0, then the procedure is the same as cv_fast in Chap. 3. How much the value of λ affects the estimation of γ depends on several conditions, and we cannot compare the λ values under different settings. Instead, we often use the effective degrees of freedom, the trace of the matrix H [λ] := T −1T X(X X + λG)X , rather than λ. The effective degrees of freedom express how well the fitness and simplicity are balanced (Fig. 7.9).

Fig. 7.9 The larger the λ is,Trace of H[λ] vs CV [λ] the smaller the effective degrees of freedom. Even if the effective degrees of0.00014 freedom are large, the predictive error of CV may increase 0.00008

Predictive Error of CV 0.00002 3.0 3.5 4.0 4.5 5.0 5.5 Effective Degree of Freedom

---

<!-- Página 155 -->

148 7 Nonlinear Regression

1 Example 58 For sample size N = 100, changing λ value from 1 to 50, we draw the graph of the effective degrees of freedom (the trace of H [λ]) and the predictive error of CV (CV [λ]). The execution is implemented via the following code.

# generating data n=100; a=-5; b=5 x=(b-a)*np.random.rand(n)+a# uniform distribution (-5,5) y=x-0.02*np.sin(x)-0.1*randn(n) index=np.argsort(x); x=x[index]; y=y[index] # X=np.zeros((n,n)) X[:,0]=1 for j in range(1,n): for i in range(n): X[i,j]=h(j,x[i],x) GG=G(x) # Calculations and plots of Effective Degree of Freedom and prediction errors v=[]; w=[] for lam in range(1,51,1): res=cv_ss_fast(X,y,lam,GG,n) v.append(res[’df’]) w.append(res[’score’]) plt.plot(v,w) plt.xlabel("Effective Degree of Freedom") plt.ylabel("prediction errors by CV ") plt.title("Effective Degree of Freedom and prediction errors by CV")

7.5 Local Regression

In this section, we consider the Nadaraya–Watson estimator and local linear regression. Let X be a set. We call a function k : X × X → R a kernel (in a strict sense) if

n×n 1. for any n ≥ 1 and x1, . . . , x n, the matrix K ∈ X with Ki,j = k(x i , x j ) is nonnegative definite (positive definiteness); 2. for any x, y ∈ X , k(x, y) = k(y, x) (symmetry).

For example, if X is a vector space, its inner product is a kernel. In fact, from the definition of the inner product 〈·, ·〉: for elements x, y, and z of the vector space and a real number c, 〈x, y + z〉 = 〈x, y〉 + 〈x, z〉, 〈cx, y〉 = c〈x, y〉, 〈x, x〉 ≥ 0 for

1 For N > 100, we could not compute the inverse matrix; errors occurred due to memory shortage.

---

<!-- Página 156 -->

7.5 Local Regression 149

arbitrary a1, . . . , a n ∈ X and c1, . . . , c n ∈ R, we have ⎛⎞ nn ∑∑∑∑ 0 ≤ k⎝c i a i ,c j a j⎠ = c i c j k(a i , a j ) i=1j =1ij ⎡⎤⎡⎤ k(a1, a1) · · · k(a1, a n )c1 ⎢.. .⎥⎢.⎥ = [c1, . . . , c n]⎣.. . .⎦⎣.⎦ . . .. k(a n , a1) · · · k(a n , a n )c n

Kernels are used to express the similarity of two elements in set X : the more similar the x, y ∈ X are, the larger the k(x, y). 2 Even if k : X × X → R does not satisfy the positive definiteness, it can be used if it accurately expresses the similarity.

Example 59 (Epanechnikov Kernel) The kernel k : X × X → R defined by ( ) |x − y| Kλ (x, y) = D λ ⎧ ⎨32 (1 − t), |t| ≤ 1 D(t) =4 ⎩ 0, Otherwise

does not satisfy positive definiteness. In fact, when λ = 2, n = 3, x1 = −1, x2 = 0, and x3 = 1, the matrix with elements Kλ (x i , x j ) can be expressed as

⎡⎤⎡⎤ Kλ (x1, x1) Kλ (x1, x2) Kλ (x1, x3)3/4 9/16 0 ⎣K(x, x) K(x, x) K(x, x)⎦ =⎣9/16 3/4 9/16⎦ . λ 21λ 22λ 23 Kλ (x3, x1) Kλ (x3, x2) Kλ (x3, x3)0 9/16 3/4

36 510 510 39 We see that the determinant is 3 /2 − 3 /2 − 3 /2 = −3 /2 . Since the determinant is equal to the product of the eigenvalues (Proposition 6), at least one of the three eigenvalues should be negative.

The Nadaraya–Watson estimator is constructed as

∑ N K(x, x i )y i ˆf (x) =i=1 ∑N K(x, x ) j =1 j

from observed data (x1, y1), . . . , (x N , y N ) ∈ X × R, where X is a set and k : X × X → R is a kernel. Then, given a new data point x∗ ∈ X , the estimator returns

2 We call such a kernel a kernel in a broader sense.

---

<!-- Página 157 -->

150 7 Nonlinear Regression

Fig. 7.10 We apply theNadaraya-Watson Estimator Epanechnikov kernel to the 3 Nadaraya–Watson estimatorλ = 0.05 and draw curves forλ = 0.25 λ = 0.05, 0.25. Finally, we2 λ = λbest compute the optimal λ and draw the curve in the same 1 graph (Example 60) y 0

-1

-2 -3 -2 -1 0 1 2 3 x

ˆf (x), which weights y, . . . , y according to the ratio ∗1N

K(x∗, x1)K(x∗, x N ) ∑, . . . , ∑. NN K(x, x ) K(x, x ) j =1 ∗j j =1 ∗j

Since we assume that k(u, v) expresses the similarity between u, v ∈ X , the larger the weight on y i , the more similar x∗ and x i are.

Example 60 We apply the Epanechnikov kernel to the Nadaraya–Watson estima- tor. The Nadaraya–Watson estimator executes successfully even for kernels that do not satisfy positive definiteness. For a given input x∗ ∈ X , the weights are only on y i , i = 1, . . . , N, such that x i − λ ≤ x∗ ≤ x i + λ. If the value of λ is small, the prediction is made based on (x i , y i ) such that x i is within a small neighboring region of x∗. We present the results obtained by executing the following code in Fig. 7.10.

n=250 x=2*randn(n) y=np.sin(2*np.pi*x)+randn(n)/4

def D(t): return np.maximum(0.75*(1-t**2),0)

def K(x,y,lam): return D(np.abs(x-y)/lam)

---

<!-- Página 158 -->

7.5 Local Regression 151

def f(z,lam): S=0; T=0 for i in range(n): S=S+K(x[i],z,lam)*y[i] T=T+K(x[i],z,lam) if T==0: return(0) else: return S/T

plt.scatter(x,y,c="black",s=10) plt.xlim(-3,3) plt.ylim(-2,3) xx=np.arange(-3,3,0.1) yy=[] for zz in xx: yy.append(f(zz,0.05)) plt.plot(xx,yy,c="green",label="lambda=0.05") yy=[] for zz in xx: yy.append(f(zz,0.25)) plt.plot(xx,yy,c="blue",label="lambda=0.25")

# The curves of lam =0.05 , 0.25 were displayed. m=int(n/10) lambda_seq=np.arange(0.05,1,0.01) SS_min=np.inf for lam in lambda_seq: SS=0 for k in range(10): test=list(range(k*m,(k+1)*m)) train=list(set(range(n))-set(test)) for j in test: u=0; v=0 for i in train: kk=K(x[i],x[j],lam) u=u+kk*y[i] v=v+kk if v==0: d_min=np.inf for i in train: d=np.abs(x[j]-x[i]) if d<d_min: d_min=d index=i z=y[index] else: z=u/v SS=SS+(y[j]-z)**2 if SS<SS_min: SS_min=SS lambda_best=lam yy=[] for zz in xx: yy.append(f(zz,lambda_best)) plt.plot(xx,yy,c="red",label="lambda=lambda_best") plt.title("Nadaraya-Watson estimator") plt.legend()

We next consider local linear regression in which the coefficients are estimated for each local point (Fig. 7.11).

---

<!-- Página 159 -->

152 7 Nonlinear Regression

Fig. 7.11 We apply theLocal Linear Regression Epanechnikov kernel to draw the graph of a local linear regression curve -1.0 (Example 61): p = 1 and N = 30 -1.5 y -2.0

-2.5

-2 -1 0 1 2 3 x

p In standard linear regression, given observed data (x1, y1), . . . , (x N , y N ) ∈ R× p+1 R, we obtain β ∈ Rthat minimizes

N ∑ 2 (y i − [1, x i ]β), i=1

p where x i ∈ Ris a row vector. By contrast, in local linear regression, we obtain p+1 β(x) ∈ Rthat minimizes

N ∑ 2 k(x, x i )(y i − [1, x i ]β(x))(7.7) i=1

pp p for each x ∈ R, where k : R× R→ R is a kernel. Note that β(x) depends on p x ∈ R, which is the main difference from standard local regression. Equation (7.7) can be expressed as the matrix ⎡⎤ k(x, x1) · · · 0 T⎢.. .⎥ (y − Xβ(x)) ⎣.. . .⎦ (y − Xβ(x)) , (7.8) . . 0 · · · k(x, x N )

N×(p+1) where the leftmost column of X ∈ Ris a column vector consisting of all ones. If we replace the diagonal matrix with the elements k(x, x1), . . . , k(x, x N ) T with W , then (7.8) is (y − Xβ) W (y − Xβ), where W depends on x. If we differentiate this equation with respect to β, we obtain

T −2X W (y − Xβ(x)) .

---

<!-- Página 160 -->

7.6 Generalized Additive Models 153

T T Therefore, if we set this result to zero, we obtain X Wy = X W Xβ(x) and

ˆβ(x) = (X T W X)−1 X T Wy .

Example 61 We apply the Epanechnikov kernel with p = 1 to local linear regression and x1, . . . , x N , and y1, . . . , y N .

def local(x,y,z=x): n=len(y) x=x.reshape(-1,1) X=np.insert(x,0,1,axis=1) yy=[] for u in z: w=np.zeros(n) for i in range(n): w[i]=K(x[i],u,lam=1) W=np.diag(w) beta_hat=np.linalg.inv(X.T@W@X)@X.T@W@y yy.append(beta_hat[0]+beta_hat[1]*u) return yy

n=30 x=np.random.rand(n)*2*np.pi-np.pi y=np.sin(x)+randn(1) plt.scatter(x,y,s=15) m=200 U=np.arange(-np.pi,np.pi,np.pi/m) V=local(x,y,U) plt.plot(U,V,c="red") plt.title(" Local linear regression(p=1,N=30)")

7.6 Generalized Additive Models

If the number of basis functions is finite, we can obtain the coefficients as we did for linear regression.

Example 62 The basis of the polynomials of order p = 4 contains five functions 234 1, x, x, x, and x, and the basis of the natural spline curves with K = 5 knots contains 1, x, h3(x), h4(x), and h5(x). However, if we mix them, we obtain eight linearly independent functions. We can estimate a function f (x) that can be expressed by the sum of an order p = 4 polynomial and a K = 5-knot natural spline function as

47 ∑∑ ˆf (x) =ˆβ x j +ˆβ h(x) j j j −2 j =0j =5

---

<!-- Página 161 -->

154 7 Nonlinear Regression

ˆβ = (X T X)−1X T y = [ ˆβ, . . . , ˆβ]T from observed data (x, y), . . . , (x , y ), 0711N N where ⎡⎤ 234 1 x1 xxxh3(x1) h4(x1) h5(x1) 1 1 1 ⎢234⎥ 1 xxxxh(x) h(x) h(x) ⎢2 2 2 2 324252⎥ X =⎢........⎥. ⎣........⎦ . . . . . . . . 234 1 x N xxxh3(x N ) h4(x N ) h5(x N ) N N N

However, as for the smoothing spline curves with large sample size N, computing the inverse matrix is difficult. Moreover, in some cases, such as local regression, the curve cannot be expressed by a finite number of basis functions. In such cases, we often use a technique called backfitting. Suppose that we express a function f (x) as the sum of functions f1(x), . . . , fp (x). We first set f1(x) = · · · = fp (x) = 0, and for each j = 1, . . . , p, we regress the residuals ∑ rj (x) := f (x) − fk (x) k =j

on fj (x) and repeat the cycle until convergence.

Example 63 To divide the function into polynomial and local regression to under- stand the relation between covariates and responses, we implement the following procedure. We repeat the polynomial and local regressions in turn and divide N y ∈ Rinto y1 + y2 = y. We present a graph that consists of the two elements in Fig. 7.12.

Polynomial RegressionLocal Linear Regression

0.5 0.04

0.0 0.00)) xx (( ff -0.5 -0.04 -1.0 -0.08 -2 -1 0 1 2-2 -1 0 1 2 xx

Fig. 7.12 We present the fitting via polynomial regression and local regression (Example 63)

---

<!-- Página 162 -->

Appendix: Proofs of Propositions 155

def poly(x,y,z=None): if z is None: z=x n=len(x) m=len(z) X=np.zeros((n,4)) for i in range(n): X[i,0]=1; X[i,1]=x[i]; X[i,2]=x[i]**2; X[i,3]=x[i]**3 beta_hat=np.linalg.inv(X.T@X)@X.T@y Z=np.zeros((m,4)) for j in range(m): Z[j,0]=1; Z[j,1]=z[j]; Z[j,2]=z[j]**2; Z[j,3]=z[j]**3 yy=Z@beta_hat return yy

n=30 x=np.random.rand(n)*2*np.pi-np.pi x=x.reshape(-1,1) y=np.sin(x)+randn(n) y_1=0; y_2=0 for k in range(10): y_1=poly(x,y-y_2) y_2=local(x,y-y_1,z=x) z=np.arange(-2,2,0.1) plt.plot(z,poly(x,y_1,z)) plt.title("polynomial regression")

plt.plot(z,local(x,y_2,z)) plt.title("Local linear regression")

Appendix: Proofs of Propositions

Proposition 20 The function f (x) has K cubic polynomials h1(x) = 1, h2(x) = x, hj +2(x) = d j (x) − d K−1(x), j = 1, . . . , K − 2, as a basis, and if we define

γ1 := β1, γ2 := β2, γ3 := (αK − α1)β3, . . . , γ K := (αK − αK−2)β K

K ∑ for each β1, . . . , β K , we can express f as f (x) =γ j hj (x), where we have j =1

33 (x − αj )− (x − αK ) + + d j (x) = , j = 1, . . . , K − 1 . αK − αj

---

<!-- Página 163 -->

156 7 Nonlinear Regression

K ∑ αK − αj −2 Proof First, the condition (7.3) β K+1 = −β j can be expressed as αK − αK−1 j =3

K ∑ γ K+1 = −γ j (7.9) j =3

with γ K+1 := (αK − αK−1)β K+1 . 

In the following, we show that γ1, . . . , γ K are coefficients when the basis consists of h1(x) = 1, h2(x) = x, hj +2(x) = d j (x) − d K−1(x), j = 1, . . . , K − 2, where

33 (x − αj )− (x − αK ) + + d j (x) = , j = 1, . . . , K − 1 αK − αj

for each case of x ≤ αK and αK ≤ x. In fact, for x ≤ αK , using (7.9), we obtain

K+13K3K3 ∑(x − α)∑(x − α)∑(x − α) j −2+j −2+K−1+ γ j=γ j−γ j αK − αj −2αK − αj −2αK − αK−1 j =3j =3j =3 { } K33 ∑ (x − αj −2)+(x − αK−1)+ =γ j− αK − αj −2αK − αK−1 j =3

K ∑ =γ j {d j −2(x) − d K−1(x)} , j =3

which means

K+1 ∑ 3 f (x) = β1 + β2x +β j (x − αj −2) + j =3

K+13 ∑ (x − αj −2)+ = γ1 + γ2x +γ j αK − αj −2 j =3

KK ∑∑ = γ1 + γ2x +γ j (d j −2(x) − d K−1(x)) =γ j hj (x) . j =3j =1

---

<!-- Página 164 -->

Appendix: Proofs of Propositions 157

For x ≥ αK , according to the definition, and j = 1, . . . , K − 2, we have

3 33 3 (x − αj )− (x − αK )(x − αK−1)− (x − αK ) hj +2(x) = − αK − αjαK − αK−1

2 2 2 = (x − αj )+ (x − αK )+ (x − αj )(x − αK ) − (x − αK )

2 −(x − αK−1)− (x − αK−1)(x − αK )

= (αK−1 − αj )(2x − αj − αK−1) + (x − αK )(αK−1 − αj ) (7.10)

= (αK−1 − αj )(3x − αj − αK−1 − αK ) , (7.11)

where the second to last equality is obtained by factorization between the first and fourth terms and between the third and sixth terms. Therefore, if we substitute x = ∑∑ K′K′ αK into f (x) = j =1 γ j hj (x) and f (x) = j =1 γ j h(x), we obtain j

K ∑ f (αK ) = γ1 + γ2αK +γ j (αK−1 − αj −2)(2αK − αj −2 − αK−1) (7.12) j =3

and

K ∑ ′ f (αK ) = γ2 + 3γ j (αK−1 − αj −2). (7.13) j =3 ∑ K Thus, for x ≥ αK , we have shown that f (x) = γ j hj (x) is such a line. On the j =1 K+13 ∑(x − α) j −2+ other hand, using the function f (x) = γ1 + γ2x +γ jfor x ≤ αK , αK − αj −2 j =1 to compute the value and its derivative at x = αK , from (7.9), we obtain

K+13K+1 ∑(α− α)∑ K j −22 f (αK ) = γ1 + γ2αK +γj= γ1 + γ2αK +γj (αK − αj −2) αK − αj −2 j =3j =3 (7.14)

KK ∑∑ 2 2 = γ1 + γ2αK +γj (αK − αj −2)−γj (αK − αK−1) j =3j =3

K ∑ = γ1 + γ2αK +γj (αK−1 − αj −2)(2αK − αj −2 − αK−1) (7.15) j =3

---

<!-- Página 165 -->

158 7 Nonlinear Regression

and

K+12K+1 ∑∑ (α− α) ′K j −2 f (αK ) = γ2 + 3γ j= γ2 + 3γ j (αK − αj −2) (7.16) αK − αj −2 j =3j =3

KK ∑∑ = γ2 + 3γ j (αK − αj −2) − 3γ j (αK − αK−1) j =3j =3

K ∑ = γ2 + 3γ j (αK−1 − αj −2). j =3

Since not only (7.12) and (7.15) but also (7.13) and (7.16) coincide, the proposition holds even for x ≥ αK .

Proposition 21 (Green and Silverman, 1994) The natural spline f with knots x1, . . . , x N minimizes L(f ).

Proof Let f (x) be an arbitrary function that minimizes (7.5), g(x) be the natural spline with knots x1, . . . , x N , and r(x) := f (x) − g(x). Since the dimension of g(x) is N, we can determine the coefficients γ1, . . . , γ N of the basis functions ∑ N h1(x), . . . , hN (x) in g(x) = γ i hi (x) such that i=1

g(x1) = f (x1), . . . , g(x N ) = f (x N ).

In fact, we can solve the following linear equation: ⎡⎤⎡⎤⎡⎤ h1(x1) · · · hN (x1)γ1f (x1) ⎢.. .⎥⎢.⎥⎢.⎥ ⎣.. . . ..⎦⎣..⎦ =⎣..⎦ . h1(x N ) · · · hN (x N )γ Nf (x N )

Then, note that we have r(x1) = · · · = rN (x N ) = 0 and that g(x) is a line and a cubic polynomial for x ≤ x1, x N ≤ x and inside these values, respectively, ′′′ which means that g(x) is a constant γ i for each interval [x i , x i+1], specifically, ′′′′ g(x1) = g(x N ) = 0. Thus, we have

∫ ∫ N−1 x Nx N∑ ′′′′′′′x N′′′′x i+1 g(x)r(x)dx = [g(x)r(x)]−g(x)r(x)dx = −γ i [r(x)]x = 0 . x1 i x1x1 i=1

---

<!-- Página 166 -->

Appendix: Proofs of Propositions 159

Hence, we have ∫ ∫ ∞x N ′′2′′′′2 {f (x)}dx ≥{g(x) + r(x)}dx −∞x1 ∫ ∫ ∫ x Nx Nx N ′′2′′2′′′′ ≥{g(x)}dx +{r(x)}dx + 2g(x)r(x)dx x1x1x1 ∫ x N ′′2 ≥{g(x)}dx , x1

which means that for each of the functions f that minimize L(·) in (7.5), there exists a natural function g such that

N∫ ∞ ∑ 2 ′′2 L(f ) =(y i − f (x i ))+ λ{f (x)}dx −∞ i=1 N∫ ∞ ∑ 2 ′′2 ≥(y i − g(x i ))+ λ{g(x)}dx = L(g) . −∞ i=1



Proposition 22 The elements gi,j defined in (7.6) are given by () 2 (x N−1 − x j −2)12x N−1 + 6x j −2 − 18x i−2 +12(x N−1 − x i−2)(x N−1 − x j −2)(x N − x N−1) gi,j =, (x N − x i−2)(x N − x j −2)

where x i ≤ x j and gi,j = 0 for either i ≤ 2 or j ≤ 2.

Proof Without loss of generality, we may assume x i ≤ x j . Then, we have ∫ ∫ x Nx N ′′′′′′′′ h(x)h(x)dx =h(x)h(x)dx i j i j x1max(x i ,x j ) ∫ ∫ x N−1x N ′′′′′′′′ =h(x)h(x)dx +h(x)h(x)dx , (7.17) i j i j x jx N−1

---

<!-- Página 167 -->

160 7 Nonlinear Regression

′′′′ where we have used h(x) = 0 for x ≤ x i and h(x) = 0 for x ≤ x j . The right-hand i j side can be computed as follows. The second term is ∫ x N ′′′′ h(x)h(x)dx i j x N−1 ∫ x ( ) ( ) Nx − x x − x x − x x − x i−2N−1j −2N−1 = 36− − dx x N−1x N − x i−2x N − x N−1x N − x j −2x N − x N−1 ∫ ( )2 x (x N−1 − x i−2)(x N−1 − x j −2)Nx − x N = 36 dx (x N − x i−2)(x N − x j −2)x x N − x N−1 N−1 (x N−1 − x i−2)(x N−1 − x j −2)(x N − x N−1) = 12 , (7.18) (x N − x i−2)(x N − x j −2)

where the second equality is obtained via the following equations:

(x − x i−2)(x N − x N−1) − (x − x N−1)(x N − x i−2) = (x − x N )(x N−1 − x i−2)

(x − x j −2)(x N − x N−1) − (x − x N−1)(x N − x j −2) = (x − x N )(x N−1 − x j −2) .

For the first term of (7.17), we have

∫ ∫ xN−1xN−1 ′′′′x − x i−2x − x j −2 hi (x)hj (x)dx = 36· dx xj −2xj −2x N − x i−2x N − x j −2 x N −1 − x j −2 = 36 (x N − x i−2)(x N − x j −2) { } 11 22 ×(x+ x N −1x j −2 + x) − (x N −1 + x j −2)(x i−2 + x j −2) + x i−2x j −2 N −1 j −2 3 2 { } x N −1 − x j −21111 22 = 36 xN −1 − x N −1x j −2 − xj −2 − x i−2(x N −1 − x j −2) (x N − x i−2)(x N − x j −2)3 6 6 2

2 (x N −1 − x j −2)() = 12x N −1 + 6x j −2 − 18x i−2, (7.19) (x N − x i−2)(x N − x j −2)

where to obtain the last equality in (7.19), we used

111 2 x− (x j −2 + 3x i−2)x N−1 − x j −2(x j −2 − 3x i−2) N−1 3 6 6 111 = (x N−1 − x j −2)( x N−1 + x j −2 − x i−2). 3 6 2



---

<!-- Página 168 -->

Exercises 57–68 161

Exercises 57–68

57. For each of the following two quantities, find a condition under which the β0, β1, . . . , β p that minimize it are unique given data (x1, y1), . . . , (x N , y N ) ∈ R × R and its solution: ⎛⎞2 Np ∑∑ j (a)⎝y i −β j x ⎠ i i=1j =0 ⎛⎞2 Np ∑∑ (b)⎝y i −β j fj (x i )⎠, f0(x) = 1, x ∈ R, fj : R → R, j = 1, . . . , p. i=1j =0 58. For K ≥ 1 and −∞ = α0 < α1 < · · · < αK < αK+1 = ∞, we define a cubic polynomial fi (x) for αi ≤ x ≤ αi+1 , i = 0, 1, . . . , K, and assume that (j )(j ) fi , i = 0, 1, . . . , K, satisfy f (αi ) = f (αi ), j = 0, 1, 2, i = 1, . . . , K, i−1i (0) (1) (2) where f (α), f (α), and f (α) denote the value, the first, and the second derivatives of f at x = α.

3 (a) Show that there exists γ i such that fi (x) = fi−1(x) + γ i (x − αi ). (b) Consider a piecewise cubic polynomial f (x) = fi (x) for αi ≤ x ≤ αi+1 i = 0, 1, . . . , K (spline curve). Show that there exist β1, β2, . . . , β K+4 such that

K ∑ 2 3 3 f (x) = β1 + β2x + β3x+ β4x+β i+4(x − αi ), + i=1

where (x − αi )+ denotes the function that takes x − αi and zero for x > αi and x ≤ αi , respectively.

59. We generate artificial data and execute spline regression for K = 5, 7, 9 knots. Define the following function f and draw spline curves.

n=100 x=randn(n)*2*np.pi y=np.sin(x)+0.2*randn(n) col_set=["red","green","blue"] K_set=[5,7,9] plt.scatter(x,y,c="black",s=10) plt.xlim(-5,5) for k in range(3): K=K_set[k] knots=np.linspace(-2*np.pi,2*np.pi,K) X=np.zeros((n,K+4)) for i in range(n): X[i,0]=1 X[i,1]=x[i] X[i,2]=x[i]**2 X[i,3]=x[i]**3 for j in range(K): X[i,j+4]=np.maximum((x[i]-knots[j])**3,0)

---

<!-- Página 169 -->

162 7 Nonlinear Regression

beta=np.linalg.inv(X.T@X)@X.T@y # some blanks (definition of function f)# u_seq=np.arange(-5,5,0.02) v_seq=[] for u in u_seq: v_seq.append(f(u)) plt.plot(u_seq,v_seq,c=col_set[k],label="K={}".format(K)) plt.legend()

60. For K ≥ 2, we define the following cubic spline curve g (natural spline): it is a line for x ≤ α1 and αK ≤ x and a cubic polynomial for αi ≤ x ≤ αi+1 , i = 1, . . . , K −1, where the values and the first and second derivatives coincide on both sides of the K knots α1, . . . , αK .

K ∑ (a) Show that γ K+1 = −γ j when j =3

333 (x − α1)(x − αK−2)(x − αK−1) g(x) = γ1+γ2x+γ3+· · ·+γ K+γ K+1 αK − α1αK − αK−2αK − αK−1

′′ for αK−1 ≤ x ≤ αK . Hint: Derive the result from g(αK ) = 0. K ∑ (b) g(x) can be written asγ i hi (x) with γ1, . . . , γ K ∈ R and the functions i=1 h1(x) = 1, h2(x) = x, hj +2(x) = d j (x) − d K−1(x), j = 1, . . . , K − 2, where

33 (x − αj )+ − (x − αK )+ d j (x) = , j = 1, . . . , K − 1 . αK − αj

Show that

hj +2(x) = (αK−1 − αj )(3x − αj − αK−1 − αK ), j = 1, . . . , K − 2

for each αK ≤ x. (c) Show that g(x) is a linear function of x for x ≤ α1 and for αK ≤ x.

61. We compare the ordinary and natural spline functions. Define the functions h1, . . . , hK , d1, . . . , d K−1 , and g, and execute the below:

def d(j,x,knots): # some blanks (definition of function d)#

def h(j,x,knots): # some blanks (definition of function h)#

---

<!-- Página 170 -->

Exercises 57–68 163

n=100 x=randn(n)*2*np.pi y=np.sin(x)+0.2*randn(n) K=11 knots=np.linspace(-5,5,K) X=np.zeros((n,K+4)) for i in range(n): X[i,0]=1 X[i,1]=x[i] X[i,2]=x[i]**2 X[i,3]=x[i]**3 for j in range(K): X[i,j+4]=np.maximum((x[i]-knots[j])**3,0) beta=np.linalg.inv(X.T@X)@X.T@y

def f(x): S=beta[0]+beta[1]*x+beta[2]*x**2+beta[3]*x**3 for j in range(K): S=S+beta[j+4]*np.maximum((x-knots[j])**3,0) return S

X=np.zeros((n,K)) X[:,0]=1 for j in range(1,K): for i in range(n): X[i,j]=h(j,x[i],knots) gamma=np.linalg.inv(X.T@X)@X.T@y

def g(x): # some blanks (definition of function g)#

u_seq=np.arange(-6,6,0.02) v_seq=[]; w_seq=[] for u in u_seq: v_seq.append(f(u)) w_seq.append(g(u)) plt.scatter(x,y,c="black",s=10) plt.xlim(-6,6) plt.xlabel("x") plt.ylabel("f(x),g(x)") plt.tick_params(labelleft=False) plt.plot(u_seq,v_seq,c="blue",label="spline ") plt.plot(u_seq,w_seq,c="red",label="natural spline") plt.vlines(x=[-5,5],ymin=-1.5,ymax=1.5,linewidth=1) plt.vlines(x=knots,ymin=-1.5,ymax=1.5,linewidth=0.5,linestyle="dashed") plt.legend()

Hint: The functions h and d need to compute the size K of the knots. Inside the function g, knots may be global.

---

<!-- Página 171 -->

164 7 Nonlinear Regression

62. We wish to prove that for an arbitrary λ ≥ 0, there exists f : R → R that minimizes

N∫ ∞ ∑ 2 ′′2 RSS(f, λ) :=(y i − f (x i ))+ λ{f (t)}dt, (7.20) −∞ i=1

given data (x1, y1), . . . , (x N , y N ) ∈ R × R among the natural spline function g with knots x1 < · · · < x N (smoothing spline function).

(a) Show that there exist γ1, . . . , γ N−1 ∈ R such that

∫ N−1 x N∑ ′′′′ g(x)r(x)dx = −γ i {r(x i+1) − r(x i )}. x1 i=1

′′′′ Hint: Use the facts that g(x1) = g(x N ) = 0 and that the third derivative of g is constant for x i ≤ x ≤ x i+1 . (b) Show that if the function h : R → R satisfies ∫ x N ′′′′ g(x)r(x)dx = 0 , (7.21) x1

then for any f (x) = g(x) + h(x), we have ∫ ∫ ∞∞ ′′2′′2 {g(x)}dx ≤{f (x)}dx . (7.22) −∞−∞

′′ Hint: For x ≤ x1 and x N ≤ x, g(x) is a linear function and g(x) = 0. Moreover, (7.21) implies ∫ ∫ ∫ x Nx Nx N ′′′′2′′2′′2 {g(x) + r(x)}dx ={g(x)}dx +{r(x)}dx . x1x1x1

(c) A natural spline curve g is contained among the set of functions f : R → R that minimize (7.20). Hint: Show that if RSS(f, λ) is the minimum value, r(x i ) = 0, i = 1, . . . , N, implies (7.21) for the natural spline g such that g(x i ) = f (x i ), i = 1, . . . , N. ∫ ∞ ′′′′ 63. It is known that gi,j :=h(x)h(x)dx is given by i j −∞ () 2 (x N−1 − x j −2)12x N−1 − 18x i−2 + 6x j −2 +12(x N−1 − x i−2)(x N−1 − x j −2)(x N − x N−1) , (x N − x i−2)(x N − x j −2)

---

<!-- Página 172 -->

Exercises 57–68 165

where h1, . . . , hK is the natural spline basis with the knots x1 < · · · < x K and gi,j = 0 for either i ≤ 2 or j ≤ 2. Write a Python function G that outputs K matrix G with elements gi,j from the K knots x ∈ R. N ∑ 64. We assume that there exist γ1, . . . , γ N ∈ R such that g(x) =gj (x)γ j and j =1 N ∑ ′′′′ g(x) =gj (x)γ j for a smoothing spline function g with knots x1 < · · · < j =1 x N , where gj , j = 1, . . . , N are cubic polynomials. Show that the coefficients T N T ′′−1T γ = [γ1, . . . , γ N ]∈ Rcan be expressed by γ = (G G + λG)G y with (∫ ) ∞ N×N ′′ ′′′′N×N G = (gj (x i )) ∈ Rand G=g(x)g(x)dx∈ R. Moreover, j k −∞ we wish to draw the smoothing spline curve to compute ˆγ for each λ. Fill in the blanks and execute the procedure.

# generating data n=100; a=-5; b=5 x=(b-a)*np.random.rand(n)+a# uniform distribution (-5,5) y=x-0.02*np.sin(x)-0.1*randn(n) index=np.argsort(x); x=x[index]; y=y[index]

X=np.zeros((n,n)) X[:,0]=1 for j in range(1,n): for i in range(n): X[i,j]=h(j,x[i],x) GG=G(x) lambda_set=[10,30,80] col_set=["red","blue","green"] plt.scatter(x,y,c="black",s=10) plt.title("smoothing spline(n=100)") plt.xlabel("x") plt.ylabel("g(x)") plt.tick_params(labelleft=False) for i in range(3): lam=lambda_set[i] gamma=# blank # def g(u): S=gamma[0] for j in range(1,n): S=S+gamma[j]*h(j,u,x) return S u_seq=np.arange(-8,8,0.02) v_seq=[] for u in u_seq: v_seq.append(g(u)) plt.plot(u_seq,v_seq,c=col_set[i],label="lambda={}".format( lambda_set[i])) plt.legend()

65. It is difficult to evaluate how much the value of λ affects the estimation of γ because λ varies and depends on the settings. To this end, we often use T −1T the effective degrees of freedom, the trace of H [λ] := X(X X + λG)X , instead of λ to evaluate the balance between fitness and simplicity. For N = 100

---

<!-- Página 173 -->

166 7 Nonlinear Regression

and λ ranging from 1 to 50, we draw the graph of the effective degrees of freedom (the trace of H [λ]) and predictive error (CV [λ]) of CV. Fill in the blanks and execute the procedure.

def cv_ss_fast(X,y,lam,G,k): n=len(y) m=int(n/k) H=X@np.linalg.inv(X.T@X+lam*G)@X.T df=# blank(1) # I=np.eye(n) e=(I-H)@y I=np.eye(m) S=0 for j in range(k): test=np.arange(j*m,(j+1)*m) S=S+(np.linalg.inv(I-H[test,:][:,test])@e[test]).T@(np.linalg. inv(I-H[test,test])@e[test]) return {’score’:S/n,’df’:df}

# generating data n=100; a=-5; b=5 x=(b-a)*np.random.rand(n)+a# (-5,5) y=x-0.02*np.sin(x)-0.1*randn(n) index=np.argsort(x); x=x[index]; y=y[index]

# calculate X X=np.zeros((n,n)) X[:,0]=1 for j in range(1,n): for i in range(n): X[i,j]=h(j,x[i],x) GG=G(x) # Calculations and plots of Effective Degree of Freedom and prediction errors v=[]; w=[] for lam in range(1,51,1): res=cv_ss_fast(# blank(2) #,n) v.append(res[’df’]) w.append(res[’score’]) plt.plot(v,w) plt.xlabel("Effective Degree of Freedom") plt.ylabel("prediction errors by CV ") plt.title("Effective Degree of Freedom and prediction errors by CV ")

66. Using the Nadaraya–Watson estimator

∑ N Kλ (x, x i )y i ˆf (x) =i=1 ∑N K(x, x ) i=1 λ i

with λ > 0 and the following kernel ( ) |x − y| Kλ (x, y) = D λ ⎧ ⎨32 (1 − t), |t| ≤ 1 D(t) =4 ⎩ 0, Otherwise ,

---

<!-- Página 174 -->

Exercises 57–68 167

we draw a curve that fits n = 250 data. Fill in the blanks and execute the procedure. When λ is small, how does the curve change?

n=250 x=2*randn(n) y=np.sin(2*np.pi*x)+randn(n)/4

def D(t): # some blanks (definition of function D)#

def K(x,y,lam): # some blanks (definition of function K)#

def f(z,lam): S=0; T=0 for i in range(n): S=S+K(x[i],z,lam)*y[i] T=T+K(x[i],z,lam) if T==0: return(0) else: return S/T

plt.scatter(x,y,c="black",s=10) plt.xlim(-3,3) plt.ylim(-2,3) xx=np.arange(-3,3,0.1) yy=[] for zz in xx: yy.append(f(zz,0.05)) plt.plot(xx,yy,c="green",label="lambda=0.05") yy=[] for zz in xx: yy.append(f(zz,0.25)) plt.plot(xx,yy,c="blue",label="E=0.25")

# # The curves of lam =0.05 , 0.25 were displayed. m=int(n/10) lambda_seq=np.arange(0.05,1,0.01) SS_min=np.inf for lam in lambda_seq: SS=0 for k in range(10): test=list(range(k*m,(k+1)*m)) train=list(set(range(n))-set(test)) for j in test: u=0; v=0 for i in train: kk=K(x[i],x[j],lam) u=u+kk*y[i] v=v+kk if v==0: d_min=np.inf for i in train: d=np.abs(x[j]-x[i])

---

<!-- Página 175 -->

168 7 Nonlinear Regression

if d<d_min: d_min=d index=i z=y[index] else: z=u/v SS=SS+(y[j]-z)**2 if SS<SS_min: SS_min=SS lambda_best=lam yy=[] for zz in xx: yy.append(f(zz,lambda_best)) plt.plot(xx,yy,c="red",label="lam=lambda_best") plt.title("Nadaraya-Watson estimator") plt.legend()

67. Let K be a kernel. We can obtain the predictive value [1, x]β(x) for each x ∈ p p+1 Rusing the β(x) ∈ Rthat minimizes

N ∑ 2 K(x, x i )(y i − [1, x i ]β(x)) i=1

(local regression).

T −1T (a) When we write β(x) = (X W (x)X)X W (x)y, what is the matrix W ? (b) Using the same kernel as we used in Problem 66 with p = 1, we applied x1, . . . , x N , y1, . . . , y N to local regression. Fill in the blanks and execute the procedure.

def local(x,y,z=x): n=len(y) x=x.reshape(-1,1) X=np.insert(x,0,1,axis=1) yy=[] for u in z: w=np.zeros(n) for i in range(n): w[i]=K(x[i],u,lam=1) W=# blank(1) # beta_hat=# blank(2) # yy.append(beta_hat[0]+beta_hat[1]*u) return yy

n=30 x=np.random.rand(n)*2*np.pi-np.pi y=np.sin(x)+randn(n) plt.scatter(x,y,s=15) m=200 U=np.arange(-np.pi,np.pi,np.pi/m) V=local(x,y,U) plt.plot(U,V,c="red") plt.title("Local linear regression (p=1,N=30)")

68. If the number of base functions is finite, the coefficient can be obtained via least squares in the same manner as linear regression. However, when the number

---

<!-- Página 176 -->

Exercises 57–68 169

of bases is large, such as for the smoothing spline, it is difficult to find the inverse matrix. Moreover, for example, local regression cannot be expressed by a finite number of bases. In such cases, a method called backfitting is often applied. To decompose the function into the sum of polynomial regression and local regression, we constructed the following procedure. Fill in the blanks and execute the process.

def poly(x,y,z=x): n=len(x) m=len(z) X=np.zeros((n,4)) for i in range(n): X[i,0]=1; X[i,1]=x[i]; X[i,2]=x[i]**2; X[i,3]=x[i]**3 beta_hat=np.linalg.inv(X.T@X)@X.T@y Z=np.zeros((m,4)) for j in range(m): Z[j,0]=1; Z[j,1]=z[j]; Z[j,2]=z[j]**2; Z[j,3]=z[j]**3 yy=# blank(1) # return yy

n=30 x=np.random.rand(n)*2*np.pi-np.pi x=x.reshape(-1,1) y=np.sin(x)+randn(n) y_1=0; y_2=0 for k in range(10): y_1=poly(x,y-y_2) y_2=# Blank # z=np.arange(-2,2,0.1) plt.plot(z,poly(x,y_1,z)) plt.title(" polynomial regression")

plt.plot(z,local(x,y_2,z)) plt.title("Local Linear Regression")

---

<!-- Página 177 -->

## Chapter 8

# Decision Trees

Abstract In this chapter, we construct decision trees by estimating the relationship between the covariates and the response from observed data. Starting from the root, each vertex traces to either the left or right at each branch, depending on whether a condition w.r.t. the covariates is met, and finally reaches a terminal node to obtain the response. Compared with the methods we have considered thus far, since it is expressed as a simple structure, the estimation accuracy of a decision tree is poor, but since it is expressed visually, it is easy to understand the relationship between the covariates and the response. Decision trees are often used to understand relationships rather than to predict the future, and decision trees can be used for regression and classification. The decision tree has the problem that the estimated tree shapes differ greatly even if observation data that follow the same distribution are used. Therefore, similar to the bootstrap discussed in Chap. 4, by sampling data of the same size from the original data multiple times, we reduce the variation in the obtained decision tree and this improvement can be considered. Finally, we introduce a method (boosting) that produces many small decision trees in the same way as the backfitting method learned in Chap. 7 to make highly accurate predictions.

8.1 Decision Trees for Regression

We wish to illustrate the relationship between the covariates (p variables) and the p response by means of the observed data (x1, y1), . . . , (x N , y N ) ∈ R× R. To this end, we consider constructing a decision tree. A decision tree consists of vertices and branches. Vertices that branch left and right are called branch nodes or interior nodes, and vertices that do not branch are called terminal nodes. Of the two adjacent vertices on a branch, the one closest to the terminal point is called the child, and the other vertex is called the parent. Furthermore, vertices that do not have parents are p called roots (Fig. 8.1). When we construct a decision tree, each x ∈ Rbelongs to one of the regions R1, . . . , Rm that correspond to terminal nodes. Then, for both regression and classification decision trees, two values in the same region should

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2021171 J. Suzuki, Statistical Learning with Math and Python, https://doi.org/10.1007/978-981-15-7877-9_8

---

<!-- Página 178 -->

172 8 Decision Trees

Fig. 8.1 Decision trees. Root Each vertex is either an inner Right TerminalLeft or terminal node. In this book, we direct the edges from theInternal (Branch) parents to their childrenRightLeft

output the same response. Specifically, when the joint probability density function is fXY (x, y), we construct a rule such that

x i ∈ Rj ⇒ ˆy i = ¯y j (8.1)

with ∫ ∫ ∞ yf(x, y)dxdy −∞Rj XY ¯y j := E[Y |Rj ] =∫ ∫(8.2) ∞ f(x, y)dxdy −∞Rj XY

by obtaining m ≥ 1 and the regions R1, . . . , Rm that minimize

∫ m∫ ∞∑ 2 (y − ¯y j )fXY (x, y)dxdy . (8.3) −∞Rj j =1

However, we must consider some problems to actually construct a decision tree from the samples. First, the simultaneous density function fXY is unknown and should be estimated from the samples. To this end, if the size of the region Rj is nj , then one might replace (8.1), (8.2), and (8.3) by

x ∈ Rj ⇒ ˆy i = ¯y j ,

∑ 1 ¯y j := y i , nj i:x i ∈Rj

and

m ∑∑ 2 (y i − ¯y j ), (8.4) j =1i:x i ∈Rj ∑ where · sums over i such that x i ∈ Rj . i:x i ∈Rj However, if we minimize (8.4) to obtain the regions, similar to the RSS value in linear regression, the greater the value of m is, the smaller the value of (8.4). We see that (8.4) always has the minimum value (zero) for m = N (one sample per region).

---

<!-- Página 179 -->

8.1 Decision Trees for Regression 173

Overfitting occurs because we use the same samples for testing and training. In fact, the testing using data other than the training data will be better if the size of each region Rj is greater than one, although the performance will be worse if the region size is too large. Thus, we may consider either separating the training and test data or applying cross-validation (CV). A typical way to explicitly avoid overfitting is to obtain m ≥ 1 and R1, . . . , Rm that minimize

m ∑∑ 2 (y i − ¯y j )+ αm , (8.5) j =1i:x i ∈Rj

where the value of α > 0 can be obtained via CV. For example, for each α, 90% of the data are used for training to obtain a decision tree that minimizes (8.5). The remaining data (10%) are used for testing to evaluate the performance of the decision tree. By using a different 10% as test data 10 times and taking the arithmetic average, we obtain the performance of a specific α > 0. We obtain such an evaluation for all α values and choose the best decision tree (Fig. 8.2). In addition, there are degrees of freedom, including how many variables are used at each branch node and how many branches are used. For example, if the positive and negative values of the linear sum of multiple variables are included, the number of combinations increases. An optimal number of branches may exist for each branch node. Furthermore, if the variables used for branching at each branch node are decided from the top down, the optimum decision tree cannot be obtained. It is necessary to look at all the vertices of the decision tree simultaneously and select the optimal combination of variables. Therefore, the optimal solution cannot be obtained. In this chapter, we choose one variable (Xj ) and one sample (x i,j is the threshold) for each branching from the root to each terminal node in a greedy and top-down manner. Often, the threshold value is set to be equal to or greater than one of the samples in the node. Suppose that a branch node contains samples x i with i ∈ S, and by the sample size S, we mean the cardinality of S, where S is a subset of {1, 2, · · · , N}. In the following, we divide a subset {x k|k ∈ S} of {x1, . . . , x N } into {x k|x k < x i,j , k ∈ S} and {x k|x k ≥ x i,j , k ∈ S} by specifying i ∈ S and j = 1, · · · p. Although this approach does not take overfitting into consideration, we may select i, j that minimize ∑∑ L2 R2 (y i − ¯y i,j )+ (y i − ¯y i,j ), k:x k,j <x i,jk:x k,j ≥x i,j

where nL and nR are the numbers of k such that x k,j < x i,j and x k,j ≥ x i,j , ∑∑ LR respectively, and ¯y and ¯y are (1/nL ) y k and (1/nR ) y k , i,j i,j k:x k,j <x i,j k:x k,j ≥x i,j respectively. We construct the following procedure for regression, where we apply a loss measure such as sq_loss to the argument f of function branch. Specifically, the

---

<!-- Página 180 -->

174 8 Decision Trees

α = 0 α = 0.1

α = 0.5α = 2

Fig. 8.2 For parameters α = 0, 0.1, 0.5, 2, we generate decision trees that minimize (8.5). If the colors of the inner nodes are the same, the variables used for branching are the same. If attribute j is zero, the node is terminal. The larger the α is, the smaller the depth of the tree because pruning is performed in an earlier stage

procedure chooses the i, j that maximize the decrease before and after branching, assuming that each k ∈ S proceeds to the left and right depending on x k,j < x i,j and x k,j ≥ x i,j .

def sq_loss(y): if len(y)==0: return 0 else: y_bar=np.mean(y) return np.linalg.norm(y-y_bar)**2

def branch(x,y,S,rf=0): if rf==0: m=x.shape[1]

---

<!-- Página 181 -->

8.1 Decision Trees for Regression 175

if x.shape[0]==0: return([0,0,0,0,0,0,0]) best_score=np.inf for j in range(x.shape[1]): for i in S: left=[]; right=[] for k in S: if x[k,j]<x[i,j]: left.append(k) else: right.append(k) left_score=f(y[left]); right_score=f(y[right]) score=left_score+right_score if score<best_score: best_score=score i_1=i; j_1=j left_1=left; right_1=right left_score_1=left_score; right_score_1=right_score return [i_1,j_1,left_1,right_1,best_score,left_score_1,right_score_1]

In the above procedure, the samples x i , i ∈ S in the node are the candidate thresholds. However, if the sample size N is large, we may reduce the candidates to avoid enormous computation, for example by choosing the median as the threshold if the node sample size exceeds twenty. Now, we construct a decision tree from the observed data. To this end, we prepare criteria for whether to continue branching. For example,

1. When the node sample size is less than nmin, 2. When branching, no sample is contained in either of the group, 3. When the decrease before and after branching is less than an a priori determined threshold (= α).

The third item is due to the fact that the difference in (8.5) is the difference in the first terms subtracted by α. When constructing a decision tree, we express each node as a list in the algorithm. For the inner nodes (excluding the terminal nodes but including the root), the attributes are the parent node, the left and right children nodes, the variable for branching, and the sample that is the threshold. For the terminal nodes, the attributes are the parent nodes and the response at the region. In the following procedure, the inner and terminal nodes contain as an attribute the set of the samples that reached the node. The following procedure realizes stacking: the stack is empty at the beginning. When a node becomes an inner node, the left and right children are pushed to the stack (the stack height will increase by two), which means that they may branch in the future. Then, we take the node from the top of the stack (the stack height will decrease by one) and check whether it needs to branch. If it branches, the two children are placed on the top of the stack (the stack height will increase by two); otherwise, we check the node on the top of the current stack. The process continues until the stack is empty (Fig. 8.3). The stack itself is a list that stores the information about the parents of the nodes in the stack.

---

<!-- Página 182 -->

176 8 Decision Trees

111

2 32 3

54 5 34 122

111

2 32 32 3

545454

4 22

Fig. 8.3 We generate decision trees using a stack. Upper Left: 1 is pushed to the stack at the beginning. Upper Middle: 1 is removed from the stack, and 2, 3 are added to the stack. Upper Right: 3 is removed from the stack, and 4, 5 are added to the stack. Lower Left: 5 is removed from the stack. Lower Middle: 4 is removed from the stack. Lower Right: 2 is removed from the stack. In the decision trees, the red circles represent POP, and the blue lines express PUSH

class Stack: def __init__(self,parent,set,score): self.parent=parent self.set=set self.score=score

class Node: def __init__(self,parent,j,th,set): self.parent=parent self.j=j self.th=th self.set=set

def dt(x,y,alpha=0,n_min=1,rf=0): if rf==0: m=x.shape[1] # A single set of stack is constructed. Decision tree is initialized. stack=[Stack(0,list(range(x.shape[0])),f(y))]# f is global node=[] k=-1 # Extracting the last element of the stack and updating the decision tree while len(stack)>0: popped=stack.pop() k=k+1

---

<!-- Página 183 -->

8.1 Decision Trees for Regression 177

i,j,left,right,score,left_score,right_score=branch(x,y,popped.set,rf ) if popped.score-score<alpha or len(popped.set)<n_min or len(left)==0 or len(right)==0: node.append(Node(popped.parent,-1,0,popped.set)) else: node.append(Node(popped.parent,j,x[i,j],popped.set)) stack.append(Stack(k,right,right_score)) stack.append(Stack(k,left,left_score)) # After these , set the value of node.left and node.right. for h in range(k,-1,-1): node[h].left=0; node[h].right=0; for h in range(k,0,-1): pa=node[h].parent if node[pa].right==0: node[pa].right=h else: node[pa].left=h # After these , calculate the value of node.center if f==sq_loss: g=np.mean else: g=mode_max for h in range(k+1): if node[h].j==-1: node[h].center=g(y[node[h].set]) else: node[h].center=0 return node

Each of the node[[1]], node[[2]], ... contains the left and right node IDs of its children as its attribute if they are inner nodes. The procedure adds the information giving the ID first to the parent, then to the left child, and finally to the right child. In each element of the output node, we have the variable for branching and its threshold for the inner nodes, the sample set in the node and the flag that the node is terminal for the terminal nodes, the parent node ID for the nodes except the root, and the left and right children node IDs for inner nodes. The attribute j expresses the variable for branching from 1 to p and is zero when the node is terminal. In the last stage, as an attribute of the list, the terminal nodes obtain the average of the responses in the region for regression and obtain the mode in the region for classification.

Example 64 (Boston Data Set) Data set for the Boston median housing prices (Response) and thirteen other covariates (N = 506). For α = 0, n.min = 50, we construct a decision tree (Fig. 8.4). The procedure is implemented via the following code:

from sklearn.datasets import load_boston

boston=load_boston() X=boston.data y=boston.target f=sq_loss node=dt(X,y,n_min=50) len(node)

---

<!-- Página 184 -->

178 8 Decision Trees

Fig. 8.4 We construct a 1 decision tree with thirteen covariates that explains the25 median housing prices in Boston. The thirteen variables3 4619 and their IDs are in the lower left, and the IDs of the7122037 branching variable and its threshold is in the lower right81113182124 9 1014 1522 232536

16 172635

2730

28 2931 32

33 34

from igraph import *

r=len(node) edge=[] for h in range(1,r): edge.append([node[h].parent,h]) TAB=[]; for h in range(r): if not node[h].j==0: TAB.append([h,node[h].j,node[h].th]) TAB

def draw_graph(node): r=len(node) col=[] for h in range(r): col.append(node[h].j) colorlist=[’#ffffff’,’#fff8ff’,’#fcf9ce’,’#d6fada’,’#d7ffff’,’#d9f2f8’,’ #fac8be’,’#ffebff’,’#ffffe0’,’#fdf5e6’,’#fac8be’,’#f8ecd5’,’#ee82ee’] color=[colorlist[col[i]] for i in range(r)] edge=[] for h in range(1,r): edge.append([node[h].parent,h]) g=Graph(edges=edge,directed=True) layout=g.layout_reingold_tilford(root=[0]) out=plot(g,vertex_size=15,layout=layout,bbox=(300,300),vertex_label=list (range(r)),vertex_color=color) return out

draw_graph(node)

---

<!-- Página 185 -->

8.1 Decision Trees for Regression 179

Optimum n.min via CVOptimal α via CV

12.0

13.0

11.5 12.0

11.0Square ErrorSquare Error 11.0

10.510.0 0.0 0.5 1.0 1.52 4 6 8 10 12 14 αn.min

Fig. 8.5 We execute CV for the Boston data set (the first N = 100 data) and change the values of α to evaluate the CV values (Left). We observe that α = 0 does not necessarily produce the best results. A value of approximately 1.0 ≤ α ≤ 1.1 is the best for CV. Additionally, we compute the CV evaluations while changing the n.min from 1 to 15 (Right). The best value is approximately n.min = 9

We wish to obtain the optimum α via CV for criterion (8.5). First, we construct p the following value; then, we obtain the region Rj to which each x ∈ Rbelongs.

def value(u,node): r=0 while node[r].j!=-1: if u[node[r].j]<node[r].th: r=node[r].left else: r=node[r].right return node[r].center

Example 65 For 10-fold CV and the Boston data set, we execute the procedure to obtain the optimum 0 ≤ α ≤ 1.5 (Fig. 8.5 Left). The execution is implemented via the following code. Because this process consumes considerable amounts of time, we execute only for the first N = 100 data.

boston=load_boston() n=100 X=boston.data[range(n),:] y=boston.target[range(n)] f=sq_loss alpha_seq=np.arange(0,1.5,0.1) s=np.int(n/10) out=[] for alpha in alpha_seq: SS=0 for h in range(10): test=list(range(h*s,h*s+s)) train=list(set(range(n))-set(test)) node=dt(X[train,:],y[train],alpha=alpha) for t in test:

---

<!-- Página 186 -->

180 8 Decision Trees

SS=SS+(y[t]-value(X[t,:],node))**2 print(SS/n) out.append(SS/n) plt.plot(alpha_seq,out) plt.xlabel(’alpha’) plt.ylabel(’MSE’) plt.title(" optimal alpha by CV (N=100)")

boston=load_boston() n=100 X=boston.data[range(n),:] y=boston.target[range(n)] n_min_seq=np.arange(1,13,1) s=np.int(n/10) out=[] for n_min in n_min_seq: SS=0 for h in range(10): test=list(range(h*s,h*s+s)) train=list(set(range(n))-set(test)) node=dt(X[train,:],y[train],n_min=n_min) for t in test: SS=SS+(y[t]-value(X[t,:],node))**2 print(SS/n) out.append(SS/n) plt.plot(n_min_seq,out) plt.xlabel(’n_min’) plt.ylabel(’MSE’) plt.title("optimal n_min by CV(N=100)")

We also perform similar executions to search for the best 1 ≤ n.min ≤ 15 via CV (Figs. 8.5 Right).

8.2 Decision Tree for Classification

Regarding decision trees for classification, the same response is assigned to the covariates that belong to the same region. If we assign the class with the highest posterior probability to each region, the error probability will be minimized. Specifically, if we map from the p covariate values to one of Y = 1, . . . , K, then if the simultaneous probability fXY (x, k) is given, the rule

x i ∈ Rj ⇒ ˆy i = ¯y j

---

<!-- Página 187 -->

8.2 Decision Tree for Classification 181

minimizes the average error probability

Km∫ ∑∑ I ( ¯y j  = k)fXY (x, k)dx , R k=1j =1j ∫ f (x, k)dx Rj where ¯y j is the k that maximizes ¯y j :=∑∫and I (A) is an K h=1Rh f (x, h)dx indicator that takes a value of one if condition A holds and zero otherwise. Let nj be the sample size of region Rj , and let ¯y j be the mode of k such that x i ∈ Rj and y i = k. Then, we define the rule such that

x i ∈ Rj ⇒ ˆy i = ¯y j

and choose m ≥ 1 and R1, . . . , Rm that minimizes

m ∑∑ I (y i  = ¯y j ) . (8.6) j =1i:x i ∈Rj

Furthermore, in classification, we are concerned with overfitting. For example, if the sample size is one for each region, the quantity of (8.6) is zero. In addition, when we generate a decision tree for classification, we choose some criterion for branching according to a specific variable and threshold for the variable. If there are nj,k samples in region Rj such that Y = k, which can be expressed by m ∑ (nj − maxnj,k ) with ˆpj,k := nj,k /nj , it is sufficient to minimize the error k j =1 probability

E j := 1 − maxˆpj,k k

for each Rj . However, if the tree is deep or if the number K of classes is large, choosing a variable based on minimizing the error probability is not always appropriate. In those cases, instead of the error probability E, either the Gini index

K ∑ G j :=ˆpj,k (1 − ˆpj,k ) k=1

or the entropy

K ∑ Dj := −ˆpj,k log ˆpj,k k=1

---

<!-- Página 188 -->

182 8 Decision Trees

can be used as a criterion. If we use E j , G j , Dj as the criteria at each branch for classification, we can change the function sq_loss for regression as follows:

def freq(y): y=list(y) return [y.count(i) for i in set(y)]

# Mode def mode(y): n=len(y) if n==0: return 0 return max(freq(y))

# error rate def mis_match(y): return len(y)-mode(y)

# Gini def gini(y): n=len(y) if n==0: return 0 fr=freq(y) return sum([fr[i]/n*(n-fr[i]) for i in range(len(fr))])

# Entropy def entropy(y): n=len(y) if n==0: return 0 freq=[y.count(i) for i in set(y)] return np.sum([-freq[i]*np.log (freq[i]/n) for i in range(len(freq))])

Note that the three values are not normalized, i.e., multiplied by nj in each region Rj , which is due to comparing the index values before and after branching because the former and latter consist of one and two regions.

Example 66 (Fisher’s Iris) For the Fisher’s Iris data set (N = 150, p = 4, Fig. 8.6), we compared the decision trees generated based on the error rate, Gini index, and entropy. The test is evaluated by the data used above, and overfitting is allowed. The error rate selects the variables that can distinguish the most frequent class from the other classes in the initial stage. On the other hand, the Gini index and entropy consider all classes and choose a tree that minimizes ambiguity (Figs. 8.7

---

<!-- Página 189 -->

8.2 Decision Tree for Classification 183

Fisher’s Iris 2.5

2.0

1.5

1.0

0.5sepal length (cm)

1 2 3 4 5 6 7 petal length (cm)

X3 : 4.5 < ≥

X3 : 3 X4 : 1.8 < ≥ < ≥ X1 : 5.1 X1 : 5.5 X3 : 5 X1 : 5.9 < ≥ < ≥ < ≥ < ≥ X1 : 4.9 < ≥

Fig. 8.6 Red, blue, and green circles express Iris setosa, Iris virginica, and Iris versicolor. Some samples of Iris virginica and Iris versicolor overlap (Upper), and if we generate a decision tree with n.min = 20 using all the 150 samples, eight inner and nine terminal nodes appear (Lower)

and 8.8). The execution of the process is implemented via the following code (n.min = 4, α = 0):

def table_count(m,u,v):# Again n=u.shape[0] count=np.zeros([m,m]) for i in range(n): count[int(u[i]),int(v[i])]+=1 return count

def mode_max(y): if len(y)==0: return -np.inf count=np.bincount(y) return np.argmax(count)

---

<!-- Página 190 -->

184 8 Decision Trees

Error Probability Gini Entropy

S VC VNS VC VNS VC VN S 50 0 0S 50 0 0S 50 0 0 VC 0 48 0VC 0 49 1VC 0 49 1 VN 0 2 50VN 0 1 49VN 0 1 49

Fig. 8.7 Generation of decision trees for classification, where “S,” “VC,” and “VN” express “Setosa,” “Versicolor,” and “Virginica,” respectively. According to Example 66, we compare the decision trees generated in terms of the error rate, Gini index, and entropy. The Gini index and entropy generated similar decision trees

from sklearn.datasets import load_iris

iris=load_iris() iris.target_names f=mis_match x=iris.data y=iris.target n=len(x) node=dt(x,y,n_min=4) m=len(node) u=[]; v=[] for h in range(m): if node[h].j==-1: w=y[node[h].set] u.extend([node[h].center]*len(w)) v.extend(w) table_count(3,np.array(u),np.array(v))

draw_graph(node)

Moreover, for classification, we can generate the optimum decision tree based on CV, as done for regression. For example, we may implement the following code:

---

<!-- Página 191 -->

8.3 Bagging 185

iris=load_iris() iris.target_names f=mis_match index=np.random.choice(n,n,replace=False)# Choose n from n candidates. X=iris.data[index,:] y=iris.target[index] n_min_seq=np.arange(5,51,5) s=15 for n_min in n_min_seq: SS=0 for h in range(10): test=list(range(h*s,h*s+s)) train=list(set(range(n))-set(test)) node=dt(X[train,:],y[train],n_min=n_min) for t in test: SS=SS+np.sum(y[t]!=value(X[t,:],node)) print(SS/n)

0.08666666666666667 0.08 0.07333333333333333 0.08 0.08 0.08 0.08 0.08 0.08 0.08

However, when the error rate (prediction performance) for new data is evaluated, the expected performance is not obtained (correct answer rate is approximately 90 %). To lower the classification error rate for future data, the K-nearest neighbor method (Chap. 2), logistic regression (Chap. 2), or support vector machine (Chap. 8) may be considered. However, as a generalization of decision tree regression and classification, we can generate multiple decision trees (random forest, boosting) and expect that these trees would have acceptable performance. These methods are described later in this chapter.

8.3 Bagging

Bagging applies the same idea as bootstrapping to the generation of decision trees: randomly select the same number of rows from a data frame (allow duplication) and use these data to generate a tree. This operation is repeated B times to obtain decision trees ˆf1, . . . , ˆfB . Each tree takes the form of a function that performs regression or classification, and it takes a real value output for regression but a finite number of values prepared in advance for classification. When we obtain the outputs p of the trees, ˆf1(x), . . . , ˆfB (x), for the new input x ∈ R, the output is the arithmetic mean of the outputs and the value with the highest frequency for regression and for classification, respectively. Such processing is called bagging. Consider two decision trees generated from the sample sets (x1, y1), . . . , (x N , y N ) ′′′′ and (x, y), . . . , (x, y) whose distributions are shared. The sets often produce 11N N

---

<!-- Página 192 -->

186 8 Decision Trees

Fig. 8.8 We sample data from one data frame and a decision tree is generated for each data frame. Each decision tree has a similar function, but the variables selected may differ greatly. After generating a large number of such trees, we output the average and the most frequent class for regression and classification, respectively

completely different decision trees because the samples are easy to fit with different decision trees. Therefore, when processing new data using the generated decision tree for either regression and classification, the result may be unreliable because the decision tree is unstable. Therefore, one approach is to generate many data frames, generate decision trees corresponding to the data frames, and obtain a solution under the consensus system of a plurality of decision trees.

Example 67 The decision trees in Fig. 8.8 are trees that actually sample data frames. The procedure uses the following code:

n=200 p=5 X=np.random.randn(n,p) beta=randn(p) Y=np.array(np.abs(np.dot(X,beta)+randn(n)),dtype=np.int64) f=mis_match node_seq=[] for h in range(8): index=np.random.choice(n,n,replace=True)# Choose n from n candidates. x=X[index,:] y=Y[index] node_seq.append(dt(x,y,n_min=6))

draw_graph(node_seq[0])

draw_graph(node_seq[1])

---

<!-- Página 193 -->

8.4 Random Forest 187

8.4 Random Forest

Although bagging suppresses variation in the generated decision trees, the corre- lation among the generated decision trees is strong, and the original purpose is not sufficiently achieved. Therefore, an improved version called a random forest has been developed. The difference between bagging and random forest is that in random forest, the candidate variables used for branching are a subset of m variables instead of all p variables. The m variables are randomly selected for each branching, and the optimal variable is selected from among this subset. The √ theoretical consideration is beyond the scope of this book, but m = p is used in this section. The procedure that has been built thus far can be used to implement random forest by simply changing (generalizing) a part of the function branch. In the default situation of m = p, the procedure behaves the same as bagging, and the previous procedure also works.

def branch(x,y,S,rf=0):## if rf==0:## T=np.arange(x.shape[1])## else:## T=np.random.choice(x.shape[1],rf,replace=False)## if x.shape[0]==0: return [0,0,0,0,0,0,0] best_score=np.inf for j in T:## for i in S: left=[]; right=[] for k in S: if x[k,j]<x[i,j]: left.append(k) else: right.append(k) left_score=f(y[left]); right_score=f(y[right]) score=left_score+right_score if score<best_score: best_score=score i_1=i; j_1=j left_1=left; right_1=right left_score_1=left_score; right_score_1=right_score return [i_1,j_1,left_1,right_1,best_score,left_score_1,right_score_1]

For Fisher’s Iris data set, the prediction was not correct when the decision tree was generated only once. In the case of random forest, however, we choose from m ≤ p variables each time with the above function branch. Compared to the case of bagging, this approach produces a set of trees with large variations, which greatly improves the prediction performance.

Example 68 The trees are trained with 100 Iris training data points, and the per- formance is evaluated with 50 test data points. During the course of the experiment, the roles of the training and test data are not changed. The tree b = 1, . . . , B is generated each time, and the result of the i-th test data classification is stored in z[b, i].

---

<!-- Página 194 -->

188 8 Decision Trees

For this two-dimensional array, we store the result of majority voting on b trees and the number of correct answers in zz[b,i] and in zzz[b], respectively, and define the function h that outputs the B-dimensional array.

def rf(z): z=np.array(z,dtype=np.int64) zz=[] for b in range(B): u=sum([mode_max(z[range(b+1),i])==y[i+100] for i in range(50)]) zz.append(u) return zz

We execute the following program:

iris=load_iris() iris.target_names f=mis_match n=iris.data.shape[0] order=np.random.choice(n,n,replace=False)# Choose n from n candidates. X=iris.data[order,:] y=iris.target[order] train=list(range(100)) test=list(range(100,150)) B=100 plt.ylim([35,55]) m_seq=[1,2,3,4] c_seq=["r","b","g","y"] label_seq=[’m=1’,’m=2’,’m=3’,’m=4’] plt.xlabel(’number of repeats’) plt.ylabel(’the number of correct answers’) plt.title(’random forest’)

for m in m_seq: z=np.zeros((B,50)) for b in range(B): index=np.random.choice(train,100,replace=True) node=dt(X[index,:],y[index],n_min=2,rf=m) for i in test: z[b,i-100]=value(X[i,],node) plt.plot(list(range(B)),np.array(rf(z))-0.2*(m-2),label=label_seq[m-1], linewidth=0.8,c=c_seq[m-1]) plt.legend(loc=’lower right’) plt.axhline(y=50,c="b",linewidth=0.5,linestyle="dashed")

The results are shown in Fig. 8.9. It appears that m = 4 (bagging), where all variables are available, would be advantageous, but m = 3 had a lower error rate, and the performances of m = 4 and m = 2 were similar. In the case of bagging, only similar trees that make similar decisions are generated. Random forests have a certain probability of branching without using dominant variables, so trees that are different from bagging often occur and multifaceted decisions can be made, which is the advantage of a random forest.

---

<!-- Página 195 -->

8.5 Boosting 189

Random Forest 50

45

40 m=4 m=3 35m=2 # Correct Ans /50m=1 30 0 20 40 60 80 100 # Tree Generation

Fig. 8.9 Random forest applied to the Iris data set. When making decisions with a small number of decision trees, the error rate is large, even at m = 4 (bagging). The error rate improves as the number of trees generated increases, with the highest correct answer rate for m = 3, followed by m = 2. The lines are offset by 0.1 each to prevent the lines from overlapping

8.5 Boosting

The concept of boosting is broad, but we limit it to the case of using a decision tree. We select an appropriate λ > 0, limit the number of branches d (the number of end points is d + 1), and set r = y (response) initially. Then, we generate trees and update the residual r sequentially as follows. We generate the tree ˆf1 so that T the difference between [ ˆf1(x1), . . . , ˆf1(x N )]and r is the smallest, and we update T r = [r1, · · · , rN ]by

r1 = r1 − λ ˆf1(x1), . . . , rN = rN − λ ˆf1(x N ).

T This process is repeated until [ ˆfB (x1), . . . , ˆfB (x N )]is close to r. Finally, we generate the tree ˆfB ,

r1 = r1 − λ ˆfB (x1), . . . , rN = rN − λ ˆfB (x N ).

N Here, the values of r ∈ Rchange as the tree generation progresses. Then, using ˆˆ the obtained f1, . . . , fB , the final function

B ∑ ˆf (·) = λˆf(·) b b=1

is obtained. First, we develop a procedure that generates appropriate trees given the number of inner points d (end points d + 1). The process b_dt is almost the same as dt: the only difference is that the number of interior points d (or the number of vertices 2d +1) is predetermined. Therefore, branching starts from the vertex with the largest

---

<!-- Página 196 -->

190 8 Decision Trees

difference in error before and after branching, and the procedure is stopped when the number of vertices reaches 2d + 1.

def b_dt(x,y,d): n=x.shape[0] node=[] first=Node(0,-1,0,np.arange(n)) first.score=f(y[first.set]) node.append(first) while len(node)<=2*d-1: r=len(node) gain_max=-np.inf for h in range(r): if node[h].j==-1: i,j,left,right,score,left_score,right_score=branch(x,y,node[ h].set) gain=node[h].score-score if gain>gain_max: gain_max=gain h_max=h i_0=i; j_0=j left_0=left; right_0=right left_score_0=left_score; right_score_0=right_score node[h_max].th=x[i_0,j_0]; node[h_max].j=j_0 next=Node(h_max,-1,0,left_0) next.score=f(y[next.set]); node.append(next) next=Node(h_max,-1,0,right_0) next.score=f(y[next.set]); node.append(next) r=2*d+1 for h in range(r): node[h].left=0; node[h].right=0 for h in range(r-1,1,-1): pa=node[h].parent if node[pa].right==0: node[pa].right=h else: node[pa].left=h if node[h].right==0 and node[h].left==0: node[h].j=-1 if f==sq_loss: g=np.mean else: g=mode_max for h in range(r): if node[h].j==-1: node[h].center=g(node[h].set) # After these , set the value of node.left and node.right. for h in range(r-1,-1,-1): node[h].left=0; node[h].right=0; for h in range(r-1,0,-1): pa=node[h].parent if node[pa].right==0: node[pa].right=h else: node[pa].left=h # # After these , calculate the value of node.center if f==sq_loss: g=np.mean else: g=mode_max for h in range(r): if node[h].j==-1: node[h].center=g(y[node[h].set]) else: node[h].center=0 return node

---

<!-- Página 197 -->

8.5 Boosting 191

For the choice of parameters d, B, λ, either d = 1 or d = 2 appears to be ideal.

Example 69 For the parameters B and λ, in general, it is necessary to decide the optimum for cross-validation, but since the implementation is in the Python language and runs slowly, in the following, we execute only the case B = 200 and λ = 0.1.

boston=load_boston() B=200 lam=0.1 X=boston.data y=boston.target f=sq_loss train=list(range(200)) test=list(range(200,300)) # Generate B boosting trees. # It takes about 5 minutes for each d, for a total of about 15 minutes trees_set=[] for d in range(1,4): trees=[] r=y[train] for b in range(B): trees.append(b_dt(X[train,:],r,d)) for i in train: r[i]=r[i]-lam*value(X[i,:],trees[b]) print(b) trees_set.append(trees)

# Evaluation with test data out_set=[] for d in range(1,4): trees=trees_set[d-1] z=np.zeros((B,600)) for i in test: z[0,i]=lam*value(X[i,],trees[0]) for b in range(1,B): for i in test: z[b,i]=z[b-1,i]+lam*value(X[i,:],trees[b]) out=[] for b in range(B): out.append(sum((y[test]-z[b,test])**2)/len(test)) out_set.append(out)

# Displayed in graphs plt.ylim([0,40]) c_seq=["r","b","g"] label_seq=[’d=1’,’d=2’,’d=3’] plt.xlabel(’The number of trees generated’) plt.ylabel(’MSE with test data’) plt.title(’This book’s program (lambda=0.1)’) for d in range(1,4): out=out_set[d-1] u=range(20,100) v=out[20:100]; plt.plot(u,v,label=label_seq[d-1],linewidth=0.8,c=c_seq[d-1]) plt.legend(loc=’upper right’)

We show how the square error (test data) changes in Fig. 8.10 for each d = 1, 2, 3 and b = 1, . . . , B.

---

<!-- Página 198 -->

192 8 Decision Trees

The Program in this book (λ = 0.1) gbm Package (λ = 0.001)

35d=180d=1 d=2d=2 30d=3 d=3 60 25 20 40 15 10 20 Test Square ErrorTest Square Error 5 00 20 40 60 80 1000 1000 2000 3000 4000 5000 # Tree Generation# Tree Generation

Fig. 8.10 The executions of the program in this book with λ = 0.1 (Left) and gbm package with λ = 0.001 (Right). The smaller the λ is, the better the performance, but many trees should be generated

Gradient boosting essentially performs the above process. In actual processing, the lightgbm package is often used in Python language. Since this approach generates thousands of trees, it is devised for high speed processing.

Example 70 Setting λ = 0.01, B = 5000, d = 1, 2, 3, we execute the gradient boosting package lightgbm (Fig. 8.10 Right). Compared to the case of λ = 0.1, the results do not converge unless B is large. However, more accurate forecasts can be obtained. Additionally, the package is sufficiently fast: the procedure was completed in practical time even for λ = 0.001 (default) and B = 5000.

import lightgbm as lgb

boston=load_boston() X=boston.data y=boston.target train=list(range(200)) test=list(range(200,300)) B=200 lgb_train=lgb.Dataset(X[train,:],y[train]) lgb_eval=lgb.Dataset(X[test,:],y[test],reference=lgb_train) B=5000 nn_seq=list(range(1,10,1))+list(range(10,91,10))+list(range(100,B,50)) out_set=[] for d in range(1,4): lgbm_params={ ’objective’: ’regression’, ’metric’: ’rmse’, ’num_leaves’: d+1, ’learning_rate’: 0.001 } out=[] for nn in nn_seq: model=lgb.train(lgbm_params,lgb_train,valid_sets=lgb_eval, verbose_eval=False,num_boost_round=nn)

---

<!-- Página 199 -->

Exercises 69–74 193

z=model.predict(X[test,:],num_iteration=model.best_iteration) out.append(sum((z-y[test])**2)/100) out_set.append(out)

# Displayed in graphs plt.ylim([0,80]) c_seq=["r","b","g"] label_seq=[’d=1’,’d=2’,’d=3’] plt.xlabel(’The number of trees generated’) plt.ylabel(’MSE with test data’) plt.title(’light (lambda=0.001)’) for d in range(1,4): out=out_set[d-1] u=range(20,100) plt.plot(nn_seq,out_set[d-1],label=label_seq[d-1],linewidth=0.8,c=c_seq[ d-1]) plt.legend(loc=’upper right’)

In this chapter, processing is implemented via the source program to understand the inner procedure of random forest and boosting, but in actual data analysis, such a package may be used.

Exercises 69–74

69. Write the following functions in the Python language, where each input y is a vector:

(a) sq_loss that given input vector y, outputs the square sum of the differences between each element and the arithmetic average. (b) mis_match that given input vector y, outputs the number of mismatches between each element and the mode.

70. We used the function branch below to construct a tree. Given matrix x, vector y, loss function f, and the set of row indices S, the procedure outputs the division of S that minimizes the sum of the losses for the two new sets of indices. Fill in the blanks and execute the program.

def sq_loss(y): if len(y)==0: return 0 else: y_bar=np.mean(y) return np.linalg.norm(y-y_bar)**2

def branch(x,y,S,rf=0): if rf==0: m=x.shape[1] if x.shape[0]==0: return [0,0,0,0,0,0,0] best_score=np.inf

---

<!-- Página 200 -->

194 8 Decision Trees

for j in range(x.shape[1]): for i in S: left=[]; right=[] for k in S: if x[k,j]<x[i,j]: left.append(k) else: # blank(1) # left_score=f(y[left]); right_score=f(y[right]) score=# blank(2) # if score<best_score: best_score=score i_1=i; j_1=j left_1=left; right_1=right left_score_1=left_score; right_score_1=right_score return [i_1,j_1,left_1,right_1,best_score,left_score_1,right_score_1]

f=sq_loss n=100; p=5 x=randn(n,p) y=randn(n) S=np.random.choice(n,10,replace=False) branch(x,y,S)

71. The following procedure constructs a decision tree using the function branch and a loss function. Execute the procedure for Fisher’s Iris data set and n.min = 5, α = 0, and draw the graph.

class Stack: def __init__(self,parent,set,score): self.parent=parent self.set=set self.score=score

class Node: def __init__(self,parent,j,th,set): self.parent=parent self.j=j self.th=th self.set=set

def dt(x,y,alpha=0,n_min=1,rf=0): if rf==0: m=x.shape[1] # A single set of stack is constructed.Decision tree is initialized stack=[Stack(0,list(range(x.shape[0])),f(y))]# f is global node=[] k=-1 # Extracting the last element of the stack and updating the decision tree while len(stack)>0: popped=stack.pop() k=k+1 i,j,left,right,score,left_score,right_score=branch(x,y,popped.set, rf) if popped.score-score<alpha or len(popped.set)<n_min or len(left )==0 or len(right)==0:

---

<!-- Página 201 -->

Exercises 69–74 195

node.append(Node(popped.parent,-1,0,popped.set)) else: node.append(Node(popped.parent,j,x[i,j],popped.set)) stack.append(Stack(k,right,right_score)) stack.append(Stack(k,left,left_score)) # After these , set the value of node.left and node.right. for h in range(k,-1,-1): node[h].left=0; node[h].right=0; for h in range(k,0,-1): pa=node[h].parent if node[pa].right==0: node[pa].right=h else: node[pa].left=h # After these , calculate the value of node.center if f==sq_loss: g=np.mean else: g=mode_max for h in range(k+1): if node[h].j==-1: node[h].center=g(y[node[h].set]) else: node[h].center=0 return node

The decision tree is obtained using below function if we get node.

from igraph import *

def draw_graph(node): r=len(node) col=[] for h in range(r): col.append(node[h].j) colorlist=[’#ffffff’,’#fff8ff’,’#fcf9ce’,’#d6fada’,’#d7ffff’,’#d9f2f8’, ’#fac8be’,’#ffebff’,’#ffffe0’,’#fdf5e6’,’#fac8be’,’#f8ecd5’,’#ee82ee ’] color=[colorlist[col[i]] for i in range(r)] edge=[] for h in range(1,r): edge.append([node[h].parent,h]) g=Graph(edges=edge,directed=True) layout=g.layout_reingold_tilford(root=[0]) out=plot(g,vertex_size=15,layout=layout,bbox=(300,300),vertex_label= list(range(r)),vertex_color=color) return out

draw_graph(node)

72. For the Boston data set, we consider finding the optimum 0 ≤ α ≤ 1.5 via 10- fold CV. Fill in either train or test in each blank to execute the procedure.

def value(u,node): r=0 while node[r].j!=-1: if u[node[r].j]<node[r].th: r=node[r].left

---

<!-- Página 202 -->

196 8 Decision Trees

else: r=node[r].right return node[r].center

boston=load_boston() n=100 X=boston.data[range(n),:] y=boston.target[range(n)] f=sq_loss alpha_seq=np.arange(0,1.5,0.1) s=np.int(n/10) out=[] for alpha in alpha_seq: SS=0 for h in range(10): test=list(range(h*s,h*s+s)) train=list(set(range(n))-set(test)) node=dt(X[train,:],y[train],alpha=alpha) for t in test: SS=SS+(y[t]-value(X[t,:],node))**2 print(SS/n) out.append(SS/n) plt.plot(alpha_seq,out) plt.xlabel(’alpha’) plt.ylabel(’MSE’) plt.title(" optimal alpha by CV (N=100)")

boston=load_boston() n=100 X=boston.data[range(n),:] y=boston.target[range(n)] n_min_seq=np.arange(1,13,1) s=np.int(n/10) out=[] for n_min in n_min_seq: SS=0 for h in range(10): # blank #=list(range(h*s,h*s+s)) # blank #=list(set(range(n))-set(# Blank #)) node=dt(X[# blank #,:],y[# blank #],n_min=n_min) for t in# blank #: SS=SS+(y[t]-value(X[t,:],node))**2 print(SS/n) out.append(SS/n) plt.plot(n_min_seq,out) plt.xlabel(’n_min’) plt.ylabel(’MSE’) plt.title(" optimal n_min by CV (N=100)")

73. We wish to modify branch and to construct a random forest procedure. Fill in the blanks, and execute the procedure.

def branch(x,y,S,rf=0):## if rf==0:## T=# blank(1) ### else:## T=# blank(2) # if x.shape[0]==0: return [0,0,0,0,0,0,0] best_score=np.inf

---

<!-- Página 203 -->

Exercises 69–74 197

for j in T:## for i in S: left=[]; right=[] for k in S: if x[k,j]<x[i,j]: left.append(k) else: right.append(k) left_score=f(y[left]); right_score=f(y[right]) score=left_score+right_score if score<best_score: best_score=score i_1=i; j_1=j left_1=left; right_1=right left_score_1=left_score; right_score_1=right_score return [i_1,j_1,left_1,right_1,best_score,left_score_1,right_score_1]

def rf(z): z=np.array(z,dtype=np.int64) zz=[] for b in range(B): u=sum([mode_max(z[range(b+1),i])==y[i+100] for i in range(50)]) zz.append(u) return zz

iris=load_iris() iris.target_names f=mis_match n=iris.data.shape[0] order=np.random.choice(n,n,replace=False)# Choose n from n candidates. X=iris.data[order,:] y=iris.target[order] train=list(range(100)) test=list(range(100,150)) B=100 plt.ylim([35,55]) m_seq=[1,2,3,4] c_seq=["r","b","g","y"] label_seq=[’m=1’,’m=2’,’m=3’,’m=4’] plt.xlabel(’the number of repeats’) plt.ylabel(’the number of correct answers’) plt.title(’random forest’) for m in m_seq: z=np.zeros((B,50)) for b in range(B): index=np.random.choice(train,100,replace=True) node=dt(X[index,:],y[index],n_min=2,rf=m) for i in test: z[b,i-100]=value(X[i,],node) plt.plot(list(range(B)),np.array(rf(z))-0.2*(m-2),label=label_seq[m-1], linewidth=0.8,c=c_seq[m-1]) plt.legend(loc=’lower right’) plt.axhline(y=50,c="b",linewidth=0.5,linestyle="dashed")

74. We execute boosting using the lightgbm package for the Boston data set. Look up the lightgbm package, fill in the blanks, and draw the graph.

import lightgbm as lgb

---

<!-- Página 204 -->

198 8 Decision Trees

boston=load_boston() X=boston.data y=boston.target train=list(range(200)) test=list(range(200,300)) B=200 lgb_train=lgb.Dataset(X[train,:],y[train]) lgb_eval=lgb.Dataset(X[test,:],y[test],reference=lgb_train) B=5000 nn_seq=list(range(1,10,1))+list(range(10,91,10))+list(range(100,B,50)) out_set=[] for d in range(1,4): lgbm_params={ ’objective’: ’regression’, ’metric’: ’rmse’, ’num_leaves’:# blank(1) #, ’learning_rate’: 0.001 } out=[] for nn in nn_seq: model=lgb.train(lgbm_params,lgb_train,valid_sets=lgb_eval, verbose_eval=False,num_boost_round=# blank(2) #) z=model.predict(X[test,:],num_iteration=model.best_iteration) out.append(sum((z-y[test])**2)/100) out_set.append(out)

# Displayed in graphs plt.ylim([0,80]) c_seq=["r","b","g"] label_seq=[’d=1’,’d=2’,’d=3’] plt.xlabel(’The number of trees generated’) plt.ylabel(’MSE with test data’) plt.title(’lightgbm package (lambda=0.001)’) for d in range(1,4): out=out_set[d-1] u=range(20,100) v=out[20:100]; plt.plot(nn_seq,out_set[d-1],label=label_seq[d-1],linewidth=0.8,c=c_seq [d-1]) plt.legend(loc=’upper right’)

---

<!-- Página 205 -->

## Chapter 9

# Support Vector Machine

Abstract Support vector machine is a method for classification and regression that draws an optimal boundary in the space of covariates (p dimension) when the samples (x1, y1), . . . , (x N , y N ) are given. This is a method to maximize the minimum value over i = 1, . . . , N of the distance between x i and the boundary. This notion is generalized even if the samples are not separated by a surface by softening the notion of a margin. Additionally, by using a general kernel that is not the inner product, even if the boundary is not a surface, we can mathematically formulate the problem and obtain the optimum solution. In this chapter, we consider only the two-class case and focus on the core part. Although omitted here, the theory of support vector machines also applies to regression and classification with more than two classes.

9.1 Optimum Boarder

In the following, we consider a classification rule with two classes from N samples, where the responses take the values of y1, . . . , y N = ±1. To consider the locations of covariates geometrically, we first consider the distance between a point and a line.

2 Proposition 23 The distance between (x, y) ∈ Rand the line l : aX + bY + c = 0, a, b ∈ R is given by

|ax + by + c| √. 2 2 a+ b

For the proof, see the Appendix at the end of this chapter. The formula assumes p = 2-dimensional Euclidean space. For the general p- dimensional case, the distance between x = [x1, . . . , x p] (row vector) and the surface β0 + β1X1 + · · · + β p Xp = 0 is

|β0 + x1β1 + · · · + x p β p| d(x) := √. 22 β+ · · · + βp 1

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2021199 J. Suzuki, Statistical Learning with Math and Python, https://doi.org/10.1007/978-981-15-7877-9_9

---

<!-- Página 206 -->

200 9 Support Vector Machine

y = 1y = 1y = 1

M M

y = −1y = −1y = −1

Fig. 9.1 Left: the samples are not separable by any surface. Middle: the samples are separable by a surface, but such surfaces are not unique. Right: the two parallel surfaces in red and blue do not contain any sample between them and they maximize the distance (twice M) between them. The middle (center) surface is the border between the samples such that yi = 1 and yi = −1. Only the samples on the red and blue surfaces determine the border; the others do not play such a role

T p In particular, if we divide each term of β0 ∈ R, β = [β1, . . . , β p]∈ Rby the same constant such that ‖β‖2 = 1, we can write the result as

d(x) = |β0 + x1β1 + · · · + x p β p| .

In the following, we say that the samples are separable (by a surface) if there exist β0 and β (Fig. 9.1) such that

y1(β0 + x1β), . . . , y N (β0 + x N β) ≥ 0 .

If the samples are separable, such a surface is not unique. In order to specify it, we define the following rule. Even if the samples are separable, we prepare two parallel surfaces that do not contain any sample between them. Then, we maximize the distance between the surfaces and regard the surface in the middle of the two surfaces as the border that divides the samples. To this end, for the N samples (x1, y1), . . . , (x N , y N ), it is sufficient to maximize the minimum distance M := mini d(x i ) between each x i and the surface β0 + X1β1+· · ·+Xp β p = 0. Without loss of generality, if we assume that the coefficients β0 and β satisfy ‖β‖2 = 1, because d(x i ) = y i (β0 + x i β), the problem reduces to finding the β0, β that maximize the margin

M := miny i (β0 + x i β) i=1,...,N

(Fig. 9.1). In this case, the subset (support vector) of {1, . . . , N} such that M = y i (β0 + x i β) determines the coefficients β0 and β and the margin M. Even if the samples are separable, another set of N samples that follow the same distribution may not be separable. If we formulate the problem of obtaining the border (surface) from the samples in the general setting, we should assume that the samples are separable. Rather, we define a formulation for any samples that are not

---

<!-- Página 207 -->

9.1 Optimum Boarder 201

necessarily separable. Now, we generalize the result as follows. Given γ ≥ 0, we p maximize M w.r.t. (β0, β) ∈ R×Rand i ≥ 0, i = 1, . . . , N, under the constraints

N ∑ i ≤ γ (9.1) i=1

and

y i (β0 + x i β) ≥ M(1 − i ). (9.2)

i = 1, . . . , N. For separable samples, we solve the problem under the setting 1 = · · · = N = 0, i.e., solve it for γ = 0 (Fig. 9.2, left). However, we may formulate the problem γ > 0 even if the samples are separable. In that case, the value of M increases because the constraint is relaxed. The i’s such that i > 0, as well as those such that M = y i (β0 + x i β) are the support vectors. In other words, all the i values that satisfy (9.2) with equality, are the support vectors for the margin M. Compared to the case of γ = 0, because the support vectors increase, more samples support the decision of β0 and β for the optimal border (Fig. 9.2, middle). For this case, the estimation is less sensitive to the variation of samples, which means that we need to adjust the value of γ appropriately, for example, via cross-validation. On the other hand, the values of i are  = 0, 0 <  < 1,  = 1, and  > 1 for y i (β0 +x i β) ≥ M, 0 < y i (β0 +x i β) < M, y i (β0 +x i β) = 0, and y i (β0 +x i β) < 0, respectively.

y = 1y = 1y = 1

MM + ΔM0 3 < 15 > 1 MM + ΔM x1 x2 x3 x4 x5 1 = 0 2 = 04 = 1 y = −1y = −1y = −1

Fig. 9.2 The samples filled in either red or blue are the support vectors. Left: there exists a solution of γ = 0 for separable samples. In this example, the border is determined by only the three samples (support vectors). However, if we set γ > 0 (middle), we allow samples to be between the red and blue surfaces because the margin becomes large, but the solution is stable because the six support vectors support the red surface. When the value of γ changes, the support vectors change, so does the border surface. Right: for {x1, x2}, x3 , x4 , and x5 , we observe  = 0, 0 <  < 1,  = 1, and  > 1, respectively. If  = 0, some are support vectors, as for x1 , and others are not, as for x2

---

<!-- Página 208 -->

202 9 Support Vector Machine

The conditions i = 1 and 0 <  < 1 are on the border and between the border and the margin in front. Some of the i’s such that i = 0 are on the margin in front and others are not (support vectors) (Fig. 9.2, right). For nonseparable samples, if the value of γ is too small, no solution exists. In fact, if γ = 0 and at least one i such that i = 0 does not satisfy (9.2), then no solution exists. On the other hand, if the number of such i values for which i > 1 exceeds γ , no such β0 and β exist. The support vector machine problem is formulated as finding β0, β, i , i = 1, . . . , N, that minimize

NNN 1∑∑∑ 2 LP := ‖β‖+ Ci −αi {y i (β0 + x i β) − (1 − i )} −μ i i , (9.3) 2 i=1i=1i=1

removing the constraint ‖β‖2 = 1 and replacing β0/M, β/M by β0, β in (9.2). Note that minimizing ‖β‖ is equivalent to maximizing the M before β is normalized as β/M. In this setting, we regard C > 0 as a cost, the last two terms are constraints, and αi , μ i ≥ 0, i = 1, . . . , N, are the Lagrange coefficients.

9.2 Theory of Optimization

Before solving (9.1) and (9.2), we prepare the theory. In the following, in the p problem of finding β ∈ Rthat minimizes f0(β) under fj (β) ≤ 0, j = 1, . . . , m, ∗ we assume that such a solution exists and that such a β is β. We define

m ∑ L(α, β) := f0(β) +αj fj (β) j =1

m1 p for α = (α1, . . . , αm ) ∈ R. Then, for an arbitrary β ∈ R, we have { f0(β), f1(β) ≤ 0, . . . , fm (β) ≤ 0 supL(α, β) =(9.4) α≥0+∞, Otherwise.

p In fact, for an arbitrarily fixed β ∈ R, if j exists such that fj (β) > 0 and we make αj larger, then L(α, β) can be infinitely large. On the other hand, if

1 We say that v is an upper bound of S if u ≤ v for any u ∈ S in a set S ⊆ R and that the minimum of the upper bounds of S is the upper limit of S, which we write as sup A. For example, the maximum does not exist for S = {x ∈ R|0 ≤ x < 1}, but sup S = 1. Similarly, we define the lower bounds and their maximum (the upper limit) of S, which we write as inf A.

---

<!-- Página 209 -->

9.2 Theory of Optimization 203

f1(β), . . . , fm (β) ≤ 0, then L(α, β) has the largest value f0(β) for α ≥ 0 when α1 = · · · = αm = 0. Moreover, we have

∗ f := infsupL(α, β) ≥ supinfL(α, β) . (9.5) β α≥0α≥0β

′ ′ p In fact, for arbitrary α≥ 0 and β∈ R, we have

′′′′ supL(α, β) ≥ L(α, β) ≥ infL(α, β) . α≥0β

′ ′ Since the inequality holds for arbitrary αand β, it still holds even if we take the ′ ′ inf and sup w.r.t. the βand αon the left and right, respectively.

2 Example 71 Suppose that p = 2, m = 1, f0(β) := β1 + β2 , and f1(β) = β+ 1 2 β− 1. Then, for 2

22 L(α, β) := β1 + β2 + α(β+ β− 1) , 1 2

we write (9.4) as { 22 β1 + β2, β+ β≤ 1 1 2 supL(α, β) = α≥0+∞, Otherwise. √√ Thus, it takes the minimum value −2 when β1 = β2 = −1/2, and the left- √ hand side of (9.5) is 2. If we partially differentiate L(α, β) w.r.t. β1, β2 , we have β1 = β2 = −1/(2α) and {} ( )( ) 22 11111 infL(α, β) = − − + α+− 1= − − α . β 2α 2α 2α2α2α

From the inequality between the arithmetic and geometric means, the value is √ maximized at 1/(2α) = α. Therefore, from α = −1/2, the right-hand side of √ (9.5) is −2 as well.

The problem of minimizing f (β) := supL(α, β) is a primary problem, while α≥0 that of maximizing g(α) := infβ L(α, β) under α ≥ 0 is a dual problem. ∗ If we write the optimum values of the primary and dual problems as f := ∗ infβ f (β) and g:= supg(α), then we have α≥0

∗ ∗ f ≥ g. (9.6)

We consider only the case that the inequality is equal in this book. Many problems, including support vector machines, satisfy this assumption.

---

<!-- Página 210 -->

204 9 Support Vector Machine

∗ ∗ Assumption 1 f = g.

p ∗ Suppose that f0, f1, . . . , fm : R→ R are convex and differentiable at β = β. We consider the equivalent conditions in the following proposition below according to the KKT (Karush–Kuhn–Tucker) conditions.

Proposition 24 (KKT Condition) Under f1(β) ≤ 0, . . . , fm (β) ≤ 0, the solution ∗ p β = β∈ Rminimizes f0(β) if and only if there exist α1, . . . , αm ≥ 0 s.t.

∗∗ f1(β), . . . , fm (β) ≤ 0 (9.7)

∗∗ α1f1(β) = · · · = αm fm (β) = 0 (9.8)

m ∑ ∗∗ ∇f0(β) +αi ∇fi (β) = 0. (9.9) i=1

Proof Sufficiency: as proved for p = 1 in Chap. 6, in general, for any p ≥ 1, if p pp f : R→ R is convex and differentiable at x = x0 ∈ R, for each x ∈ R, we have

T f (x) ≥ f (x0) + ∇f (x0) (x − x0) . (9.10)

p Using the fact that, under the KKT conditions, for each solution β ∈ R, we have

m ∑ ∗∗T ∗∗T ∗ f0(β) ≤ f0(β) − ∇f0(β) (β − β) = f0(β) +αi ∇fi (β) (β − β) i=1 mm ∑∑ ∗ ≤ f0(β) +αi {fi (β) − fi (β)} = f0(β) +αi fi (β) ≤ f0(β) , i=1i=1

∗ which means that βis optimum, and we used (9.10), (9.9), (9.10), (9.8), and f1(β) ≤ 0, . . . , fm (β) ≤ 0 in the above derivation steps. 

∗ Necessity: if βis the solution of the primary problem, then a solution β exists ∗ such that f1(β), . . . , fm (β) ≤ 0, and we require (9.7). From the assumption f = ∗∗ g, there exists α≥ 0 such that {} mm ∑∑ ∗∗∗∗∗∗∗ f0(β) = g(α) = inff0(β) +αf i (β)≤ f0(β)+αf i (β) ≤ f0(β) , i i β i=1i=1

---

<!-- Página 211 -->

9.3 The Solution of Support Vector Machines 205

where the first equality is due to Assumption 1 and the last inequality is due to (9.7) ∗ and α≥ 0. Thus, the above inequality is an equality, and we have (9.8). Finally, ∗ βminimizes

m ∑ ∗ f0(β) +αfi (β) , i i=1

and we require (9.9).

Example 72 For Example 71, the KKT conditions (9.7), (9.8), and (9.9) are

22 β+ β− 1 ≤ 0 (9.11) 1 2 22 α(β+ β− 1) = 0 (9.12) 1 2 [ ][ ][ ] 1β10 + 2α=, (9.13) 1β20

where α = 0 satisfies (9.12) but does not satisfy (9.13). Thus, the equalities in (9.11) and (9.13) are the KKT conditions.

9.3 The Solution of Support Vector Machines

The following seven equations are the KKT conditions:

y i (β0 + x i β) − (1 − i ) ≥ 0 (9.14)

i ≥ 0 (9.15)

are from (9.7), and

αi [y i (β0 + x i β) − (1 − i )] = 0 (9.16)

μ i i = 0 (9.17)

are from (9.8). Moreover, from (9.9), differentiating (9.3) w.r.t. β, β0 , and i , we obtain

N ∑ Tp β =αi y i x ∈ R(9.18) i i=1

N ∑ αi y i = 0 (9.19) i=1 C − αi − μ i = 0 , (9.20)

respectively.

---

<!-- Página 212 -->

206 9 Support Vector Machine

The dual problem of LP in (9.3) is constructed as follows. In order to optimize w.r.t. β0, i , if we differentiate by these values, we obtain (9.19) and (9.20); thus, Lp can be stated as

NN ∑∑ 1 2 αi + ‖β‖−x i βαi y i . 2 i=1i=1

From (9.18), the second and third terms become

( )T ( )( ) NNNN ∑∑∑∑ 1 TTT αi y i x αi y i x −x iαi y i x αi y i , iii 2 i=1i=1i=1i=1

so we construct the function with input as the Lagrange coefficients αi , μ i ≥ 0, i = 1, . . . , N,

NNN ∑1∑∑ T LD :=αi − αi αj y i y j x i x , (9.21) j 2 i=1i=1j =1

where α ranges over (9.19) and

0 ≤ αi ≤ C . (9.22)

Note that although μ i is not included in LD , μ i = C − αi ≥ 0 and αi ≥ 0 are left as (9.22). We can compute β via (9.18) from the α obtained in this manner. In solving the dual problem, we note that (9.22) can be divided into the three cases.

Proposition 25 ⎧ ⎨αi = 0 ⇐ y i (β0 + x i β) > 1 0 < αi < C ⇒ y i (β0 + x i β) = 1(9.23) ⎩ αi = C ⇐ y i (β0 + x i β) < 1.

For the proof, see the end of this chapter. We show that at least one i satisfies y i (β0 + x i β) = 1. If there exists an i such that 0 < αi < C, then from Proposition 25, the i satisfies y i (β0 + x i β) = 1, and we obtain β0 via β0 = y i − x i β. Suppose α1 = · · · = αN = 0. From (8.18), we have β = 0. Moreover, from (8.17) and (8.20), we have μ i = C and i = 0, i = 1, · · · , N, which means y i (β0 + x i β) ≥ 1, from Proposition 25. Therefore, we require y i β0 ≥ 1, i.e., y1 = · · · = y N . Then, β0 = 1 and β0 = −1 satisfy y i (β0 + x i β) = 1 when y i = 1 and y i = −1, respectively.

---

<!-- Página 213 -->

9.3 The Solution of Support Vector Machines 207

Suppose next that αi = C for at least one i (we denote the set of such i by S) and that αi = 0 for {1, · · · , N}\S. From (8.16), we have y i (β0 + x i β) − (1 − i ) = 0. In the following, we show that i = 0 for at least one i ∈ S. To this end, we assume i > 0 for all i ∈ S. If we define ∗ := mini∈S i , and replace i and β0 − ∗ and β0 + y i ∗, respectively, the latter satisfies the constraint (8.14) and has a smaller value of

N ∑ 1 2 f0(β, β0, ) = ‖β‖+ Ci , 2 i=1

which contradicts the underlying assumption that β, β0, and  were optimal. Thus, we have i = 0 for at least one i ∈ S. Then, we can compute β0 = y i − x i β, and j ∑ N for j ∈ S\{i}. For each i ∈ S, we set i = 0 and compute j . We choose the j =1 i(i = 0) that minimizes the quantity and set such β0 as the final β0 . The β, β0, and  minimize f0(β, β0, ). We solve the dual problem (9.19), (9.21), and (9.22) using a quadratic program- ming solver. In the R language, a package called {quadprog} is available for this N×N m×N N m purpose. We specify Dmat ∈ R, Amat ∈ R, dvec ∈ R, bvec ∈ R(m ≥ 1) such that

1T T LD = − α Dmatα + d vecα 2

Amatα ≥ bvec ,

N for α ∈ R, where we assume that the first meq and m − med are equality and inequality constraints in Amatα ≥ bvec and specify the number 0 ≤ meq ≤ m. In particular, in the formulation derived above, we take m = 2N + 1, meq = 1, ⎡⎤ y1 · · · yN ⎢⎥ ⎢−1 · · · 0⎥ ⎡⎤⎢⎥ ⎢. ⎥ x1,1y1 · · · x1,p y1⎢0 . . 0⎥ ⎢⎥⎢⎥ ⎢...⎥N×p ⎢⎥(2N+1)×N z =...∈ R, Amat =0 · · · −1∈ R ⎣. . .⎦ ⎢⎥ ⎢⎥ 1 · · · 0 xN,1yN · · · xN,p yN⎢⎥ ⎢⎥ ⎢. . ⎥ ⎣0 . 0⎦ 0 · · · 1

---

<!-- Página 214 -->

208 9 Support Vector Machine

T N×N Dmat = zz ∈ R(if the rank is below N, the matrix is singular), bvec = T 2N+1 T N [0, −C, . . . , −C, 0, . . . , 0]∈ R, dvec = [1, . . . , 1]∈ R, and α = N [α1, . . . , αN ] ∈ R. For example, we construct the following procedure:

import cvxopt from cvxopt import matrix

a=randn(1); b=randn(1) n=100 X=randn(n,2) y=np.sign(a*X[:,0]+b*X[:,1]+0.1*randn(n)) y=y.reshape(-1,1)# The shape needs to be clearly marked

def svm_1(X,y,C): eps=0.0001 n=X.shape[0] P=np.zeros((n,n)) for i in range(n): for j in range(n): P[i,j]=np.dot(X[i,:],X[j,:])*y[i]*y[j] # It must be specified using the matrix function in cvxopt. P=matrix(P+np.eye(n)*eps) A=matrix(-y.T.astype(np.float)) b=matrix(np.array([0]).astype(np.float)) h=matrix(np.array([C]*n+[0]*n).reshape(-1,1).astype(np.float)) G=matrix(np.concatenate([np.diag(np.ones(n)),np.diag(-np.ones(n))])) q=matrix(np.array([-1]*n).astype(np.float))

res=cvxopt.solvers.qp(P,q,A=A,b=b,G=G,h=h)# execute solver alpha=np.array(res[’x’])# where x corresponds to alpha in the text beta=((alpha*y).T@X).reshape(2,1) index=np.arange(0,n,1) index (eps<alpha[:,0])&(alpha[:,0]<c-eps) beta_0=np.mean(y[index]-X[index,:]@beta)

return {’beta’:beta,’beta_0’:beta_0}

Example 73 Using the function svm_1, we execute the following procedure and drew the samples and the border as in Fig. 9.3:

a=randn(1); b=randn(1) n=100 X=randn(n,2) y=np.sign(a*X[:,0]+b*X[:,1]+0.1*randn(n)) y=y.reshape(-1,1)# The shape needs to be clearly marked for i in range(n): if y[i]==1: plt.scatter(X[i,0],X[i,1],c="red") else : plt.scatter(X[i,0],X[i,1],c="blue") res=svm_1(X,y,C=10)

---

<!-- Página 215 -->

9.4 Extension of Support Vector Machines Using a Kernel 209

Fig. 9.3 Generating samples,3 we draw the border of the support vector machine2

1

0

-1 Second Factor -2

-3 -3 -2 -1 0 1 2 3 First Factor

def f(x): return -res[’beta_0’]/res[’beta’][1]-x*res[’beta’][0]/res[’beta’][1]

x_seq=np.arange(-3,3,0.5) plt.plot(x_seq,f(x_seq)) res

pcost dcost gap pres dres 0: -1.6933e+02 -7.9084e+03 2e+04 8e-01 8e-15 1: -1.4335e+01 -2.5477e+03 4e+03 1e-01 1e-14 2: 3.4814e+01 -3.6817e+02 5e+02 1e-02 4e-14 3: -2.0896e+01 -1.3363e+02 1e+02 3e-03 2e-14 4: -4.4713e+01 -1.0348e+02 6e+01 1e-03 8e-15 5: -5.8178e+01 -8.1212e+01 2e+01 4e-04 6e-15 6: -6.4262e+01 -7.5415e+01 1e+01 1e-04 4e-15 7: -6.7750e+01 -7.0997e+01 3e+00 2e-05 5e-15 8: -6.9204e+01 -6.9329e+01 1e-01 9e-15 7e-15 9: -6.9259e+01 -6.9261e+01 2e-03 2e-15 8e-15 10: -6.9260e+01 -6.9260e+01 2e-05 2e-15 7e-15 Optimal solution found. {’beta’: array([[ 7.54214409], [-1.65772882]]), ’beta_0’: -0.14880733394172593}

9.4 Extension of Support Vector Machines Using a Kernel

The reason for solving the dual problem rather than the primary problem is that LD can be expressed by the inner product 〈·, ·〉 as

NNN ∑∑∑ 1 LD :=αi − αi αj y i y j 〈x i , x j 〉 . 2 i=1i=1j =1

---

<!-- Página 216 -->

210 9 Support Vector Machine

p Let V be the vector space with inner product φ : R→ V . Then, we may replace 〈x i , x j 〉 by k(x i , x j ) := 〈φ(x i ), φ(x j )〉. In such a case, we construct a nonlinear classification rule from (φ(x1), y1), . . . , (φ(x N ), y N ). In other words, even if the mapping φ(x) → y is linear and the learning via a support vector machine remains p the same, the mapping x → y can be nonlinear. For the new data (x∗, y∗) ∈ R× {−1, 1}, the mapping x∗ → y∗ is nonlinear. In the following, let V be a vector space with an inner product; we construct a N matrix K such that the (i, j )-th element is φ(x i ), φ(x j ) ∈ V . In fact, for z ∈ R, the matrix

NN ∑∑〈〉 T z Kz =ziφ(x i ), φ(x j )zj i=1j =1 〈 〉∥∥2 NN∥N∥ ∑∑∑ ∥∥ =zi φ(x i ),zj φ(x j )=∥zi φ(x i )∥≥ 0 ∥∥ i=1j =1i=1

is symmetric and nonnegative definite, and k(·, ·) is a kernel in the strict sense.

Example 74 (Polynomial Kernel) For the d-dimensional polynomial kernel d p k(x, y) = (1 + 〈x, y〉) with x, y ∈ R, if d = 1 and p = 2, then since

1 + x1y1 + x2y2 = 1 · 1 + x1y1 + x2y2 = 〈[1, x1, x2], [1, y1, y2]〉 ,

3 we have φ : [x1, x2] → [1, x1, x2] with V = R. For p = 2 and d = 2. Because

2 2222 (1 + x1y1 + x2y2)= 1 + x1 y1 + x2 y2 + 2x1y1 + 2x2y2 + 2x1x2y1y2 √√√ 22 = 〈[1, x, x, 2x1, 2x2, 2x1x2], 1 2 √√√ 22 [1, y, y, 2y1, 2y2, 2y1y2]〉 , 1 2

we have √√√ 22 φ : [x1, x2] → [1, x, x, 2x1, 2x2, 2x1x2] 1 2

6 p with V = R. In this way, there exists φ : R→ V such that k(x, y) = 〈φ(x), φ(y)〉. We can write the inner product and the polynomial kernel with d = p = 2 using the Python language as

def K_linear(x,y): return x.T@y def K_poly(x,y): return (1+x.T@y)**2

---

<!-- Página 217 -->

9.4 Extension of Support Vector Machines Using a Kernel 211

We say that V is a vector space over R if

a, b ∈ V , α, β ∈ R ⇒ αa + βb ∈ V (9.24)

and that any element in V is a vector. There are various inner products. We say that the mapping 〈·, ·〉: V × V → R is an inner product of V if the following properties hold for a, b, c ∈ V , α ∈ R〈a + b, c〉 = 〈a, c〉 + 〈b, c〉, 〈a, b〉 = 〈b, a〉, 〈αa, b〉 = 2 α〈a, b〉, 〈a, a〉 = ‖a‖≥ 0, and ‖a‖ = 0 ⇒ a = 0.

Example 75 The set V of continuous functions defined in [0, 1] is a vector space. In fact, V satisfies (9.24). The function V × V → R defined by 〈f, g〉 := ∫ 1 f (x)g(x)dx for f, g ∈ V is an inner product. In fact, we can check the four 0 properties: ∫ 1 〈f + g, h〉 =(f (x) + g(x))h(x)dx 0 ∫ ∫ 11 =f (x)h(x)dx +g(x)h(x)dx = 〈f, h〉 + 〈g, h〉 00 ∫ ∫ 11 〈f, g〉 =f (x)g(x)dx =g(x)f (x)dx = 〈g, f 〉 00 ∫ ∫ 11 〈αf, g〉 =αf (x) · g(x)dx = αf (x)g(x)dx = α〈f, g〉 00 ∫ 1 2 〈f, f 〉 ={f (x)}dx ≥ 0. 0 ∫ 12 Moreover, since f is continuous, f (x)dx = 0 if and only if f = 0. 0 T 2 p Example 76 The map V × V → R defined by f (x, y) := (1 + x y), x, y ∈ R, p is not an inner product of V := R. In fact, since f (0 · x, y) = 1  = 0 · f (x, y), the mapping does not satisfy the definition of an inner product.

p In the following, we replace x i ∈ R, i = 1, . . . , N, by φ(x i ) ∈ V using N ∑ p p φ : R→ V . Therefore, β ∈ Ris β =αi y i φ(x i ) ∈ V , and the inner product i=1 〈x i , x j 〉 in LD is replaced by the inner product of φ(x i ) and φ(x j ), the kernel of K(x i , x j ). If we extend in this way, the border becomes φ(X)β + β0 = 0, which N ∑ means thatαi y i K(X, x i ) + β0 = 0 is not necessarily a surface. i=1

---

<!-- Página 218 -->

212 9 Support Vector Machine

We modify the function svm_1 as follows:

1. add argument K to the function definition, 2. replace np.dot(X[:,i]*X[:,j]) with K(X[i,:],X[j,:]), and 3. replace beta in return() with alpha.

In this manner, we can generalize the support vector machine.

def svm_2(X,y,C,K): eps=0.0001 n=X.shape[0] P=np.zeros((n,n)) for i in range(n): for j in range(n): P[i,j]=K(X[i,:],X[j,:])*y[i]*y[j] # It must be specified using the matrix function in cvxopt P=matrix(P+np.eye(n)*eps) A=matrix(-y.T.astype(np.float)) b=matrix(np.array([0]).astype(np.float)) h=matrix(np.array([C]*n+[0]*n).reshape(-1,1).astype(np.float)) G=matrix(np.concatenate([np.diag(np.ones(n)),np.diag(-np.ones(n))])) q=matrix(np.array([-1]*n).astype(np.float))

res=cvxopt.solvers.qp(P,q,A=A,b=b,G=G,h=h) alpha=np.array(res[’x’])# where x corresponds to alpha in the text beta=((alpha*y).T@X).reshape(2,1) index=np.arange(0,n,1) index (eps<alpha[:,0])&(alpha[:,0]<c-eps) beta_0=np.mean(y[index]-X[index,:]@beta)

return {’alpha’:alpha,’beta’:beta,’beta_0’:beta_0}

Example 77 Using the function svm_2, we compare the borders generated by linear and nonlinear kernels (Fig. 9.4).

# execute a=3;b=-1 n=200 X=randn(n,2) y=np.sign(a*X[:,0]+b*X[:,1]**2+0.3*randn(n)) y=y.reshape(-1,1)

def plot_kernel(K,line):# Specify the type of line by argument line. res=svm_2(X,y,1,K) alpha=res[’alpha’][:,0] beta_0=res[’beta_0’] def f(u,v): S=beta_0 for i in range(X.shape[0]): S=S+alpha[i]*y[i]*K(X[i,:],[u,v]) return S[0] uu=np.arange(-2,2,0.1); vv=np.arange(-2,2,0.1); ww=[] for v in vv: w=[] for u in uu: w.append(f(u,v)) ww.append(w) plt.contour(uu,vv,ww,levels=0,linestyles=line)

---

<!-- Página 219 -->

9.4 Extension of Support Vector Machines Using a Kernel 213

Fig. 9.4 Generating samples,3 we draw linear and nonlinear borders that are flat and2 curved surfaces, respectively

0 1

0 X[,2] -1

0 -2

-3 -3 -2 -1 0 1 2 3 X[,1]

for i in range(n): if y[i]==1: plt.scatter(X[i,0],X[i,1],c="red") else: plt.scatter(X[i,0],X[i,1],c="blue") plot_kernel(K_poly,line="dashed") plot_kernel(K_linear,line="solid")

pcost dcost gap pres dres 0: -7.5078e+01 -6.3699e+02 4e+03 4e+00 3e-14 1: -4.5382e+01 -4.5584e+02 9e+02 6e-01 2e-14 2: -2.6761e+01 -1.7891e+02 2e+02 1e-01 1e-14 3: -2.0491e+01 -4.9270e+01 4e+01 2e-02 1e-14 4: -2.4760e+01 -3.3429e+01 1e+01 5e-03 5e-15 5: -2.6284e+01 -2.9464e+01 4e+00 1e-03 3e-15 6: -2.7150e+01 -2.7851e+01 7e-01 4e-05 4e-15 7: -2.7434e+01 -2.7483e+01 5e-02 2e-06 5e-15 8: -2.7456e+01 -2.7457e+01 5e-04 2e-08 5e-15 9: -2.7457e+01 -2.7457e+01 5e-06 2e-10 6e-15 Optimal solution found. pcost dcost gap pres dres 0: -9.3004e+01 -6.3759e+02 4e+03 4e+00 4e-15 1: -5.7904e+01 -4.6085e+02 8e+02 5e-01 4e-15 2: -3.9388e+01 -1.5480e+02 1e+02 6e-02 1e-14 3: -4.5745e+01 -6.8758e+01 3e+01 9e-03 3e-15 4: -5.0815e+01 -6.0482e+01 1e+01 3e-03 2e-15 5: -5.2883e+01 -5.7262e+01 5e+00 1e-03 2e-15 6: -5.3646e+01 -5.6045e+01 3e+00 6e-04 2e-15 7: -5.4217e+01 -5.5140e+01 1e+00 2e-04 2e-15 8: -5.4531e+01 -5.4723e+01 2e-01 1e-05 2e-15 9: -5.4617e+01 -5.4622e+01 6e-03 3e-07 3e-15 10: -5.4619e+01 -5.4619e+01 6e-05 3e-09 3e-15 11: -5.4619e+01 -5.4619e+01 6e-07 3e-11 2e-15 Optimal solution found.

Thus far, we construct Python language programs to understand the principle. In actual data analysis, the svm in the sklearn package, is available for support vector machines.

---

<!-- Página 220 -->

214 9 Support Vector Machine

Fig. 9.5 Using the e1071 package with the radical kernel, we draw a nonlinear (curved) surface. C = 100 and γ = 1

Example 78 For artificial data, using the svm in the sklearn package we executed the radical kernel {} 1 2 k(x, y) = exp− ‖x − y‖ 2 2σ

with γ = 1 for cost C = 1 (Fig. 9.5).

import sklearn from sklearn import svm

x=randn(200,2) x[0:100,]=x[0:100,]+2 x[100:150,]=x[100:150,]-2 y=np.concatenate(([1 for i in range(150)],[2 for i in range(50)])) train=np.random.choice(200,100,replace=False) test=list(set(range(200))-set(train))

res_svm=svm.SVC(kernel="rbf",gamma=1,C=100)# SVM without tuning res_svm.fit(x[train,],y[train])# execute

SVC(C=100, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape=’ovr’, degree=3, gamma=1, kernel=’rbf’, max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)

res_svm.predict(x[test,])# prediction with test data

array([1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 1])

---

<!-- Página 221 -->

9.4 Extension of Support Vector Machines Using a Kernel 215

import mlxtend from mlxtend.plotting import plot_decision_regions

plot_decision_regions(x,y,clf=res_svm)

Using the GridSearchCV command in the sklearn.model_selection, we compare via cross-validation the optimum combination of C and γ over C = 0.1, 1, 10, 100, 1000 and γ = 0.5, 1, 2, 3, 4 and find that the pair of C = 1 and γ = 0.5 is the best.

from sklearn.model_selection import GridSearchCV

grid={’C’:[0.1,1,10,100,1000],’gamma’:[0.5,1,2,3,4]} tune=GridSearchCV(svm.SVC(),grid,cv=10) tune.fit(x[train,],y[train])

GridSearchCV(cv=10, error_score=’raise-deprecating’, estimator=SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape=’ovr’, degree=3, gamma=’auto_deprecated’, kernel=’rbf’, max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False), iid=’warn’, n_jobs=None, param_grid={’C’: [0.1, 1, 10, 100, 1000], ’gamma’: [0.5, 1, 2, 3, 4]}, pre_dispatch=’2*n_jobs’, refit=True, return_train_score=False, scoring=None, verbose=0)

tune.best_params_# we find that C=1 , gamma=0.5 are optimal.

{’C’: 1, ’gamma’: 0.5}

Example 79 In general, a support vector machine can execute even when the number of classes is more than two. For example, the function svm runs without specifying the number of classes. For Fisher’s Iris dataset, we divide the 150 samples into 120 training and 30 test data to evaluate the performance: the kernel is radical and the parameters are γ = 1 and C = 10.

from sklearn.datasets import load_iris

iris=load_iris() iris.target_names x=iris.data y=iris.target train=np.random.choice(150,120,replace=False) test=np.ones(150,dtype=bool) test[train]=False iris_svm=svm.SVC(kernel="rbf",gamma=1,C=10) iris_svm.fit(x[train,],y[train])

---

<!-- Página 222 -->

216 9 Support Vector Machine

SVC(C=10, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape=’ovr’, degree=3, gamma=1, kernel=’rbf’, max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)

For example, we obtain the following result:

y_pre=iris_svm.predict(x[test,]) table_count(3,y[test],y_pre)

array([[ 9., 0., 0.], [ 0., 10., 0.], [ 0., 3., 8.]])

Appendix: Proofs of Propositions

2 Proposition 23 The distance between a point (x, y) ∈ Rand a line l : aX + bY + c = 0, a, b ∈ R is given by

|ax + by + c| √. 2 2 a+ b

′ Proof Let (x0, y0) be the perpendicular foot of l from (x, y). lis a normal of l and can be written by

X − xY − y ′ 00 l: = = t a b

′ for some t (Fig. 9.6). Since (x0, y0) and (x, y) are on l and l, respectively, we have ⎧ ⎨ax0 + by0 + c = 0 x − xy − y ⎩00 = = t . a b

Fig. 9.6 The distance between a point and a line(x, y) √ 2 2 (x − x0)+ (y − y0), ′ where lis the normal of l l : aX + bY + c = 0 that goes through (x0, y0) X − xY − y 00 l : = = t a b

(x0, y0)(x0, y0)

---

<!-- Página 223 -->

Exercises 75–87 217

If we erase (x0, y0), from x0 = x − at, y0 = y − bt, a(x − at) + b(y − bt) + c = 0, 2 2 we have t = (ax + by + c)/(a+ b). Thus, the distance is √ √ |ax + by + c| 2 2 2 22 (x − x0)+ (y − y0)= (a+ b)t= √. a2 + b2



Proposition 25 ⎧ ⎨αi = 0 ⇐ y i (β0 + x i β) > 1 0 < αi < C ⇒ y i (β0 + x i β) = 1 ⎩ αi = C ⇐ y i (β0 + x i β) < 1.

Proof When αi = 0, applying (9.20), (9.17), and (9.14) in this order, we have

αi = 0 ⇒ μ i = C > 0 ⇒ i = 0 ⇒ y i (β0 + x i β) ≥ 1 .

When 0 < αi < C, from (9.17) and (9.20), we have i = 0. Moreover, applying (9.16), we have

0 < αi < C ⇒ y i (β0 + x i β) − (1 − i ) = 0 ⇒ y i (β0 + x i β) = 1 .

When αi = C, from (9.15), we have i ≥ 0. Moreover, applying (9.16), we have

αi = C ⇒ y i (β0 + x i β) − (1 − i ) = 0 ⇒ y i (β0 + x i β) ≤ 1 .

Furthermore, from (9.16), we have y i (β0 + x i β) > 1 ⇒ αi = 0. On the other hand, applying (9.14), (9.17), and (9.20) in this order, we have

y i (β0 + x i β) < 1 ⇒ i > 0 ⇒ μ i = 0 ⇒ αi = C .



Exercises 75–87

2 We define the distance between a point (u, v) ∈ Rand a line aU + bV + c = 0, a, b ∈ R by

|au + bv + c| √. 2 2 a+ b

---

<!-- Página 224 -->

218 9 Support Vector Machine

p For β ∈ Rsuch that β0 ∈ R and ‖β‖2 = 1, when samples (x1, y1), . . . , (x N , y N ) ∈ p R× {−1, 1} satisfy the separability y1(β0 + x1β), . . . , y N (β0 + x N β) ≥ 0, the support vector machine is formulated as the problem of finding (β0, β) that maximize the minimum value M := mini y i (β0 + x i β) over the distances between x i (row vector) and the surface β0 + Xβ = 0.

p 75. We extend the support vector machine problem to finding (β0, β) ∈ R×Rand i ≥ 0, i = 1, . . . , N, that maximize M under the constraints γ ≥ 0, M ≥ 0, N ∑ i ≤ γ , and i=1

y i (β0 + x i β) ≥ M(1 − i ), i = 1, . . . , N .

(a) What can we say about the locations of samples (x i , y i ) when i = 0, 0 < i < 1, i = 1, 1 < i . (b) Suppose that y i (β0 + x i β) < 0 for at least r samples and for any β0 and β. Show that if γ ≤ r, then no solution exists. Hint: i > 1 for such an i. (c) The larger the γ is, the smaller the M. Why?

p 76. We wish to obtain β ∈ Rthat minimizes f0(β) under fj (β) ≤ 0, j = ∗ 1, . . . , m. If such a solution exists, we denote the minimum value by f . Consider the following two equations { f0(β), fj (β) ≤ 0 , j = 1, . . . , m supL(α, β) =(9.25) α≥0+∞ Otherwise ∗ f := infsupL(α, β) ≥ supinfL(α, β) (9.26) β β α≥0α≥0

under

m ∑ L(α, β) := f0(β) +αj fj (β) j =1

m for α = (α1, . . . , αm ) ∈ R. Moreover, suppose p = 2 and m = 1. For

22 L(α, β) := β1 + β2 + α(β+ β− 1) , (9.27) 1 2

such that the equality holds in the inequality (9.26). p 77. Suppose that f0, f1, . . . , fm : R→ R are convex and differentiable at β = ∗∗ p β. It is known that β∈ Ris the optimum value of min{f0(β) | fi (β) ≤ 0, i = 1, . . . , m} if and only if there exist αi ≥ 0, i = 1, . . . , m, such that

∗ fi (β) ≤ 0, i = 1, . . . , m, (9.28)

---

<!-- Página 225 -->

Exercises 75–87 219

and the two conditions are met (KKT conditions)

∗ αi fi (β) = 0, i = 1, . . . , m, (9.29)

m ∑ ∗∗ ∇f0(β) +αi ∇fi (β) = 0. (9.30) i=1

In this problem, we consider the sufficiency.

p (a) If f : R→ R is convex and differentiable at x = x0 ∈ R, then

T f (x) ≥ f (x0) + ∇f (x0) (x − x0) (9.31)

p∗ for each x ∈ R. From this fact, show that f0(β) ≤ f0(β) for arbitrary p β ∈ Rthat satisfies (9.28). Hint: Use (9.29) and (9.30) once, (9.31) twice, and f1(β) ≤ 0, . . . , fm (β) ≤ 0 once. (b) For (9.27), find the conditions that correspond to (9.28)–(9.30).

78. If we remove the condition ‖β‖2 = 1 in Problem 75 and regard β0/M, β/M as β0 and β, then the problem reduces to finding β0, β, i , i = 1, . . . , N, that minimize

NNN 1∑∑∑ 2 LP := ‖β‖+Ci −αi {y i (β0+x i β)−(1−i )}−μ i i , (9.32) 2 2 i=1i=1i=1

where C > 0 (cost), the last two terms are constraints, and αi , μ i ≥ 0, i = 1, . . . , N, are the Lagrange coefficients. Show that the KKT conditions (9.28)– (9.30) are the following:

N ∑ αi y i = 0 (9.33) i=1

N ∑ p β =αi y i x i ∈ R(9.34) i=1 C − αi − μ i = 0 (9.35)

αi [y i (β0 + x i β) − (1 − i )] = 0 (9.36)

μ i i = 0 (9.37)

y i (β0 + x i β) − (1 − i ) ≥ 0 (9.38)

i ≥ 0. (9.39)

---

<!-- Página 226 -->

220 9 Support Vector Machine

79. Show that the dual problem (9.32) of LP is given by

NNN ∑∑∑ 1 T LD :=αi − αi αj y i y j x x j , (9.40) i 2 i=1i=1j =1

where α ranges over (9.33) and

0 ≤ αi ≤ C . (9.41)

Moreover, how is β obtained from such an α? 80. Show the following: ⎧ ⎨αi = 0 ⇐ y i (β0 + x i β) > 1 0 < αi < C ⇒ y i (β0 + x i β) = 1 ⎩ αi = C ⇐ y i (β0 + x i β) < 1.

81. We wish to obtain the value of β0 by y i (β0 + x i β) = 1 for at least one i.

(a) Show that α1 = · · · = αN = 0 and y i (β0 + x i β) = 1 imply β0 = y i , i = 1, . . . , N. (b) Suppose that (α = 0 or α = C) and y i (β0 + x i β)  = 1 for each i, and let ∗ := mini i . Show that Lp decreases when replacing i and β by i − ∗ and β0+y i ∗, respectively, for each i, which means that no optimum solution 2 can be obtained under the assumption. Hint: y i = ±1 ⇐⇒ y= 1. i (c) Show that y i (β0 + x i β) = 1 for at least one i.

82. In order to input the dual problem (9.40), (9.33), and (9.41) into a quadratic N×N m×N N programming solver, we specify Dmat ∈ R, Amat ∈ R, dvec ∈ R, m and bvec ∈ R(m ≥ 1) such that

1 T T LD = − α Dmatα + d vecα 2

Amatα ≥ bvec ,

where the first meq and the last m − meq are equalities and inequalities, N respectively, in the m constraints Amatα ≥ bvec, α ∈ R. If we define

T bvec := [0, −C, . . . , −C, 0, . . . , 0],

what are Dmat, Amat, dvec, and meq? Moreover, fill in the blanks below and execute the result.

import cvxopt from cvxopt import matrix

---

<!-- Página 227 -->

Exercises 75–87 221

a=randn(1); b=randn(1) n=100 X=randn(n,2) y=np.sign(a*X[:,0]+b*X[:,1]+0.1*randn(n)) y=y.reshape(-1,1)# The shape needs to be clearly marked

def svm_1(X,y,C): eps=0.0001 n=X.shape[0] P=np.zeros((n,n)) for i in range(n): for j in range(n): P[i,j]=np.dot(X[i,:],X[j,:])*y[i]*y[j] # It must be specified using the matrix function in cvxopt. P=matrix(P+np.eye(n)*eps) A=matrix(-y.T.astype(np.float)) b=matrix(# blank(1) #).astype(np.float)) h=matrix(# blank(2) #).reshape(-1,1).astype(np.float)) G=matrix(np.concatenate([# blank(3) #,np.diag(-np.ones(n))])) q=matrix(np.array([-1]*n).astype(np.float)) res=cvxopt.solvers.qp(P,q,A=A,b=b,G=G,h=h)# execute solver alpha=np.array(res[’x’])# # where x corresponds to alpha in the text beta=((alpha*y).T@X).reshape(2,1) index=np.arange(0,n,1) index_1=index[eps<alpha[:,0]] index_2=index[(alpha<C-eps)[:,0]] index=np.concatenate((index_1,index_2)) beta_0=np.mean(y[index]-X[index,:]@beta) return {’beta’:beta,’beta_0’:beta_0}

a=randn(1); b=randn(1) n=100 X=randn(n,2) y=np.sign(a*X[:,0]+b*X[:,1]+0.1*randn(n)) y=y.reshape(-1,1)# The shape needs to be clearly marked for i in range(n): if y[i]==1: plt.scatter(X[i,0],X[i,1],c="red") else : plt.scatter(X[i,0],X[i,1],c="blue") res=svm_1(X,y,C=10)

def f(x): return -res[’beta_0’]/res[’beta’][1]-x*res[’beta’][0]/res[’beta’][1]

x_seq=np.arange(-3,3,0.5) plt.plot(x_seq,f(x_seq))

p 83. Let V be a vector space. We define a kernel K(x, y) w.r.t. φ : R→ V as the p p inner product of φ(x) and φ(y) given (x, y) ∈ R× R. For example, for the

---

<!-- Página 228 -->

222 9 Support Vector Machine

T d d-dimensional polynomial kernel K(x, y) = (1 + x y) , if d = 1 and p = 2, then the mapping is

T ((x1, x2), (y1, y2)) → 1 · 1 + x1y1 + x2y2 = (1, x1, x2) (1, y1, y2) .

In this case, we regard the map φ as (x1, x2) → (1, x1, x2). What is φ for p = 2 and d = 2? Write a Python function K_poly(x,y) that realizes the d = 2-dimensional polynomial kernel. 84. Let V be a vector space over R.

(a) Suppose that V is the set of continuous functions in [0, 1]. Show that ∫ 1 f (x)g(x)dx, f, g ∈ V , is an inner product of V . 0 pT 2 p (b) For vector space V := R, show that (1 + x y), x, y ∈ R, is not an inner product of V . (c) Write a Python function K_linear(x,y) for the standard inner product.

Hint: Check the definition of an inner product, for a, b, c ∈ V , α ∈ R, 〈a + 2 b, c〉 = 〈a, c〉 + 〈b, c〉; 〈a, b〉 = 〈b, a〉; 〈αa, b〉 = α〈a, b〉; 〈a, a〉 = ‖a‖≥ 0. p p 85. In the following, using φ : R→ V , we replace x i ∈ R, i = 1, . . . , N, with ∑ p N φ(x i ) ∈ V . Thus, β ∈ Ris expressed as β = αi y i φ(x i ) ∈ V , and the i=1 inner product 〈x i , x j 〉 in LD is replaced by the inner product of φ(x i ) and φ(x j ), i.e., K(x i , x j ). If we extend the vector space, the border φ(X)β + β0 = 0, i.e., ∑ N αy K(X, x ) + β= 0, is not necessarily a surface. Modify the svm_1 i=1 i i i 0 in Problem 82 as follows:

(a) add argument K to the definition, (b) replace np.dot(X[,i]*X[,j]) with K(X[i,],X[j,]), and (c) replace beta in return by alpha.

Then, execute the function svm_2 by filling in the blanks.

# generating data a=3;b=-1 n=200 X=randn(n,2) y=np.sign(a*X[:,0]+b*X[:,1]**2+0.3*randn(n)) y=y.reshape(-1,1)

def plot_kernel(K,line):# Specify the type of line by argument line res=svm_2(X,y,1,K) alpha=res[’alpha’][:,0] beta_0=res[’beta_0’] def f(u,v): S=beta_0 for i in range(X.shape[0]): S=S+# blank # return S[0] uu=np.arange(-2,2,0.1); vv=np.arange(-2,2,0.1); ww=[] for v in vv: w=[]

---

<!-- Página 229 -->

Exercises 75–87 223

for u in uu: w.append(f(u,v)) ww.append(w) plt.contour(uu,vv,ww,levels=0,linestyles=line)

for i in range(n): if y[i]==1: plt.scatter(X[i,0],X[i,1],c="red") else: plt.scatter(X[i,0],X[i,1],c="blue") plot_kernel(K_poly,line="dashed") plot_kernel(K_linear,line="solid")

pcost dcost gap pres dres 0: -7.5078e+01 -6.3699e+02 4e+03 4e+00 3e-14 1: -4.5382e+01 -4.5584e+02 9e+02 6e-01 2e-14 2: -2.6761e+01 -1.7891e+02 2e+02 1e-01 1e-14 3: -2.0491e+01 -4.9270e+01 4e+01 2e-02 1e-14 4: -2.4760e+01 -3.3429e+01 1e+01 5e-03 5e-15 5: -2.6284e+01 -2.9464e+01 4e+00 1e-03 3e-15 6: -2.7150e+01 -2.7851e+01 7e-01 4e-05 4e-15 7: -2.7434e+01 -2.7483e+01 5e-02 2e-06 5e-15 8: -2.7456e+01 -2.7457e+01 5e-04 2e-08 5e-15 9: -2.7457e+01 -2.7457e+01 5e-06 2e-10 6e-15 Optimal solution found. pcost dcost gap pres dres 0: -9.3004e+01 -6.3759e+02 4e+03 4e+00 4e-15 1: -5.7904e+01 -4.6085e+02 8e+02 5e-01 4e-15 2: -3.9388e+01 -1.5480e+02 1e+02 6e-02 1e-14 3: -4.5745e+01 -6.8758e+01 3e+01 9e-03 3e-15 4: -5.0815e+01 -6.0482e+01 1e+01 3e-03 2e-15 5: -5.2883e+01 -5.7262e+01 5e+00 1e-03 2e-15 6: -5.3646e+01 -5.6045e+01 3e+00 6e-04 2e-15 7: -5.4217e+01 -5.5140e+01 1e+00 2e-04 2e-15 8: -5.4531e+01 -5.4723e+01 2e-01 1e-05 2e-15 9: -5.4617e+01 -5.4622e+01 6e-03 3e-07 3e-15 10: -5.4619e+01 -5.4619e+01 6e-05 3e-09 3e-15 11: -5.4619e+01 -5.4619e+01 6e-07 3e-11 2e-15 Optimal solution found.

(a) Execute the support vector machine with γ = 1 and C = 100.

import sklearn from sklearn import svm

x=randn(200,2) x[0:100,]=x[0:100,]+2 x[100:150,]=x[100:150,]-2 y=np.concatenate(([1 for i in range(150)],[2 for i in range(50)])) train=np.random.choice(200,100,replace=False) test=list(set(range(200))-set(train)) res_svm=svm.SVC(kernel="rbf",gamma=1,C=1)# SVM without tuning res_svm.fit(x[train,],y[train])# execute

res_svm.predict(x[test,])# prediction with test data

---

<!-- Página 230 -->

224 9 Support Vector Machine

import mlxtend from mlxtend.plotting import plot_decision_regions

plot_decision_regions(x,y,clf=res_svm)

(b) Use the GridSearchCV cosmmand to find the optimal C and γ over C = 0.1, 1, 10, 100, 1000 and γ = 0.5, 1, 2, 3, 4 via cross-validation.

from sklearn.model_selection import GridSearchCV

grid={’C’:[0.1,1,10,100,1000],’gamma’:[0.5,1,2,3,4]} tune=GridSearchCV(svm.SVC(),grid,cv=10) tune.fit(x[train,],y[train])

GridSearchCV(cv=10, error_score=’raise-deprecating’, estimator=SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape=’ovr’, degree=3, gamma=’auto_deprecated’, kernel=’rbf’, max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False), iid=’warn’, n_jobs=None, param_grid={’C’: [0.1, 1, 10, 100, 1000], ’gamma’: [0.5, 1, 2, 3, 4]}, pre_dispatch=’2*n_jobs’, refit=True, return_train_score=False, scoring=None, verbose=0)

86. A support vector machine works even when more than two classes exist. In fact, the function svm in the sklearn packages runs even if we give no information about the number of classes. Fill in the blanks and execute it.

from sklearn.datasets import load_iris

iris=load_iris() iris.target_names x=iris.data y=iris.target train=np.random.choice(150,120,replace=False) test=np.ones(150,dtype=bool) test[train]=False iris_svm=svm.SVC(kernel="rbf",gamma=1,C=10) iris_svm.fit(# blank(1) #)

SVC(C=10, cache_size=200, class_weight=None, coef0=0.0, decision_function_shape=’ovr’, degree=3, gamma=1, kernel=’rbf’, max_iter=-1, probability=False, random_state=None, shrinking=True, tol=0.001, verbose=False)

---

<!-- Página 231 -->

Exercises 75–87 225

y_pre=# blank(2) # table_count(3,y[test],y_pre)

array([[ 9., 0., 0.], [ 0., 10., 0.], [ 0., 3., 8.]])

---

<!-- Página 232 -->

## Chapter 10

# Unsupervised Learning

Abstract Thus far, we have considered supervised learning from N observation data (x1, y1), . . . , (x N , y N ), where y1, . . . , y N take either real values (regression) or a finite number of values (classification). In this chapter, we consider unsupervised learning, in which such a teacher does not exist, and the relations between the N samples and between the p variables are learned only from covariates x1, . . . , x N . There are various types of unsupervised learning; in this chapter, we focus on clustering and principal component analysis. Clustering means dividing the samples x1, . . . , x N into several groups (clusters). We consider K-means clustering, which requires us to give the number of clusters K in advance, and hierarchical clustering, which does not need such information. We also consider the principal component analysis (PCA), a data analysis method that is often used for machine learning and multivariate analysis. For PCA, we consider another equivalent definition along with its mathematical meaning.

10.1 K-means Clustering

Clustering divides N samples x1, . . . , x N with p variable values into K disjoint sets (clusters). Among the clustering methods, K-means clustering requires K to be determined in advance. In the initial stage, one of 1, . . . , K is randomly assigned to each of the N samples, and we execute the following two steps:

1. for each cluster k = 1, . . . , K, find the center (mean vector), and 2. for each sample i = 1, · · · , N, assign the cluster such that the center is the closest among the K clusters,

where a cluster is a set of p-dimensional vectors and its (arithmetic) mean corresponds to the center. In the second step, we evaluate the distance in terms of the L2 norm √ 2 2 ‖a − b‖ =(a1 − b1)+ · · · + (a p − b p )

T T p for a = [a1, . . . , a p], b = [b1, . . . , b p]∈ R.

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2021227 J. Suzuki, Statistical Learning with Math and Python, https://doi.org/10.1007/978-981-15-7877-9_10

---

<!-- Página 233 -->

228 10 Unsupervised Learning

For example, the following procedure can be constructed. If a cluster contains no samples in the middle of the run, the cluster is no longer used since its center cannot be calculated. This can occur if N is relatively small compared to K. In addition, in the following code, the line with # is not for generating the clusters but for tracing the changes in the score values.

def k_means(X,K,iteration=20): n,p=X.shape center=np.zeros((K,p)) y=np.random.choice(K,n,replace=True) scores=[] for h in range(iteration): for k in range(K): if np.sum(y==k)==0: center[k,0]=np.inf else: for j in range(p): center[k,j]=np.mean(X[y==k,j]) S_total=0 for i in range(n): S_min=np.inf for k in range(K): S=np.sum((X[i,]-center[k,])**2) if S<S_min: S_min=S y[i]=k S_total+=S_min scores.append(S_total) return {’clusters’:y,’scores’:scores}

Example 80 K-means clustering executed with the function k_means to display clusters of p = 2-dimensional artificial data (Fig. 10.1).

Fig. 10.1 K-means3 clustering with K = 5, N = 1000, and p = 2.2 Samples in the same cluster share the same color 1 2 0 X

-1

-2

-3 -3 -2 -1 0 1 2 3 X1

---

<!-- Página 234 -->

10.1 K-means Clustering 229

n=1000; K=5; p=2 X=randn(n,p)# data generation y=k_means(X,5)[’clusters’]# getting cluster for each sample # Change the color of each cluster and draw a dot plt.scatter(X[:,0],X[:,1],c=y) plt.xlabel("first component") plt.ylabel("second component")

Text(0, 0.5, ’second component’)

We see that the score

K ∑∑ 2 S :=min‖x i − zk ‖ p zk ∈R k=1i∈C k

does not increase for each update of Steps 1 and 2 while executing K-means clustering, where Ck is the set of indexes i of samples in the kth cluster. In fact, ∑ 2 p the square sum ‖x i − x‖of the distances between x ∈ Rand the points is i∈C k minimized when x is chosen to be the center ¯x k of cluster k: ∑∑ 2 2 ‖x i − x‖= ‖(x i − ¯x k ) − (x − ¯x k )‖ i∈C ki∈C k ∑∑∑ 2 2 T = ‖x i − ¯x k‖+ ‖x − ¯x k‖− 2(x − ¯x k ) (x i − ¯x k ) i∈C ki∈C ki∈C k ∑∑∑ 2 2 2 = ‖x i − ¯x k‖+ ‖x − ¯x k‖≥ ‖x i − ¯x k‖, i∈C ki∈C ki∈C k

∑ 1 where we have used ¯x k = x i . In other words, the score does not increase |Ck | i∈C k after executing Step 1. Moreover, in Step 2, if the cluster to which a sample belongs is changed to the nearest cluster, the score S does not increase either. Moreover, the result of K-means clustering depends on the randomly selected initial clusters, which means that even if K-means clustering is applied, there is no guarantee that an optimum solution will be obtained, and it is necessary to execute it several times with different initial values and select the clustering with the best score.

Example 81 Suppose that there are samples at 0, 6, 10 with N = 3, p = 1, and K = 2 (Fig. 10.2). If “red” and “blue” are initially assigned to 0, 6 and 10, respectively, then 3 and 8 are the centers of the clusters. In that case, the centers of the nearest clusters of 0, 6, 10 are 3, 3, 10 (the square error is 9 + 9 + 0 = 18), and the clusters do not change even if we continue the process. Conversely, if “red” and “blue” are initially assigned to 0 and 6, 10, respectively, then 0 and 8 are the centers

---

<!-- Página 235 -->

230 10 Unsupervised Learning

Center Center

0 3 6 10

Center Center

0 6 8 10

Fig. 10.2 Suppose that we have three samples and that the left two and right one circles are initially clustered as red and blue (upper), respectively. Then, K-means clustering does not further change the assignments of the clusters. The same situation occurs if the left one and right two circles are clustered as red and blue (lower), respectively

Initial values determine the score.

7.4

7.2

7.0

6.8 log(Score) 6.6

6.4

6.2 5 10 15 20 # Cycles

Fig. 10.3 K-means clustering repeated 10 times changing the initial values: each run uses a different color. The score decreases monotonically with each update, and the values at convergence do not match in each update. The horizontal and vertical axes express the number of iterations and the logarithm of the score, respectively

of the clusters. In that case, the closest cluster centers of 0, 6, 10 are 0, 8, 8 (the square error is 0 + 4 + 4 = 8), and the clusters do not change even if we continue the process. The latter is optimal in the sense of the minimum score, but once the first configuration appears, we do not reach the optimal solution.

Example 82 We changed the initial values and repeated K-means clustering (Fig. 10.3). The score decreased in each execution, and the converged value differed

---

<!-- Página 236 -->

10.1 K-means Clustering 231

for each initial value, which means that some executions have not reached the optimum. The code was as follows:

n=1000; p=2 X=randn(n,p) itr=np.arange(1,21,1) for r in range(10): scores=k_means(X,5)[’scores’] plt.plot(itr,np.log(scores)) plt.xlabel(" the number of iteration") plt.ylabel("log(value)") plt.title("See how the score changes with each initial value") plt.xticks(np.arange(1,21,1))

T T Let x1 = [x1,1, . . . , x1,p], . . . , x N = [x N,1, . . . , x N,p]be N samples. If we write the set of sample indexes that belong to a cluster k (a subset of {1, . . . , N}) and T its center as Ck and ¯x k = [ ¯x k,1, . . . , ¯x k,p], respectively, for each k = 1, . . . , K, we have the following relation:

pp ∑∑∑∑ 1 2 2 (x i,j − x i′,j )= 2 (x i,j − ¯x k,j )(10.1) |Ck | i,i′ ∈C kj =1i∈C kj =1

In fact, (10.1) holds if

∑∑∑ 1 2 2 (x i,j − x i′,j )= 2 (x i,j − ¯x k,j ). |Ck | i∈C ki′ ∈C ki∈C k

for j = 1, . . . , p. In particular, the left-hand side can be transformed into

1∑∑ 2 {(x i,j − ¯x k,j ) − (x i′,j − ¯x k,j )} |Ck | i∈C ki′ ∈C k 1∑∑2∑∑ 2 = (x i,j − ¯x k,j )− (x i,j − ¯x k,j ) (x i′,j − x k,j ) |Ck ||Ck | i∈C ki′ ∈C ki∈C ki′ ∈C k ∑∑ 1 2 + (x i′,j − ¯x k,j ), (10.2) |Ck | i∈C ki′ ∈C k

∑ 1 where the second term of (10.2) is zero due to ¯x k,j = x i′,j , the first and |Ck | i′ ∈C k ∑ 2 third terms in (10.2) share the same value (x i,j − ¯x k,j ), and its sum coincides i∈C k with the right-hand side of (10.1). From (10.1), we see that K-means clustering seeks the configuration that minimizes the squared sum of the distances of the sample pairs in the clusters.

---

<!-- Página 237 -->

232 10 Unsupervised Learning

10.2 Hierarchical Clustering

Hierarchical clustering is another commonly used clustering method. Initially, we construct N clusters, each of which contains only one sample. Then, based on a criterion, we merge two clusters in each stage until the number of clusters is two. For each of the stages k = N, N − 1, · · · , 2, one clustering exists. The clusters for k = N, N − 1, · · · , 2 can be obtained by returning the history of connections without determining the number of clusters K. We use the L2 norm for the distance d(·, ·) between samples. However, it is necessary to define the distance between clusters that contain multiple samples (which does not necessarily satisfy the axiom of distance). The frequently used definitions are listed in Table 10.1. The following procedure can be implemented for each of the complete, single, centroid, and average linkages. However, the input is given by a pair of matrices N×p x, y that extract multiple rows of X ∈ R. The distance between the clusters is the output.

def dist_complete(x,y): r=x.shape[0] s=y.shape[0] dist_max=0 for i in range(r): for j in range(s): d=np.linalg.norm(x[i,]-y[j,])**2 if d>dist_max: dist_max=d return dist_max

def dist_single(x,y): r=x.shape[0] s=y.shape[0] dist_min=np.inf for i in range(r): for j in range(s): d=np.linalg.norm(x[i,]-y[j,])**2 if d<dist_min: dist_min=d return dist_min

Table 10.1 Distance between clusters Linkage Definition Distance between clusters A and B Complete The maximum distance between the clusters maxd(xi , xj ) i∈A,j ∈B Single The minimum distance between the clusters mind(xi , xj ) i∈A,j ∈B ⎛⎞ 1∑1∑ Centroid The distance between the centers of the clusters d⎝ xi , xj⎠ |A||B| i∈Aj ∈B 1∑∑ Average The mean distance between the clusters d(xi , xj ) |A| · |B| i∈Aj ∈B

---

<!-- Página 238 -->

10.2 Hierarchical Clustering 233

def dist_centroid(x,y): r=x.shape[0] s=y.shape[0] x_bar=0 for i in range(r): x_bar=x_bar+x[i,] x_bar=x_bar/r y_bar=0 for i in range(s): y_bar=y_bar+y[i,] y_bar=y_bar/s return (np.linalg.norm(x_bar-y_bar)**2)

def dist_average(x,y): r=x.shape[0] s=y.shape[0] S=0 for i in range(r): for j in range(s): S=S+np.linalg.norm(x[i,]-y[j,])**2 return (S/r/s)

Furthermore, when the distance between such clusters is defined, the procedure of hierarchical clustering can be defined as follows. Given the distances between samples and between clusters, the clustering is obtained (a list called index), and the list that consists of such lists is called cluster. If two clusters i < j are connected, then cluster j is absorbed into cluster i, and j disappears. The indices j + 1 or larger are decreased by one, and the cluster k is deleted.

import copy

def hc(X,dd="complete"): n=X.shape[0] index=[[i] for i in range(n)] cluster=[[] for i in range(n-1)] for k in range(n,1,-1): # index_2=[] dist_min=np.inf for i in range(k-1): for j in range(i+1,k): i_0=index[i]; j_0=index[j] if dd=="complete": d=dist_complete(X[i_0,],X[j_0,]) elif dd=="single": d=dist_single(X[i_0,],X[j_0,]) elif dd=="centroid": d=dist_centroid(X[i_0,],X[j_0,]) elif dd=="average": d=dist_average(X[i_0,],X[j_0,]) if d<dist_min: dist_min=d i_1=i# list of index which would be combined j_1=j# list of index which would join index[i_1].extend(index[j_1])# add if j_1<k:# put the added index forward

---

<!-- Página 239 -->

234 10 Unsupervised Learning

for h in range(j_1+1,k,1): index[h-1]=index[h] index2=copy.deepcopy(index[0:(k-1)])# If you use "index" without deepcopy , "index" will be rewritten each time. cluster[k-2].extend(index2) return cluster# The results from below show that one by one, the congruence occurs.

Thus, clusterings of sizes k = n, n − 1, · · · , 2 are stored in cluster[[n]], cluster[[n-1]], . . . ,cluster[[2]].

Example 83 Hierarchical clustering was performed for artificially generated data with N = 100 and p = 2. Samples in the same cluster are shown in the same color. First, we changed the number of clusters K and output the results (Fig. 10.4).

K= 3K= 5 33 22 11 2 2 00 XX -1-1 -2-2 -3-3 -3 -2 -1 0 1 2 3-3 -2 -1 0 1 2 3 X1X1

K= 7K= 9 33 22 11 2 2 00 XX -1-1 -2-2 -3-3 -3 -2 -1 0 1 2 3-3 -2 -1 0 1 2 3 X1X1

Fig. 10.4 We execute hierarchical clustering (complete linkage) for artificial data with N = 200, p = 2 and K = 3, 5, 7, 9. The samples in the same cluster share the same color. Compared to k-means clustering, not all the samples belong to the cluster with the nearest center

---

<!-- Página 240 -->

10.2 Hierarchical Clustering 235

n=200; p=2 X=randn(n,p) cluster=hc(X,"complete") K=[2,4,6,8]# the number of clusters are 3,5,7 and 9. for i in range(4): grp=cluster[K[i]]# From the overall result, the result for K[i] is taken plt.subplot(2,2,i+1) for k in range(len(grp)): x=X[grp[k],0] y=X[grp[k],1] plt.scatter(x,y,s=5) plt.text(2,2,"K={}".format(K[i]+1),fontsize=12)

Next, we changed the definition of the distance between clusters (complete, single, average, and centroid) and output the results, as shown in Fig. 10.5. Samples in the same cluster are shown in the same color.

completesingle 33

22

11 2 2 00 XX -1-1

-2-2

-3-3 -3 -2 -1 0 1 2 3-3 -2 -1 0 1 2 3 X1X1

centroidaverage 33

22

11 2 2 00 XX -1-1

-2-2

-3-3 -3 -2 -1 0 1 2 3-3 -2 -1 0 1 2 3 X1X1

Fig. 10.5 Hierarchical clustering was performed for artificial data with N = 100, p = 2, and K = 7 for each complete, single, centroid, and average linkages. The most commonly used complete linkage appears to result in intuitively acceptable clustering

---

<!-- Página 241 -->

236 10 Unsupervised Learning

n=100; p=2; K=7 X=randn(n,p) i=1 for d in ["complete","single","centroid","average"]: cluster=hc(X,dd=d) plt.subplot(2,2,i) i=i+1 grp=cluster[K-1] for k in range(K): x=X[grp[k],0] y=X[grp[k],1] plt.scatter(x,y,s=5) plt.text(-2,2.1,"{}".format(d),fontsize=12)

Hierarchical clustering does not require the number of clusters K to be decided in advance. Compared to K-means clustering, in this case, the samples in each cluster are not close (Fig. 10.4). This result appears to be due to the phenomenon that hierarchical clustering is initially locally connected, and relatively distant samples were connected earlier after going to the higher layers. In addition, complete linkage is often used as a measure of the distance between clusters, depending on the application. The results in this case are closer to K-means clustering and are intuitively reasonable. The result of hierarchical clustering is represented by a dendrogram (tree diagram) (Fig. 10.6). The shorter the distance of the cluster is, the earlier the

centroidsingle

136282324101171915172527822141826291620302214591312191321032912266281516192320241452242171782711301825

completeaverage

129161882226301420421723172527611192410153512282913116814262922302219133104561923241517728112718251220

Fig. 10.6 Hierarchical clustering was executed for the artificial data with N = 30 and p = 3 using centroid, single, complete, and average linkages. The resulting dendrogram is displayed

---

<!-- Página 242 -->

10.2 Hierarchical Clustering 237

clusters are connected, which means that the distance tends to increase as the process proceeds. A tree is constructed so that the distance of the connected clusters is represented by the height of the branch at which they are connected. The higher we go, the fewer the branches. Then, for any 2 ≤ k ≤ N, there is a height with the number of branches being k. If we cut the dendrogram horizontally at one of the heights, we obtain the clustering. The samples under the k branches consist of the k clusters. However, when constructing a dendrogram, the samples in connected clusters should not cross, i.e., the branches should not intersect. It is necessary to arrange the samples at the lowest level so that this rule is not violated. For single linkage, although the distance between the clusters is small in the early stages, the distance often rapidly increases after the connections become higher. For centroid linkage, which is often used in biology-related fields, inversion occurs such that two clusters are connected later than more distant pairs (Fig. 10.7).

Example 84 Suppose that we apply centroid linkage to the samples (0, 0), (5, 8), (9, 0) with N = 3 and p = 2 (Fig. 10.8). Then, after the first connection, we obtain

1 cluster High 2 cluster Middle 3 cluster Low 4 cluster

Fig. 10.7 The height, the number of clusters, and the distance between clusters for hierarchical clustering. The cluster distance indicated by red is larger than those indicated by blue and green. In addition, there are k = 1, 2, 3, . . . branches at each height below the root of the tree, but the cluster that consists of samples under a branch constitutes a cluster

(5,8) √ 42 + 82 √ 2 2 4+ 8√ 2 2 7+ 4 √ (7,4)72 + 42

(0,0) (5,8) (9,0) 0 (9,0)

Fig. 10.8 Inversion for centroid linkage. The center of the blue cluster that connects (5, 8) and √√ (9, 0) (the shortest among the three edge lengths 89, 9, 80) is (7, 4). However, the distance of the red line between (0, 0) and (7, 4), which are connected later, is smaller. The dendrogram on the right displays the distance of connected clusters by the height of the branch: the red branch is lower than the branch of the already connected clusters, and they cross in the dendrogram

---

<!-- Página 243 -->

238 10 Unsupervised Learning

√√ 2 2 two clusters {(0, 0)} and {(5, 8), (9, 0)} with the cluster distance 4 + 8 = 80. √√ 2 2 The distance between the centers (0, 0) and (7, 4) is 7 + 4 = 65 in the next connection, which is smaller than the distance for the previous connection. This is an example of inversion, in which the branches cross in a dendrogram, as in Fig. 10.6 (lower left: centroid linkage).

However, no inversion occurs for complete, single, and average linkages: the later the connection is, the larger the distance between the connected clusters. In fact, from the definitions of the distances of clusters A and B for complete linkage in Table 10.1, because the two clusters to be connected have the largest cluster distance among the current clusters, no future cluster distance will be lower than the current distance. For single linkage, if clusters A and B connect and the pair A, B becomes a new cluster, the distance between the pair A, B and the other cluster C cannot be lowered. In fact, if such a phenomenon occurs, either A, C or B, C should have been connected prior to A, B, which contradicts the rule of single linkage to choose the clusters that minimize the minimum sample distance. Additionally, for average linkage, if the average distance between the pair A, B and the other cluster C is smaller than that between A and B, either the distance between A and C or that between B and C is smaller than that between A and B, which contradicts the rule of average linkage. We generate a dendrogram based on the considerations in this section and list the code in the Appendix of this chapter because it may be complicated to follow in the main text. The dendrogram in Fig. 10.6 is obtained via the program. Alternatively, we can use the function scipy.cluster.hierarchy pre- N×p pared for the Python language. For X ∈ R, via dist function, we obtain the matrix in which the distances among N samples with p variables are in the lower left positions. We specify the matrix and the option method = “complete”, “single”, “centroid”, “average”.

Example 85

from scipy.cluster.hierarchy import linkage,dendrogram

X=randn(20,2) i=1 for d in ["single","average","complete","weighted"]: res_hc=linkage(X,method=d) plt.subplot(2,2,i) i+=1 dendrogram(res_hc)

---

<!-- Página 244 -->

10.3 Principle Component Analysis 239

10.3 Principle Component Analysis

The principle component analysis (PCA) is the procedure used to obtain p vectors p φ1 ∈ Rwith ‖φ1‖ = 1 that maximizes ‖Xφ1‖, p φ2 ∈ Rwith ‖φ2‖ = 1 that is orthogonal to φ1 and maximizes ‖Xφ2‖, · · · , . . . p φp ∈ Rwith ‖φp ‖ = 1 that is orthogonal to φ1, · · · , φp−1 and maximizes ‖Xφp ‖. N×p from a data matrix X ∈ R(p ≤ N). Before performing the PCA, we often centralize the matrix X, i.e., we subtract the arithmetic mean x j of column j from each element x i,j , i = 1, · · · , N, j = 1, · · · , p. The purpose of PCA is to summarize the matrix X as φ1, · · · , φ m (1 ≤ m ≤ p): the smaller the m is, the more compressed the information in X. We note that there exists μ1 such that

T X Xφ1 = μ1φ1 . (10.3)

In fact, φ1 maximizes ‖Xφ1‖, and if we differentiate

2 2 L := ‖Xφ1‖− γ (‖φ1‖− 1)

2 with a Lagrange constant γ and set it equal to zero, we find ‖φ1‖= 1 and T X Xφ1 = γ φ1 . Although more than one μ1 may satisfy (10.3), from

2 TT 2 ‖Xφ1‖= φ X Xφ1 = μ1‖φ1‖= μ1, 1

we need to choose the largest μ1 . Additionally, for φ2 ,

T X Xφ2 = μ2φ2

T is required for some μ2 . Hence, φ2 is the eigenvector of X X as well. If we note that μ1 ≥ μ2 and that φ1 and φ2 are orthogonal, the possibility is either μ1 = μ2 (φ1 and φ2 are in the same eigenspace) or μ2 is the largest but μ1 . Moreover, they are nonnegative because they are eigenvalues of a nonnegative definite matrix. 1 T In the actual PCA formulation, we define := X X, replace N μ1/N, . . . , μ m /N by λ1, . . . , λN , and write (10.3) as

φ1 = λ1φ1,

where is the sample-based covariance matrix and λ1 ≥ · · · ≥ λp ≥ 0 are the eigenvalues. We choose the m principle components φ1, . . . , φ m with the largest variances λ1 ≥ · · · ≥ λm ≥ 0.

---

<!-- Página 245 -->

240 10 Unsupervised Learning

∑ k λkλi i=1 We say that ∑pand∑pare the proportion of the k-th principle λλ i=1 ii=1 i component and the accumulated proportion up to the k-th principle components, respectively. If the units of the p columns in X are different, we often need to scale X such that the result of PCA does not depend on the units. For example, if each column expresses the test score of math, English, science, etc., they may not have to be scaled, even if the variances are different. However, if each column expresses height, weight, age, etc., they may have to be scaled because if we replace centimeters, kilograms, and years by inches, pounds, and months, then the PCA produces significantly different results. If the dimension of an eigenspace is not one, the only constraints are that the basis is orthogonal and the length is one. However, if the dimension is one, the eigenvector is either a vector or its oppositely directed vector. When the matrix X is randomly generated, it is unlikely that more than one eigenvalue coincide, so we assume

λ1 > · · · > λm .

T Since is symmetric, we have λi  = λj ⇒ φ φ j = 0. Moreover, from i

TTTT λj φ φ j = φ φ j = φ φ i = λi φ φ j , i i j i

TT we have (λi − λj )φ φ j = 0, which means φ φ j = 0. We note that if we find the i i m largest eigenvalues and their eigenvectors, we do not have to check whether those eigenvectors are orthogonal. Using the Python language function np.linalg.eig, given the matrix X ∈ N×p Ras an input, we can construct the function pca that outputs the vectors with the elements λ1, . . . , λp and the matrix with the columns φ1, . . . , φ p.

def pca(X): n,p=X.shape center=np.average(X,0) X=X-center# Centralization by column Sigma=X.T@X/n lam,phi=np.linalg.eig(Sigma)# eigen values , eigen vectors index=np.argsort(-lam)# Sort by descending order lam=lam[index] phi=phi[:,index] return {’lam’:lam,’vectors’:phi,’centers’:center}

Even if we do not use the above function, the function PCA in the sklearn.decomposition is available for the Python language.

Example 86 We do not distinguish the two directions (a vector or its (−1) multiplication) of each of the principle component vectors, although they depend on the software.

---

<!-- Página 246 -->

10.3 Principle Component Analysis 241

X=randn(100,5) res=pca(X) res[’lam’]

array([110.53492367, 103.30322442, 94.67566385, 78.62762373, 71.98586376])

array([0.24075006, 0.22499909, 0.20620787, 0.17125452, 0.15678846])

res[’vectors’]

array([[ 0.1904871 , 0.86655739, 0.23631724, 0.34643019, -0.19218023], [ 0.65407668, 0.09134685, -0.59040129, -0.35265467, -0.30149701], [-0.13324667, -0.20604928, -0.50496326, 0.78034922, -0.27542008], [-0.5430764 , 0.44470055, -0.57750325, -0.22518257, 0.35084505], [ 0.47245286, -0.02278504, -0.08415809, 0.30978817, 0.82049853]])

res[’centers’]

from sklearn.decomposition import PCA

pca=PCA() pca.fit(X)# execute

PCA(copy=True, iterated_power=’auto’, n_components=None, random_state=None, svd_solver=’auto’, tol=0.0, whiten=False)

score=pca.fit_transform(X)# PC score ((rows: n, columns: PC score) score[0:5,]

array([[-0.20579722, 0.63537368, 1.20127757, -0.17642322, 0.08331289], [ 1.81876319, 0.7014673 , -0.76877222, 0.94195901, 1.32429876], [-1.64856653, 1.27063092, -1.36066169, -0.0763228 , -0.81823956], [-1.01126137, -0.21633468, 1.21589032, -0.54061369, 0.14468562], [-0.71078308, 0.74867317, 0.81140784, -0.45036742, -0.27535244]])

array([[ 0.1904871 , 0.65407668, -0.13324667, -0.5430764 , 0.47245286], [ 0.86655739, 0.09134685, -0.20604928, 0.44470055, -0.02278504], [ 0.23631724, -0.59040129, -0.50496326, -0.57750325, -0.08415809], [-0.34643019, 0.35265467, -0.78034922, 0.22518257, -0.30978817], [ 0.19218023, 0.30149701, 0.27542008, -0.35084505, -0.82049853]])

pca.mean_# it is same as above "centers"

array([-0.03670141, 0.03260174, 0.13786866, 0.00316844, -0.12808206])

We compute the proportions and the accumulated proportion in Fig. 10.9 (left).

---

<!-- Página 247 -->

242 10 Unsupervised Learning

4 1.01.0

0.80.82

0.60.6 0y 0.40.4 Proportions -2 0.20.2 Accumulated Proportion 0.00.0-4 1 3 51 3 5-4 -2 0 2 4 Principle ComponentsPrinciple Componentsx

Fig. 10.9 Proportions and their accumulated proportion (left) and the mutually orthogonal first and second principle components (right)

plt.plot(np.arange(1,6),evr) plt.scatter(np.arange(1,6),evr) plt.xticks(np.arange(1,6)) plt.ylim(0,1) plt.xlabel("principal component") plt.ylabel("contribution rate")

Text(0, 0.5, ’contribution rate’)

plt.plot(np.arange(1,6),np.cumsum(evr)) plt.scatter(np.arange(1,6),np.cumsum(evr)) plt.xticks(np.arange(1,6)) plt.ylim(0,1) plt.xlabel("principal component ") plt.ylabel("contribution rate")

Text(0, 0.5, ’contribution rate’)

Example 87 Given N observations (x1, y1), . . . , (x N , y N ), we wish to find the mutually orthogonal principle components φ1 and φ2 .

n=100; a=0.7; b=np.sqrt(1-a**2) u=randn(n); v=randn(n) x=u; y=u*a+v*b plt.scatter(x,y); plt.xlim(-4,4); plt.ylim(-4,4)

(-4, 4)

D=np.concatenate((x.reshape(-1,1),y.reshape(-1,1)),1) pca.fit(D)

PCA(copy=True, iterated_power=’auto’, n_components=None, random_state=None, svd_solver=’auto’, tol=0.0, whiten=False)

---

<!-- Página 248 -->

10.3 Principle Component Analysis 243

T=pca.components_ T[0,1]/T[0,0]*T[1,1]/T[1,0]# PC vectors are orthogonal

-1.0

def f_1(x): y=T[0,1]/T[0,0]*x return y

def f_2(x): y=T[1,1]/T[1,0]*x return y

x_seq=np.arange(-4,4,0.5) plt.scatter(x,y,c="black") plt.xlim(-4,4) plt.ylim(-4,4) plt.plot(x_seq,f_1(x_seq)) plt.plot(x_seq,f_2(x_seq)) plt.gca().set_aspect("equal",adjustable="box")

(-4.375, 3.875, -4.4445676982833735, 5.018060304513487)

Note that the product of the two lines is −1 (Fig. 10.9, right).

Using the obtained φ1, . . . , φ m and their projections z1 = Xφ1, . . . , zm = Xφ m, we can see the N data projected on the m-dimensional space, and the function biplot is available for this purpose.

Example 88 A dataset containing the numbers of arrests for four crimes in all fifty states is available. We scale the data so that the four variances are equal, execute PCA, and plot the first and second principle components. The function like biplot in R is not available in the Python language for this purpose, so we make the function. Because we project the data onto two dimensions, our analysis considers the first two components (m = 2). If we multiply the first and second principle components by −1, we obtain principle component vectors that have the same variance but the opposite direction and projection values (Fig. 10.10)

import pandas as pd

USA=pd.read_csv(’USArrests.csv’,header=0,index_col=0) X=(USA-np.average(USA,0))/np.std(USA,0) index=USA.index col=USA.columns pca=PCA(n_components=2) pca.fit(X) score=pca.fit_transform(X) vector=pca.components_ vector

---

<!-- Página 249 -->

244 10 Unsupervised Learning

Fig. 10.10 Using the function biplot, we project the data on the crimes in the fifty states on the first and second components

array([[ 0.53589947, 0.58318363, 0.27819087, 0.54343209], [ 0.41818087, 0.1879856 , -0.87280619, -0.16731864]])

vector.shape[1]

4

evr=pca.explained_variance_ratio_ evr

array([0.62006039, 0.24744129])

plt.figure(figsize=(7,7)) for i in range(score.shape[0]): plt.scatter(score[i,0],score[i,1],s=5) plt.annotate(index[i],xy=(score[i,0],score[i,1])) for j in range(vector.shape[1]): plt.arrow(0,0,vector[0,j]*2,vector[1,j]*2,color="red")# 2 is the length of the line, you can choose arbitrary. plt.text(vector[0,j]*2,vector[1,j]*2,col[j],color="red")

The principal component analysis is used to reduce the dimensionality of multivariate data. The clustering learned in the previous section cannot be displayed unless the data are two-dimensional. A possible method is to display samples after reducing the space to two dimensions via principal component analysis. Example 89 We display the output of the K-means clustering of the Boston data as a two-dimensional principal component (Fig. 10.11). Since the data are projected in two dimensions, when viewed as a two-dimensional graph, it does not appear that close samples consist of a cluster.

---

<!-- Página 250 -->

10.3 Principle Component Analysis 245

Fig. 10.11 We projected theClustering for Boston Data K-means clustering results of the Boston data on the first and second components100

0

-100

-200Second Component

-200 -100 0 100 200 300 First Component

from sklearn.datasets import load_boston from sklearn.cluster import KMeans

Boston=load_boston() Z=np.concatenate((Boston.data,Boston.target.reshape(-1,1)),1) K_means=KMeans(n_clusters=5) K_means.fit(Z) y=K_means.fit_predict(Z)# predict which cluster pca.fit(Z) W=pca.fit_transform(Z)[:,[0,1]]# The first and second principal components for each n plt.scatter(W[:,0],W[:,1],c=y) plt.xlabel(" first PC component") plt.ylabel(" second PC component") plt.title(" clustering with Boston data")

Text(0.5, 1.0, ’clustering with Boston data’)

There is another equivalent definition of PCA. Suppose we centralize the matrix N×p N×p p×m X ∈ Rand let x i be the i-th row vector of X ∈ Rand  ∈ Rbe vectors such that the columns φ1, . . . , φ m have unit length and are mutually orthogonal. m Then, we obtain the projections z1 = x1, . . . , zN = x N  ∈ R(row vectors) from x1, . . . , x N to φ1, . . . , φ m. We evaluate how close the recovered vectors are to the original x1, . . . , x N by

N ∑ T 2 L :=‖x i − x i  ‖, (10.4) i=1

T which is obtained by multiplying z1, . . . , zN by  from the right. If m = p, the value of (10.4) is zero. We may regard PCA as the problem of finding φ1, . . . , φ m

---

<!-- Página 251 -->

246 10 Unsupervised Learning

that minimize (10.4). In fact, we have the following two equations:

NN ∑∑ T 2 2 T T T T T ‖x i − x i  ‖={‖x i ‖− 2x i (x i  ) + (x i  )(x i  ) } i=1i=1

NNN ∑∑∑ 2 T T2 2 ={‖x i ‖− x i  x } =‖x i ‖−‖x i ‖ i i=1i=1i=1 ⎡⎤ { }xφ NNmmNm1jm ∑∑∑∑∑∑⎢⎥∑ 2 2 2.2 2 ‖x i ‖=(x i φ j )=(x i φ j )=‖⎢.⎥‖=‖Xφ j ‖. ⎣.⎦ i=1i=1j=1j=1i=1j=1j=1 x N φ j

T In other words, if λ1, . . . , λm are the largest m eigenvalues of = X X/N, the NNm ∑∑∑ T 2 2 value‖x i − x i  ‖takes the minimum value‖x i ‖−λj by the m i=1i=1j =1 largest eigenvalues whose eigenvectors are φ1, . . . , φ m. In addition to PCA and linear regression, we may use principle component N×m regression: find the matrix Z = X ∈ Rthat consists of the m principle m 2 components via PCA, find θ ∈ Rthat minimizes ‖y − Zθ ‖, and display via ˆθ the relation between the response and m components (a replacement of the p covariates). Principle component regression regresses y on the columns of Z instead of those of X. T −1T For m = p,  ˆθ and ˆβ = (X X)X y coincide. In fact, since minβ ‖y − 2 2 2 Xβ‖≤ minθ ‖y − Xθ ‖= minθ ‖y − Zθ‖, the matrix  is nonsingular when p p = m. Thus, for arbitrary β ∈ R, there exists a θ such that β = θ . For example, we may construct the following program:

def pca_regression(X,y,m): pca=PCA(n_components=m) pca.fit(X) Z=pca.fit_transform(X)# rows:n , columns:PC score phi=pca.components_# rows : PC , columns : variables theta=np.linalg.inv(Z.T@Z)@Z.T@y beta=phi.T@theta return {’theta’:theta,’beta’:beta}

Example 90 We execute the function pca_regression:

n=100; p=5 X=randn(n,p) X=X-np.average(X,0) y=X[:,0]+X[:,1]+X[:,2]+X[:,3]+X[:,4]+randn(n) y=y-np.mean(y) pca_regression(X,y,3)

---

<!-- Página 252 -->

Appendix: Program 247

{’beta’: array([1.33574835, 0.45612768, 0.6710805 , 0.28063559, 0.97748932]), ’theta’: array([ 0.41755766, 0.19389454, -1.80690824])}

pca_regression(X,y,5)[’beta’]

array([0.86513279, 1.01698307, 0.7496746 , 0.91010065, 1.12420093])

np.linalg.inv(X.T@X)@X.T@y

array([0.86513279, 1.01698307, 0.7496746 , 0.91010065, 1.12420093])

Appendix: Program

A program generates the dendrogram of hierarchical clustering. After obtaining the cluster object via the function hc, we compare the distances between consecutive clusters using the ordered sample y. Specifically, we express the positions of the branches by z[k, 1], z[k, 2], z[k, 3], z[k, 4], and z[k, 5].

import matplotlib.pyplot as plt import matplotlib.collections as mc import matplotlib.cm as cm

def unlist(x): y=[] for z in x: y.extend(z) return(y)

def hc_dendroidgram(cluster,dd="complete",col="black"): y=unlist(cluster[0]) n=len(y) z=np.zeros([n,5]) index=[[y[i]] for i in range(n)] height=np.zeros(n) for k in range(n-1,0,-1): dist_min=np.inf for i in range(k): i_0=index[i]; j_0=index[i+1] if dd=="complete": d=dist_complete(X[i_0,],X[j_0,]) elif dd=="single": d=dist_single(X[i_0,],X[j_0,]) elif dd=="centroid": d=dist_centroid(X[i_0,],X[j_0,]) elif dd=="average": d=dist_average(X[i_0,],X[j_0,]) if d<dist_min: dist_min=d i_1=i# list of index which would be combined

---

<!-- Página 253 -->

248 10 Unsupervised Learning

j_1=j# list of index which would join # below, calculate the position of the line segments i=0 for h in range(i_1): i=i+len(index[h]) z[k,0]=i+len(index[i_1])/2 z[k,1]=i+len(index[i_1])+len(index[j_1])/2 z[k,2]=height[i_1] z[k,3]=height[j_1] z[k,4]=dist_min index[i_1].extend(index[j_1]) if j_1<k:# put the added index forward for h in range(j_1,k): index[h]=index[h+1] height[h]=height[h+1] height[i_1]=dist_min height[k]=0 # Loop ends here. lines=[[(z[k,0],z[k,4]),(z[k,0],z[k,2])] for k in range(1,n)]# Vertical line segment (left) lines2=[[(z[k,0],z[k,4]),(z[k,1],z[k,4])] for k in range(1,n)]# Horizontal line segment (center) lines3=[[(z[k,1],z[k,4]),(z[k,1],z[k,3])] for k in range(1,n)]# Vertical line segment (right) lines.extend(lines2) lines.extend(lines3) lc=mc.LineCollection(lines,colors=col,linewidths=1) fig=plt.figure(figsize=(4,4)) ax=fig.add_subplot() ax.add_collection(lc) ax.autoscale() plt.show() fig=plt.figure(figsize=(4,4))

n=100; p=2; K=7 X=randn(n,p) cluster=hc(X,dd="complete") hc_dendroidgram(cluster,col="red")

Exercises 88–100

88. The following procedure divides N samples with p variables into K disjoint sets, given K (K-means clustering). We repeat the following two steps after randomly assigning one of 1, . . . , K to each sample:

(a) Compute the centers of clusters k = 1, . . . , K. (b) To each of the N samples, assign the nearest center among the K clusters. Fill in the blanks and execute the procedure.

def k_means(X,K,iteration=20): n,p=X.shape center=np.zeros((K,p)) y=np.random.choice(K,n,replace=True) scores=[]

---

<!-- Página 254 -->

Exercises 88–100 249

for h in range(iteration): for k in range(K): if np.sum(y==k)==0: center[k,0]=np.inf else: for j in range(p): center[k,j]=# blank(1) # S_total=0 for i in range(n): S_min=np.inf for k in range(K): S=np.sum((X[i,]-center[k,])**2) if S<S_min: S_min=S # blank(2) # S_total+=S_min scores.append(S_total) return {’clusters’:y,’scores’:scores}

n=1000; K=5; p=2 X=randn(n,p)# data generation y=k_means(X,5)[’clusters’]# getting cluster for each sample plt.scatter(X[:,0],X[:,1],c=y) plt.xlabel("first component") plt.ylabel("second component")

89. The clusters that K-means clustering generates depend on the randomly cho- sen initial values. Repeat ten times to find the sequence of values immediately after the 2-step update. Display each transition as a line graph on the same graph. 90. K-means clustering minimizes

Kp ∑1∑∑∑ 2 S :=(x i,j − x i′,j ) |Ck | k=1i∈C ki′ ∈C kj =1

w.r.t. C1, . . . , CK from data X = (x i,j ).

(a) Show the following equation:

pp 1∑∑∑∑∑ 2 2 (x i,j − x i′,j )= 2 (x i,j − ¯x k,j ). |Ck | i∈C ki′ ∈C kj =1i∈C kj =1

(b) Show that the score S is monotonously decreasing each time the two steps are executed in Problem 88. (c) Let N = 3, p = 1, and K = 2, and assume that the samples are in 0, 6, 10. We consider two cases: one and two are assigned to 0, 6 and 10, respectively, and one and two are assigned to 0 and 6, 10, respectively. What values do they converge to if the initial state is each of the two cases? What score do they finally obtain?

---

<!-- Página 255 -->

250 10 Unsupervised Learning

91. Write Python codes for the functions dist_complete, dist_single, dist_centroid, and dist_average to find the maximum distance between the rows in x, y, the minimum distance between the rows in x, y, the distance between the centers of x, y, and the average distance between the rows in x, y, given matrices x and y composed of multiple rows extracted N×p from X ∈ R. 92. The following procedure executes hierarchical clustering w.r.t. data p x1, . . . , x N ∈ R. Initially, each cluster contains exactly one sample. We merge the clusters to obtain a clustering with any number K of clusters. Fill in the blanks and execute the procedure.

import copy def hc(X,dd="complete"): n=X.shape[0] index=[[i] for i in range(n)] cluster=[[] for i in range(n-1)] for k in range(n,1,-1): # index_2=[] dist_min=np.inf for i in range(k-1): for j in range(i+1,k): i_0=index[i]; j_0=index[j] if dd=="complete": d=dist_complete(X[i_0,],X[j_0,]) elif dd=="single": d=dist_single(X[i_0,],X[j_0,]) elif dd=="centroid": d=dist_centroid(X[i_0,],X[j_0,]) elif dd=="average": d=dist_average(X[i_0,],X[j_0,]) if d<dist_min: # blank(1) # i_1=i# list of index which would be combined j_1=j# list of index which would join index[i_1].extend(index[j_1])# add if j_1<k:# put the added index forward for h in range(j_1+1,k,1): index[h-1]=# blank(2) # index2=copy.deepcopy(index[0:(k-1)])# If you use "index" without deepcopy , "index" will be rewritten each time. cluster[k-2].extend(index2) return cluster# The results from below show that one by one, the congruence occurs.

93. In hierarchical clustering, if we use centroid linkage, which connects the clusters with the smallest value of dist_centroid, inversion may occur, i.e., clusters with a smaller distance can be connected later. Explain the phenomenon for the case (0, 0), (5, 8), (9, 0) with N = 3 and p = 2. T N×p 94. Let = X X/N for X ∈ R, and let λi be the i-th largest eigenvalue in .

2 N (a) Show that the φ that maximizes ‖Xφ‖among φ ∈ Rwith ‖φ‖ = 1 satisfies φ = λ1φ. (b) Show φ1, . . . , φ m such that φ1 = λ1φ1, . . . , and φ m = λm φ m are orthogonal when λ1 > · · · > λm.

---

<!-- Página 256 -->

Exercises 88–100 251

95. Using the np.linalg.eig function in the Python language, write a Python program pca that outputs the average of the p columns, the eigenvalues N×p λ1, . . . , λp , and the matrix that consists of φ1, . . . , φ p , given input X ∈ R. Moreover, execute the following to show that the results obtained via PCA in sklearn.decomposition coincide:

X=randn(100,5) res=pca(X) res[’lam’] res[’vectors’] res[’centers’]

from sklearn.decomposition import PCA

pca=PCA() pca.fit(X)# execute score=pca.fit_transform(X)# PC score ((rows: n, columns: PC score) score[0:5,] pca.mean_# it is same as above "centers"

96. The following procedure produces the first and second principle component vectors φ1 and φ2 from N samples (x1, y1), . . . , (x N , y N ). Fill in the blanks and execute it.

n=100; a=0.7; b=np.sqrt(1-a**2) u=randn(n); v=randn(n) x=u; y=u*a+v*b plt.scatter(x,y); plt.xlim(-4,4); plt.ylim(-4,4) D=np.concatenate((x.reshape(-1,1),y.reshape(-1,1)),1) pca.fit(D) T=pca.components_ T[1,0]/T[0,0]*T[1,1]/T[0,1]# PC vectors are orthogonal

-1.0

def f_1(x): y=# blank(1) # return y

def f_2(x): y=T[1,1]/T[1,0]*x return y

x_seq=np.arange(-4,4,0.5) plt.scatter(x,y,c="black") plt.xlim(-4,4) plt.ylim(-4,4) plt.plot(x_seq,f_1(x_seq)) plt.plot(x_seq,# blank(2) #) plt.gca().set_aspect("equal",adjustable="box")

---

<!-- Página 257 -->

252 10 Unsupervised Learning

Moreover, show that the product of the slopes is −1. 97. There is another equivalent definition of PCA. Suppose that we have central- N×p N×p ized the matrix X ∈ R, and let x i be the i-th row vector of X ∈ R p×m and  ∈ Rbe the matrix that consists of the mutually orthogonal vectors φ1, . . . , φ m of unit length. Then, we can obtain the projection z1 = m x1, . . . , zN = x N  ∈ Rof x1, . . . , x N on φ1, . . . , φ m. We evaluate ∑ NT 2 how the x1, . . . , x N are recovered by L := ‖x i − x i  ‖, which i=1 T is obtained by multiplying z1, . . . , zN by  from the right. We can regard PCA as the problem of finding φ1, . . . , φ m that minimize the value. Show the two equations:

NNN ∑∑∑ T 2 2 2 ‖x i − x i  ‖=‖x i ‖−‖x i ‖ i=1i=1i=1

Nm ∑∑ 2 2 ‖x i ‖=‖Xφ j ‖. i=1j =1

98. We prepare a dataset containing the numbers of arrests for four crimes in all fifty states.

import pandas as pd

USA=pd.read_csv(’USArrests.csv’,header=0,index_col=0) X=(USA-np.average(USA,0))/np.std(USA,0) index=USA.index col=USA.columns pca=PCA(n_components=2) pca.fit(X) score=pca.fit_transform(X) vector=pca.components_ vector vector.shape[1] evr=pca.explained_variance_ratio_ evr

plt.figure(figsize=(7,7)) for i in range(score.shape[0]): plt.scatter(# blank(1) #,# blank(2) #,s=5) plt.annotate(# blank(3) #,xy=(score[i,0],score[i,1])) for j in range(vector.shape[1]): plt.arrow(0,0,vector[0,j]*2,vector[1,j]*2,color="red")# 2 is the length of the line, you can choose arbitrary. plt.text(vector[0,j]*2,vector[1,j]*2,col[j],color="red")

---

<!-- Página 258 -->

Exercises 88–100 253

Fill in the blanks and execute the following code: λk 99. The proportions and accumulated proportion are defined by ∑pand λ j =1 j ∑ m λ k=1 k ∑pfor each 1 ≤ m ≤ p. Fill in the blanks and draw the graph. λ j =1 j

res[’lam’]/np.sum(res[’lam’])# Contributions of each principal component

evr=pca.explained_variance_ratio_# evr

plt.plot(np.arange(1,6),evr) plt.scatter(np.arange(1,6),evr) plt.xticks(np.arange(1,6)) plt.ylim(0,1) plt.xlabel("principal component ") plt.ylabel("contribution rate")

plt.plot(np.arange(1,6),np.cumsum(evr)) plt.scatter(np.arange(1,6),np.cumsum(evr)) plt.xticks(np.arange(1,6)) plt.ylim(0,1) plt.xlabel("principal component ") plt.ylabel("contribution rate")

100. In addition to PCA and linear regression, we may use principle component N×m regression: find the matrix Z = X ∈ Rthat consists of the m principle m 2 components obtained via PCA, find θ ∈ Rthat minimizes ‖y − Zθ‖, and display via ˆθ the relation between the response and m components (a replacement of the p covariates). Principle component regression regresses y on the columns of Z instead of those of X. T −1T Show that  ˆθ and β = (X X)X y coincide for m = p. Moreover, fill in the blanks and execute it.

def pca_regression(X,y,m): pca=PCA(n_components=m) pca.fit(X) Z=pca.fit_transform(X)# rows:n, columns: PCscore phi=pca.components_# rows:PC, columns: variables theta=# blank # beta=phi.T@theta return {’theta’:theta,’beta’:beta}

2 2 2 Hint: Because minβ ‖y − Xβ‖≤ minθ ‖y − Xθ ‖= minθ ‖y − Zθ‖, it is sufficient to show that there exists θ such that β = θ for an arbitrary p β ∈ Rwhen p = m.

---

<!-- Página 259 -->

# Index

ADual problem, 203, 205, 209 Accumulated proportion, 240, 241 Adjusted coefficient of determination, 34, 37, 96, 98E Akaike’s information criterion (AIC), 95, 96,Effective degrees of freedom, 147 98, 100, 107Efficient estimator, 100, 101 AUC, 67Entropy, 181 Average linkage, 235Epanechnikov kernel, 150 Error probability, 181 ESS, 35 B Back-fitting, 154 Bagging, 185 F Bayesian information criterion (BIC), 95, 96, False negative, 67 98 False positive, 67 Boosting, 189 False positive rate, 67 Bootstrap, 85, 86 Fisher information matrix, 100–102 Bootstrapping, 89 Fitness, 95, 98 Branch node, 171

G C Gini index, 181 Centroid linkage, 237 Gradient boosting, 192 Coefficient of determination, 34, 36, 37, 96 Complete linkage, 234 Confidence interval, 39, 85, 115, 127 H Convex, 118 Hat matrix, 26 Convex function, 118, 119 Hierarchical clustering, 233, 236, 237, 247 Correlation coefficient, 36 Hypothesis testing, 30 Cramér-Rao inequality, 100, 102 Cross-validation, 77, 78, 82, 126, 173, 191 I Information criterion, 95 D Interior node, 171 Decision tree, 171, 181 Inversion, 237 Dendrogram, 236, 238, 247

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2021255 J. Suzuki, Statistical Learning with Math and Python, https://doi.org/10.1007/978-981-15-7877-9

---

<!-- Página 260 -->

256 Index

KQ K-nearest neighbor, 65Quadprog, 207 Karush–Kuhn–Tucker (KKT), 204Quadratic discrimination, 62 Kernel, 148, 149 K-means clustering, 230 Kullback-Leibler, 103, 105R Radical kernel, 213 Random forest, 187 LReceiver operating characteristic (ROC), 68 L1 norm, 121Ridge, 115, 121, 124 L1 regularization, 125ROC curve, 67 L2 norm, 121Root, 171 L2 regularization, 125RSS, 26–28, 32, 96, 125 Lasso, 124, 126 Least squares, 19, 22, 25, 41 S Linear discrimination, 62 Schwarz’s inequality, 105 Linear regression, 19, 77, 78, 80, 81, 85, Separable, 200 115 Sherman-Morrison-Woodbury, 82 Local linear regression, 148, 151 Significance level, 30 Logistic regression, 54, 60 Simplicity, 95, 98 LOOCV, 81 Single linkage, 237 Single regression, 22, 36 Smoothing spline, 144, 145, 154 M Sparse, 115 Margin, 200, 201 Spline curve, 141 Maximum likelihood, 55, 59, 60 Spline function, 137, 138 Maximum posterior probability, 64 Spline regression, 138, 140 Multiple regression, 23 Subderivative, 118, 119 Supervised learning, 227 Support vector, 200, 201 N Support vector machine, 199, 202, 210, 212 Nadaraya-Watson estimator, 149, 150 Natural spline, 140, 142, 144, 153, 158 Newton–Raphson method, 56 T Neyman–Pearson criterion, 67 Terminal node, 171 Nonnegative definite, 15 True negative, 67 Null hypothesis, 30, 35 True positive, 67 TSS, 36 Type I Error, 66 O Type II Error, 66 Overfitting, 79, 80

U PUnbiased, 26 Polynomial kernel, 210Unbiased estimate, 102, 105 Positive definite, 15Unbiased estimator, 100 Posterior probability, 61Unsupervised learning, 227 Power, 67 Prediction interval, 40 Primary problem, 203, 204, 209V Principal component analysis (PCA), 239Vandermonde’s determinant, 5 Principle component regression, 246Vandermonde’s matrix, 135 Prior probability, 61, 62Variable selection, 106 Proportion, 240, 241VIF, 38