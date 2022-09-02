Pynguin Core exploration:
==========================

### `./__main__.py`

Provides main entry location for the program execution when pynguin is used as a library. Calls `cli.py` -> main().

### `./cli.py`

This module provides the main entry location for the program execution from the command line.

```def main(): 
```
    - Arguments:  List of command-line args
    - Returns: An integer:
                    - 0 -> successful test case generation
                    - Any Non-zero -> indicates Errors
    
    Tasks:
        - TODO: Checks ```_DANGER_ENV``` is set or not
        - TODO: Checks for arguments in the command - if set parses them otherwise defaults to system args
        - 

