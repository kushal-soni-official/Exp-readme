import re

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 1. Fix divider height
readme = readme.replace('<img width="100%" src="https://raw.githubusercontent.com/kushal-soni-official/Exp-readme/main/divider_circuit.svg" alt="section divider" />', 
                        '<img width="100%" height="5" src="https://raw.githubusercontent.com/kushal-soni-official/Exp-readme/main/divider_circuit.svg" alt="section divider" />')

# 2. Fix GitHub Stats
# Replace everything from `## `▸` GitHub Stats` to the `<p align="center">` of the streak stats with the activity graph + streak.
stats_regex = r'## `▸` GitHub Stats.*?<p align="center">\s*<img width="65%" src="https://streak-stats\.demolab\.com'
new_stats = '''## `▸` GitHub Stats

<p align="center">
  <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=kushal-soni-official&custom_title=Kushal%20Soni%27s%20Contribution%20Graph&bg_color=050510&color=4FC3FF&line=00BFFF&point=7FDBFF&area=true&hide_border=true&area_color=001D3D" alt="Contribution Graph" />
</p>

<p align="center">
  <img width="65%" src="https://streak-stats.demolab.com'''

readme = re.sub(stats_regex, new_stats, readme, flags=re.DOTALL)

# 3. Fix Connect Buttons
readme = re.sub(r'badge/Email.*?style=for-the-badge.*?alt="Email" />', 
                r'badge/Email-Ofc.kusharu%40gmail.com-0A0A0A?style=for-the-badge&logo=gmail&logoColor=EA4335&labelColor=050510" alt="Email" />', readme)

readme = re.sub(r'badge/LinkedIn.*?style=for-the-badge.*?alt="LinkedIn" />', 
                r'badge/LinkedIn-Kushal%20Soni-0A0A0A?style=for-the-badge&logo=linkedin&logoColor=0A66C2&labelColor=050510" alt="LinkedIn" />', readme)

readme = re.sub(r'badge/TryHackMe.*?style=for-the-badge.*?alt="TryHackMe" />', 
                r'badge/TryHackMe-kusharusan-0A0A0A?style=for-the-badge&logo=tryhackme&logoColor=88cc14&labelColor=050510" alt="TryHackMe" />', readme)

readme = re.sub(r'badge/GitHub.*?style=for-the-badge.*?alt="GitHub" />', 
                r'badge/GitHub-kushal--soni--official-0A0A0A?style=for-the-badge&logo=github&logoColor=ffffff&labelColor=050510" alt="GitHub" />', readme)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("Fixes applied successfully!")
