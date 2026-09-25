def get_css(theme: str = "dark") -> str:
    """
    Returns the full CSS block for the app, themed for either
    'dark' or 'light' mode.
    """

    if theme == "light":
        vars_css = """
        --bg-primary: #f5f7fa;
        --bg-gradient-1: rgba(31, 111, 235, 0.06);
        --bg-gradient-2: rgba(139, 92, 246, 0.05);
        --text-primary: #0d1117;
        --text-secondary: #57606a;
        --text-muted: #8b949e;
        --card-bg: #ffffff;
        --card-bg-alt: #f6f8fa;
        --border-color: #d0d7de;
        --border-color-soft: #e5e9ee;
        --accent: #1f6feb;
        --accent-soft: rgba(31, 111, 235, 0.08);
        --accent-2: #8957e5;
        --accent-2-soft: rgba(137, 87, 229, 0.08);
        --shadow-color: rgba(140, 149, 159, 0.25);
        --input-bg: #ffffff;
        --notice-bg: rgba(31, 111, 235, 0.06);
        --notice-border: rgba(31, 111, 235, 0.25);
        --notice-text: #24292f;
        """
    else:
        vars_css = """
        --bg-primary: #080b10;
        --bg-gradient-1: rgba(88, 166, 255, 0.08);
        --bg-gradient-2: rgba(168, 85, 247, 0.07);
        --text-primary: #e6edf3;
        --text-secondary: #c9d1d9;
        --text-muted: #8b949e;
        --card-bg: #0d1117;
        --card-bg-alt: #111820;
        --border-color: #212b36;
        --border-color-soft: #30363d;
        --accent: #58a6ff;
        --accent-soft: rgba(88, 166, 255, 0.12);
        --accent-2: #d2a8ff;
        --accent-2-soft: rgba(168, 85, 247, 0.1);
        --shadow-color: rgba(0, 0, 0, 0.35);
        --input-bg: #0d1117;
        --notice-bg: rgba(88, 166, 255, 0.07);
        --notice-border: rgba(88, 166, 255, 0.25);
        --notice-text: #c9d1d9;
        """

    return f"""
<style>

    :root {{
        {vars_css}
    }}

    /* =====================================================
       GLOBAL
       ===================================================== */

    .stApp {{
        background:
            radial-gradient(circle at 15% 5%, var(--bg-gradient-1), transparent 30%),
            radial-gradient(circle at 85% 15%, var(--bg-gradient-2), transparent 30%),
            var(--bg-primary);
        color: var(--text-primary);
        transition: background 0.25s ease, color 0.25s ease;
    }}

    .block-container {{
        max-width: 1050px;
        padding-top: 1.5rem;
        padding-bottom: 5rem;
    }}

    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}

    /* =====================================================
       TOP BAR / THEME TOGGLE
       ===================================================== */

    .topbar {{
        display: flex;
        justify-content: flex-end;
        align-items: center;
        margin-bottom: -0.5rem;
    }}

    div[data-testid="stHorizontalBlock"] .stButton > button {{
        height: 2.4rem;
        font-size: 0.85rem;
        background: var(--card-bg-alt);
        border: 1px solid var(--border-color);
        color: var(--text-secondary);
        font-weight: 600;
        box-shadow: none;
    }}

    div[data-testid="stHorizontalBlock"] .stButton > button:hover {{
        border-color: var(--accent);
        color: var(--accent);
        transform: none;
        box-shadow: none;
    }}

    /* =====================================================
       NOTICE BANNER
       ===================================================== */

    .notice-banner {{
        display: flex;
        gap: 0.7rem;
        align-items: flex-start;

        background: var(--notice-bg);
        border: 1px solid var(--notice-border);
        border-radius: 12px;

        padding: 0.85rem 1.1rem;
        margin: 0.5rem 0 1.5rem 0;

        font-size: 0.85rem;
        line-height: 1.5;
        color: var(--notice-text);
    }}

    .notice-icon {{
        font-size: 1rem;
        line-height: 1.5;
    }}

    /* =====================================================
       HERO
       ===================================================== */

    .hero {{
        text-align: center;
        padding: 1rem 0 2rem 0;
    }}

    .hero-badge {{
        display: inline-block;
        padding: 0.35rem 0.8rem;
        margin-bottom: 1rem;
        border: 1px solid var(--notice-border);
        border-radius: 999px;
        background: var(--accent-soft);
        color: var(--accent);
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.5px;
    }}

    .hero-title {{
        font-size: 3.2rem;
        font-weight: 750;
        letter-spacing: -2px;
        margin: 0;
        background: linear-gradient(90deg, var(--text-primary), var(--accent), var(--accent-2));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .hero-subtitle {{
        margin-top: 0.7rem;
        font-size: 1.05rem;
        color: var(--text-muted);
        letter-spacing: 0.2px;
    }}

    /* =====================================================
       RESEARCH INPUT
       ===================================================== */

    .input-section {{
        background: color-mix(in srgb, var(--card-bg) 85%, transparent);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 1.4rem;
        margin-top: 0.5rem;
        box-shadow: 0 10px 40px var(--shadow-color);
    }}

    .input-label {{
        font-size: 0.9rem;
        font-weight: 600;
        color: var(--text-secondary);
        margin-bottom: 0.5rem;
    }}

    textarea {{
        background-color: var(--input-bg) !important;
        border: 1px solid var(--border-color-soft) !important;
        border-radius: 10px !important;
        color: var(--text-primary) !important;
        font-size: 1rem !important;
    }}

    textarea:focus {{
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 1px var(--accent) !important;
    }}

    /* =====================================================
       PRIMARY BUTTON
       ===================================================== */

    .stButton > button[kind="primary"] {{
        border-radius: 10px;
        border: 1px solid var(--notice-border);
        background: linear-gradient(135deg, var(--accent), var(--accent-2));
        color: white;
        font-weight: 650;
        height: 3rem;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }}

    .stButton > button[kind="primary"]:hover {{
        transform: translateY(-1px);
        box-shadow: 0 8px 25px var(--shadow-color);
    }}

    /* =====================================================
       PIPELINE
       ===================================================== */

    .section-title {{
        font-size: 1.15rem;
        font-weight: 650;
        color: var(--text-primary);
        margin-top: 2rem;
        margin-bottom: 1rem;
    }}

    .pipeline {{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 0;
        margin: 1.2rem 0 2rem 0;
    }}

    .pipeline-step {{
        display: flex;
        align-items: center;
        gap: 0.55rem;
        padding: 0.65rem 0.9rem;
        border-radius: 10px;
        background: var(--card-bg-alt);
        border: 1px solid var(--border-color);
        color: var(--text-secondary);
        font-size: 0.85rem;
    }}

    .pipeline-number {{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        background: var(--accent-soft);
        color: var(--accent);
        font-size: 0.75rem;
        font-weight: 700;
    }}

    .pipeline-arrow {{
        color: var(--text-muted);
        padding: 0 0.6rem;
        font-size: 1.1rem;
    }}

    /* =====================================================
       STATUS
       ===================================================== */

    div[data-testid="stStatusWidget"] {{
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
    }}

    /* =====================================================
       STAT CARDS
       ===================================================== */

    .stats-container {{
        display: flex;
        gap: 1rem;
        margin: 1.5rem 0;
        flex-wrap: wrap;
    }}

    .stat-card {{
        flex: 1;
        min-width: 140px;
        padding: 1rem 1.2rem;
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
    }}

    .stat-value {{
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--text-primary);
    }}

    .stat-label {{
        margin-top: 0.2rem;
        font-size: 0.8rem;
        color: var(--text-muted);
    }}

    /* =====================================================
       SOURCES
       ===================================================== */

    .source-card {{
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 12px;
        padding: 1rem 1.1rem;
        margin-bottom: 0.7rem;
        transition: border-color 0.15s ease, transform 0.15s ease;
    }}

    .source-card:hover {{
        border-color: var(--border-color-soft);
        transform: translateY(-1px);
    }}

    .source-top {{
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 0.45rem;
    }}

    .source-number {{
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 25px;
        height: 25px;
        border-radius: 50%;
        background: var(--accent-soft);
        color: var(--accent);
        font-size: 0.72rem;
        font-weight: 700;
    }}

    .source-label {{
        color: var(--text-secondary);
        font-size: 0.82rem;
        font-weight: 600;
    }}

    .source-url {{
        color: var(--accent);
        font-size: 0.82rem;
        text-decoration: none;
        word-break: break-all;
    }}

    /* =====================================================
       RESEARCH REPORT
       ===================================================== */

    .report-wrapper {{
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 2rem 2.2rem;
        margin-top: 1rem;
        box-shadow: 0 15px 50px var(--shadow-color);
    }}

    .report-label {{
        display: inline-block;
        padding: 0.3rem 0.65rem;
        border-radius: 6px;
        background: var(--accent-2-soft);
        color: var(--accent-2);
        font-size: 0.72rem;
        font-weight: 650;
        letter-spacing: 0.4px;
        margin-bottom: 1rem;
    }}

    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {{
        text-align: center;
        margin-top: 3rem;
        color: var(--text-muted);
        font-size: 0.75rem;
    }}

</style>
"""


# Backwards-compatible default export (dark theme), in case other
# modules still import CSS directly.
CSS = get_css("dark")