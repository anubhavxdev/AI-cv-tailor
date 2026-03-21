<div align="center">

<br />

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=AI%20CV%20Tailor&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=32&desc=Stop%20embarrassing%20yourself%20with%20generic%20resumes.&descAlignY=55&descSize=16" width="100%"/>

<br/>

> ### *"You spent 3 hours tailoring that resume. The ATS rejected it in 0.3 seconds."*
> **There's a better way.**

<br/>

[![Made with Python](https://img.shields.io/badge/Built_with-Python_3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Powered by Gemini](https://img.shields.io/badge/AI-Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)
[![GitHub Actions](https://img.shields.io/badge/Automated-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![LaTeX Safe](https://img.shields.io/badge/LaTeX-Template_Safe-008080?style=for-the-badge&logo=latex&logoColor=white)](https://latex-project.org)
[![License MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

<br/>

</div>

---

<div align="center">

## Are you tired of this?

</div>

```
Monday 11:47 PM.

You: *opens job description*
You: *opens resume*
You: *stares at screen for 20 minutes*
You: *changes one bullet point*
You: *calls it "tailored"*
ATS: lol no
Recruiter: never sees it
You: "why am I not getting callbacks"
```

**Yeah. We built this for you.**

---

<div align="center">

## What AI CV Tailor Does

### Push your resume. Push a job description. Go touch grass.

</div>

<br/>

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                    │
│    YOU                        AI CV TAILOR           OUTPUT       │
│                                                                    │
│  cv.txt ──────────────►  ┌─────────────────┐                     │
│  job1.txt ─────────────► │  Gemini Analysis │ ──► ATS Score       │
│  resume.tex ───────────► │  Keyword Engine  │ ──► Gap Report      │
│                           │  LaTeX Patcher  │ ──► Tailored CV     │
│  git push ─────────────► └─────────────────┘ ──► Updated .tex    │
│                                   │                               │
│                            GitHub Actions                         │
│                           (does it all, automatically)            │
│                                                                    │
└──────────────────────────────────────────────────────────────────┘
```

No dashboard to learn. No subscription to forget about. No "premium plan" holding your resume hostage.
**Just push and get results.**

---

## The Brutal Truth About Your Resume

Before AI CV Tailor, your resume probably looks like this:

```diff
- "Worked on backend APIs"           ← what does this even mean
- "Helped with deployment process"   ← helped? helped how??
- "Familiar with Docker"             ← familiar = never used in prod
- "Good communication skills"        ← everyone writes this. everyone.
- Skills: Python, Java, C++, React, Angular, Vue, AWS, Azure, GCP  ← pick a lane
```

After:

```diff
+ "Engineered 12 REST API endpoints with Node.js, cutting avg response time by 40%"
+ "Automated CI/CD pipeline via GitHub Actions, reducing deployment time from 45 min to 8 min"
+ "Containerized 3 microservices with Docker, deployed to AWS ECS with zero-downtime rollouts"
+ "Led cross-functional sprint planning for a team of 6, shipping 3 features ahead of schedule"
```

**That's the difference between a rejection and an interview.**

---

## Features That Actually Matter

<br/>

### Recruiter-Level Analysis — *"Why your CV gets thrown in the bin"*

The AI doesn't sugarcoat it. It simulates a strict recruiter with 200 CVs in the inbox and tells you:

- Exact reasons your resume would be rejected
- Which bullet points are weak and why
- Skills you're missing that are non-negotiable for the role
- ATS landmines you didn't even know existed

<br/>

### ATS Score Engine — *"The robot that decides your fate before any human does"*

Gets you a hard match score between your resume and the job description.

```
ATS Match Score: 58/100   ← this is why you're not hearing back
ATS Match Score: 91/100   ← this is how you get the callback
```

<br/>

### Keyword Gap Detection — *"Words that get you hired vs words that don't"*

Pulls every high-frequency keyword from the job description and tells you exactly what's missing from your resume. ATS systems rank by keyword density. Now you know what to add.

<br/>

### AI-Generated Tailored Resume — *"What your resume should have looked like from the start"*

Generates a fully optimized, job-specific resume with:
- Action verbs that aren't "assisted" or "helped"
- Quantified impact (%, $, time saved, users served)
- Clean, ATS-readable structure
- Keywords that actually match the role

<br/>

### LaTeX Template Optimization — *"The feature no one else built"*

This is the one that required actual engineering.

Every other AI resume tool either outputs plain text or destroys your LaTeX formatting. Useless if you're using a university template or a standardized format your institution mandates.

AI CV Tailor patches your LaTeX file using comment markers — updating only content, never touching structure:

```latex
% START_SKILLS
  \item Python, Node.js, AWS, Docker, TypeScript   ← AI updates this
% END_SKILLS

% START_EXPERIENCE
  \item Engineered REST APIs serving 50k+ daily requests   ← and this
% END_EXPERIENCE

% START_PROJECTS
  \item Built full-stack SaaS with CI/CD, Docker, and Stripe   ← and this
% END_PROJECTS
```

Everything outside the markers? **Untouched.** Your formatting, packages, page layout — all intact.

<br/>

### Fully Automated via GitHub Actions — *"Set it up once, use it forever"*

```bash
git push   # that's it. that's the whole workflow.
```

No Python environment to maintain. No API keys to juggle locally. Push and outputs appear automatically in your repo artifacts.

---

## Project Structure

```
ai-cv-tailor/
│
├── input/
│   └── cv.txt                    # Your current resume (plain text)
│
├── jobs/
│   └── job1.txt                  # The job description you're targeting
│
├── templates/
│   └── resume.tex                # Your LaTeX template (with markers)
│
├── output/                       # Auto-generated on every push
│   ├── analysis.txt              # The brutal recruiter report
│   ├── improvements.txt          # Exactly what to fix and how
│   ├── final_cv.txt              # The optimized resume
│   ├── ats_score.txt             # Your match percentage
│   ├── keywords.txt              # What keywords you were missing
│   └── updated_resume.tex        # Your LaTeX resume, patched and ready
│
├── scripts/
│   ├── analyze.py                # Gemini analysis module
│   ├── score.py                  # ATS scoring engine
│   ├── improve.py                # Improvement generator
│   ├── patch_latex.py            # Marker-based LaTeX patcher
│   └── main.py                   # Orchestration entry point
│
├── .github/workflows/
│   └── cv_pipeline.yml           # The automation that runs it all
│
└── requirements.txt
```

---

## Getting Started

**1. Fork this repo**

```bash
git clone https://github.com/anubhavxdev/ai-cv-tailor.git
cd ai-cv-tailor
```

**2. Add your Gemini API key as a GitHub Secret**

```
Repository → Settings → Secrets and variables → Actions → New secret

Name : GEMINI_API_KEY
Value: your_key_here
```

**3. Drop your files in**

```bash
# Your current resume
nano input/cv.txt

# The job you actually want
nano jobs/job1.txt

# Your LaTeX template (add the markers — see below)
cp my_resume.tex templates/resume.tex
```

**4. Push**

```bash
git add .
git commit -m "time to stop getting rejected"
git push
```

Watch the Actions tab. Come back to a folder full of outputs.

---

## Setting Up LaTeX Markers

Add these comment markers anywhere in your `.tex` file:

```latex
\section{Technical Skills}
\begin{itemize}
% START_SKILLS
  \item Add your skills here
% END_SKILLS
\end{itemize}

\section{Experience}
\begin{itemize}
% START_EXPERIENCE
  \item Add your experience here
% END_EXPERIENCE
\end{itemize}

\section{Projects}
\begin{itemize}
% START_PROJECTS
  \item Add your projects here
% END_PROJECTS
\end{itemize}
```

The patcher replaces only what's inside the markers. Your document class, packages, header, footer, and every other line — completely safe.

---

## Example Output

**`ats_score.txt`**
```
══════════════════════════════════════
  ATS MATCH SCORE: 79 / 100
══════════════════════════════════════

  Matched  →  React, Node.js, MongoDB, REST API, Git, AWS
  Missing  →  TypeScript, Docker, CI/CD, Agile, Jest, Redis

  Verdict  →  Strong match. Add missing keywords to cross 90.
══════════════════════════════════════
```

**`analysis.txt`**
```
RECRUITER SIMULATION — REJECTION ANALYSIS
──────────────────────────────────────────
[HIGH RISK] No quantified impact in any experience bullet
[HIGH RISK] 6 ATS-critical keywords absent from resume
[MEDIUM]    Skills section includes tools not relevant to this role
[MEDIUM]    Project descriptions missing scope, scale, and outcome
[LOW]       Summary section is too generic — reads like a template
```

**`improvements.txt`**
```
BULLET REWRITES
───────────────
BEFORE → "Worked on the company's internal dashboard"
AFTER  → "Rebuilt internal analytics dashboard with React + D3.js,
           reducing report generation time from 12s to 1.4s"

BEFORE → "Helped with deployment"
AFTER  → "Automated deployment pipeline using GitHub Actions and Docker,
           cutting release cycle from 3 days to 4 hours"

KEYWORDS TO ADD
───────────────
TypeScript · Docker · Jest · Redis · Agile · CI/CD
```

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11 | Core processing engine |
| Google Gemini API | AI analysis and generation |
| GitHub Actions | Full pipeline automation |
| LaTeX | Resume template support |
| Plain text I/O | Simple, portable file handling |

---

## Roadmap

- [x] Gemini-powered recruiter analysis
- [x] ATS match scoring
- [x] Keyword gap detection
- [x] AI-driven bullet point rewrites
- [x] LaTeX marker-based safe patching
- [x] GitHub Actions full automation
- [ ] PDF auto-generation from patched LaTeX
- [ ] React web dashboard — drag, drop, done
- [ ] Multi-job comparison and ranking
- [ ] Chrome extension for one-click job description import
- [ ] SaaS launch with per-application pricing

---

## Why This Is Different

Every AI resume tool on the market does one of two things:

1. Spits out a new resume in a generic template and calls it "tailored"
2. Gives you vague feedback like *"add more keywords"* with no specifics

AI CV Tailor does neither. It works with your existing resume and your existing template — including strict LaTeX formats that no other tool can touch — and outputs precise, actionable improvements on every single push.

It's not a product trying to replace your resume. It's infrastructure for people who take job applications seriously.

---

<div align="center">

## Built by

**Anubhav Jaiswal**
B.Tech Computer Science · Lovely Professional University
Founder @ FounDev Studio · Tech Lead @ AWS Cloud Community · 2x Hackathon Winner

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-anubhavxdev-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/anubhavxdev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-anubhavxdev-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/anubhavxdev)
[![Portfolio](https://img.shields.io/badge/Portfolio-anubhavjaiswal.me-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://anubhavjaiswal.me)

<br/>

---

*If this saved you from sending one more generic resume into the void —*

[![Star this repo](https://img.shields.io/github/stars/anubhavxdev/ai-cv-tailor?style=for-the-badge&color=f59e0b&label=Star%20this%20repo)](https://github.com/anubhavxdev/ai-cv-tailor)

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
