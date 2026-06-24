# Python for Computational Neuroscience

This book teaches you to program in Python in the context of **computational neuroscience** and **experimental psychology**, starting from zero programming experience.

The goal is to develop *computational thinking* — the skill of giving a computer explicit, correct instructions to carry out a desired computation. Most examples come from the kinds of data you actually meet in a behavioral or brain-science lab: reaction times, accuracy, spike trains, EEG/MEG traces, fMRI time series, psychophysical thresholds, and trial-by-trial experiment logs.

## How this book is organized

* **Core content (P01–P09).** The heart of the book. These chapters build up the language from the ground up — variables and data types, control flow, containers, functions, classes — and then the scientific stack: `pandas`, `matplotlib`, and `numpy`. Each topic is followed by a short **"Applications & Modern Python"** companion that (a) shows the topic at work on neuroscience/psychology data and (b) points out where the language has moved on since the original material was written.
* **Appendix A — A 2-Hour Python Crash Course.** A fast, self-contained sprint through the fundamentals and the most common data-science tools. It does *not* replace the full chapters; it is for someone who needs to get productive quickly and wants a guided tour they can finish in an afternoon.
* **Appendix B — Coding with AI.** A gentle, assumes-nothing introduction to using AI coding tools (like Cursor) to build scientific software, ending with an honest discussion of the benefits, risks, and methodological responsibilities of letting an AI help write code you will publish.

## Why Python?

Python is the most widely used general-purpose language in both academia and industry. In the brain and behavioral sciences specifically, the entire modern analysis ecosystem — `numpy`, `scipy`, `pandas`, `matplotlib`, `scikit-learn`, plus domain tools like `MNE`, `nilearn`, `PsychoPy`, and `Brian2` — is built in and around Python. Learning it well means you can read other people's analysis code, reproduce published results, and build your own experiments and pipelines.

## A note on learning to code in the age of AI

You are learning to program at a moment when an AI can write a great deal of code for you. That is genuinely useful, and this book will teach you to use it well (Appendix B). But it makes *understanding* the code more important, not less. Throughout the book you will see callouts marked **"Human check"** that flag exactly the kinds of code an AI (or a hurried human) can write so that it *runs without error but is scientifically wrong*. Those moments are where your judgment as a scientist matters most.

Let's get started.
