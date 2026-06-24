# Python for Computational Neuroscience

An introductory Python programming book aimed at students in **computational
neuroscience** and **experimental psychology**, written as a
[MyST / Jupyter Book 2](https://jupyterbook.org/) site (the MyST-native format
configured by a single `myst.yml`).

It covers the core of Python (control flow, atomic data types, containers, data
cleaning, functions, classes) and the scientific stack (`pandas`, `matplotlib`,
`numpy`), and adds:

* a short **"Applications & Modern Python"** companion to each core chapter, with
  neuroscience/psychology examples and notes on how the language has changed; plus
* **Appendix A — A 2-Hour Python Crash Course** for a fast start; and
* **Appendix B — Coding with AI**, on using tools like Cursor responsibly in science.

Throughout, **"Human check"** callouts flag code that can run without error yet be
scientifically wrong — the places where human judgment matters most.

---

## Repository structure

```
.
├── myst.yml             # ALL config: title, author, build options, and the TOC
├── index.md             # landing page (the TOC root)
├── requirements.txt     # toolchain (mystmd) + scientific stack for the notebooks
├── README.md            # this file
├── .github/workflows/   # GitHub Actions workflow that auto-deploys to Pages
├── binder/              # requirements.txt for Binder (in-page live compute)
├── course/              # reference pages: debugging guide + extra resources (.md)
├── lectures/            # core chapters P01-P09 (.ipynb) + *-applications companions
│   └── img/             # figures used by the lectures
├── crash_course/        # Appendix A: the 2-hour crash course
├── ai_coding/           # Appendix B: coding with AI
└── datasets/            # example datasets used in the notebooks
```

`_build/` (the generated site) is created by the build and is **not** committed
(see `.gitignore`). The files `_config.yml.jb1.bak` and `_toc.yml.jb1.bak` are the
retired Jupyter Book v1 config, kept only for reference; they are not used and can
be deleted.

---

## Building the book locally

This is a **MyST-native (Jupyter Book 2)** book. It is built with the MyST Document
Engine, which runs on Node.js. The easiest setup uses the `mystmd` PyPI package,
which installs the `myst` command and bootstraps a local Node runtime for you.

You need Python 3.9+ (3.11 recommended). From the repository root:

```bash
# 1) create and activate an isolated environment
python3 -m venv .venv
source .venv/bin/activate        # on Windows: .venv\Scripts\activate

# 2) install the toolchain + scientific stack
pip install -r requirements.txt

# (first run of `myst` downloads a local Node runtime; if that hangs, install Node
#  yourself once with:  nodeenv -p --node=lts )

# 3) build the static site (renders the notebooks' committed outputs)
myst build --html

# 4) preview with a live local server instead
myst start
```

The built site is written to `_build/html/` (open `_build/html/index.html`).

> **Note — this is Jupyter Book *2* (MyST), not v1.** v1 used `_config.yml` +
> `_toc.yml`; everything now lives in `myst.yml`. If you have an older `jupyter-book`
> (v1) installed and try `jupyter-book build .`, it will not understand `myst.yml`.
> Use `myst` (or `jupyter book`, the v2 CLI) instead.

### Re-executing notebooks

The committed notebooks already contain their outputs, so the build renders them
as-is. To re-run them locally and refresh those outputs, either:

```bash
# A) execute in place with Jupyter (handles cells that intentionally raise errors)
jupyter nbconvert --to notebook --execute --allow-errors --inplace lectures/*.ipynb

# B) or let MyST execute during the build
myst build --html --execute
```

Option B stops at any cell that raises unless that cell is tagged
`raises-exception`; several original chapters intentionally show errors, so Option A
is the simpler way to refresh everything.

---

## Deploying to GitHub Pages

This repo ships a MyST workflow at `.github/workflows/deploy.yml` that builds the
site and publishes it every time you push to `main`. (Because the notebooks carry
their outputs, the CI build is pure Node and needs no Python kernel.)

