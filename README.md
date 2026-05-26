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
git clone <repo-url>
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
