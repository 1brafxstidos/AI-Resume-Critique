import streamlit as st

from backend.resume_parser import (
    extract_resume_text
)

from backend.job_parser import (
    extract_keywords
)

from backend.matcher import (
    calculate_similarity,
    find_resume_skills,
    calculate_skill_match
)

from backend.scoring import (
    calculate_keyword_score,
    calculate_ats_readiness,
    calculate_overall_score
)

from backend.ai_critic import (
    critique_resume
)

from utils.text_cleaner import (
    clean_text
)


# -----------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------

st.set_page_config(
    page_title="AI Resume Critiquer",
    page_icon="📄",
    layout="wide"
)


# -----------------------------------------
# HEADER
# -----------------------------------------

st.title("AI Resume Critiquer")

st.write(
    "Analyze your resume against a target "
    "job description using AI, NLP and "
    "semantic matching."
)


st.divider()


# -----------------------------------------
# INPUTS
# -----------------------------------------

resume_file = st.file_uploader(
    "Upload your resume",
    type=[
        "pdf",
        "docx",
        "txt"
    ]
)


job_description = st.text_area(
    "Paste the target job description",
    height=300,
    placeholder=(
        "Paste the complete job description here..."
    )
)


analyze_button = st.button(
    "Analyze Resume",
    type="primary"
)


# -----------------------------------------
# ANALYSIS
# -----------------------------------------

if analyze_button:

    if resume_file is None:

        st.error(
            "Please upload your resume."
        )

        st.stop()


    if not job_description.strip():

        st.error(
            "Please enter a job description."
        )

        st.stop()


    # -------------------------------------
    # PROCESSING
    # -------------------------------------

    with st.spinner(
        "Analyzing your resume..."
    ):

        # Extract resume
        resume_text = (
            extract_resume_text(
                resume_file
            )
        )

        # Clean text
        resume_text = clean_text(
            resume_text
        )

        job_description = clean_text(
            job_description
        )


        # ---------------------------------
        # JOB SKILLS
        # ---------------------------------

        job_skills = extract_keywords(
            job_description
        )


        # ---------------------------------
        # RESUME SKILLS
        # ---------------------------------

        resume_skills = find_resume_skills(
            resume_text,
            job_skills
        )


        # ---------------------------------
        # SKILL SCORE
        # ---------------------------------

        skill_score = calculate_skill_match(
            resume_skills,
            job_skills
        )


        # ---------------------------------
        # SEMANTIC SCORE
        # ---------------------------------

        semantic_score = calculate_similarity(
            resume_text,
            job_description
        )


        # ---------------------------------
        # KEYWORD SCORE
        # ---------------------------------

        keyword_score = calculate_keyword_score(
            resume_text,
            job_skills
        )


        # ---------------------------------
        # ATS READINESS
        # ---------------------------------

        ats_score = calculate_ats_readiness(
            resume_text
        )


        # ---------------------------------
        # OVERALL SCORE
        # ---------------------------------

        overall_score = calculate_overall_score(
            semantic_score,
            skill_score,
            keyword_score,
            ats_score
        )


        # ---------------------------------
        # AI CRITIQUE
        # ---------------------------------

        critique = critique_resume(
            resume_text,
            job_description
        )


    # -------------------------------------
    # RESULTS
    # -------------------------------------

    st.header("Resume Analysis")


    # -------------------------------------
    # SCORE CARDS
    # -------------------------------------

    col1, col2, col3, col4, col5 = (
        st.columns(5)
    )


    col1.metric(
        "Overall Match",
        f"{overall_score}%"
    )


    col2.metric(
        "Semantic Match",
        f"{semantic_score}%"
    )


    col3.metric(
        "Skill Match",
        f"{skill_score}%"
    )


    col4.metric(
        "Keywords",
        f"{keyword_score}%"
    )


    col5.metric(
        "ATS Readiness",
        f"{ats_score}%"
    )


    st.divider()


    # -------------------------------------
    # SKILLS
    # -------------------------------------

    st.header("Skill Analysis")


    st.write(
        "**Skills detected in job:**"
    )

    if job_skills:

        st.write(
            ", ".join(job_skills)
        )

    else:

        st.info(
            "No skills were detected."
        )


    st.write(
        "**Skills found in resume:**"
    )

    if resume_skills:

        st.write(
            ", ".join(resume_skills)
        )

    else:

        st.warning(
            "No matching skills were found."
        )


    # -------------------------------------
    # STRENGTHS
    # -------------------------------------

    st.header("Strengths")


    for strength in critique["strengths"]:

        st.success(
            strength
        )


    # -------------------------------------
    # WEAKNESSES
    # -------------------------------------

    st.header("Weaknesses")


    for weakness in critique["weaknesses"]:

        st.warning(
            weakness
        )


    # -------------------------------------
    # MISSING KEYWORDS
    # -------------------------------------

    st.header("Missing Keywords")


    for keyword in critique[
        "missing_keywords"
    ]:

        st.write(
            f"• {keyword}"
        )


    # -------------------------------------
    # ATS ISSUES
    # -------------------------------------

    st.header("ATS Issues")


    for issue in critique[
        "ats_issues"
    ]:

        st.write(
            f"• {issue}"
        )


    # -------------------------------------
    # RECOMMENDATIONS
    # -------------------------------------

    st.header(
        "AI Recommendations"
    )


    for recommendation in critique[
        "recommendations"
    ]:

        st.write(
            f"→ {recommendation}"
        )


    # -------------------------------------
    # REWRITES
    # -------------------------------------

    st.header(
        "Suggested Resume Rewrites"
    )


    for rewrite in critique[
        "rewrites"
    ]:

        with st.expander(
            "View suggested rewrite"
        ):

            st.write(
                "**Original**"
            )

            st.write(
                rewrite["original"]
            )


            st.write(
                "**Improved**"
            )

            st.success(
                rewrite["improved"]
            )


            st.write(
                "**Why this is better**"
            )

            st.caption(
                rewrite["reason"]
            )