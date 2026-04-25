import os
import re
from collections import defaultdict

# =========================
# INPUT (SINGLE VIDEO)
# =========================

REPORTS = [
    {
       "title": "SEO in 2025: Visibility, Trust & the End of the Click Economy",
        "url": "https://www.youtube.com/watch?v=Vt_C1pEfNd8",
        "date": "Dec 10, 2024",
        "channel": "AirOps & Kevin Indig",
        "views": "2,100",
        "transcript": """
Kevin explains that 2024 was the 'Peak Traffic' year. In 2025 and 2026, click-through rates 
are declining because AI Overviews answer the user's question directly on the search page. 
He argues that SEOs must now focus on 'Information Gain'—providing data that AI doesn't 
already have—to force a click.
"""
    }
]

# =========================
# OUTPUT FOLDER
# =========================

OUTPUT_DIR = r"R:\Cursor\Task\ai-seo-research\research\youtube-transcripts\manual"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# HELPERS
# =========================

def clean(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

counter = defaultdict(int)

# =========================
# DYNAMIC INSIGHTS
# =========================

def extract_insights(transcript):
    t = transcript.lower()
    insights = []

    if "link" in t or "backlink" in t:
        insights.append("Link building is shifting toward authority-based acquisition (Digital PR)")

    if "guest" in t:
        insights.append("Traditional guest posting is losing effectiveness")

    if "content" in t:
        insights.append("Content originality and depth are key SEO signals")

    return insights if insights else ["General SEO discussion"]

def action_items(transcript):
    t = transcript.lower()
    actions = []

    if "link" in t or "backlink" in t:
        actions.append("Focus on Digital PR instead of guest posting")

    if "content" in t:
        actions.append("Create more original, high-value content")

    return actions if actions else ["Apply general SEO strategy"]

def system_implication(transcript):
    t = transcript.lower()

    if "link" in t:
        return "SEO is shifting from quantity-based links to authority-driven acquisition."

    return "SEO is evolving into a multi-signal ranking system beyond keywords."

# =========================
# MARKDOWN BUILDER
# =========================

def build_md(r):
    insights = extract_insights(r["transcript"])
    actions = action_items(r["transcript"])
    system_imp = system_implication(r["transcript"])

    return f"""# {r['title']}

- URL: {r['url']}
- Date: {r['date']}
- Channel: {r['channel']}
- Views: {r['views']}

---

## Transcript (raw)

{r['transcript']}

---

## Key Insights

- """ + "\n- ".join(insights) + f"""

---

## Actionable Takeaways

- """ + "\n- ".join(actions) + f"""

---

## System Implication (SEO / AI)

{system_imp}
"""

# =========================
# RUNNER
# =========================

for r in REPORTS:

    expert = clean(r["channel"])
    video = clean(r["title"])

    counter[expert] += 1
    num = str(counter[expert]).zfill(2)

    filename = f"{num}_{expert}_{video}.md"
    path = os.path.join(OUTPUT_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(build_md(r))

    print(f"✅ Saved: {path}")