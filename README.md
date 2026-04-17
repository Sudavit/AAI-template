![Coverage](./coverage.svg)
# agent-base-template
Template for new repos.

- Customize ```LICENSE``` to contain your name and the year
- Make a more meaningful ```README.md``` (this file), but ***LEAVE THE FIRST (Coverage) line as-is***!
- Edit a few files to change every string that contains *AI* (e.g., ```AI-template```) to whatever your project is called.

    - pyproject.toml
    - tools/profile-exhaustive.py

Note: both files assume that you launch your file with ```main.main```: that is, by executing the file ```src/AI/main.py```, and calling the function ```main()```.
If you want to call your primary executable something else, you'll need to find and tweak those names, too.
