# -*- coding: utf-8 -*-
c = open("E:/WORKFLOW/PRICEWEB/index.html", "r", encoding="utf-8").read()

# Find sections 1 and 6
s1_start = c.find("<!-- === 1.")
s1_end = c.find("<!-- === 2.")
if s1_start > 0 and s1_end > 0:
    s1 = c[s1_start:s1_end]
    print("=== SECTION 1 (BANNER) ===")
    print(s1[:2000])
    print("...TOTAL:", len(s1), "chars")

print()
print("=== SECTION 6 (SEO PRODVIZHENIE) ===")
s6_start = c.find("<!-- === 6.")
s7_start = c.find("<!-- === ", s6_start + 10) if s6_start > 0 else -1
if s6_start > 0:
    # Find next section or next similar marker
    s7_start = c.find("<!-- === 7")
    if s7_start < 0:
        s7_start = c.find("<!-- КАК Я РАБОТАЮ")
    if s7_start < 0:
        s7_start = s6_start + 3000
    s6 = c[s6_start:s7_start]
    print(s6[:2500])
    print("...TOTAL:", len(s6), "chars")
