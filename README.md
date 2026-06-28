# Python for Psychology and Neuroscience 

An introductory Python programming book aimed at students interested in using **computational** 
approaches in psychology and neuroscience, written as a
[MyST / Jupyter Book 2](https://jupyterbook.org/) site (the MyST-native format
configured by a single `myst.yml`).

It covers the core of Python (control flow, atomic data types, containers, data
cleaning, functions, classes) and the scientific stack (`pandas`, `matplotlib`,
`numpy`), and adds:

* a short **"Applications and advanced tips"** companion to each core chapter, with
  psychology/neuroscience examples; plus
* **Appendix A: Python Crash Course** for a fast start; and
* **Appendix B: Coding with AI**, on using tools like Cursor responsibly in science.

Throughout, **"Advanced tips"** highlight the Pythonic way to do things, and they point to common
situations where code runs without error yet might be *wrong* for your particular context. These tips also 
point to situations where you need to be especially careful using AI assistants - ultimately you judgment matters most
and if you don't know what you're doing, you won't know how to provide guidance for an AI.

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
├── crash_course/        # Appendix A: the Python Crash Course
├── ai_coding/           # Appendix B: coding with AI
└── datasets/            # example datasets used in the notebooks
```

`_build/` (the generated site) is created by the build and is **not** committed
(see `.gitignore`). The files `_config.yml.jb1.bak` and `_toc.yml.jb1.bak` are the
retired Jupyter Book v1 config, kept only for reference.

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

> **Note: this is Jupyter Book *2* (MyST), not v1.** v1 used `_config.yml` +
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
site and publishes it to GitHub Pages on every push to `main`. Because the notebooks
carry their committed outputs, the CI build is pure Node and needs no Python kernel.
The workflow also **turns Pages on for you** (`enablement: true` on the
`configure-pages` step), so you do not have to enable Pages by hand first.

### Option A: GitHub Desktop (recommended, no command line)

1. **Add the project.** GitHub Desktop → **File → Add Local Repository…** and choose
   this folder (`python_for_psych_neuro.github.io`). It already has a git history, so
   Desktop just adopts it.
2. **Commit anything pending.** In the **Changes** tab, type a summary and click
   **Commit to main**.
3. **Publish.** Click **Publish repository** and set:
   * **Name:** `python_for_psych_neuro.github.io`
   * **Owner:** `jserences`
   * **Uncheck "Keep this code private"** — GitHub Pages (on free accounts) and Binder
     both require a **public** repo.

   Then click **Publish repository** to push `main` to GitHub.
4. **Watch the build.** On github.com open the **Actions** tab. "MyST GitHub Pages
   Deploy" runs automatically (~2–4 min); a green check means it is live.
5. **Visit the site:**
   `https://jserences.github.io/python_for_psych_neuro.github.io/`

For later updates: edit files → **Commit to main** → **Push origin**. Each push
rebuilds and redeploys automatically.

### Option B: command line

```bash
git add .
git commit -m "Publish site"
git branch -M main
git remote add origin https://github.com/jserences/python_for_psych_neuro.github.io.git
git push -u origin main
```

Then watch the **Actions** tab as above.

### If a run fails with "Get Pages site failed … Not Found"

`enablement: true` normally enables Pages automatically on the first run. If you ever
hit this error anyway, enable it manually once at **Settings → Pages → Build and
deployment → Source → "GitHub Actions"**, then re-run the job from the **Actions**
tab. (The "Node.js 20 is deprecated" message in the logs is only a warning and does
not affect the build.)

### Notes

* **URL / sub-path.** A *project* repo is served from `/<repo-name>`, and the
  workflow's `BASE_URL` is already `/${{ github.event.repository.name }}`, so the
  sub-path matches automatically. 
* **Owner handle.** `jserences` is a GitHub *username*, not the email
  `jserences@ucsd.edu` (owners cannot contain `@` or `.`).
* **Manual one-off deploy.** You can also run `myst build --html` locally and publish
  `_build/html` to a `gh-pages` branch (e.g. `npx gh-pages -d _build/html`), then
  point **Settings → Pages** at that branch.

---

## Live compute (run code in the browser)

The site has **in-page live compute** enabled (MyST's Thebe, backed by
[Binder](https://mybinder.org)). On any page with code, a reader can start a session
and **run** the cells right in the browser, with nothing to install.

### How binder works

* `myst.yml` → `project.jupyter.binder` points Thebe at this repo
  (`jserences/python_for_psych_neuro.github.io`, ref `main`, provider `github`).
* `binder/requirements.txt` defines the kernel environment (numpy, pandas,
  matplotlib, scipy, scikit-learn, seaborn). **Binder builds from this file**, not the
  repo-root `requirements.txt`.

### Turning binder on

There is no separate Binder deploy step. Once the repo is **public on GitHub** (see
deployment above), Binder can build it on demand:

1. Open a page with code on the live site.
2. Click the rocket / **launch** button (or the **run** control on a code cell) to
   start a Binder session.
3. The **first** launch tells mybinder.org to build the image from
   `binder/requirements.txt` — this can take ~1–3 mintes. Later launches reuse the
   cached image and start in seconds.

**Optional — pre-build so the first reader does not wait:** visit
`https://mybinder.org/v2/gh/jserences/python_for_psych_neuro.github.io/main` once in a
browser and let the build finish.

### Keeping it working

* If you `import` a new library in a notebook, **also add it to
  `binder/requirements.txt`** (otherwise the live kernel cannot import it). Push the
  change and the next Binder launch rebuilds.
* Binder runs on free, shared infrastructure: ideal for casual
  interactivity, but it can be slow or briefly unavailable. For heavy or reliable
  compute, run the notebooks in JupyterLab locally instead.
* To use a different backend (another Binder federation member or a JupyterHub), edit
  `project.jupyter` in `myst.yml` (see the
  [MyST in-page execution docs](https://mystmd.org/guide/in-page-execution)).

---

## Making updates in the future

The notebooks (`.ipynb`) and markdown (`.md`) files are the source, so edit
them directly in Jupyter or any editor.

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
* **Publish.** Commit and push to `main` (in GitHub Desktop: **Commit to main** →
  **Push origin**, or `git push` on the command line) and the site rebuilds
  automatically via the Actions workflow.

---

## Credits & license

Material © John Serences (with content from Ed Vul from ~2021 Computational Social Sciences 001 at UCSD). Please retain attribution if you reuse or adapt this material, and add a `LICENSE` file appropriate to how you intend to share it.
