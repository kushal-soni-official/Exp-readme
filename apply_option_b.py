import re

RAW = "https://raw.githubusercontent.com/kushal-soni-official/Exp-readme/main"
MAIN_RAW = "https://raw.githubusercontent.com/kushal-soni-official/Kushal-soni-official/main"

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 1. Hero TV Section
# We find everything from <!-- ▓▓▓ HERO BANNER SVG ▓▓▓ --> to the end of the first divider (inclusive)
# Or we can just find the hero_banner and banner.png tags and replace them.
hero_pattern = r'<!-- ▓▓▓ HERO BANNER SVG ▓▓▓ -->\s*<img width="100%" src=".*?hero_banner\.svg" alt=".*?" />\s*<!-- ▓▓▓ BANNER ▓▓▓ -->\s*<img width="100%" src=".*?banner\.png" alt=".*?" />'
tv_block = f'''<!-- ▓▓▓ TV ROOM & HERO GIFS ▓▓▓ -->
<div align="center">
  <img width="100%" src="{RAW}/tv_top.svg" alt="TV Top Bezel" />
  <img width="100%" src="{MAIN_RAW}/welcome.gif" alt="Welcome Hacker" />
  <img width="100%" src="{RAW}/tv_bottom.svg" alt="TV Bottom Bezel" />
  <br/>
  <img width="100%" src="{MAIN_RAW}/banner.gif" alt="Hero Banner" />
</div>'''
readme = re.sub(hero_pattern, tv_block, readme, flags=re.DOTALL)

# 2. About Me Section
# Remove about_hud.svg and the 7 bullet points
about_pattern = r'<img width="100%" src=".*?about_hud\.svg".*?/>\s*(- 🎓.*?obsession and lifelong pursuit\.)'
new_about = f'<img width="100%" src="{RAW}/about_text.svg" alt="About Me Text" />'
readme = re.sub(about_pattern, new_about, readme, flags=re.DOTALL)

# 3. GitHub Stats - Remove "Most Used Languages" block
# It looks like:
# **◈ Most Used Languages**
# <p align="center"> ... </a> </p>
lang_pattern = r'\*\*◈ Most Used Languages\*\*.*?</p>'
readme = re.sub(lang_pattern, '', readme, flags=re.DOTALL)

# 4. Add Contribution Graph before Streak
# We find "## `▸` GitHub Live Stats & Streak" and insert the graph right under it
stats_header_pattern = r'(## `▸` GitHub Live Stats & Streak\s*\*\*◈ Live Streak & Total Contributions\*\*)'
contrib_graph = f'''## `▸` GitHub Live Stats & Streak

**◈ Contribution Activity**
<p align="center">
  <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=kushal-soni-official&custom_title=Kushal%20Soni%27s%20Contribution%20Graph&bg_color=050510&color=4FC3FF&line=00BFFF&point=7FDBFF&area=true&hide_border=true&area_color=001D3D" alt="Contribution Graph" />
</p>

**◈ Live Streak & Total Contributions**'''
readme = re.sub(stats_header_pattern, contrib_graph, readme, count=1)

# 5. Update Contact Buttons to have darker bg
# Replacing color=0d1117 (or similar) with labelColor=050510 & color=0A0A0A
readme = readme.replace('badge/LinkedIn-0d1117', 'badge/LinkedIn-0A0A0A')
readme = readme.replace('badge/GitHub-0d1117', 'badge/GitHub-0A0A0A')
readme = readme.replace('badge/Email-0d1117', 'badge/Email-0A0A0A')
readme = readme.replace('badge/TryHackMe-0d1117', 'badge/TryHackMe-0A0A0A')
readme = readme.replace('badge/tgl.prince-0d1117', 'badge/tgl.prince-0A0A0A')

# Also ensure shields use labelColor=050510 (if not already there)
readme = re.sub(r'(logoColor=[^&"\s]+)', r'\1&labelColor=050510', readme)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("README update script completed.")
