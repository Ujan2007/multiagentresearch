import sys
import os

# =========================================================
# PROJECT ROOT
# =========================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, PROJECT_ROOT)


# =========================================================
# IMPORTS
# =========================================================

import streamlit as st

from agents.search_agent import get_search_agent
from agents.reader_agent import get_content
from agents.writer_agent import write_research

from ui.styles import CSS


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Research Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(CSS, unsafe_allow_html=True)


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
<div class="hero">

    <div class="hero-badge">
        ✦ AI-POWERED RESEARCH
    </div>

    <h1 class="hero-title">
        Research Agent
    </h1>

    <div class="hero-subtitle">
        A multi-agent system that searches, reads and synthesizes
        information from the web.
    </div>

</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# PIPELINE VISUALIZATION
# =========================================================

st.markdown(
    """
<div class="pipeline">

    <div class="pipeline-step">
        <div class="pipeline-number">1</div>
        <span>Search</span>
    </div>

    <div class="pipeline-arrow">→</div>

    <div class="pipeline-step">
        <div class="pipeline-number">2</div>
        <span>Read</span>
    </div>

    <div class="pipeline-arrow">→</div>

    <div class="pipeline-step">
        <div class="pipeline-number">3</div>
        <span>Synthesize</span>
    </div>

</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# INPUT SECTION
# =========================================================

st.markdown(
    '<div class="input-section">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="input-label">What would you like to research?</div>',
    unsafe_allow_html=True
)

question = st.text_area(
    label="Research question",
    placeholder=(
        "Ask anything... "
        "e.g. How do neural networks learn?"
    ),
    height=120,
    label_visibility="collapsed"
)

research_button = st.button(
    "🔎  Start Research",
    type="primary",
    use_container_width=True
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)


# =========================================================
# MAIN PIPELINE
# =========================================================

if research_button:

    if not question.strip():

        st.warning(
            "Enter a research question to get started."
        )

        st.stop()


    # -----------------------------------------------------
    # AGENT 1
    # -----------------------------------------------------

    with st.status(
        "🔎 Searching the web...",
        expanded=True
    ) as status:

        st.write(
            "Finding relevant sources for your question..."
        )

        try:

            sharedmemory = get_search_agent(question)

            urls = sharedmemory.get("urls", [])

            st.write(
                f"Found {len(urls)} relevant sources."
            )

            status.update(
                label="✓ Web search completed",
                state="complete"
            )

        except Exception as e:

            status.update(
                label="✕ Search failed",
                state="error"
            )

            st.error(str(e))

            st.stop()


    # -----------------------------------------------------
    # AGENT 2
    # -----------------------------------------------------

    with st.status(
        "📖 Reading sources...",
        expanded=True
    ) as status:

        urls = sharedmemory.get("urls", [])

        st.write(
            f"Extracting useful information from "
            f"{len(urls)} sources..."
        )

        try:

            sharedmemory = get_content(sharedmemory)

            content = sharedmemory.get(
                "content",
                []
            )

            st.write(
                f"Processed {len(content)} sources."
            )

            status.update(
                label="✓ Sources processed",
                state="complete"
            )

        except Exception as e:

            status.update(
                label="✕ Source extraction failed",
                state="error"
            )

            st.error(str(e))

            st.stop()


    # -----------------------------------------------------
    # AGENT 3
    # -----------------------------------------------------

    with st.status(
        "✍️ Synthesizing research...",
        expanded=True
    ) as status:

        st.write(
            "Combining the extracted information "
            "into a research report..."
        )

        try:

            research = write_research(
                sharedmemory
            )

            status.update(
                label="✓ Research synthesized",
                state="complete"
            )

        except Exception as e:

            status.update(
                label="✕ Synthesis failed",
                state="error"
            )

            st.error(str(e))

            st.stop()


    # =====================================================
    # RESULTS
    # =====================================================

    st.markdown(
        '<div class="section-title">Research complete</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # STATS
    # -----------------------------------------------------

    source_count = len(
        sharedmemory.get("urls", [])
    )

    content_count = len(
        sharedmemory.get("content", [])
    )

    st.markdown(
        f"""
<div class="stats-container">

    <div class="stat-card">

        <div class="stat-value">
            {source_count}
        </div>

        <div class="stat-label">
            Sources discovered
        </div>

    </div>


    <div class="stat-card">

        <div class="stat-value">
            {content_count}
        </div>

        <div class="stat-label">
            Sources analyzed
        </div>

    </div>


    <div class="stat-card">

        <div class="stat-value">
            3
        </div>

        <div class="stat-label">
            AI agents involved
        </div>

    </div>

</div>
""",
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # SOURCES
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">📚 Sources</div>',
        unsafe_allow_html=True
    )

    urls = sharedmemory.get("urls", [])

    if urls:

        for i, url in enumerate(
            urls,
            start=1
        ):

            st.markdown(
                f"""
<div class="source-card">

    <div class="source-top">

        <div class="source-number">
            {i}
        </div>

        <div class="source-label">
            Web source
        </div>

    </div>

    <a
        class="source-url"
        href="{url}"
        target="_blank"
    >
        {url}
    </a>

</div>
""",
                unsafe_allow_html=True
            )

    else:

        st.info(
            "No sources were returned."
        )


    # -----------------------------------------------------
    # REPORT
    # -----------------------------------------------------

    st.markdown(
        '<div class="section-title">📄 Research Report</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="report-wrapper">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="report-label">GENERATED RESEARCH</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        research
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # FOOTER
    # -----------------------------------------------------

    st.markdown(
        """
<div class="footer">
    Research Agent · Multi-Agent AI Research System
</div>
""",
        unsafe_allow_html=True
    )