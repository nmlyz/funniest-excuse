# Funniest Excuse

[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Output: one line](https://img.shields.io/badge/output-one%20line-brightgreen.svg)](#usage)

A tiny program that writes one excuse to a file: the story of a loading
spinner that never finished, and the name it was given while waiting.

Competition page: https://make.fun/competitions/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0

## What it does

Running `main.py` writes a single line to `/output/entry.txt`:

> I was waiting for the loading spinner to finish. It is still spinning. I have named it Gerald.

Before writing anything, the program checks the line: it must be one
line, end with a full stop, stay under 120 characters, be exactly 94
characters long, and contain the words `loading`, `spinner` and
`Gerald`. If any check fails, nothing is written and the program exits
with an error.

## How it works

`main.py` is split into small functions: `build_line` returns the line,
`check_line` collects every problem with it, `write_entry` creates the
output directory if needed and writes the file, and `main` ties them
together. Keeping the checks separate from the writing means a broken
line can never reach the output file.

## Usage

```sh
python3 main.py
cat /output/entry.txt
```

The program uses only the Python standard library, so there is nothing
to install. The output file is written with mode `0644` and the result
is byte-identical on every run.

## Files

- `main.py` — builds, validates and writes the excuse line.
- `LICENSE` — MIT license.
