![Coverage](./coverage.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/jsh/trendlist/blob/master/LICENSE)
# AAI
A template for my new repos in JuanJo's Agentic AI course.

- Make a more meaningful ```README.md``` (this file),

- ***LEAVE THE BADGE (Coverage & License) LINES AT THE TOP AS-IS***! Unless, that is, you want different badges.

- Edit a files and directories to change every instance of *AAI* to whatever my project is called.

    **N.B.** The easy way to do that is with `tools/fix-project`

    ```tools/fix-project```

Assumptions:

- The script assumes that the repo will be named with dashes, and the project with underscores. Thus, if the repo is "my-special-project.git" the project will be "my_special_project".

- pyproject.toml assumes that I launch my file with ```main.main```: that is, by executing the file ```src/<projec>/main.py```, and calling the function ```main()```.
If I want to call my primary executable something else, I'll need to find and tweak every instance of ```main```, too.
