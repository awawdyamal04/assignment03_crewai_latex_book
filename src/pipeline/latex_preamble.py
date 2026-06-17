"""LuaLaTeX preamble fragment for the assembled article (Phase 5).

Holds only the document preamble as a raw string so the builder can compose
``latex/main.tex``. Engine is LuaLaTeX; bibliography is biblatex + biber.
Importing this module never calls an LLM and never builds a PDF.
"""

from __future__ import annotations

# Raw string: backslashes are literal LaTeX, not Python escapes.
PREAMBLE = r"""% main.tex — academic article assembled by the Phase 5 pipeline.
% Build engine: lualatex (NOT pdflatex) — required for fontspec + Hebrew BiDi.
% Bibliography:  biblatex with the biber backend.
% Build order:   lualatex -> biber -> lualatex -> lualatex
\documentclass[11pt,a4paper]{report}

% ── Fonts & languages (LuaLaTeX) ────────────────────────────────────────────
\usepackage{fontspec}
\usepackage{polyglossia}
\setmainlanguage{english}
\setotherlanguage{hebrew}
\setmainfont{Latin Modern Roman}
% A Hebrew-capable font (Culmus "David CLM" ships with TeX Live). Swap this
% for any installed Hebrew font if David CLM is unavailable on the build host.
\newfontfamily\hebrewfont[Script=Hebrew]{David CLM}

% ── Mathematics ─────────────────────────────────────────────────────────────
\usepackage{amsmath}
\usepackage{amssymb}

% ── Graphics & tables ───────────────────────────────────────────────────────
\usepackage{graphicx}
\usepackage{booktabs}
\graphicspath{{../figures/}{figures/}}

% ── Headers & footers (every body page) ─────────────────────────────────────
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{From RNN and LSTM to Transformers and AI Agents}
\fancyhead[R]{\thepage}
\fancyfoot[C]{Course 203.3763 — Orchestration of AI Agents}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}

% ── Bibliography (biblatex + biber) ─────────────────────────────────────────
\usepackage[backend=biber,style=numeric,sorting=nyt]{biblatex}
\addbibresource{references.bib}

% ── Hyperlinks (load late) ──────────────────────────────────────────────────
\usepackage[hidelinks]{hyperref}
\hypersetup{
  pdftitle={From RNN and LSTM to Transformers and AI Agents},
  pdfsubject={Course 203.3763 — Orchestration of AI Agents},
  colorlinks=true,
  linkcolor=blue!50!black,
  citecolor=green!40!black,
  urlcolor=blue!60!black
}

% ── Document metadata (filled by the title page) ────────────────────────────
\newcommand{\coursenumber}{203.3763}
\newcommand{\coursename}{Orchestration of AI Agents}
\newcommand{\lecturername}{Dr.\ Yoram Reuven Segal}
% Student name is a placeholder: replace before submission.
\newcommand{\studentname}{[STUDENT NAME — replace before submission]}
"""
