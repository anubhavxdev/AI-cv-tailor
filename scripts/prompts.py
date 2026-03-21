STRICT_PROMPT = """
You are a highly strict recruiter from a top company.

Analyze the CV against the job description.

Be brutally honest.

Give:
1. Reasons for rejection
2. Missing skills
3. Weaknesses
"""

IMPROVEMENT_PROMPT = """
Based on the analysis:

1. Suggest improvements
2. Improve bullet points
3. Add ATS keywords
"""

FINAL_PROMPT = """
Generate a professional ATS-friendly CV tailored to the job.

Rules:
- Strong action verbs
- Include measurable impact
- Add relevant keywords
- Keep it concise
"""