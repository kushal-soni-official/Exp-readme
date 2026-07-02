with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

RAW = "https://raw.githubusercontent.com/kushal-soni-official/Exp-readme/main"

# 1. Add hero_banner.svg as very first element (before banner.png)
old_banner_line = '<!-- \u2593\u2593\u2593 BANNER \u2593\u2593\u2593 -->\n<img width="100%" src="https://raw.githubusercontent.com/kushal-soni-official/Exp-readme/main/banner.png" alt="Kushal Soni Banner" />'
new_banner_block = (
    '<!-- \u2593\u2593\u2593 HERO BANNER SVG \u2593\u2593\u2593 -->\n'
    f'<img width="100%" src="{RAW}/hero_banner.svg" alt="Kushal Soni \u2014 Cybersecurity &amp; AI Engineer" />\n\n'
    '<!-- \u2593\u2593\u2593 BANNER \u2593\u2593\u2593 -->\n'
    '<img width="100%" src="https://raw.githubusercontent.com/kushal-soni-official/Exp-readme/main/banner.png" alt="Kushal Soni Banner" />'
)
readme = readme.replace(old_banner_line, new_banner_block)

# 2. Replace ALL capsule-render dividers with divider_circuit.svg
import re
readme = re.sub(
    r'<img width="100%" src="https://capsule-render\.vercel\.app/api\?[^"]*" alt="divider" />',
    f'<img width="100%" src="{RAW}/divider_circuit.svg" alt="section divider" />',
    readme
)

# 3. Replace footer capsule-render wave with footer_v2.svg
old_footer = '<!-- \u2593\u2593\u2593 FOOTER \u2014 Electric Blue Wave \u2593\u2593\u2593 -->\n<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0088ff&height=120&section=footer" alt="Footer" />'
new_footer = (
    '<!-- \u2593\u2593\u2593 FOOTER V2 \u2593\u2593\u2593 -->\n'
    f'<img width="100%" src="{RAW}/footer_v2.svg" alt="Footer \u2014 Think Like an Attacker, Defend Like a Guardian" />'
)
readme = readme.replace(old_footer, new_footer)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("README updated successfully")
