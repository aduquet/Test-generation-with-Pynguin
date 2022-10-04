## Experiment Replication ontribute
====================================

Replication their empiricial study Experiment with One project


### Tools and prjects with versions
===================================
1. Python 3.10.6
2. Poetry 1.2.1
3. Pynguin 0.25.2

### Steps
==========

1. Unzipped their artifact given for replication
2. Explore the project files and folders
3. Kept only httpie in the projects folders
4. Deleted other projects from experiment-projects.xml
5. Deleted other projects from experiment-assertions.xml
6. Changed pynguin path 
7. Installed Poetry
8. Installed virtual env using Poetry
9. Activated poetry venv
10. Ran python execution.py -d "experiment-projects.xml"  command 
11. It generated around 5000 run shell scripts
12. There is no data to run the experiments on a PC.
13. Channging `execution.py` using rercommendations from Stephan.
    - Fixed `_write_run_script` to use local PC paths
    