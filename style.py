import streamlit as st

# ─────────────────────────────────────────────
#  DESIGN SYSTEM — BLUE THEME + WHATSAPP GREEN ACCENT
#  Single source of truth for all styling.
#  Edit colors / spacing / radii here only.
#
#  Blue  = app primary (navbar, buttons, focus, headings)
#  Green = contact & money accents (WhatsApp / Call buttons,
#          amounts, total bar, table header line)
#
#  Note: --green* tokens are legacy names — they hold BLUE values.
#  The real green tokens are --wa-*.
# ─────────────────────────────────────────────
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    /* ═══════════════════════════════════════
       TOKENS
       ═══════════════════════════════════════ */
    :root {
        /* WhatsApp green accent */
        --wa-green:      #25d366;   /* WhatsApp brand green */
        --wa-green-dark: #128c4a;
        --wa-green-mid:  #34d574;
        --wa-green-light:#dcfce7;
        --wa-border:     #bbf7d0;

        /* Blue primary palette (legacy "green" names) */
        --green:         #0284c7;
        --green-dark:    #0b4a6f;
        --green-mid:     #0ea5e9;
        --green-light:   #e0f2fe;
        --green-lighter: #f0f9ff;
        --navbar-bg:     #0b4a6f;

        --line:          #dbe6ed;
        --line-strong:   #b8cbd8;
        --muted:         #5b6e7b;

        --bg-page:       #f5f8fa;
        --bg-card:       #ffffff;
        --bg-input:      #ffffff;
        --bg-hover:      #eef6fb;
        --text-main:     #14212b;
        --text-td:       #1c2b35;
        --empty:         #9aa8b0;

        /* Interactive buttons get their own tokens so they stay
           legible and vivid in both themes, independent of --green
           (which is also used as a text/accent color). */
        --btn-bg:        #0284c7;
        --btn-bg-hover:  #0ea5e9;
        --btn-bg-active: #0b3a56;
        --btn-text:      #ffffff;
        --focus-ring:    rgba(2, 132, 199, 0.35);
        --pulse:         rgba(2, 132, 199, 0.28);

        --sp-1: 4px;  --sp-2: 8px;  --sp-3: 12px; --sp-4: 16px;
        --sp-5: 20px; --sp-6: 24px; --sp-7: 32px; --sp-8: 48px;

        --r-sm: 6px;
        --r-md: 8px;
        --r-lg: 12px;

        --fs-xs:   0.75rem;
        --fs-sm:   0.8125rem;
        --fs-base: 0.9375rem;
        --fs-md:   1rem;
        --fs-lg:   1.125rem;
        --fs-xl:   1.375rem;
        --fs-2xl:  1.75rem;

        --shadow-1: 0 1px 2px rgba(15, 30, 20, 0.06);
        --shadow-2: 0 4px 16px rgba(15, 30, 20, 0.08), 0 1px 3px rgba(15, 30, 20, 0.06);
        --shadow-card: 0 1px 2px rgba(15, 30, 20, 0.05), 0 1px 0 rgba(15, 30, 20, 0.04);
        --mob-divider: var(--line);
    }

    /* Inputs deliberately DO NOT follow OS dark mode — kept a fixed,
       high-contrast light surface so text is always readable no matter
       what theme Streamlit itself is set to. A visible border keeps the
       light input from looking like a stray white box on a dark page. */

    @media (prefers-color-scheme: dark) {
        :root {
            --wa-green:      #25d366;
            --wa-green-dark: #86efac;
            --wa-green-mid:  #4ade80;
            --wa-green-light:#052e16;
            --wa-border:     #14532d;

            --green:         #38bdf8;
            --green-dark:    #7dd3fc;
            --green-mid:     #38bdf8;
            --green-light:   #0c2a3d;
            --green-lighter: #0b2535;
            --navbar-bg:     #0c3a56;

            --line:          #1a3345;
            --line-strong:   #27475e;
            --muted:         #8aa3b3;

            --bg-page:       #060f16;
            --bg-card:       #0d1e29;
            --bg-hover:      #10283a;
            --text-main:     #e7f2f8;
            --text-td:       #dce8ee;
            --empty:         #5c7180;

            --btn-bg:        #0f8fc7;
            --btn-bg-hover:  #38bdf8;
            --btn-bg-active: #0c6a96;
            --btn-text:      #04141f;
            --focus-ring:    rgba(56, 189, 248, 0.35);
            --pulse:         rgba(56, 189, 248, 0.30);

            --shadow-1: 0 1px 2px rgba(0, 0, 0, 0.45);
            --shadow-2: 0 8px 24px rgba(0, 0, 0, 0.5), 0 1px 3px rgba(0, 0, 0, 0.4);
            --shadow-card: 0 1px 0 rgba(255, 255, 255, 0.03), 0 8px 20px rgba(0, 0, 0, 0.35);
            --mob-divider: var(--line);
        }
    }

    html, body, .stApp, label, button {
        font-family: 'Inter', 'Noto Sans', sans-serif !important;
        color: var(--text-main);
    }

    .stApp { background: var(--bg-page); }
    footer { visibility: hidden; }
    .block-container { padding-top: var(--sp-5); padding-bottom: var(--sp-8); max-width: 1160px; }

    /* ═══════════════════════════════════════
       INPUTS — fixed, always-readable surface
       ═══════════════════════════════════════ */
    .stTextInput input,
    .stTextInput input:focus,
    div[data-baseweb="input"] input {
        background: var(--bg-input) !important;
        color: #14212b !important;
        -webkit-text-fill-color: #14212b !important;
        caret-color: var(--green-mid) !important;
    }
    .stTextInput input::placeholder { color: #8a9aa5 !important; opacity: 1 !important; }

    .stTextInput > div,
    div[data-baseweb="input"] {
        background: var(--bg-input) !important;
        border-radius: var(--r-md) !important;
        border: 1.5px solid var(--line-strong) !important;
        box-shadow: var(--shadow-1);
    }
    .stTextInput > div:hover,
    div[data-baseweb="input"]:hover {
        border-color: var(--green-mid) !important;
    }
    .stTextInput > div:focus-within,
    div[data-baseweb="input"]:focus-within {
        border-color: var(--green-mid) !important;
        box-shadow: 0 0 0 3px var(--focus-ring) !important;
    }
    .stTextInput input { height: 2.6rem !important; font-size: var(--fs-base) !important; }
    .stTextInput label { font-weight: 600 !important; font-size: var(--fs-sm) !important; color: var(--muted) !important; }

    /* ═══════════════════════════════════════
       BUTTONS — native Streamlit buttons
       (st.button / st.form_submit_button), used
       throughout the app including the login page.
       ═══════════════════════════════════════ */
    .stButton > button,
    .stFormSubmitButton > button,
    button[kind="primary"],
    button[kind="secondary"] {
        background: var(--btn-bg) !important;
        color: var(--btn-text) !important;
        border: 1px solid var(--btn-bg) !important;
        border-radius: var(--r-md) !important;
        font-weight: 600 !important;
        font-size: var(--fs-base) !important;
        padding: 0.6rem 1.4rem !important;
        box-shadow: var(--shadow-1);
        transition: background-color 150ms ease, border-color 150ms ease,
                    transform 150ms ease, box-shadow 150ms ease;
    }
    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        background: var(--btn-bg-hover) !important;
        border-color: var(--btn-bg-hover) !important;
        transform: translateY(-1px);
        box-shadow: var(--shadow-2);
    }
    .stButton > button:active,
    .stFormSubmitButton > button:active {
        background: var(--btn-bg-active) !important;
        border-color: var(--btn-bg-active) !important;
        transform: translateY(0);
        box-shadow: var(--shadow-1);
    }
    .stButton > button:focus-visible,
    .stFormSubmitButton > button:focus-visible {
        outline: 2px solid var(--green-mid);
        outline-offset: 2px;
    }
    .stButton > button:disabled {
        opacity: 0.5;
        transform: none;
        box-shadow: none;
        cursor: not-allowed;
    }
    /* A quieter, outline variant — add class "bm-ghost" via
       wrapper markup where a softer action is needed. */
    .stButton.bm-ghost > button {
        background: transparent !important;
        color: var(--green-dark) !important;
        border-color: var(--line-strong) !important;
        box-shadow: none;
    }
    .stButton.bm-ghost > button:hover {
        background: var(--green-light) !important;
        border-color: var(--green-mid) !important;
    }

    /* ═══════════════════════════════════════
       LOGIN / GATE CARD (shared)
       ═══════════════════════════════════════ */
    @keyframes bm-fade-up {
        from { opacity: 0; transform: translateY(8px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes bm-pulse {
        0%, 100% { box-shadow: 0 0 0 0 var(--pulse); }
        50%      { box-shadow: 0 0 0 10px rgba(0,0,0,0); }
    }
    .login-box {
        text-align: center;
        padding: var(--sp-7) var(--sp-5) var(--sp-6);
        /* No card surface here on purpose — this block sits directly
           on the page background with no box/border/shadow behind it. */
        background: transparent;
        border: none;
        box-shadow: none;
        animation: bm-fade-up 380ms ease;
    }
    .login-box .icon {
        display: inline-flex; align-items: center; justify-content: center;
        width: 4.5rem; height: 4.5rem;
        border-radius: var(--r-lg);
        background: transparent;
        border: none;
        margin-bottom: var(--sp-4);
        overflow: hidden;
    }
    .login-box .icon img {
        width: 100%;
        height: 100%;
        object-fit: contain;
    }
    .login-box h1 {
        color: var(--green-dark);
        font-size: var(--fs-2xl);
        font-weight: 800;
        letter-spacing: -0.02em;
        margin: 0 0 var(--sp-2) 0;
        line-height: 1.25;
    }
    .login-box p { color: var(--muted); font-size: var(--fs-base); margin: 0; }
    .login-box .badge {
        display: inline-block;
        margin-top: var(--sp-3);
        padding: var(--sp-1) var(--sp-3);
        background: var(--green-light);
        color: var(--green-dark);
        border: 1px solid var(--line);
        border-radius: 999px;
        font-size: var(--fs-xs);
        font-weight: 700;
        letter-spacing: 0.03em;
        text-transform: uppercase;
    }
    /* Keep the login card's own text-input + button snug and centered
       when Streamlit renders them just below the markup above. */
    .login-box + div .stTextInput,
    .login-box + div .stButton {
        max-width: 360px;
        margin-left: auto;
        margin-right: auto;
    }

    /* ═══════════════════════════════════════
       NAVBAR
       ═══════════════════════════════════════ */
    .navbar {
        display: flex; align-items: center; justify-content: space-between;
        background: var(--navbar-bg);
        border-radius: var(--r-lg);
        padding: var(--sp-3) var(--sp-5);
        margin-bottom: var(--sp-5);
        box-shadow: var(--shadow-1);
        flex-wrap: wrap; gap: var(--sp-3);
    }
    .navbar-brand { display: flex; align-items: center; gap: var(--sp-3); color: #ffffff; font-weight: 700; font-size: var(--fs-md); line-height: 1.25; }
    .navbar-brand .logo { height: 28px; width: 28px; object-fit: contain; display: block; flex-shrink: 0; }
    .navbar-brand small { display: block; font-weight: 400; font-size: var(--fs-xs); color: rgba(255,255,255,0.72); margin-top: 1px; }

    /* ═══════════════════════════════════════
       PAGE HEADER — green left bar
       ═══════════════════════════════════════ */
    .pg-header { border-left: 3px solid var(--wa-green); padding-left: var(--sp-4); margin-bottom: var(--sp-5); }
    .pg-header h2 { margin: 0; color: var(--green-dark); font-size: var(--fs-xl); font-weight: 700; letter-spacing: -0.01em; }
    .pg-header p { margin: var(--sp-1) 0 0 0; color: var(--muted); font-size: var(--fs-sm); }

    /* ═══════════════════════════════════════
       TABLE
       ═══════════════════════════════════════ */
    .bm-wrap {
        background: var(--bg-card);
        border: 1px solid var(--line);
        border-radius: var(--r-lg);
        overflow-x: auto;
        margin-top: var(--sp-3);
        box-shadow: var(--shadow-card);
    }
    .bm-table { width: 100%; border-collapse: collapse; font-size: var(--fs-base); color: var(--text-td); }
    .bm-table thead { border-top: 3px solid var(--wa-green); }   /* green top line */
    .bm-table thead th {
        background: var(--green-lighter);
        color: var(--green-dark);
        padding: var(--sp-3) var(--sp-4);
        text-align: left;
        font-weight: 700;
        font-size: var(--fs-xs);
        text-transform: uppercase;
        letter-spacing: 0.05em;
        white-space: nowrap;
        border-bottom: 1px solid var(--wa-green);                /* green bottom line */
        position: sticky; top: 0; z-index: 1;
    }
    .bm-table td { padding: var(--sp-3) var(--sp-4); border-bottom: 1px solid var(--line); vertical-align: middle; color: var(--text-td); }
    .bm-table tbody tr:last-child td { border-bottom: 0; }
    .bm-table tbody tr:hover { background: var(--bg-hover); }

    .bm-num { text-align: right; font-variant-numeric: tabular-nums; font-weight: 600; color: var(--text-td); font-size: var(--fs-base); white-space: nowrap; }

    /* Amount — green text (money) */
    .bm-amt-badge { display: inline-block; color: var(--wa-green-dark) !important; font-weight: 700; font-size: var(--fs-base); font-variant-numeric: tabular-nums; }
    .bm-amt-zero  { display: inline-block; color: var(--empty); font-weight: 500; font-size: var(--fs-base); font-variant-numeric: tabular-nums; }

    .bm-sr    { color: var(--muted); width: 3rem; font-weight: 500; font-size: var(--fs-sm); }
    .bm-ph    { white-space: nowrap; font-variant-numeric: tabular-nums; color: var(--text-td); font-weight: 500; }
    .bm-empty { color: var(--empty); }

    .bm-btn {
        display: inline-flex; align-items: center; justify-content: center; gap: var(--sp-1);
        height: 2rem; padding: 0 var(--sp-3);
        border-radius: var(--r-sm);
        font-size: var(--fs-sm); font-weight: 600;
        text-decoration: none !important; white-space: nowrap;
        border: 1px solid transparent;
        box-shadow: var(--shadow-1);
        transition: background-color 150ms ease, border-color 150ms ease,
                    transform 150ms ease, box-shadow 150ms ease;
    }
    .bm-btn:hover  { transform: translateY(-1px); box-shadow: var(--shadow-2); }
    .bm-btn:active { transform: translateY(0); box-shadow: var(--shadow-1); }
    .bm-btn:focus-visible { outline: 2px solid var(--wa-green-mid); outline-offset: 2px; }

    /* ── WhatsApp button — real WA green ── */
    .bm-wa {
        color: #ffffff !important;
        background: var(--wa-green);
        border-color: var(--wa-green);
    }
    .bm-wa:hover {
        background: var(--wa-green-dark);
        border-color: var(--wa-green-dark);
    }

    /* ── Call button — soft green tint ── */
    .bm-call {
        color: var(--wa-green-dark) !important;
        background: var(--wa-green-light);
        border-color: var(--wa-border);
    }
    .bm-call:hover {
        background: var(--wa-border);
        border-color: var(--wa-green-mid);
    }

    /* ═══════════════════════════════════════
       TOTAL BAR — green top + left accent
       ═══════════════════════════════════════ */
    .bm-total {
        display: flex; justify-content: space-between; align-items: center;
        margin-top: var(--sp-4); padding: var(--sp-4) var(--sp-5);
        background: var(--bg-card);
        border: 1px solid var(--line);
        border-top: 2px solid var(--wa-green);
        border-left: 4px solid var(--wa-green);
        border-radius: var(--r-lg);
        box-shadow: var(--shadow-card);
        flex-wrap: wrap; gap: var(--sp-2);
    }
    .bm-total-label { color: var(--muted); font-size: var(--fs-sm); font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; }
    .bm-total-value { color: var(--wa-green-dark); font-size: var(--fs-xl); font-weight: 800; letter-spacing: -0.01em; font-variant-numeric: tabular-nums; }

    /* ═══════════════════════════════════════
       SIDEBAR BRAND
       ═══════════════════════════════════════ */
    .bm-brand       { font-size: var(--fs-md); font-weight: 700; color: var(--green-dark); line-height: 1.35; }
    .bm-brand small { display: block; font-weight: 400; font-size: var(--fs-xs); color: var(--muted); margin-top: 2px; }

    /* ═══════════════════════════════════════
       RESPONSIVE — TABLET
       ═══════════════════════════════════════ */
    @media (max-width: 900px) {
        .block-container { padding-left: var(--sp-4); padding-right: var(--sp-4); }
    }

    /* ═══════════════════════════════════════
       RESPONSIVE — MOBILE
       ═══════════════════════════════════════ */
    @media (max-width: 700px) {
        .block-container { padding-top: var(--sp-4); padding-left: var(--sp-3); padding-right: var(--sp-3); }

        .navbar { border-radius: var(--r-md); padding: var(--sp-3); flex-direction: column; align-items: stretch; }
        .navbar-brand { font-size: var(--fs-base); }
        .navbar-brand .logo { height: 24px; width: 24px; }

        .pg-header { padding-left: var(--sp-3); margin-bottom: var(--sp-4); }
        .pg-header h2 { font-size: var(--fs-lg); }

        .bm-wrap { border-radius: var(--r-md); box-shadow: none; }
        .bm-table thead { display: none; }
        .bm-table, .bm-table tbody, .bm-table tr { display: block; width: 100%; }

        .bm-table tr {
            display: grid;
            grid-template-columns: 1fr 1fr;
            column-gap: var(--sp-3);
            row-gap: var(--sp-1);
            padding: var(--sp-3);
            border-bottom: 1px solid var(--mob-divider);
        }
        .bm-table tbody tr:last-child { border-bottom: 0; }

        .bm-table td { display: flex; flex-direction: column; align-items: flex-start; gap: 2px; border: 0; padding: 0; text-align: left; }
        .bm-table td::before {
            content: attr(data-label);
            font-weight: 600; color: var(--muted);
            font-size: var(--fs-xs); text-transform: uppercase; letter-spacing: 0.03em;
        }

        .bm-table td.bm-primary { grid-column: 1 / -1; }
        .bm-table td.bm-primary::before { display: none; }
        .bm-table td.bm-primary { font-size: var(--fs-md); font-weight: 700; color: var(--text-main); }

        .bm-table td.bm-act {
            grid-column: 1 / -1;
            flex-direction: row;
            justify-content: flex-start;
            gap: var(--sp-2);
            margin-top: var(--sp-1);
        }
        .bm-table td.bm-act::before { display: none; }
        .bm-table td.bm-act .bm-btn { flex: 1 1 0; }

        .bm-num { text-align: left; }
        .bm-amt-badge, .bm-amt-zero { font-size: var(--fs-base); }

        .bm-total { flex-direction: column; align-items: flex-start; padding: var(--sp-4); }
        .bm-total-value { font-size: var(--fs-lg); }

        .login-box { padding: var(--sp-6) var(--sp-4) var(--sp-5); }
    }

    @media (min-width: 1400px) {
        .block-container { max-width: 1280px; }
    }

    /* Respect users who prefer less motion */
    @media (prefers-reduced-motion: reduce) {
        .login-box, .login-box .icon, .stButton > button, .bm-btn {
            animation: none !important;
            transition: none !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def hide_sidebar():
    st.markdown(
        "<style>[data-testid='stSidebar'],[data-testid='stSidebarCollapsedControl']"
        "{display:none}</style>",
        unsafe_allow_html=True,
    )