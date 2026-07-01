# Setting up Python and JupyterLab

The pages of this book are Jupyter notebooks, and the best way to learn is to **run the code yourself** as you read: change a value, re-run a cell, and see what happens. To do that on your own computer you need three things:

1. **Python** — the language interpreter.
2. **A virtual environment** — an isolated place to install packages for this book, kept separate from the rest of your system so nothing conflicts.
3. **JupyterLab plus the scientific packages** — the app you edit notebooks in, and the libraries the book uses (`numpy`, `pandas`, `matplotlib`, `scipy`, `scikit-learn`, `seaborn`).

This page walks through all three, from zero. You only do the setup once; after that, starting work is two commands.

:::{admonition} In a hurry? Run the code without installing anything
:class: tip
Every code page in this book has **in-page live compute**: press the 🚀 launch/run control at the top of a page to start a kernel in your browser (via [Binder](https://mybinder.org)) and run cells with no install. You can also open any notebook in [Google Colab](https://colab.research.google.com/). These are great for a quick look, but they are slower to start and reset when idle, so for sustained work a local setup is worth it.
:::

## Step 1 — Install Python

You have two common ways to get Python. Either works for this book.

**Option A — Miniforge/conda (recommended for beginners).** This installs Python *and* `conda`, a tool that manages both environments and scientific packages, and handles tricky compiled dependencies well.

- Download the installer for your operating system from [conda-forge/miniforge](https://github.com/conda-forge/miniforge#download) (or use [Anaconda](https://www.anaconda.com/download) if you prefer a graphical distribution).
- Run the installer, accepting the defaults.
- When it finishes, **open a new terminal** (macOS/Linux: Terminal; Windows: the "Miniforge Prompt" it installed) so the `conda` command is available.

**Option B — python.org + venv.** Use Python's own tooling, which is already on many systems.

- Install Python 3.11+ from [python.org/downloads](https://www.python.org/downloads/) (on Windows, tick **"Add Python to PATH"** in the installer).
- This gives you `python` (or `python3`) and the built-in `venv` and `pip` tools used below.

Check it worked by opening a terminal and running:

```bash
python --version      # or: python3 --version
```

You should see something like `Python 3.11.x`.

## Step 2 — Get the book's notebooks

To run a chapter you need its `.ipynb` file (and the datasets it uses) on your computer. Either:

- **Download:** on the book's [GitHub repository](https://github.com/JohnSerences/python_for_psych_neuro.github.io), click **Code → Download ZIP**, then unzip it somewhere you can find (e.g. `Documents/python-book`); or
- **Clone with Git** (so you can pull updates later — see [Version control with Git](./git.md)):

```bash
git clone https://github.com/JohnSerences/python_for_psych_neuro.github.io.git
cd python_for_psych_neuro.github.io
```

Work from inside that folder for the remaining steps.

## Step 3 — Create an isolated environment

An environment keeps this book's packages together and out of the way of other projects. Create it once.

**Option A — conda:**

You can pick your own name, here using pyneuro just as an example.

```bash
conda create -n pyneuro python=3.11
conda activate pyneuro
```

**Option B — venv (from inside the book folder):**

```bash
python -m venv .venv
source .venv/bin/activate      # Windows (PowerShell): .venv\Scripts\Activate.ps1
```

Once an environment is **active**, your terminal prompt shows its name (e.g. `(pyneuro)` or `(.venv)`). Everything you install now goes into that environment only.

## Step 4 — Install JupyterLab and the packages

With the environment active, install JupyterLab plus the scientific stack the book uses.

**Option A — conda:**

```bash
conda install -c conda-forge jupyterlab numpy pandas matplotlib scipy scikit-learn seaborn
```

**Option B — pip (works in either kind of environment):**

```bash
pip install jupyterlab numpy pandas matplotlib scipy scikit-learn seaborn
```

:::{tip}
If you cloned the repository, it ships a `requirements.txt`. You can install its scientific stack in one shot with `pip install -r requirements.txt` (that file also includes the tooling used to *build* the book, which you don't need just to run the notebooks).
:::

## Step 5 — Launch JupyterLab

Still in the book folder, with the environment active:

```bash
jupyter lab
```

This starts a local server and opens JupyterLab in your browser. In the file browser on the left, open a chapter (for example `lectures/P01-python.ipynb`), click a code cell, and press **Shift+Enter** to run it.

:::{admonition} Double check: is your notebook using the right environment?
:class: tip
A notebook runs on a **kernel** (a Python interpreter). If an `import` fails even though you just installed the package, the notebook is probably using a different kernel than the environment you installed. Check the kernel name shown at the **top-right** of the notebook, and switch it with **Kernel → Change Kernel**. If your environment isn't listed, register it once while it is active:

```bash
python -m ipykernel install --user --name pyneuro --display-name "Python (pyneuro)"
```
:::

## Step 6 — Confirm it all works

Open a new notebook (or use a code cell in any chapter) and run:

```python
import sys, numpy, pandas, matplotlib, scipy, sklearn, seaborn
print("Python:", sys.version.split()[0])
print("NumPy:", numpy.__version__, "| pandas:", pandas.__version__)
```

If that prints versions with no errors, you are ready to work through the book.

## Coming back later

You do the install once. Each time you sit down to work, just open a terminal, go to the book folder, reactivate the environment, and launch:

```bash
# Option A (conda):
conda activate pyneuro
jupyter lab

# Option B (venv):
source .venv/bin/activate      # Windows: .venv\Scripts\Activate.ps1
jupyter lab
```

When you're done, close the browser tab and press **Ctrl+C** in the terminal to stop the server. To leave the environment, run `conda deactivate` (Option A) or `deactivate` (Option B).

## Troubleshooting

- **`command not found: python` / `conda` / `jupyter`.** The tool isn't on your PATH, or you opened the terminal before installing. Close and reopen the terminal; on Windows use the Miniforge Prompt (Option A) or re-run the python.org installer and tick "Add Python to PATH" (Option B).
- **`ModuleNotFoundError` for a package you installed.** You almost certainly installed into one environment but the notebook is running in another. Confirm the environment is active (its name is in the prompt) and check **Kernel → Change Kernel** (see the Double-check callout above).
- **The `jupyter lab` command hangs or the page doesn't open.** Copy the `http://localhost:8888/...?token=...` URL that the terminal prints and paste it into your browser manually.
- **A chapter can't find a dataset.** Make sure you launched `jupyter lab` from the book folder so relative paths like `datasets/...` resolve, and that you downloaded/cloned the data files alongside the notebooks.

For editing and version-controlling your own copies of the notebooks, see [Version control with Git](./git.md); for more places to run and learn Python, see [Extracurricular Resources](./resources.md).
