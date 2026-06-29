# Version control with Git

When you write code for an experiment or an analysis, you change it constantly: you fix a bug, try a new model, tweak a figure, only to realize that yesterday's version actually worked better. **Version control** is a system that records snapshots of your project over time so you can see what changed, go back to any earlier state, work on changes safely, and share the project with others.

**Git** is the most widely used version control tool. **GitHub** is a website that hosts Git projects online (this book itself lives in a GitHub repository and is published from it). The two are often mentioned together, but they are different things: Git is the tool that tracks your files, and GitHub is one place to store a copy online and collaborate.

There are two main ways to interface with Git, and they do the same underlying work:

1. **GitHub Desktop**, a free graphical app with buttons for the common actions. This is the easiest place to start.
2. **The command line**, which is more powerful and is what you will see in most tutorials and documentation.

This chapter covers both. Pick whichever you prefer and you can always switch later (or you can use both on the same project).

## A few core ideas

A handful of terms show up no matter which interface you use:

- **Repository** ("repo"): a folder that Git is tracking, including its full history.
- **Commit**: a saved snapshot of your project at one moment, with a short message describing what changed. Think of it as a labeled checkpoint you can always return to.
- **Remote**: a copy of the repository hosted elsewhere, usually on GitHub. The default remote is named `origin`.
- **Push / pull**: *push* sends your local commits up to the remote. *pull* brings new commits from the remote down to your computer.
- **Branch**: an independent line of work. The main branch is usually called `main`. You can make a branch to try something risky without disturbing `main`.
- **Clone**: download a full copy of a remote repository (history included) to your computer.

Using Git effectively is a simple loop: **make changes → commit them with a message → push to the remote.** Everything below is a variation on that loop.

:::{admonition} Double check: what you commit
:class: tip
Git records *everything* you commit, and that history is hard to scrub once it is shared. Before committing, make sure you are **not** including things that should stay out of version control:

- **Secrets** (API keys, passwords, tokens) — never commit these.
- **Large data files** and generated outputs (big `.csv`, `.nii`, build folders). Track the *code* that produces results, not tons of raw data.
- **Participant-identifying information** — keep human-subjects data out of public repos entirely.

Use a `.gitignore` file (described below) to tell Git which files to skip.
:::

## 1. Using Git with GitHub Desktop

