<div align="center">

<br/>

```
   ______  _    __   _____      _  __          __
  / ____/ | |  / /  / ___/     | |/ /    ___  / /___
 / /      | | / /   \__ \      |   /    / _ \/ // _ \
/ /___    | |/ /   ___/ /     /   |    /  __/ // ___/
\____/    |___/   /____/     /_/|_|    \___/_//_/
```

# AI CV Tailor

### ATS-Optimized Resume Intelligence. LaTeX-Safe. GitHub-Native.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Gemini API](https://img.shields.io/badge/Gemini_API-Google_AI-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![LaTeX](https://img.shields.io/badge/LaTeX-Template_Safe-008080?style=flat-square&logo=latex&logoColor=white)](https://www.latex-project.org)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/anubhavxdev/ai-cv-tailor?style=flat-square&color=f59e0b)](https://github.com/anubhavxdev/ai-cv-tailor/stargazers)

<br/>

> **Push your CV. Push a job description. Get a recruiter-ready, ATS-optimized resume — automatically.**

<br/>

</div>

---

## The Problem

Every serious job application demands a tailored resume. Most candidates either skip this entirely or spend hours doing it manually — neither works.

| Pain Point | Reality |
|---|---|
| Generic resumes | Rejected before a human sees them |
| Manual tailoring | Takes 1–2 hours per application |
| ATS blind spots | 75% of resumes never reach a recruiter |
| LaTeX templates | Hard to edit without breaking formatting |

**AI CV Tailor solves all four.** In one push.

---

## How It Works

```
You push two files.  The system does the rest.
```

```
┌─────────────────────────────────────────────────────┐
│                     YOUR INPUT                       │
│                                                      │
│   input/cv.txt          jobs/job1.txt               │
│   └─ Your resume        └─ Target job description   │
│                                                      │
│   templates/resume.tex                              │
│   └─ Your LaTeX template (university / standard)    │
└───────────────────────┬─────────────────────────────┘
                        │  git push
                        ▼
┌─────────────────────────────────────────────────────┐
│                 GITHUB ACTIONS CI/CD                 │
│                                                      │
│   ① Gemini API — Recruiter-level CV analysis        │
│   ② ATS scoring engine — keyword match %            │
│   ③ Gap detection — missing skills & keywords       │
│   ④ Improvement generator — verbs, metrics, impact  │
│   ⑤ LaTeX patch engine — marker-safe content swap   │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────┐
│                    YOUR OUTPUTS                      │
│                                                      │
│   analysis.txt          improvements.txt            │
│   └─ Rejection reasons  └─ Specific fixes           │
│                                                      │
│   ats_score.txt         keywords.txt                │
│   └─ Match percentage   └─ Missing ATS keywords     │
│                                                      │
│   final_cv.txt          updated_resume.tex          │
│   └─ Optimized CV       └─ Patched LaTeX file       │
└─────────────────────────────────────────────────────┘
```

---

## Features

### Recruiter-Level Analysis
Simulates a strict recruiter evaluating your resume against the job description. Surfaces exact rejection reasons, weak bullet points, and skill gaps — not generic advice.

### ATS Score Engine
Calculates a quantified match score between your resume and the job description. Gives you a clear benchmark before you apply.

### Keyword Gap Detection
Identifies every ATS-critical keyword in the job description that is absent from your resume. Directly impacts your ranking in applicant tracking systems.

### AI-Generated Improvements
Produces concrete, drop-in suggestions: stronger action verbs, quantified impact statements, restructured bullet points, and role-specific terminology.

### LaTeX Template Optimization
The standout feature. Works with rigid LaTeX templates — the kind universities and institutions mandate — using a marker-based patching system:

```latex
% START_SKILLS
  \item Python, Node.js, AWS, Docker
% END_SKILLS

% START_EXPERIENCE
  \item Built REST APIs serving 10k+ requests/day
% END_EXPERIENCE

% START_PROJECTS
  \item Developed full-stack SaaS platform with CI/CD pipeline
% END_PROJECTS
```

The engine updates content within markers only. Structure, formatting, and layout remain completely intact.

### Fully Automated Pipeline
Triggered on every push via GitHub Actions. No manual steps. No local setup required after initial configuration.

---

## Project Structure

