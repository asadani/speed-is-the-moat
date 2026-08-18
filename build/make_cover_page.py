# -*- coding: utf-8 -*-
"""Fit the cover art to a full-bleed A4 page.

The art is 2:3; A4 is 1:1.414. Filling the page by width leaves 212px of excess
height at 300dpi. That is trimmed asymmetrically -- mostly off the top, where the
art is empty sky -- so the author name near the foot is never clipped.
"""
import os
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "speed-is-the-moat-cover.png")
DST = os.path.join(REPO, "build", "cover-page.jpg")

DPI = 300
A4_W = int(round(8.2677 * DPI))   # 210mm
A4_H = int(round(11.6929 * DPI))  # 297mm

TRIM_TOP_SHARE = 0.47   # of the excess; the rest comes off the bottom


def main():
    im = Image.open(SRC).convert("RGB")
    scale = A4_W / float(im.width)
    new_h = int(round(im.height * scale))
    im = im.resize((A4_W, new_h), Image.LANCZOS)

    excess = new_h - A4_H
    if excess < 0:
        raise SystemExit("art is shorter than the page; would letterbox")
    top = int(round(excess * TRIM_TOP_SHARE))
    im = im.crop((0, top, A4_W, top + A4_H))

    im.save(DST, "JPEG", quality=92, optimize=True, progressive=True, dpi=(DPI, DPI))
    print("cover page %dx%d px (A4 @ %ddpi), trimmed %dpx top / %dpx bottom, %d KB"
          % (A4_W, A4_H, DPI, top, excess - top, os.path.getsize(DST) // 1024))


if __name__ == "__main__":
    main()
