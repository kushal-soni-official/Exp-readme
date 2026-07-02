import re

RAW = "https://raw.githubusercontent.com/kushal-soni-official/Exp-readme/main"

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 1. Add terminal.svg BEFORE the About Me heading
old_about_heading = '## `▸` About Me'
new_about_block = (
    f'<img width="100%" src="{RAW}/terminal.svg" alt="Live Terminal — Kushal Soni" />\n\n'
    '## `▸` About Me'
)
readme = readme.replace(old_about_heading, new_about_block, 1)

# 2. Add about_hud.svg RIGHT AFTER the About Me heading (before the bullets)
# The about section looks like:
# ## `▸` About Me
# <blank line>
# - bullet...
old_about_first_bullet = '\n\n- 🎓 **Computer Science'
new_about_first_bullet = (
    f'\n\n<img width="100%" src="{RAW}/about_hud.svg" alt="About Me — Kushal Soni Profile HUD" />\n\n'
    '- 🎓 **Computer Science'
)
readme = readme.replace(old_about_first_bullet, new_about_first_bullet, 1)

# 3. Replace the entire Technical Stack content with tech_stack_hud.svg + skills_scanner.svg
# Find from the first badge after "## `▸` Technical Stack" to the divider
old_tech_start = '<p align="center"><b>⚡ Core Languages &amp; Scripting</b></p>'
# Find where it ends (at the next divider img tag)
# We'll use regex to find the whole block
pattern = r'(<p align="center"><b>⚡ Core Languages.*?)(<img width="100%" src="https://raw\.githubusercontent\.com/kushal-soni-official/Exp-readme/main/divider_circuit\.svg")'
replacement = (
    f'<img width="100%" src="{RAW}/tech_stack_hud.svg" alt="Technical Arsenal — Tech Stack HUD" />\n\n'
    f'<img width="100%" src="{RAW}/skills_scanner.svg" alt="Skills Scanner" />\n\n'
    r'\2'
)
readme = re.sub(pattern, replacement, readme, count=1, flags=re.DOTALL)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("README Phase 2 update complete")