[GitHub Desktop](https://desktop.github.com/) gives you the whole workflow through a single window, with no commands to memorize.

### Set up

1. Download and install **GitHub Desktop**, then open it.
2. Sign in: **GitHub Desktop → Settings/Preferences → Accounts → Sign in** with your GitHub account. (Create a free account at [github.com](https://github.com) first if you do not have one). Signing in stores your credentials so you don't have to type a password when pushing.

### Start a project

You have three common starting points:

- **Track a folder you already have:** **File → Add Local Repository…**, choose the folder, and if it is not yet a repo, Desktop offers to create one.
- **Start fresh:** **File → New Repository…**, give it a name and location. Tick "Initialize with a README," and choose a `.gitignore` template (e.g. *Python*) so common junk is ignored automatically.
- **Copy an existing online project:** **File → Clone Repository…** and pick one of your GitHub repos or paste a URL.

### Day to day use

1. Edit your files in your normal editor (Jupyter, Spyder, VS Code, Cursor, etc.) and save.
2. Switch to GitHub Desktop. The **Changes** tab lists every file you touched, with a line-by-line view of what changed (green = added, red = removed).
3. Tick the files you want to include (all of them, usually).
4. At the bottom left, type a short **Summary** of the change (e.g. "Add reaction-time outlier filter"). A good summary finishes the sentence "This commit will do…".
5. Click **Commit to main**. That saves the snapshot *on your computer*.
6. Click **Push origin** (top right) to send your commits to GitHub.

To bring down changes made elsewhere (another computer, a collaborator, or an edit you made on github.com), click **Fetch origin**, then **Pull origin** if it reports new commits.

### Other useful things

- **History tab:** browse every past commit and exactly what each one changed.
- **Branches:** the **Current Branch** menu lets you create and switch branches. Use a branch (e.g. `try-new-model`) for experimenting with new code, then **Branch → Create Pull Request** or merge it back into `main` when you are happy.
- **Undo:** right-click a commit in History to **Revert** it (creates a new commit that undoes those changes — safe even after pushing).
- **Publish:** for a brand-new local repo, click **Publish repository** to create it on GitHub and push in one step. Untick "Keep this code private" if you want it public.

## 2. Using Git from the command line

The command line exposes the same actions as explicit commands. It is worth learning because documentation, tutorials, and error messages are written in terms of these commands, and it works anywhere (including remote servers with no graphical interface).

### One-time setup

Install Git (macOS: it comes with the Xcode command line tools, or use [git-scm.com](https://git-scm.com); Windows: install [Git for Windows](https://git-scm.com)). Then tell Git who you are, so your commits are attributed correctly:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Start a project

```bash
# turn the current folder into a repository
git init

# OR copy an existing repository from GitHub
git clone https://github.com/USERNAME/REPO.git
```

### Day to day use

```bash
git status                       # what has changed / what is staged?
git add analysis.py figures.py   # stage specific files...
git add .                        # ...or stage everything that changed
git commit -m "Add RT outlier filter"   # save a snapshot with a message
git push                         # send commits to the remote (origin)
```

`git add` chooses what goes into the next commit (this is called *staging*); `git commit` records it; `git push` uploads it. To bring down others' changes:

```bash
git pull        # fetch new commits from the remote and merge them in
```

### Looking around and undoing

```bash
git log --oneline        # compact list of past commits
git diff                 # show unstaged changes
git diff --staged        # show what is staged for the next commit
git restore FILE         # discard unsaved changes to a file
git revert <commit>      # make a new commit that undoes an earlier one
```

### Branches

```bash
git switch -c try-new-model   # create and move to a new branch
git switch main               # move back to main
git merge try-new-model       # merge a branch into the current one
```

### Connecting to GitHub

If you started with `git init` locally, link it to a GitHub repo you have created, then push the first time:

```bash
git remote add origin https://github.com/USERNAME/REPO.git
git branch -M main
git push -u origin main
```

### `.gitignore`

Create a plain-text file named `.gitignore` in the repo root listing patterns Git should never track, one per line:

```
# Python caches and environments
__pycache__/
.venv/

# Notebook checkpoints and OS cruft
.ipynb_checkpoints/
.DS_Store

# Large data / generated outputs
data/raw/
*.nii
```

## Desktop ↔ command-line cheat sheet

The two interfaces map directly onto each other:

| You want to…            | GitHub Desktop                | Command line                  |
| ----------------------- | ----------------------------- | ----------------------------- |
| See what changed        | **Changes** tab               | `git status` / `git diff`     |
| Save a snapshot         | Summary + **Commit to main**  | `git add …` then `git commit` |
| Upload to GitHub        | **Push origin**               | `git push`                    |
| Download others' changes| **Fetch** then **Pull origin**| `git pull`                    |
| View history            | **History** tab               | `git log`                     |
| Make/switch a branch    | **Current Branch** menu       | `git switch -c` / `git switch`|
| Undo a commit           | Right-click → **Revert**      | `git revert <commit>`         |

## References

- [GitHub's "Hello World" guide](https://docs.github.com/get-started/quickstart/hello-world) — a 10-minute hands-on intro.
- [Pro Git](https://git-scm.com/book) — the free, comprehensive Git book.
- [Software Carpentry: Version Control with Git](https://swcarpentry.github.io/git-novice/) — a lesson aimed at researchers.

The single most important habit is the easiest one: **commit early and often, with clear messages.** Small, well-described commits make your project easy to understand, easy to fix, and easy to share.
