import os
import google.generativeai as genai
from prompts import STRICT_PROMPT, IMPROVEMENT_PROMPT, FINAL_PROMPT

# Configure API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use correct working model
model = genai.GenerativeModel("gemini-flash-latest")

# ---------------- FILE HELPERS ---------------- #

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""

# ---------------- ATS SCORE ---------------- #

def calculate_ats_score(cv, jd):
    cv_words = set(cv.lower().split())
    jd_words = set(jd.lower().split())

    match = cv_words.intersection(jd_words)
    score = (len(match) / len(jd_words)) * 100 if jd_words else 0

    return round(score, 2)

# ---------------- KEYWORD GAP ---------------- #

def keyword_gap(cv, jd):
    cv_words = set(cv.lower().split())
    jd_words = set(jd.lower().split())

    missing = jd_words - cv_words
    return list(missing)[:20]

# ---------------- GEMINI CALL ---------------- #

def ask(prompt):
    try:
        response = model.generate_content(prompt)

        if response and hasattr(response, "text") and response.text:
            return response.text.strip()
        else:
            print("⚠️ Empty response:", response)
            return "No response from model"

    except Exception as e:
        print("❌ ERROR:", e)
        return "Error generating response"

# ---------------- MAIN LOGIC ---------------- #

cv = read_file("input/cv.txt")
jd = read_file("jobs/job1.txt")

if not cv.strip() or not jd.strip():
    print("❌ CV or Job Description is empty!")

# Create output folder
os.makedirs("output", exist_ok=True)

# ---------------- ATS SCORE ---------------- #

ats_score = calculate_ats_score(cv, jd)

with open("output/ats_score.txt", "w") as f:
    f.write(f"ATS Score: {ats_score}/100")

# ---------------- KEYWORDS ---------------- #

missing_keywords = keyword_gap(cv, jd)

with open("output/keywords.txt", "w") as f:
    f.write("Missing Keywords:\n")
    for word in missing_keywords:
        f.write(f"- {word}\n")

# ---------------- ANALYSIS ---------------- #

analysis_prompt = f"""
{STRICT_PROMPT}

CV:
{cv}

JOB DESCRIPTION:
{jd}
"""

analysis = ask(analysis_prompt)

with open("output/analysis.txt", "w", encoding="utf-8") as f:
    f.write(analysis)

# ---------------- IMPROVEMENTS ---------------- #

improvement_prompt = f"""
{IMPROVEMENT_PROMPT}

Analysis:
{analysis}

JOB DESCRIPTION:
{jd}
"""

improvements = ask(improvement_prompt)

with open("output/improvements.txt", "w", encoding="utf-8") as f:
    f.write(improvements)

# ---------------- FINAL CV ---------------- #

final_prompt = f"""
{FINAL_PROMPT}

ORIGINAL CV:
{cv}

JOB DESCRIPTION:
{jd}

IMPROVEMENTS:
{improvements}
"""

final_cv = ask(final_prompt)

with open("output/final_cv.txt", "w", encoding="utf-8") as f:
    f.write(final_cv)

print("🎉 All outputs generated successfully!")