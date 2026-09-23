import os
import json

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

print("API KEY FOUND:", os.getenv("OPENAI_API_KEY") is not None)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def critique_resume(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert technical recruiter,
professional resume writer, and AI career assistant.

Your task is to critically analyze a resume
against a target job description.

Do not invent experience, skills,
achievements, numbers, employers,
certifications, or technologies.

If something is missing, say that it is missing.

RESUME:
----------------
{resume_text}
----------------

JOB DESCRIPTION:
----------------
{job_description}
----------------

Analyze:

1. Professional summary
2. Technical skills
3. Work experience
4. Projects
5. Education
6. Achievements
7. Keywords
8. ATS readiness
9. Relevance to the target role
10. Writing quality

Identify:

- Strengths
- Weaknesses
- Missing keywords
- ATS issues
- Recommendations
- Weak resume bullets
- Suggested rewrites

Return ONLY valid JSON.

Use exactly this structure:

{{
    "overall_assessment": "",

    "strengths": [],

    "weaknesses": [],

    "missing_keywords": [],

    "ats_issues": [],

    "recommendations": [],

    "rewrites": [
        {{
            "original": "",
            "improved": "",
            "reason": ""
        }}
    ]
}}
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    result = response.output_text

    try:
        return json.loads(result)

    except json.JSONDecodeError:
        print("AI returned invalid JSON:")
        print(result)

        return {
            "overall_assessment": result,
            "strengths": [],
            "weaknesses": [],
            "missing_keywords": [],
            "ats_issues": [],
            "recommendations": [],
            "rewrites": []
        }