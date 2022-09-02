Pynguin Core exploration:
==========================

### `./__main__.py`

Provides main entry location for the program execution when pynguin is used as a library. Calls `cli.py` -> main().

### `./cli.py`

This module provides the main entry location for the program execution from the command line.

`def main():`

- Arguments:  List of command-line args
- Returns: An integer:
                - 0 -> successful test case generation
                - Any Non-zero -> indicates Errors

Tasks:
    - TODO: Checks ```_DANGER_ENV``` is set or not
    - TODO: Checks for arguments in the command - if set parses them otherwise defaults to system args
    - TODO: Parse the Arguments
    - TODO: Setup console logging
    - TODO: Collect configurations from command-line if provided otherwise defaults to basic config 
    - TODO: Run pynguin:
        * Calls `run_pynguin()` method form `generator.py` 
            - The result of the test generation is indicated again by ReturnCode
            - Returns ReturnCode: 
                    - 0 = OK, 
                    - 1 = SETUP_FAILED,
                    - 2 = NO_TEST_GENERATED
            - Raises ConfigurationException

            TODO: Calls the internal `_run()`:
                STEP-1: SETUP AND CHECK
                STEP-2: Generate Test Cluster
                STEP-3: Start Generating test cases
                STEP-4: Clear observers
                STEP-5: TRACK coverage metrics
                STEP-6: REMOVE statements which generate exceptions
                STEP-7: Start POST test case generation Process (If any)
                STEP-8: Start Generating assertions(defaults to MUTATION ANALYSIS)


