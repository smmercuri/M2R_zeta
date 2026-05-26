# Computing with $L$-functions
Repository for the M2R Group 31 research project.

## Setup

This contains setup instructions for installing the project
environment and recommended extensions.
These extensions are for VSCode so it is recommended to use
that as your code editor.

### 1. Install Miniconda
If you don't already have conda, install Miniconda from
<https://docs.conda.io/projects/miniconda/en/latest/>.

### 2. Clone the repository

Inside a terminal navigate to where you would like to place the project and run the following.
```bash
git clone https://github.com/smmercuri/M2R_zeta.git
cd M2R_zeta
```

### 3. Create the conda environment
The project dependencies (SageMath, matplotlib, seaborn, plotly) are listed in
`environment.yml`.

```bash
conda env create -f environment.yml
```

This creates an environment named `m2r-zeta`. If you'd prefer a different name:
```bash
conda env create -f environment.yml -n my-env-name
```

### 4. Activate the environment
```bash
conda activate m2r-zeta
```
(Replace `m2r-zeta` with whatever name you chose in step 3.)

### 5. Open in VS Code
```bash
code .
```
When prompted, install the recommended extensions (Python, Pylance, Black
Formatter). Then select the `m2r-zeta` interpreter via the Command Palette:
`Python: Select Interpreter` -> choose the one under `…/envs/m2r-zeta/`.
You should then be all set up and ready to edit and run code.

## Workflow

We follow a branch-and-pull-request workflow. **Do not push directly to
`main`** — it is protected, and all changes must go through a pull
request (PR) so they can be reviewed before being merged.

### 1. Pick up a task
Tasks live in [GitHub Issues](https://github.com/smmercuri/M2R_zeta/issues).
Assign yourself to the issue you're working on so the rest of the group
knows it's taken.

### 2. Create a branch
Always start from an up-to-date `main`:
```bash
git checkout main
git pull
git checkout -b your-name/short-description
```
Use a short, descriptive branch name, e.g. `alice/euler-product` or
`bob/fix-plot-axes`.

### 3. Commit your changes
Make small, focused commits with clear messages:
```bash
git add path/to/file
git commit -m "Add Euler product computation for small primes"
```
Prefer several small commits over one giant one — they are easier to
review and easier to undo if something goes wrong.

### 4. Push and open a PR
```bash
git push -u origin your-name/short-description
```
GitHub will print a link to open a PR. In the PR description, briefly
say what the change does and link the issue it closes (e.g.
`Closes #12`).

### 5. Review and merge
Every PR requires **one approval** from **smmercuri** before it can be merged.
However, group members are encouraged to review each other's code within PRs and leave comments.

Address review comments by pushing more commits to the same branch —
the PR updates automatically. Once both approvals are in, use **Squash
and merge** on GitHub to keep `main` history tidy. The branch is
deleted automatically after merge.

### 6. Keep your local copy in sync
After a PR is merged, update your local `main`:
```bash
git checkout main
git pull
```
Before starting the next task, branch off the fresh `main` again.
