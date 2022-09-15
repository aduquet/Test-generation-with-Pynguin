##A Replication Study on An Empirical Study of Automated Unit Test Generation for Python


### Future Work scopes from the Paper:
=======================================
 -  it is non-trivial to identify the existing attributes of an object and we
leave it as future work.
- Future work shall refine the branch distance for different operators and
operand types.
- Future work needs to address those challenges by, for example, providing a virtualised file system to Pynguin executions or mocking calls to critical functions, such as sys.exit.

- Constructs such as generators, iterators,
decorators, coroutines, or higher-order functions provide open challenges for
Pynguin and aim for future research.

- We leave a detailed investigation of the influence of the parameter values as future work.

- Also finding appropriate input values for function parameters might influence the achievable coverage. We study the influence of type information in RQ2, and leave exploring further factors as future work.

- a context manager (due to its decorator) and a generator (indicated by the yield statement). Pynguin currently supports neither;

- RQ1 - Future work shall repeat our evaluation using more complex subject systems in order to evaluate whether the assumed improvements can be achieved there.

- RQ2: Pynguin is, for example, not able to provide generators or iterators as arguments; neither does is provide higher-order functions. Adding these features is open as future work. Higher-order functions are required as an argument to 49 functions throughout the 134 modules. Being able to generate higher-order functions in the context of a dynamically-typed programming language has also been shown to be beneficial (Selakovic et al. 2018); we leave this for future work.

- Furthermore, we also note many modules for those the tests
achieve 100 % coverage but the achieved mutation scores range from 0 % to
100 %; this shows that the effectiveness of our assertions can still be improved
in the future.

- Although we fixed the obvious issues in MutPy, our customised version of MutPy is
an issue for crashes: future work shall replace this component by our own
implementation of the various mutation operators for a more fine-grained
control.

- Therefore, we accept that Pynguin generates flaky tests, which can influence the assertion generation and cause failures.

- The results we report here, however, are promising. They show that also
mutation-based assertion generation is feasible for dynamically typed programming languages; this again opens up new research perspectives targeting the
underlying oracle problem. 

### Motivation

input  from DIETMAR
-> Have to have  a really strong Motivation.

- To better understand the behaviour of PYNGUIN on different complex python modules 

- To ontribute to the core of PYNGUIN , first need to understand limitations of it.

- To find if the statistics from previous study still validates