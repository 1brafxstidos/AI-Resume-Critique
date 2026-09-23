def calculate_keyword_score(
    resume_text,
    job_skills
):
    """
    Calculate keyword overlap.
    """

    if not job_skills:
        return 0

    resume_lower = resume_text.lower()

    matches = 0

    for skill in job_skills:

        if skill.lower() in resume_lower:
            matches += 1

    score = (
        matches / len(job_skills)
    ) * 100

    return round(score, 2)


def calculate_ats_readiness(resume_text):
    """
    Estimate basic ATS readiness.

    This is NOT an actual ATS score.
    Different ATS platforms behave differently.
    """

    score = 100

    text_length = len(resume_text)

    if text_length < 500:
        score -= 20

    if text_length > 15000:
        score -= 10

    sections = [
        "experience",
        "education",
        "skills"
    ]

    for section in sections:

        if section not in resume_text.lower():
            score -= 10

    return max(score, 0)


def calculate_overall_score(
    semantic_score,
    skill_score,
    keyword_score,
    ats_score
):
    """
    Calculate the overall resume-job match score.
    """

    score = (
        semantic_score * 0.35
        + skill_score * 0.30
        + keyword_score * 0.20
        + ats_score * 0.15
    )

    return round(score, 2)