## Abstract
=========
- In this paper, previous work is extended to support more aspects of PYTHON language.
- Other algorithms are also studied - DynaMOSA,MIO and MOSA
- Improved regression assertion generation and evaluated
- Evolutionary algorithms outperform Random test generation
- DynaMOSA like for Java yields better coverage in Pyhton
- But other remaining issues - like type information still linger and have impact on the effectiveness of the algorithms

## Intro
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

- Background:
    - The main approaches to automatically generate unit tests are either by creating random sequences, or by applying meta-heuristic search algorithms.
        - Random test generation would typically generate tests in a forward way.
        - An alternative approach, for example applied during the mutation step of an evolutionary test generator, is to select necessary calls in a backwards fashion.
        - In both scenarios, type information is crucial: In the forward construction type information is used to inform the choice of call to append to the sequence, while in the backward construction type information is used to select generators of dependency objects.

## Unit Test Generation with Pynguin
=====================================

- THE FRAMEWORK:

    - PYNGUIN takes as input a Python module and allows the generation of unit tests using different techniques.
    - For details about the process that PYNGUIN uses refer the [Tool Paper](https://arxiv.org/pdf/2202.05218.pdf)
    - Pynguin comes with a variety of well-received test-generation algorithms

- THE ALGORITHMS: 

    - Feedback-Directed Random Test Generation:
        - Adopted from RANDOOP
        -Test cases that do not raise an exception are added to the passing test suite; otherwise they are added to the failing test suite.
        - PYNGUIN's version only differs: 
            - the algrithm does not check for contract violations.
            - Doesn't require users to provide a list of relavent classes, functions and methods.
            - Does not use a fitness func to guide its random search process
            - Checks the coverage of the generated test suite
    
    - Whole suite test generation:
        - implements a monotic genetic algorithm that takes a test suite, that is a set of test cases, as an individual 
        - the sum of all branch distances as a fitness function.
    
    - MOSA:
        - Designed to foster branch coverage, overcomes limitation of WS
        - Each branch is assigned its individual objective function, in contrast with WS (combined the obejctives into one single value)
        - Earlier many-objective genetic algos suffered dominance resistance problem i.e. the exponential increase of non-dominated solutions with the number of goals to optimize
        - Tackled by prefrence criterion: choose optimization targets to focus the search on the still relevant targerts(the yet uncovered branches)
        - Also has ARCHIVE: storage for already found solutons and is built to automatically prefer shorter test cases.
    
    - DynaMOSA:
        - dynamically selects targets for optimization
        - To compute the control dependencies within Pynguin, we generate a control-flow graph from the module under test’s byte code using the bytecode7 library; we use standard algorithms to compute post-dominator tree and control-dependence graph from the control-flow graph 

    - MIO:
        - MIO was designed with the aim of overcoming some intrinsic limitations of the Whole Suite or MOSA algorithms that arise especially in system-level test generation
        - It furthermore turns out that exploration is good at the beginning of the search whereas a focused exploitation is beneficial for better results in the end; MIO addresses this insight by a dynamic exploration/exploitation control. Lastly, again addressing the large number of objectives and limited resources, MIO selects the objectives to focus its search on by using a feedback-directed sampling technique. 

- Problem Representation:

    - As the unit for unit test generation, we consider Python modules.
    - For each statement sj in a test case ti we assign one value v(sj) with type τ(v(sj)) 2 T , with the finite set of types T used in the subject-under-test (SUT) and the modules transitively imported by the SUT
    -  A set of test cases form a test suite.
    - Primitive statements represent int, float, bool, bytes and str variables,
    - Constructor statements create new instances of a class, for example, var_0 = SomeType().
    - Method statements invoke methods on objects, for example, var_1 = var_0.foo().
    - Collection statements create new collections,(*****NEW*******)
    - We improved our representation of statements with parameters, by (1) passing parameters in the correct way, that is, positional or by keyword, and (2) leaving optional parameters empty with some probability


- TEST CLUSTER:
    -  set of available functions and classes along with their methods and constructors.
    - recursively includes all imports from other modules, starting from the subject under test. The test cluster also includes all primitive types as well as Python’s built-in collection types, that are, List, Set, Dict, and Tuple
    - Uses INSPECT module from standard Python API
    - The resulting test cluster basically consists of two maps and one set
    - The set stores: info of all callable and accessible elements which used to select elements in SUT during TCG
    - THE TWO MAPS:  stoer info about which callable and accessible elements can generate a specific type or modify it.
    - Pynguin uses these two maps to generate or modify specific types, if needed

- Operators for the Genetic Algorithms: 

    - Genetic algorithms encode a solution to the problem as an individual, called chromosome; a set of individuals is called population.
    - Genetic Operations: 
        - Crossover merges genetic material from at least two individuals into a new offspring, while mutation independently changes the elements of an individual. Selection is being used to choose individuals for reproduction that are considered better with respect to some fitness criterion 
        - Generic types currently cannot be handled properly in Pynguin, only Python’s collection types are addressed. A parameter that has no type annotation or the annotation Any, requires us to consider all available types in the test cluster as potential candidates. For those, we can only randomly pick an element from the test cluster

- Covering and Tracing Python Code:

    - Everything executable in Python is represented as a code object.
    - Code objects which contain branches do not have to be considered as individual coverage targets, since covering one of their branches also covers the respective code object.
    - Branch distance is a heuristic to determine how far a predicate is away from evaluating to true or false, respectively. In contrast to previous work on Java, where most predicates at the bytecode level operate only on Boolean or numeric values, in our case the operands of a predicate can be any Python object.


- Fitness Functions:

    - The fitness function required by genetic algorithms is an estimate of how close an individual is towards fulfilling a specific goal.
    - fitness function for Whole Suite, which operates on the test-suite level, and the fitness function for DynaMOSA, MIO, and MOSA, which operates on the test-case level.
    - The Test-suite Fitness fitness function estimates how close a test suite is to covering all branches of the SUT. Thus, every predicate has to be executed at least twice, which we enforce in the same way as existing work
    -  Test-case Fitness DynaMOSA, MIO, and MOSA consider individual coverage goals. Such a goal is to cover either a certain branch-less code object

- Assertion Generation:
    
    - Pynguin aims to generate regression assertions (Xie 2006) within its generated test cases based on the values it observes during test-case execution.
    - assertable: enum values, builtin types (int, str, bytes, bool, and None), as well as builtin collection types (tuple, list, dict, and set) as long as they only consist of assertable elements.
    - For non-assertable collections, Pynguin creates an assertion on their size by calling the len function on the collection and assert for that size. As a fallback, if none of the aforementioned strategies is successful, Pynguin is asserting that an object is not None.
    - To generate Assertions: 
        - First, Pynguin executes every test case twice in random order. We do this to remove trivially flaky assertions,
        - To minimise the set of assertions (Fraser and Zeller 2012) to those that are likely to be relevant to ensure the quality of the current test case, Pynguin utilises a customised fork of MutPy9 to generate mutants of the module under test.
        - From the previous executions, Pynguin knows the result of each test case. It then executes all test cases against all mutants. If the outcome for one test case differs on a particular mutant between the original module and that mutant, the mutant is said to be killed; otherwise it is classified as survived.

- Limitations of Pynguin:
    
    - Does not isolate the test executions properly in all cases.
    - Fails on modules with calls to file system access like sys.exit()
    - Dynamic features of Python as a language
    - Suporting all features of Python and also new versions bring new challenges
    - Generators, iterators,decorators,coroutines or higher-order functions challenges
    - The ability to implement modules in C/C++ and gets compiles to native binaries without any abstract syntax tree, without which PYNGUIN struggles in it.
    - The lack of built-in support in python to deccide at runtime whether one is a subtype of another.


- Empirical Evaluation

    - A crucial metric to measure the quality of a test suite is the coverage value it achieves; a test suite cannot reveal any faults in parts of the subject under test (SUT) that are not executed at all. Therefore, achieving high coverage is an essential property of a good test suite.
    - we aim to determine whether these previous findings on the performance of test generation techniques also generalise to Python with respect to coverage:
        - Research Question 1 (RQ1) How do the test-generation approaches compare on Python code?
        - Research Question 2 (RQ2) How does the availability of type information influence test generation?
        - Research Question 3 (RQ3) How effective are the generated assertions at revealing faults?

- Evaluation Metrics

    - We use code coverage to evaluate the performance of the test generation in RQ1 and RQ2 which is defined as the number of covered, that is, executed ranches in the subject under test divided by the total number of branches in the subject under test. We also keep track of coverage over time to shed light on the speed of convergence of the test-generation process; besides, we note the final overall coverage.
    - To evaluate the quality of the generated assertions in RQ3 we compute the mutation score.
    - A mutant is a variant of the original subject under test obtained by injecting artificial modifications into them. It is referred to as killed if there exists a test that passes on the original subject under test but fails on the mutated subject under test.
    - The mutation score is defined as the number of killed mutants divided by the total number of generated mutants

    - In terms of coverage, the null hypothesis states that none of the compared algorithms reaches significantly higher coverage; the alternative hypothesis states that one of the algorithms reaches significantly higher coverage values.

- Threats to Validity

    - Internal Validity:
        - The standard coverage tool for Python is Coverage.py. It, however, measures branch coverage by comparing the transitions between sources lines that have occurred and that are possible. Measuring branch coverage using this technique is possibly imprecise.
        - implemented the computation of mutation scores ourselves. the mutation of the subject under test itself is done using a customised version of the MutPy mutation testing tool 
        - the mutation of the subject under test itself is done using a customised version of the MutPy mutation testing tool 
        - Mitigated the threat of handling types of native dependencies by exclusion. However this does not exclude any functions which is partially implemented inC and could influentce our restults.

    - External Validity:
        - It is conceivable that the exclusion of projects without type annotations or nativecode libraries leads to a selection of smaller projects, and the results may thus not generalise to other Python projects. 
        - Furthermore, to make the different configurations comparable, we omitted all modules from the final evaluation for that Pynguin was not able to generate test cases for each configuration

    - Construct Validity:
        - we have not applied any parameter tuning to the search parameters but use default values, which have been shown to be reasonable choices in practice 