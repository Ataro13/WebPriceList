# -*- coding: utf-8 -*-
import re
c = open("E:/WORKFLOW/PRICEWEB/index.html", "r", encoding="utf-8").read()

# Sections
secs = re.findall(r'<div class="section-title">(.*?)</div>', c)
for i, s in enumerate(secs):
    print(f"  {i+1}. {s}")

# Form
m = re.search(r'<form[^>]+action="([^"]+)"', c)
print(f"  FORM ACTION: {m.group(1) if m else 'NOT FOUND'}")

# Tariff cards
print(f"  TARIFFS: {c.count('tariff-card')} cards")

# Section 1 content
s1_start = c.find('<!-- === 1.')
s1_end = c.find('</div>', c.find('</div>', s1_start) + 10)
if s1_start > 0:
    s1 = c[s1_start:s1_end+6]
    print(f"  SEC1 length: {len(s1)} chars")

# Section 2 note
s2_start = c.find('ПРАВКИ В БЛОКАХ')
if s2_start > 0:
    note = c[s2_start:s2_start+200]
    print(f"  SEC2 note sample: {note[:100]}")
