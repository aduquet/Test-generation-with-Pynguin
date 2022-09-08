Abstract
=========
- In this paper, previous work is extended to support more aspects of PYTHON language.
- Other algorithms are also studied - DynaMOSA,MIO and MOSA
- Improved regression assertion generation and evaluated
- Evolutionary algorithms outperform Random test generation
- DynaMOSA like for Java yields better coverage in Pyhton
- But other remaining issues - like type information still linger and have impact on the effectiveness of the algorithms

Intro
===========
- Past  techniques enable the automated generation of unit tests for statically typed programming languages, such as Java, and remove the burden of the potentially tedious task of writing unit
tests from the programmer

- Due to the recent popularity of Dynamic typed languages(PYTHON), TCG in these languages have become imminent.
- But lack of static types is particularly problematic for automated test generation, which requires type information to provide appropriate parameter types for method calls or to assemble complex objects.
- TCG can only guess.
- To overcome this limitation, existing test generators for dynamically typed languages often do not target test-generation for general APIs, but resort to other means such as using the document object
model of a web browser to generate tests for JavaScript

- PYNGUIN : takes a Python module as input together with the module’s dependencies, and aims to automatically generate unit tests that maximise code coverage. Previously used algorithms: Whole-suite & Feedback- directed Random. Empirical study results:  empirical evaluation showed that the whole-suite approach is able to achieve higher code coverage than random testing

- IN THIS PAPER : 
    - implemented further test generation algorithms: MOSA, DynaMOSA, MIO
    - compare the performance of all algorithms in terms of resulting branch coverage
    - furthermore enlarge the corpus of subjects for test generation to get a broader insight into test generation for Python
    - implemented the generation of regression assertions based on mutation testing

- FINDINGS: 
    - similar to prior findings on Java, DynaMOSA and MOSA perform best on Python code, with a median of 80:7 % branch coverage.
    - type information is an important contributor to coverage on all studied test-generation algorithms
    - these results also suggest there are other open challenges for future research, such as dealing
    with type hierarchies and constructing complex objects