import os
import google.generativeai as genai
from prompts import STRICT_PROMPT, IMPROVEMENT_PROMPT, FINAL_PROMPT

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

# Read file helper
def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""

# Safe API call
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

# Read inputs
cv = read_file("input/cv.txt")
jd = read_file("jobs/job1.txt")

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Create empty files first (prevents GitHub error)
open("output/analysis.txt", "w").close()
open("output/improvements.txt", "w").close()
open("output/final_cv.txt", "w").close()

# ----------- STEP 1: ANALYSIS ----------- #
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

# ----------- STEP 2: IMPROVEMENTS ----------- #
improvement_prompt = f"""
{IMPROVEMENT_PROMPT}

Analysis:
{analysis}
"""

improvements = ask(improvement_prompt)

with open("output/improvements.txt", "w", encoding="utf-8") as f:
    f.write(improvements)

# ----------- STEP 3: FINAL CV ----------- #
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

print("🎉 Process Completed Successfully")