1. **Create the GitHub repository** and push this folder:

   ```bash
   git init
   git add .
   git commit -m "Initial commit: Python for Computational Neuroscience"
   git branch -M main
   git remote add origin https://github.com/jserences/python_for_computational_neuroscience.github.io.git
   git push -u origin main
   ```

   > **Note.** The owner is set to the GitHub handle `jserences` throughout (in
   > `myst.yml`'s `github:` field and the URLs here). A GitHub owner must be a valid
   > username/org and cannot contain `@` or `.`, so this is **not** the same as the
   > email `jserences@ucsd.edu`. If your handle differs, change `jserences` here and
   > in `myst.yml`.

2. **Turn on Pages with the "GitHub Actions" source:**
   **Settings → Pages → Build and deployment → Source → "GitHub Actions."**

3. **Done.** Every push to `main` rebuilds and redeploys (watch the **Actions** tab).
   The site will be at:

   * `https://jserences.github.io/python_for_computational_neuroscience.github.io/`
     — this is the default; the workflow's `BASE_URL` is already set to the repo name
     to match.
   * If you instead name the repo literally `jserences.github.io`, it is served at
     `https://jserences.github.io/`; in that case set `BASE_URL: ''` in the workflow.

To deploy by hand instead, run `myst build --html` and publish the `_build/html`
folder to a `gh-pages` branch (e.g. with `npx gh-pages -d _build/html`), then point
**Settings → Pages** at that branch.

---

## Live compute (run code in the browser)

The site has **in-page live compute** enabled (MyST's Thebe, backed by
[Binder](https://mybinder.org)). On any page with code, readers can start a session
and actually *run* the cells in their browser — no install required.

How it is wired up:

* `myst.yml` sets `project.jupyter.binder` to point at this repo
  (`jserences/python_for_computational_neuroscience.github.io`, ref `main`).
* `binder/requirements.txt` defines the kernel environment (numpy, pandas,
  matplotlib, scipy, scikit-learn, seaborn). Binder builds from *this* file, not the
  repo-root `requirements.txt`.

Things to know:

* Live compute only works **after the repo is pushed to GitHub** at the owner/ref in
  `myst.yml` and mybinder.org has built the image. The **first** launch can take a
  few minutes while Binder builds; later launches are cached and fast.
* If you add a library to a notebook, also add it to `binder/requirements.txt` so the
  live kernel can import it.
* To point live compute at a different environment or a JupyterHub, edit
  `project.jupyter` in `myst.yml` (see the
  [MyST in-page execution docs](https://mystmd.org/guide/in-page-execution)).

---

## Making updates in the future

The notebooks (`.ipynb`) and markdown (`.md`) files are the **source of truth** — edit
them directly in Jupyter, Cursor, or any editor.

* **Edit existing content.** Open the relevant file under `lectures/`, `course/`,
  `crash_course/`, or `ai_coding/`, make your changes, then preview with
  `myst start` (live reload) or `myst build --html`. If you change code in a
  notebook, re-execute it (see "Re-executing notebooks" above) so its committed
  outputs stay in sync.
* **Add a new page.** Create the `.ipynb`/`.md` file, then add it to the `toc:`
  section of `myst.yml` (with its file extension) in the right place. A file not in
  the TOC will not appear. Tip: `myst init --write-toc` can regenerate a TOC from the
  file structure.
* **Reorder or renest pages.** Edit the `toc:` in `myst.yml` (`children:` nests pages;
  a bare `title:` with `children:` makes a section/dropdown).
* **Change the title, author, logo, or repo link.** Edit `myst.yml`.
* **Add a Python dependency** used by a notebook: add it to `requirements.txt`.
* **Publish.** Just `git push` to `main` — the site rebuilds automatically.

### How the new chapters were authored

The `*-applications` companions and the two appendices were generated with a small
`nbformat` script kept *outside* this repository (so the published book stays clean).
That was a one-time scaffold; the resulting `.ipynb` files are now the source of truth
and should be edited directly. There is no need to regenerate them.

---

## Credits & license

Material © John Serences (with Ed Vul). Please retain attribution if you reuse or
adapt this material, and add a `LICENSE` file appropriate to how you intend to share
it.
