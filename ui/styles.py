CSS = """
<style>

    /* =====================================================
       GLOBAL
       ===================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 15% 5%,
                rgba(88, 166, 255, 0.08),
                transparent 30%
            ),
            radial-gradient(
                circle at 85% 15%,
                rgba(168, 85, 247, 0.07),
                transparent 30%
            ),
            #080b10;

        color: #e6edf3;
    }

    .block-container {
        max-width: 1050px;
        padding-top: 2.5rem;
        padding-bottom: 5rem;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* =====================================================
       HERO
       ===================================================== */

    .hero {
        text-align: center;
        padding: 2rem 0 2.5rem 0;
    }

    .hero-badge {
        display: inline-block;

        padding: 0.35rem 0.8rem;
        margin-bottom: 1rem;

        border: 1px solid rgba(88, 166, 255, 0.25);
        border-radius: 999px;

        background: rgba(88, 166, 255, 0.08);

        color: #58a6ff;

        font-size: 0.78rem;
        font-weight: 600;

        letter-spacing: 0.5px;
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 750;

        letter-spacing: -2px;

        margin: 0;

        background: linear-gradient(
            90deg,
            #f0f6fc,
            #79c0ff,
            #d2a8ff
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        margin-top: 0.7rem;

        font-size: 1.05rem;

        color: #8b949e;

        letter-spacing: 0.2px;
    }


    /* =====================================================
       RESEARCH INPUT
       ===================================================== */

    .input-section {
        background: rgba(17, 24, 32, 0.75);

        border: 1px solid #212b36;

        border-radius: 16px;

        padding: 1.4rem;

        margin-top: 0.5rem;

        box-shadow:
            0 10px 40px rgba(0, 0, 0, 0.2);
    }

    .input-label {
        font-size: 0.9rem;

        font-weight: 600;

        color: #c9d1d9;

        margin-bottom: 0.5rem;
    }

    /* Text area */
    textarea {
        background-color: #0d1117 !important;

        border: 1px solid #30363d !important;

        border-radius: 10px !important;

        color: #f0f6fc !important;

        font-size: 1rem !important;
    }

    textarea:focus {
        border-color: #58a6ff !important;

        box-shadow:
            0 0 0 1px #58a6ff !important;
    }


    /* =====================================================
       BUTTON
       ===================================================== */

    .stButton > button {
        border-radius: 10px;

        border: 1px solid rgba(88, 166, 255, 0.35);

        background:
            linear-gradient(
                135deg,
                #1f6feb,
                #8957e5
            );

        color: white;

        font-weight: 650;

        height: 3rem;

        transition:
            transform 0.15s ease,
            box-shadow 0.15s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);

        box-shadow:
            0 8px 25px rgba(31, 111, 235, 0.25);
    }


    /* =====================================================
       PIPELINE
       ===================================================== */

    .section-title {
        font-size: 1.15rem;

        font-weight: 650;

        color: #f0f6fc;

        margin-top: 2rem;

        margin-bottom: 1rem;
    }

    .pipeline {
        display: flex;

        align-items: center;

        justify-content: center;

        gap: 0;

        margin: 1.2rem 0 2rem 0;
    }

    .pipeline-step {
        display: flex;

        align-items: center;

        gap: 0.55rem;

        padding: 0.65rem 0.9rem;

        border-radius: 10px;

        background: #111820;

        border: 1px solid #212b36;

        color: #c9d1d9;

        font-size: 0.85rem;
    }

    .pipeline-number {
        display: flex;

        align-items: center;

        justify-content: center;

        width: 24px;
        height: 24px;

        border-radius: 50%;

        background: rgba(88, 166, 255, 0.12);

        color: #58a6ff;

        font-size: 0.75rem;

        font-weight: 700;
    }

    .pipeline-arrow {
        color: #484f58;

        padding: 0 0.6rem;

        font-size: 1.1rem;
    }


    /* =====================================================
       STATUS
       ===================================================== */

    div[data-testid="stStatusWidget"] {
        background: #0d1117;

        border: 1px solid #212b36;

        border-radius: 12px;
    }


    /* =====================================================
       STAT CARDS
       ===================================================== */

    .stats-container {
        display: flex;

        gap: 1rem;

        margin: 1.5rem 0;
    }

    .stat-card {
        flex: 1;

        padding: 1rem 1.2rem;

        background: #0d1117;

        border: 1px solid #212b36;

        border-radius: 12px;
    }

    .stat-value {
        font-size: 1.5rem;

        font-weight: 700;

        color: #f0f6fc;
    }

    .stat-label {
        margin-top: 0.2rem;

        font-size: 0.8rem;

        color: #8b949e;
    }


    /* =====================================================
       SOURCES
       ===================================================== */

    .source-card {
        background: #0d1117;

        border: 1px solid #212b36;

        border-radius: 12px;

        padding: 1rem 1.1rem;

        margin-bottom: 0.7rem;

        transition:
            border-color 0.15s ease,
            transform 0.15s ease;
    }

    .source-card:hover {
        border-color: #30363d;

        transform: translateY(-1px);
    }

    .source-top {
        display: flex;

        align-items: center;

        gap: 0.6rem;

        margin-bottom: 0.45rem;
    }

    .source-number {
        display: inline-flex;

        align-items: center;

        justify-content: center;

        width: 25px;
        height: 25px;

        border-radius: 50%;

        background: rgba(88, 166, 255, 0.12);

        color: #58a6ff;

        font-size: 0.72rem;

        font-weight: 700;
    }

    .source-label {
        color: #c9d1d9;

        font-size: 0.82rem;

        font-weight: 600;
    }

    .source-url {
        color: #58a6ff;

        font-size: 0.82rem;

        text-decoration: none;

        word-break: break-all;
    }


    /* =====================================================
       RESEARCH REPORT
       ===================================================== */

    .report-wrapper {
        background: #0d1117;

        border: 1px solid #212b36;

        border-radius: 16px;

        padding: 2rem 2.2rem;

        margin-top: 1rem;

        box-shadow:
            0 15px 50px rgba(0, 0, 0, 0.18);
    }

    .report-label {
        display: inline-block;

        padding: 0.3rem 0.65rem;

        border-radius: 6px;

        background: rgba(168, 85, 247, 0.1);

        color: #d2a8ff;

        font-size: 0.72rem;

        font-weight: 650;

        letter-spacing: 0.4px;

        margin-bottom: 1rem;
    }


    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {
        text-align: center;

        margin-top: 3rem;

        color: #484f58;

        font-size: 0.75rem;
    }

</style>
"""