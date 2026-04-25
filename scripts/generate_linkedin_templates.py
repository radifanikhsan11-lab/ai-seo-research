import os

BASE_DIR = "research/linkedin-posts"

experts = [
    "brian-dean",
    "kevin-indig",
    "lily-ray",
    "aleyda-solis",
    "rand-fishkin",
    "marie-haynes",
    "cyrus-shepard",
    "ross-simmonds",
    "kyle-roof",
    "a-j-ghergich"
]

def template(expert, i):
    return f"""# LinkedIn Post Template - {expert.replace('-', ' ').title()}

- Expert: {expert}
- Post #: {i}
- Source URL: PASTE LINKEDIN URL HERE
- Date: YYYY-MM-DD

---

## Post Content
PASTE LINKEDIN POST HERE

---

## Key Insight
- What is the main idea?

## Strategy Mentioned
- What tactic/system is described?

## Why It Matters (SEO / SaaS)
- How does this apply to SaaS growth or SEO systems?

## Actionable Takeaway
- What can be implemented?

"""

for expert in experts:
    folder = os.path.join(BASE_DIR, expert)
    os.makedirs(folder, exist_ok=True)

    for i in range(1, 4):  # 3 templates per expert
        file_path = os.path.join(folder, f"post-0{i}.md")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(template(expert, i))

        print(f"✅ Created: {file_path}")