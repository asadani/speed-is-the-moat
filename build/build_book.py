# -*- coding: utf-8 -*-
"""Build the designed edition: HTML -> headless Chrome -> folio-stamped PDF.

Reads  build/book.html.in   (template, with a {{COVER_DATA_URI}} slot)
Writes speed-is-the-moat.html
       speed-is-the-moat.pdf
"""
import io, os, sys, base64, subprocess, shutil, tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

TEMPLATE = "build/book.html.in"
HTML_OUT = "speed-is-the-moat.html"
PDF_OUT = "speed-is-the-moat.pdf"
COVER_SRC = "speed-is-the-moat-cover.png"
COVER_PAGE = "build/cover-page.jpg"
FOLIO_TTF = "build/fonts/IBMPlexMono-Regular.ttf"

CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"


FACES = [
    ("Archivo",        400, "Archivo-Regular.woff2"),
    ("Archivo",        600, "Archivo-SemiBold.woff2"),
    ("Archivo",        700, "Archivo-Bold.woff2"),
    ("Source Serif 4", 400, "SourceSerif4-Regular.woff2"),
    ("Source Serif 4", 600, "SourceSerif4-SemiBold.woff2"),
    ("IBM Plex Mono",  400, "IBMPlexMono-Regular.woff2"),
    ("IBM Plex Mono",  500, "IBMPlexMono-Medium.woff2"),
    ("IBM Plex Mono",  600, "IBMPlexMono-SemiBold.woff2"),
]


def font_faces():
    """Inline every face. Static instances only -- Chrome degrades variable
    fonts to Type 3 when printing, which is unusable for print."""
    out, total = [], 0
    for fam, wght, fname in FACES:
        path = os.path.join("build", "fonts", fname)
        if not os.path.exists(path):
            sys.exit("missing font %s -- run build/make_fonts.py first" % path)
        blob = open(path, "rb").read()
        total += len(blob)
        b64 = base64.b64encode(blob).decode("ascii")
        out.append(
            '@font-face{font-family:"%s";font-style:normal;font-weight:%d;'
            'font-display:block;src:url(data:font/woff2;base64,%s) format("woff2")}'
            % (fam, wght, b64)
        )
    print("  fonts  %d faces inlined, %d KB raw" % (len(FACES), total // 1024))
    return "\n".join(out)


# ---------------------------------------------------------------- 1. HTML
def build_html():
    if not os.path.exists(COVER_PAGE):
        sys.exit("missing %s -- run build/make_cover_page.py first" % COVER_PAGE)
    blob = open(COVER_PAGE, "rb").read()
    uri = "data:image/jpeg;base64," + base64.b64encode(blob).decode("ascii")
    print("  cover  full-bleed A4 page, %d KB embedded" % (len(blob) // 1024))

    s = io.open(TEMPLATE, encoding="utf-8").read()
    if "{{COVER_PAGE_URI}}" not in s:
        sys.exit("template has no cover slot")
    s = s.replace("{{COVER_PAGE_URI}}", uri)
    s = s.replace("{{FONT_FACES}}", font_faces())
    io.open(HTML_OUT, "w", encoding="utf-8", newline="\n").write(s)
    print("  html   %s, %.2f MB" % (HTML_OUT, len(s.encode("utf-8")) / 1048576.0))


# ---------------------------------------------------------------- 2. PDF
def build_pdf():
    if not os.path.exists(CHROME):
        sys.exit("chrome not found at %s" % CHROME)
    raw = os.path.join(tempfile.gettempdir(), "speed-moat-raw.pdf")
    if os.path.exists(raw):
        os.remove(raw)
    profile = tempfile.mkdtemp(prefix="chrome-book-")
    url = "file:///" + os.path.abspath(HTML_OUT).replace("\\", "/")
    cmd = [
        CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=30000",
        "--user-data-dir=" + profile,
        "--print-to-pdf=" + raw,
        url,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    shutil.rmtree(profile, ignore_errors=True)
    if not os.path.exists(raw):
        sys.exit("chrome produced no pdf\nstdout:%s\nstderr:%s" % (r.stdout[-1500:], r.stderr[-1500:]))
    print("  chrome rendered %d KB" % (os.path.getsize(raw) // 1024))
    return raw


# ---------------------------------------------------------------- 3. folios
def stamp(raw):
    import fitz
    doc = fitz.open(raw)
    n = doc.page_count
    for i, page in enumerate(doc):
        if i == 0:          # no folio on the cover
            continue
        w, h = page.rect.width, page.rect.height
        page.insert_text(
            (w / 2.0 - 12, h - 30),
            "%d" % (i + 1),
            fontsize=8,
            fontfile=FOLIO_TTF,
            fontname="PlexMono",
            color=(0.49, 0.52, 0.58),
        )
    doc.subset_fonts()
    if os.path.exists(PDF_OUT):
        try:
            os.remove(PDF_OUT)
        except PermissionError:
            sys.exit("%s is open in a viewer -- close it and rebuild" % PDF_OUT)
    doc.save(PDF_OUT, garbage=4, deflate=True)
    doc.close()
    print("  pdf    %s, %d pages, %d KB" % (PDF_OUT, n, os.path.getsize(PDF_OUT) // 1024))
    return n


# ---------------------------------------------------------------- 4. verify
def verify(pages):
    import fitz
    doc = fitz.open(PDF_OUT)
    problems = []

    fonts = set()
    for p in doc:
        for f in p.get_fonts(full=True):
            fonts.add((f[3], f[1]))          # basefont, type
    embedded = [f for f in fonts if not f[0].startswith("Helv")]
    print("  fonts  %d face(s):" % len(fonts))
    for bf, typ in sorted(fonts):
        print("         %-42s %s" % (bf, typ))
    if len(embedded) < len(fonts):
        problems.append("a base-14 font leaked in (not embedded)")
    t3 = [f for f in fonts if "T3" in f[0] or f[1] == "n/a" or not f[0]]
    if t3:
        problems.append("Type 3 / unembedded faces present: %s" % t3)

    import re as _re
    txt = _re.sub(r"\s+", " ", "".join(doc[i].get_text() for i in range(min(3, doc.page_count))))
    for probe in ["Speed Is", "the Moat", "Anuj Sadani"]:
        if probe not in txt.replace("\n", " ").replace("  ", " "):
            problems.append("cover/front text missing: %r" % probe)

    import re
    all_txt = re.sub(r"\s+", " ", "".join(p.get_text() for p in doc))
    for probe in ["half-life", "CHI 2026", "Latency Service Level Agreement",
                  "source ledger", "PagedAttention"]:
        if probe.lower() not in all_txt.lower():
            problems.append("body text missing: %r" % probe)
    if "{{COVER_PAGE_URI}}" in all_txt:
        problems.append("template placeholder leaked into output")

    images = sum(len(p.get_images()) for p in doc)
    print("  images %d embedded" % images)
    if images < 1:
        problems.append("cover image did not render")

    print("  text   %d chars extracted across %d pages" % (len(all_txt), doc.page_count))
    doc.close()
    return problems


if __name__ == "__main__":
    print("building designed edition")
    build_html()
    raw = build_pdf()
    n = stamp(raw)
    issues = verify(n)
    print("")
    if issues:
        print("PROBLEMS:")
        for p in issues:
            print("  - %s" % p)
        sys.exit(1)
    print("OK - %s and %s built and verified" % (HTML_OUT, PDF_OUT))
