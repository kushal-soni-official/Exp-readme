import re

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 1. Remove TV SVGs
readme = re.sub(r'<img width="100%" src="[^"]*?tv_top\.svg" alt="TV Top Bezel" />\s*', '', readme)
readme = re.sub(r'<img width="100%" src="[^"]*?tv_bottom\.svg" alt="TV Bottom Bezel" />\s*', '', readme)

# 2. Remove About SVG and add markdown bullets back
about_svg_pattern = r'<img width="100%" src="https://raw\.githubusercontent\.com/kushal-soni-official/Exp-readme/main/about_text\.svg" alt="About Me Text" />'
markdown_bullets = '''- 🎓 **Computer Science & Engineering Student** — Diploma in CSE (**~75%**) | XII UP Board (**89%**) — building real-world security systems while still in college
- 🔐 Building **AI-powered cybersecurity tools from scratch** — zero paid subscriptions, pure skill
- ⚔️ Core focus: **Ethical Hacking, Network Security & AI-layer defense** — Kali Linux to multi-agent pipelines
- 🤖 Trained ML models achieving high accuracy on security classification tasks (Random Forest + PyTorch)
- 🌐 Dual-track: **offensive recon** (NetSpectre + Nmap) and **defensive AI** (Prompt Injection detection)
- 💡 Every project: **open source, free-tier only, built on persistence** — no shortcuts taken'''

readme = re.sub(about_svg_pattern, markdown_bullets, readme)

# 3. Center the tables
# Find table: | # | Project ... and convert to HTML
# Wait, parsing markdown tables to HTML in regex is hard.
# Instead, we can wrap them in `<div align="center">` and see if they parse.
# GitHub markdown allows tables inside HTML if there are blank lines before and after.
# Wait, the user just wants the tables centered. 
# GitHub recently updated their markdown renderer. `<div align="center">\n\n|...|\n\n</div>` works.
# Let's try wrapping them safely.
def wrap_table(match):
    table_content = match.group(0)
    return f'<div align="center">\n\n{table_content}\n\n</div>'

table_regex = r'(\|.*\|(?:\n\|[-:| ]+\|)(?:\n\|.*\|)+)'
readme = re.sub(table_regex, wrap_table, readme)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
print("Readme updated")
