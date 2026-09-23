import re


SKILLS_DATABASE = [
    "python",
    "java",
    "javascript",
    "typescript",
    "c++",
    "c#",

    "react",
    "next.js",
    "node.js",
    "fastapi",
    "django",
    "flask",

    "html",
    "css",
    "tailwind",

    "sql",
    "postgresql",
    "mysql",
    "mongodb",

    "aws",
    "azure",
    "gcp",

    "docker",
    "kubernetes",

    "git",
    "github",

    "machine learning",
    "deep learning",
    "artificial intelligence",

    "tensorflow",
    "pytorch",
    "scikit-learn",

    "natural language processing",
    "nlp",
    "computer vision",

    "llm",
    "generative ai",

    "langchain",

    "rest api",
    "graphql",

    "figma",
    "ui/ux",
    "product design",
]


def extract_keywords(text):
    """
    Find skills mentioned in the job description.
    """

    text_lower = text.lower()

    found_skills = []

    for skill in SKILLS_DATABASE:

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return list(set(found_skills))