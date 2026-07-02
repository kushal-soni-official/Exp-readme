import re

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Replace divider_circuit.svg with static capsule-render divider
static_divider = 'https://capsule-render.vercel.app/api?type=rect&color=0:050510,15:002255,50:0088ff,85:002255,100:050510&height=2&section=header'

# Replace any img tags that use the old divider
old_divider_pattern = r'<img width="100%" (height="\d+" )?src="https://raw\.githubusercontent\.com/kushal-soni-official/Exp-readme/main/divider_circuit\.svg" alt="section divider" />'
new_divider_tag = f'<img width="100%" src="{static_divider}" alt="section divider" />'

readme = re.sub(old_divider_pattern, new_divider_tag, readme)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
