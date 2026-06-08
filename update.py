import re
c = open("E:/WORKFLOW/PRICEWEB/index.html", "r", encoding="utf-8").read()

# 1. Remove TARIFF CARDS CSS block
pat_start = "/* ═══════════════════════════════════════════════\n   TARIFF CARDS (radio group)"
pat_end = "/* ═══════════════════════════════════════════════\n   WORK STEPS (info only)"
idx_start = c.find(pat_start)
if idx_start >= 0:
    while idx_start > 0 and c[idx_start-1] == "\n":
        idx_start -= 1
    idx_end = c.find(pat_end)
    if idx_end >= 0:
        c = c[:idx_start] + c[idx_end:]
        print("Removed TARIFF CSS block")

# 2. Remove TARIFF CARDS JS block
js_pat = "// ═══ TARIFF CARDS ═══"
idx_start = c.find(js_pat)
if idx_start >= 0:
    while idx_start > 0 and c[idx_start-1] == "\n":
        idx_start -= 1
    js_end_marker = "  if(radio.checked) card.classList.add('\''checked'\'');"
    idx_rel = c[idx_start:].find(js_end_marker)
    if idx_rel >= 0:
        idx_end = idx_start + idx_rel + len(js_end_marker) + 1
        while idx_end < len(c) and c[idx_end] == "\n":
            idx_end += 1
        c = c[:idx_start] + c[idx_end:]
        print("Removed TARIFF JS block")
    else:
        print("JS end marker not found")
else:
    print("JS start marker not found")

# 3. Remove responsive and transition tariff-card CSS
c = c.replace(".tariff-card{min-width:100%}", "")
c = re.sub(r"\.tariff-card\{transition:all \.3s cubic-bezier\(\.4,0,\.2,1\)\}\n", "", c)
c = re.sub(r"\.tariff-card:hover\{transform:translateY\(-2px\);border-color:rgba\(220,38,38,\.3\);box-shadow:0 4px 24px rgba\(220,38,38,\.1\)\}\n", "", c)

open("E:/WORKFLOW/PRICEWEB/index.html", "w", encoding="utf-8").write(c)
final = open("E:/WORKFLOW/PRICEWEB/index.html", "r", encoding="utf-8").read()
print(f"Remaining: tariff-card refs = {final.count('\''tariff-card'\'')}, TARIFF CARDS text = {'TARIFF CARDS' in final}")
print(f"Size: {len(final)} bytes")
