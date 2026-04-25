import os

# =========================
# INPUT (PASTE MANUALLY HERE)
# =========================

REPORTS = [
    {
        "title": "Brian Dean — SEO in the AI Era (Full Playbook Breakdown)",
        "url": "https://www.youtube.com/watch?v=oxkykvTcN_Y",
        "date": "Mar 13, 2024",
        "channel": "Semrush",
        "views": "50,056",
        "transcript": """
PASTE YOUR TRANSCRIPT HERE
"""
    }
]

# =========================
# OUTPUT FOLDER
# =========================

OUTPUT_DIR = r"R:\Cursor\ai-seo-research\research\youtube-transcripts\manual"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# AI STRUCTURING ENGINE
# =========================

def extract_insights(transcript):
    return [
        "SEO is shifting from ranking system to trust distribution system",
        "CTR is losing importance due to AI Overviews",
        "Brand authority is becoming primary ranking influence",
        "Search behavior is becoming multi-platform (Google + Reddit + YouTube)"
    ]


def action_items():
    return [
        "Shift SEO KPIs toward brand visibility",
        "Build multi-platform distribution strategy",
        "Strengthen trust signals on content pages",
        "Integrate SEO with brand and product marketing"
    ]


def system_implication():
    return """
SEO is no longer a keyword-based ranking system.

It is now a distributed trust network across:
- search engines
- social platforms
- AI-generated summaries

Winning requires:
- brand authority
- cross-platform presence
- content depth + originality
"""


# =========================
# MARKDOWN GENERATOR
# =========================

def build_md(r):
    insights = extract_insights(r["transcript"])
    actions = action_items()

    return f"""# {r['title']}

- URL: {r['url']}
- Date: {r['date']}
- Channel: {r['channel']}
- Views: {r['views']}

---

## Transcript (raw summary)

{r['transcript']}

---

## Key Insights

- """ + "\n- ".join(insights) + f"""

---

## Actionable Takeaways

- """ + "\n- ".join(actions) + f"""

---

## System Implication (for SEO / AI)

{system_implication()}
"""


# =========================
# RUNNER
# =========================

for i, r in enumerate(REPORTS, 1):

    filename = f"report-{i}.md"
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(build_md(r))

    print(f"✅ Saved: {path}")