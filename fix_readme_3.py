import re

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Remove about_hud.svg completely
readme = re.sub(r'<img width="100%" src="[^"]*?about_hud\.svg".*?/>\s*', '', readme)

# Change divider height from 5 to 2
readme = readme.replace('height="5" src="https://raw.githubusercontent.com/kushal-soni-official/Exp-readme/main/divider_circuit.svg"',
                        'height="2" src="https://raw.githubusercontent.com/kushal-soni-official/Exp-readme/main/divider_circuit.svg"')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
