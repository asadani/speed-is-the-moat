# -*- coding: utf-8 -*-
"""Flatten the variable display/body faces into static woff2 instances.

Chrome emits Type 3 fonts when printing variable-font instances to PDF, which is
unusable for print. Static instances embed properly. Google Fonts ships only the
variable masters for these families, so the statics are cut here.
"""
import io, os, sys, urllib.request
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
os.makedirs(OUT, exist_ok=True)

RAW = "https://raw.githubusercontent.com/google/fonts/main/ofl/%s"

# family dir, variable file, axis pins per instance -> output name
JOBS = [
    ("archivo", "Archivo[wdth,wght].ttf",
     [({"wdth": 100, "wght": 400}, "Archivo-Regular"),
      ({"wdth": 100, "wght": 600}, "Archivo-SemiBold"),
      ({"wdth": 100, "wght": 700}, "Archivo-Bold")]),
    ("sourceserif4", "SourceSerif4[opsz,wght].ttf",
     [({"opsz": 11, "wght": 400}, "SourceSerif4-Regular"),
      ({"opsz": 11, "wght": 600}, "SourceSerif4-SemiBold")]),
]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=90).read()


def main():
    made = []
    for fam, varfile, instances in JOBS:
        cache = os.path.join(OUT, "_var_" + varfile.replace("[", "_").replace("]", "_"))
        if not os.path.exists(cache):
            data = fetch(RAW % (fam + "/" + urllib.parse.quote(varfile)))
            open(cache, "wb").write(data)
            print("fetched %-34s %d KB" % (varfile, len(data) // 1024))
        for pins, name in instances:
            font = TTFont(cache)
            static = instancer.instantiateVariableFont(font, pins, inplace=False, updateFontNames=True)
            dst = os.path.join(OUT, name + ".woff2")
            static.flavor = "woff2"
            static.save(dst)
            static.close()
            font.close()
            made.append(dst)
            print("  cut   %-28s %d KB" % (name + ".woff2", os.path.getsize(dst) // 1024))

    # mono is already static upstream; just convert to woff2 for size
    for name in ["IBMPlexMono-Regular", "IBMPlexMono-Medium", "IBMPlexMono-SemiBold"]:
        src = os.path.join(OUT, name + ".ttf")
        dst = os.path.join(OUT, name + ".woff2")
        if os.path.exists(src) and not os.path.exists(dst):
            f = TTFont(src)
            f.flavor = "woff2"
            f.save(dst)
            f.close()
            print("  conv  %-28s %d KB" % (name + ".woff2", os.path.getsize(dst) // 1024))
            made.append(dst)

    total = sum(os.path.getsize(m) for m in made if os.path.exists(m))
    print("\n%d faces, %d KB total" % (len(made), total // 1024))


if __name__ == "__main__":
    import urllib.parse
    main()
