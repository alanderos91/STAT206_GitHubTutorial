# GitHub Tutorial

## Student Instructions

1. **Clone** this repository to your computer.
2. **Create your own branch** from the `main` branch using your SIS ID as the branch name.
3. **Edit** `motivation.py` in the specified section of the code.
    + Add a single line of Python code changing *your* grade to an `'A'`.
4. **Commit** your changes.
5. **Push** your work onto the remote repository (on GitHub).
6. **Create a pull request** asking merge your work with `DIS002` or `DIS003`, depending on which section you are enrolled in.

At the end, we will merge everyone's code to `main`, run the script, and commit any additional changes made.

## Summary

- Use GitHub Desktop to avoid CLI unless you're comfortable learning `git` directly.
    - **Beware**: The graphical interface is *opinionated* in the sense that it makes some choices for you automatically.
    - For example, avoid creating a [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo). Make edits to **your** group's repository using [branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches).
- Working on projects won't be as chaotic as 30+ people making simultaneous edits!
    - Delegate work among group members.
    - Make sure you all start from a common point (e.g. someone has to setup the repo on GitHub with starter code/files).
- **Basic Workflow**: Branch from `main` → *your branch* → local commits → publish *your branch* → merge to `main`
    - Makes it easy to merge your changes to the group.
    - Use branches to work locally, then publish your branch on GitHub.
    - Use the pull request interface on GitHub (is partially accessible on GitHub Desktop tool).
- **Check each other's code before merging**!
    - GitHub Desktop allows you to see edits from a pull request locally.
    - Grab the changes, then run the code on your computer to make sure it works.
    - Make edits as needed.
- Avoid committing non-code files until required.
    - Example: Running the code would result in constant changes to `new_grades.json`. Increases likelihood of merge conflicts.
    - What matters is that everyone on the team can recreate the relevant outputs on the project.