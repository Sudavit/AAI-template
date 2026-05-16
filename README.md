![GitHub Release](https://img.shields.io/github/v/tag/Sudavit/expenses-ai-agent)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/jsh/trendlist/blob/master/LICENSE)
![Pytest Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/jsh/adf6157270f535d96810040c16f44a3f/raw/expenses_badge.json)


# AAI
A template for my new repos.

- Make a more meaningful ```README.md``` (this file),

- ***LEAVE THE BADGE (Coverage & License) LINES AT THE TOP AS-IS***! Unless, that is, you want different badges.

- Edit a files and directories to change every instance of *AAI* to whatever my project is called.

    **N.B.** The easy way to do that is with `tools/fix-project`

    ```tools/fix-project```


- The script assumes that the repo will be named with dashes, and the project with underscores. Thus, if the repo is "my-special-project.git" the project will be "my_special_project".

## CI/CD

The project may need secret keys, such as API keys, to run successfully.
Putting these into the repository for everyone to see is a bad idea.
To put these into the environment for CI/CD on GitHub, under GitHub Actions, they need to be GitHub secrets.

You can run them locally by copying .env-template to .env and filling in your own values for these keys.
To do CI/CD on GitHub actions yourself, you also need to make them GitHub Secrets.
Once that's done, `.github/workflow/ci.yaml` can retrieve these values and place them in the environment during each CI/CD run.

To add them as secrets, go to your repository on GitHub, then

"""
Settings -> Secreta and variables -> Actions -> New repository secret
"""

## Scripts

- pyproject.toml assumes that I launch my file with ```main.main```: that is, by executing the file ```src/<projec>/main.py```, and calling the function ```main()```.
If I want to call my primary executable something else, I'll need to find and tweak every instance of ```main```, too.
