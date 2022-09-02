Test Generation with Pynguin
=============================
Automated unit test generation is a well-known methodology aiming to reduce the developers’ effort of writing tests manually. The most well-known open-source tools that perform automated unit test generation are Randoop and EvoSuite for Java programming language. Automated tool support for test generation is currently lacking for dynamically typed programming languages like Python.

A crucial problem impeding the development of test generation techniques is the fact that programs written in a dynamically typed language usually do not provide any information about variable types, as these languages often allow changing the type of a variable’s value throughout the program, dynamically modify objects at runtime, or provide type coercions that might not match the intent of the programmer.

Recently, an automated unit test generation for Python named Pyngin was proposed. Pynguin is an open-source framework written in and for Python. It uses search-based test generation to generate tests that maximize code coverage. Pynguin incorporates type information into the test-generation process. it is also able to generate covering test cases for programs that do not explicitly provide type information.

The aim of this thesis is to explore Pynguin capabilities on different systems by following the mutation testing approach. One can start by replicating "An Empirical Study of Automated Unit Test Generation for Python" study, and then extend the evaluation to different systems.

Papers:
-------
1. [Comaparative Evaluation - Automatic TCG](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9810694&tag=1) 
2. [Empirical Study - Automatic TCG for python](https://arxiv.org/pdf/2111.05003.pdf) Suggested by Pynguin Author


Working Docs (Both Have access):
--------------------------------
1. [Comaparative Evaluation - Paper summary](https://docs.google.com/document/d/1tBip_EG9wJUdumjOo4vsxub-iLG9yiqlaGzSzg89vX4/)
2. [Empirical Study - Paper Summary](https://docs.google.com/document/d/1uTcYdztm9CU4cHGMYQFEAtFE5R6KSCPY4R4MGQ4YwbY)
3. [Codebase Exploration- PYNGUIN CORE](https://docs.google.com/document/d/1Okn0y8MI0Dikg2V5PLTJGG3qNG5jnUhUrnOIxOw2ERY)
4. Google [Drive Folder](https://drive.google.com/drive/u/1/folders/144bG5CFz7vZdkCHgLqd0Ra6GHQjl9tE1)

Important Links:
----------------
1. Pynguin [docs](https://pynguin.readthedocs.io/en/latest/index.html)
2. Pynguin [Website](https://www.pynguin.eu/)

