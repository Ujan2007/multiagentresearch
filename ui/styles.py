def get_css(theme: str = "dark") -> str:
    """
    Returns the full CSS block for the app, themed for either
    'dark' or 'light' mode.
    """

    if theme == "light":
        vars_css = """
        --bg-primary: #f6f7fb;
        --bg-gradient-1: rgba(59, 130, 246, 0.10);
        --bg-gradient-2: rgba(139, 92, 246, 0.08);
        --bg-gradient-3: rgba(236, 72, 153, 0.05);
        --text-primary: #14171f;
        --text-secondary: #4b5361;
        --text-muted: #8a92a3;
        --card-bg: #ffffff;
        --card-bg-alt: #eef1f6;
        --border-color: #e2e6ee;
        --border-color-soft: #d5dae4;
        --accent: #3b6fe0;
        --accent-rgb: 59, 111, 224;
        --accent-soft: rgba(59, 111, 224, 0.08);
        --accent-2: #8957e5;
        --accent-2-rgb: 137, 87, 229;
        --accent-2-soft: rgba(137, 87, 229, 0.08);
        --shadow-color: rgba(30, 41, 59, 0.10);
        --shadow-color-strong: rgba(30, 41, 59, 0.16);
        --input-bg: #ffffff;
        --notice-bg: rgba(59, 111, 224, 0.06);
        --notice-border: rgba(59, 111, 224, 0.20);
        --notice-text: #33415c;
        """
    else:
        vars_css = """
        --bg-primary: #090b10;
        --bg-gradient-1: rgba(69, 140, 255, 0.10);
        --bg-gradient-2: rgba(168, 85, 247, 0.09);
        --bg-gradient-3: rgba(236, 72, 153, 0.05);
        --text-primary: #eef2f7;
        --text-secondary: #b6bfcc;
        --text-muted: #7c8695;
        --card-bg: #10141c;
        --card-bg-alt: #141a24;
        --border-color: #212836;
        --border-color-soft: #2a3242;
        --accent: #5b9dff;
        --accent-rgb: 91, 157, 255;
        --accent-soft: rgba(91, 157, 255, 0.10);
        --accent-2: #c9a3ff;
        --accent-2-rgb: 201, 163, 255;
        --accent-2-soft: rgba(201, 163, 255, 0.09);
        --shadow-color: rgba(0, 0, 0, 0.35);
        --shadow-color-strong: rgba(0, 0, 0, 0.5);
        --input-bg: #0d1117;
        --notice-bg: rgba(91, 157, 255, 0.07);
        --notice-border: rgba(91, 157, 255, 0.22);
        --notice-text: #c3cbd8;
        """

    return f"""
<style>

    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Sora:wght@600;700;800&display=swap');

    :root {{
        {vars_css}
    }}

    * {{
        font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    /* =====================================================
       ANIMATED BACKGROUND
       ===================================================== */

    @keyframes drift {{
        0%   {{ background-position: 0% 0%, 100% 0%, 50% 100%; }}
        50%  {{ background-position: 30% 20%, 70% 30%, 40% 70%; }}
        100% {{ background-position: 0% 0%, 100% 0%, 50% 100%; }}
    }}

    .stApp {{
        background:
            radial-gradient(circle at 15% 5%, var(--bg-gradient-1), transparent 32%),
            radial-gradient(circle at 85% 15%, var(--bg-gradient-2), transparent 32%),
            radial-gradient(circle at 50% 100%, var(--bg-gradient-3), transparent 35%),
            var(--bg-primary);
        background-size: 180% 180%, 180% 180%, 180% 180%, 100% 100%;
        animation: drift 22s ease-in-out infinite;
        color: var(--text-primary);
        transition: background-color 0.35s ease, color 0.35s ease;
    }}

    .block-container {{
        max-width: 1050px;
        padding-top: 1.5rem;
        padding-bottom: 5rem;
    }}

    #MainMenu {{ visibility: hidden; }}
    footer {{ visibility: hidden; }}

    ::selection {{
        background: var(--accent-soft);
        color: var(--accent);
    }}

    /* =====================================================
       TOP BAR / THEME TOGGLE & GITHUB
       ===================================================== */

    div[data-testid="stHorizontalBlock"] {{
        margin-top: 1.4rem;
    }}

    div[data-testid="stHorizontalBlock"] .stButton > button,
    div[data-testid="stHorizontalBlock"] .stLinkButton > a {{
        height: 2.6rem;
        font-size: 0.95rem;
        font-weight: 600;
        background: var(--card-bg-alt);
        border: 1px solid var(--border-color);
        color: var(--text-secondary);
        box-shadow: none;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
    }}

    div[data-testid="stHorizontalBlock"] .stButton > button:hover,
    div[data-testid="stHorizontalBlock"] .stLinkButton > a:hover {{
        border-color: var(--accent);
        color: var(--accent);
        background: var(--accent-soft);
        transform: translateY(-2px) scale(1.03);
        box-shadow: 0 6px 16px var(--shadow-color);
    }}

    div[data-testid="stHorizontalBlock"] .stButton > button:active,
    div[data-testid="stHorizontalBlock"] .stLinkButton > a:active {{
        transform: translateY(0) scale(0.98);
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
        border-radius: 14px;

        padding: 1rem 1.3rem;
        margin: 0.5rem 0 1.7rem 0;

        font-size: 0.98rem;
        line-height: 1.6;
        color: var(--notice-text);

        animation: fadeInUp 0.5s ease both;
        animation-delay: 0.15s;
    }}

    .notice-icon {{
        font-size: 1rem;
        line-height: 1.55;
    }}

    /* =====================================================
       HERO
       ===================================================== */

    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(12px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
    }}

    .hero {{
        text-align: center;
        padding: 1.2rem 0 2rem 0;
    }}

    .hero-badge {{
        display: inline-block;
        padding: 0.4rem 0.9rem;
        margin-bottom: 1.2rem;
        border: 1px solid var(--notice-border);
        border-radius: 999px;
        background: var(--accent-soft);
        color: var(--accent);
        font-size: 0.88rem;
        font-weight: 700;
        letter-spacing: 0.6px;
        animation: fadeInUp 0.5s ease both;
    }}

    .hero-title {{
        font-family: 'Sora', 'Manrope', sans-serif;
        font-size: 4.2rem;
        font-weight: 800;
        letter-spacing: -2.2px;
        line-height: 1.08;
        margin: 0;
        background: linear-gradient(90deg, var(--text-primary), var(--accent), var(--accent-2));
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: fadeInUp 0.6s ease both, shimmer 6s linear infinite;
        animation-delay: 0.05s, 0.6s;
    }}

    @keyframes shimmer {{
        0%   {{ background-position: 0% center; }}
        100% {{ background-position: 200% center; }}
    }}

    .hero-subtitle {{
        margin-top: 0.85rem;
        font-size: 1.3rem;
        font-weight: 500;
        color: var(--text-muted);
        letter-spacing: 0.1px;
        max-width: 640px;
        margin-left: auto;
        margin-right: auto;
        animation: fadeInUp 0.55s ease both;
        animation-delay: 0.1s;
    }}

    /* =====================================================
       RESEARCH INPUT
       ===================================================== */

    .input-section {{
        background: color-mix(in srgb, var(--card-bg) 88%, transparent);
        border: 1px solid var(--border-color);
        border-radius: 18px;
        padding: 1.5rem;
        margin-top: 0.5rem;
        box-shadow: 0 10px 40px var(--shadow-color);
        transition: border-color 0.25s ease, box-shadow 0.25s ease;
    }}

    .input-section:hover {{
        border-color: var(--border-color-soft);
    }}

    .input-label {{
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--text-secondary);
        margin-bottom: 0.6rem;
        letter-spacing: 0.1px;
    }}

    textarea {{
        background-color: var(--input-bg) !important;
        border: 1px solid var(--border-color-soft) !important;
        border-radius: 12px !important;
        color: var(--text-primary) !important;
        font-size: 1.15rem !important;
        font-weight: 450 !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
    }}

    textarea:focus {{
        border-color: var(--accent) !important;
        box-shadow: 0 0 0 3px var(--accent-soft) !important;
    }}

    /* =====================================================
       PRIMARY BUTTON
       ===================================================== */

    .stButton > button[kind="primary"] {{
        border-radius: 12px;
        border: 1px solid rgba(16, 185, 129, 0.35);
        background: linear-gradient(135deg, #0ea5a0, #10b981);
        background-size: 160% 160%;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        letter-spacing: 0.2px;
        height: 3.2rem;
        transition: transform 0.18s cubic-bezier(0.4, 0, 0.2, 1),
                    box-shadow 0.18s cubic-bezier(0.4, 0, 0.2, 1),
                    background-position 0.5s ease;
    }}

    .stButton > button[kind="primary"]:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 30px rgba(16, 185, 129, 0.35);
        background-position: 100% 50%;
    }}

    .stButton > button[kind="primary"]:active {{
        transform: translateY(0px) scale(0.985);
    }}

    /* =====================================================
       PIPELINE
       ===================================================== */

    .section-title {{
        font-family: 'Sora', 'Manrope', sans-serif;
        font-size: 1.45rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.3px;
        margin-top: 2.2rem;
        margin-bottom: 1.1rem;
    }}

    .pipeline {{
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 0;
        margin: 1.4rem 0 2.2rem 0;
        animation: fadeInUp 0.6s ease both;
        animation-delay: 0.2s;
    }}

    .pipeline-step {{
        display: flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.7rem 1rem;
        border-radius: 12px;
        background: var(--card-bg-alt);
        border: 1px solid var(--border-color);
        color: var(--text-secondary);
        font-size: 0.98rem;
        font-weight: 600;
        transition: all 0.2s ease;
    }}

    .pipeline-step:hover {{
        border-color: var(--accent);
        color: var(--text-primary);
        transform: translateY(-2px);
        box-shadow: 0 6px 18px var(--shadow-color);
    }}

    .pipeline-number {{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 25px;
        height: 25px;
        border-radius: 50%;
        background: var(--accent-soft);
        color: var(--accent);
        font-size: 0.76rem;
        font-weight: 800;
    }}

    .pipeline-arrow {{
        color: var(--text-muted);
        padding: 0 0.7rem;
        font-size: 1.1rem;
    }}

    /* =====================================================
       STATUS
       ===================================================== */

    div[data-testid="stStatusWidget"] {{
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 14px;
    }}

    /* =====================================================
       STAT CARDS
       ===================================================== */

    .stats-container {{
        display: flex;
        gap: 1rem;
        margin: 1.6rem 0;
        flex-wrap: wrap;
    }}

    .stat-card {{
        flex: 1;
        min-width: 140px;
        padding: 1.1rem 1.3rem;
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 14px;
        transition: all 0.2s ease;
    }}

    .stat-card:hover {{
        transform: translateY(-3px);
        border-color: var(--accent);
        box-shadow: 0 10px 24px var(--shadow-color);
    }}

    .stat-value {{
        font-family: 'Sora', 'Manrope', sans-serif;
        font-size: 1.9rem;
        font-weight: 800;
        color: var(--text-primary);
    }}

    .stat-label {{
        margin-top: 0.25rem;
        font-size: 0.92rem;
        font-weight: 500;
        color: var(--text-muted);
    }}

    /* =====================================================
       SOURCES
       ===================================================== */

    .source-card {{
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 14px;
        padding: 1.05rem 1.2rem;
        margin-bottom: 0.75rem;
        transition: border-color 0.2s ease, transform 0.2s ease, box-shadow 0.2s ease;
    }}

    .source-card:hover {{
        border-color: var(--accent);
        transform: translateY(-2px) translateX(2px);
        box-shadow: 0 8px 22px var(--shadow-color);
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
        width: 26px;
        height: 26px;
        border-radius: 50%;
        background: var(--accent-soft);
        color: var(--accent);
        font-size: 0.74rem;
        font-weight: 800;
    }}

    .source-label {{
        color: var(--text-secondary);
        font-size: 0.92rem;
        font-weight: 650;
    }}

    .source-url {{
        color: var(--accent);
        font-size: 0.92rem;
        text-decoration: none;
        word-break: break-all;
        transition: opacity 0.15s ease;
    }}

    .source-url:hover {{
        opacity: 0.75;
        text-decoration: underline;
    }}

    /* =====================================================
       RESEARCH REPORT
       ===================================================== */

    .report-wrapper {{
        background: var(--card-bg);
        border: 1px solid var(--border-color);
        border-radius: 18px;
        padding: 2.1rem 2.3rem;
        margin-top: 1rem;
        box-shadow: 0 15px 50px var(--shadow-color);
    }}

    .report-label {{
        display: inline-block;
        padding: 0.32rem 0.7rem;
        border-radius: 7px;
        background: var(--accent-2-soft);
        color: var(--accent-2);
        font-size: 0.73rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        margin-bottom: 1.1rem;
    }}

    /* =====================================================
       FOOTER
       ===================================================== */

    .footer {{
        text-align: center;
        margin-top: 3rem;
        color: var(--text-muted);
        font-size: 0.78rem;
        font-weight: 500;
        letter-spacing: 0.2px;
    }}

</style>
"""


CSS = get_css("dark")