```
ai-cv-tailor/
│
├── input/
│   └── cv.txt                  # Your current resume (plain text)
│
├── jobs/
│   └── job1.txt                # Target job description
│
├── templates/
│   └── resume.tex              # Your LaTeX resume template
│
├── output/
│   ├── analysis.txt            # Recruiter analysis + rejection reasons
│   ├── improvements.txt        # Suggested improvements
│   ├── final_cv.txt            # AI-optimized resume content
│   ├── ats_score.txt           # ATS match score
│   ├── keywords.txt            # Missing keywords list
│   └── updated_resume.tex      # Patched LaTeX resume
│
├── scripts/
│   ├── analyze.py              # CV analysis module
│   ├── score.py                # ATS scoring engine
│   ├── improve.py              # Improvement generator
│   ├── patch_latex.py          # LaTeX marker-based patcher
│   └── main.py                 # Orchestration entry point
│
├── .github/
│   └── workflows/
│       └── cv_pipeline.yml     # GitHub Actions workflow
│
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11+ |
| AI Engine | Google Gemini API |
| Automation | GitHub Actions |
| Resume Format | LaTeX |
| Output Formats | `.txt`, `.tex` |

---

## Getting Started

**1. Fork or clone this repository**

```bash
git clone https://github.com/anubhavxdev/ai-cv-tailor.git
cd ai-cv-tailor
```

**2. Add your Gemini API key as a GitHub Secret**

```
Settings → Secrets and variables → Actions → New repository secret
Name: GEMINI_API_KEY
```

**3. Add your files**

```bash
# Paste your current resume
nano input/cv.txt

# Paste the job description you're targeting
nano jobs/job1.txt

# Add your LaTeX resume template with markers
cp your_resume.tex templates/resume.tex
```

**4. Push**

```bash
git add .
git commit -m "add cv and job description"
git push
```

The GitHub Actions pipeline runs automatically. Outputs appear in the `output/` directory of the workflow artifacts.

---

## LaTeX Marker Setup

Add the following comment markers to your LaTeX template to enable safe content patching:

```latex
\section{Skills}
\begin{itemize}
% START_SKILLS
  \item Your current skills here
% END_SKILLS
\end{itemize}

\section{Experience}
\begin{itemize}
% START_EXPERIENCE
  \item Your current experience here
% END_EXPERIENCE
\end{itemize}

\section{Projects}
\begin{itemize}
% START_PROJECTS
  \item Your current projects here
% END_PROJECTS
\end{itemize}
```

Everything outside the markers is untouched. The patcher only replaces content between the `START_*` and `END_*` comment pairs.

---

## Example Output

**`ats_score.txt`**
```
ATS Match Score: 73/100

Matched Keywords : React, Node.js, REST API, MongoDB, Git
Missing Keywords : TypeScript, CI/CD, Docker, Agile, Jest
```

**`analysis.txt`**
```
REJECTION RISK: MEDIUM-HIGH

1. No measurable impact in experience bullets
2. Missing 5 high-frequency ATS keywords for this role
3. Skills section does not reflect job-required technologies
4. Project descriptions lack scope and outcome data
```

**`improvements.txt`**
```
BULLET POINT IMPROVEMENTS

Before: "Worked on backend APIs"
After:  "Engineered 12 REST API endpoints using Node.js and Express,
         reducing average response time by 40%"

SKILLS TO ADD: TypeScript, Docker, Jest, Agile methodologies
```

---

## Roadmap

- [x] Gemini-powered recruiter analysis
- [x] ATS score calculation
- [x] Keyword gap detection
- [x] LaTeX marker-based patching
- [x] GitHub Actions automation
- [ ] PDF auto-generation from patched LaTeX
- [ ] React web dashboard with drag-and-drop input
- [ ] Multi-job comparison and ranking
- [ ] Support for multiple LaTeX templates
- [ ] SaaS deployment with user accounts

---

## Why This Exists

University students and professionals who use standardized or institution-mandated LaTeX templates face a specific constraint: AI tools that rewrite resumes either produce plain text or break LaTeX formatting entirely.

This project solves that constraint with a marker-based patching approach — updating only the content sections while leaving document structure, packages, and formatting commands completely untouched. It is the only open-source resume optimizer built specifically for LaTeX template compatibility.

---

## Author

**Anubhav Jaiswal**
Final Year B.Tech — Computer Science, Lovely Professional University
Founder, FounDev Studio | Tech Lead, AWS Cloud Community | 2x Hackathon Winner

[![GitHub](https://img.shields.io/badge/GitHub-anubhavxdev-181717?style=flat-square&logo=github)](https://github.com/anubhavxdev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-anubhavxdev-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/anubhavxdev)
[![Portfolio](https://img.shields.io/badge/Portfolio-anubhavjaiswal.me-000000?style=flat-square&logo=vercel)](https://anubhavjaiswal.me)

---

<div align="center">

If this project helped you land interviews, consider giving it a star.

[![Star this repo](https://img.shields.io/github/stars/anubhavxdev/ai-cv-tailor?style=for-the-badge&color=f59e0b&label=Star%20this%20repo)](https://github.com/anubhavxdev/ai-cv-tailor)

</div>
