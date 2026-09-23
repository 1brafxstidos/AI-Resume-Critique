from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the embedding model once.
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def calculate_similarity(
    resume_text,
    job_description
):
    """
    Calculate semantic similarity between
    the resume and job description.
    """

    embeddings = model.encode([
        resume_text,
        job_description
    ])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(
        float(similarity) * 100,
        2
    )


def find_resume_skills(
    resume_text,
    job_skills
):
    """
    Find which required job skills
    are present in the resume.
    """

    resume_lower = resume_text.lower()

    matched_skills = []

    for skill in job_skills:

        if skill.lower() in resume_lower:
            matched_skills.append(skill)

    return matched_skills


def calculate_skill_match(
    resume_skills,
    job_skills
):
    """
    Calculate percentage of required skills
    found in the resume.
    """

    if not job_skills:
        return 0

    matched = set(resume_skills)

    required = set(job_skills)

    score = (
        len(matched & required)
        / len(required)
    ) * 100

    return round(score, 2)