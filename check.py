"""Sanity checks for the book. Run from the repo root:  python3 check.py"""
import re, os, sys, collections
EXPECT_ITEMS = {"10": 50, "12": 49}          # \item count of the original chapters (nothing may be dropped)
CH = {"10": "10/chapters/cbse-2018.tex", "12": "12/chapters/65-5-2.tex"}
bad = 0
def fail(msg):
    global bad; bad += 1; print("FAIL:", msg)
rd = lambda p: open(p).read()
for c in ("10", "12"):
    ch, fm = rd(CH[c]), rd(f"{c}/formulae/formulae.tex")
    n = len(re.findall(r"^\s*\\item", ch, re.M))
    if n != EXPECT_ITEMS[c]: fail(f"class {c}: {n} items, expected {EXPECT_ITEMS[c]} (question lost or duplicated)")
    qs = [l.strip() for l in ch.splitlines() if re.match(r"\s*\\item\s+\S", l)]
    for q, k in collections.Counter(qs).items():
        if k > 1: fail(f"class {c}: duplicated question text: {q[:60]}")
    labels = re.findall(r"\\label\{([^}]*)\}", ch + fm)
    for l, k in collections.Counter(labels).items():
        if k > 1: fail(f"class {c}: label defined twice: {l}")
    refs = set(re.findall(r"\\(?:eqref|ref|figref)\{([^}]*)\}", ch + fm))
    for r in sorted(refs - set(labels)): fail(f"class {c}: undefined reference {r}")
    for item in re.split(r"\\item", fm)[1:]:                     # each formula ITEM should be used
        ls = re.findall(r"\\label\{(eq:[^}]*)\}", item)
        others = fm.replace(item, "")
        if ls and not any(l in ch or l in others for l in ls):
            print(f"warn: class {c}: formula item with {ls[0]} is not used anywhere")
    for f in re.findall(r"\\includegraphics[^{]*\{([^}]*)\}", ch):
        if not os.path.exists(f"{c}/{f}"): fail(f"class {c}: missing figure {f}")
    for f in [x.replace("\\_","_") for x in re.findall(r"\{(codes/[^}]*)\}", ch)]:
        if not os.path.exists(f"{c}/{f}"): fail(f"class {c}: missing code {f}")
print("all checks passed" if not bad else f"{bad} problem(s)"); sys.exit(1 if bad else 0)
