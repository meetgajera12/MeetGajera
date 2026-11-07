#!/usr/bin/env python3
"""
Regenerates every image under assets/ (banner, project diagrams, tech chips).
Optional: the README does not need this script to render on GitHub.

    pip install pillow
    python tools/build_assets.py --pizza path/to/Home.jpeg

Icons: Simple Icons (CC0) paths, exported to tools/icons.json.
The Pizza preview uses a genuine screenshot from the Pizza-Seles-Dashboard repo.
All other project previews are system diagrams drawn from each repo's README.
"""
import json, math, random, argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ICONS = json.loads((Path(__file__).parent / "icons.json").read_text())

# ---------- design tokens ----------
BG      = (11, 13, 16)
PANEL   = (18, 22, 27)
PANEL2  = (23, 28, 34)
BORDER  = (38, 45, 54)
TEXT    = (230, 237, 243)
MUTED   = (139, 148, 158)
DIM     = (88, 98, 110)
ACCENT  = (61, 220, 151)          # the single accent colour
ARROW   = (96, 106, 118)

def hexc(c): return "#%02x%02x%02x" % c

INTER = "/usr/share/fonts/opentype/inter/Inter-{}.otf"
MONO  = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono{}.ttf"
def inter(sz, w="Regular"): return ImageFont.truetype(INTER.format(w), sz)
def mono(sz, bold=False):   return ImageFont.truetype(MONO.format("-Bold" if bold else ""), sz)

# =====================================================================
#  SVG chips (technology strips + contact links)
# =====================================================================
CHIP_FONT = "'Inter','Segoe UI',-apple-system,Helvetica,Arial,sans-serif"
_measure = inter(14, "Medium")

def text_w(s): return _measure.getlength(s) * 1.06      # small safety margin

def chip(x, y, label, icon=None, h=36):
    w = 14 + 18 + 8 + text_w(label) + 16
    parts = [f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h}" rx="8" fill="{hexc(PANEL)}" stroke="{hexc(BORDER)}"/>']
    cy = y + h / 2
    if icon in ICONS and icon != "kaggle":
        s = 16 / 24
        parts.append(f'<g transform="translate({x+14},{cy-8}) scale({s})"><path fill="#c9d1d9" d="{ICONS[icon]["path"]}"/></g>')
    elif icon in ("in", "kaggle"):   # LinkedIn glyph removed from Simple Icons; Kaggle's is a tiny wordmark
        g = "in" if icon == "in" else "K"
        parts.append(f'<text x="{x+14}" y="{cy+5}" font-family="{CHIP_FONT}" font-size="14" font-weight="700" fill="#c9d1d9">{g}</text>')
    else:                   # no brand icon available: accent dot keeps the rhythm consistent
        parts.append(f'<circle cx="{x+22}" cy="{cy}" r="3.5" fill="{hexc(ACCENT)}"/>')
    parts.append(f'<text x="{x+40}" y="{cy+5}" font-family="{CHIP_FONT}" font-size="14" font-weight="500" fill="#d0d7de">{label}</text>')
    return "".join(parts), w

def chip_strip(items, path, max_w=880, h=36, gap=10):
    x = 0; rows = []; cur = []
    for label, icon in items:
        _, w = chip(0, 0, label, icon, h)
        if x + w > max_w and cur:
            rows.append(cur); cur = []; x = 0
        cur.append((label, icon, x, w)); x += w + gap
    rows.append(cur)
    body = []
    for r, row in enumerate(rows):
        for label, icon, cx, w in row:
            body.append(chip(cx, r * (h + gap), label, icon, h)[0])
    H = len(rows) * (h + gap) - gap
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{max_w}" height="{H}" viewBox="0 0 {max_w} {H}" role="img" '
           f'aria-label="{", ".join(l for l, _ in items)}">{"".join(body)}</svg>')
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(svg)

def single_chip(label, icon, path):
    inner, w = chip(1, 1, label, icon, 38)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w+2:.0f}" height="40" viewBox="0 0 {w+2:.0f} 40" role="img" aria-label="{label}">{inner}</svg>')
    Path(path).write_text(svg)

SKILLS = {
    "languages":    [("Python","python"),("SQL",None),("HTML","html5"),("CSS","css"),("JavaScript","javascript")],
    "databases":    [("MySQL","mysql")],
    "data":         [("NumPy","numpy"),("Pandas","pandas"),("Matplotlib",None),("Plotly","plotly"),("Seaborn",None),("Power BI",None)],
    "ml":           [("Scikit-learn","scikitlearn"),("XGBoost",None),("LightGBM",None),("CatBoost",None),("Optuna","optuna"),("SHAP",None)],
    "deeplearning": [("PyTorch","pytorch"),("TensorFlow","tensorflow"),("Keras","keras")],
    "genai":        [("LangChain","langchain"),("LangGraph","langgraph"),("HF Transformers","huggingface")],
    "backend":      [("FastAPI","fastapi"),("Streamlit","streamlit"),("REST APIs",None)],
    "tools":        [("Git","git"),("GitHub","github"),("Docker","docker"),("Hugging Face","huggingface"),("Groq",None),("FAISS",None),("Sentence Transformers",None)],
}
TECH = {
    "video":    [("Python","python"),("LangChain","langchain"),("LangGraph","langgraph"),("FastAPI","fastapi"),("Streamlit","streamlit"),("Hugging Face","huggingface"),("Groq",None),("Tavily",None)],
    "credit":   [("Python","python"),("Pandas","pandas"),("NumPy","numpy"),("Scikit-learn","scikitlearn"),("LightGBM",None),("Optuna","optuna"),("SHAP",None),("FastAPI","fastapi"),("Streamlit","streamlit")],
    "whatsapp": [("Python","python"),("Pandas","pandas"),("NumPy","numpy"),("Matplotlib",None),("Seaborn",None),("Streamlit","streamlit")],
    "rag":      [("LangGraph","langgraph"),("LangChain","langchain"),("FAISS",None),("Sentence Transformers",None),("Groq",None),("FastAPI","fastapi"),("Streamlit","streamlit")],
    "expense":  [("FastAPI","fastapi"),("LangChain","langchain"),("Groq",None),("Scikit-learn","scikitlearn"),("Pandas","pandas"),("RapidOCR",None),("Chart.js",None)],
}
LINKS = {"github": ("GitHub", "github"), "linkedin": ("LinkedIn", "in"), "email": ("Email", "gmail"), "kaggle": ("Kaggle", "kaggle")}

def build_chips():
    for k, v in SKILLS.items(): chip_strip(v, ASSETS / "skills" / f"{k}.svg")
    for k, v in TECH.items():   chip_strip(v, ASSETS / "tech" / f"{k}.svg", h=32, gap=8)
    (ASSETS / "links").mkdir(parents=True, exist_ok=True)
    for k, (l, i) in LINKS.items(): single_chip(l, i, ASSETS / "links" / f"{k}.svg")
    print("wrote SVG chips")

# =====================================================================
#  PNG helpers
# =====================================================================
def dotted_bg(W, H, step=40, col=(20, 25, 31)):
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    for yy in range(step // 2, H, step):
        for xx in range(step // 2, W, step):
            d.ellipse((xx-1.5, yy-1.5, xx+1.5, yy+1.5), fill=col)
    return im

def spaced(d, xy, s, font, fill, tracking=0):
    x, y = xy
    for ch in s:
        d.text((x, y), ch, font=font, fill=fill)
        x += font.getlength(ch) + tracking
    return x

def center_text(d, cx, y, s, font, fill):
    w = d.textlength(s, font=font); d.text((cx - w/2, y), s, font=font, fill=fill)

def node(d, x, y, w, h, title, sub=(), accent=False, tsz=28, ssz=21):
    d.rounded_rectangle((x, y, x+w, y+h), 14, fill=PANEL2 if accent else PANEL, outline=ACCENT if accent else BORDER, width=3 if accent else 2)
    ft, fs = inter(tsz, "SemiBold"), inter(ssz)
    lines = list(sub); th = tsz + (len(lines) * (ssz + 8) if lines else 0)
    ty = y + (h - th) / 2 - 2
    center_text(d, x + w/2, ty, title, ft, TEXT)
    for i, ln in enumerate(lines):
        center_text(d, x + w/2, ty + tsz + 8 + i * (ssz + 8), ln, fs, MUTED)
    return (x, y, w, h)

def arrow(d, pts, col=ARROW, wd=3, head=11):
    d.line(pts, fill=col, width=wd, joint="curve")
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    a = math.atan2(y2 - y1, x2 - x1)
    p = [(x2, y2), (x2 - head*math.cos(a - .42), y2 - head*math.sin(a - .42)), (x2 - head*math.cos(a + .42), y2 - head*math.sin(a + .42))]
    d.polygon(p, fill=col)

def label(d, x, y, s, col=MUTED, sz=19, center=True):
    f = inter(sz, "Medium")
    if center: x -= d.textlength(s, font=f) / 2
    d.text((x, y), s, font=f, fill=col)

def header(d, W, kind, title, sub):
    d.text((70, 52), kind, font=mono(19, True), fill=ACCENT)
    d.text((70, 88), title, font=inter(46, "Bold"), fill=TEXT)
    d.text((70, 150), sub, font=inter(24), fill=MUTED)
    d.line((70, 205, W-70, 205), fill=BORDER, width=2)

def canvas(kind, title, sub, W=1600, H=800):
    im = dotted_bg(W, H); d = ImageDraw.Draw(im)
    header(d, W, kind, title, sub); return im, d

def save(im, name):
    p = ASSETS / "projects" / name; p.parent.mkdir(parents=True, exist_ok=True)
    im.save(p, optimize=True); print("wrote", p.relative_to(ROOT))

R = lambda b: (b[0]+b[2], b[1]+b[3]//2)     # right-middle of node box
L = lambda b: (b[0], b[1]+b[3]//2)          # left-middle
B = lambda b: (b[0]+b[2]//2, b[1]+b[3])     # bottom-middle
T = lambda b: (b[0]+b[2]//2, b[1])          # top-middle

# =====================================================================
#  Project diagrams (every box maps to something in the repo README)
# =====================================================================
def video():
    im, d = canvas("SYSTEM DIAGRAM", "Video Intelligence & Research Agent", "LangGraph multi-agent workflow  ·  YouTube URL to structured research output")
    w, h, gap, x0 = 310, 130, 80, 70
    r1, r2 = 270, 520
    xs = [x0 + i*(w+gap) for i in range(4)]
    a = node(d, xs[0], r1, w, h, "YouTube URL", ["user input"])
    b = node(d, xs[1], r1, w, h, "Transcript extraction", ["transcript / video data"])
    c = node(d, xs[2], r1, w, h, "LangGraph workflow", ["agent orchestration"], accent=True)
    e = node(d, xs[3], r1, w, h, "Parallel agents", ["summary · key points · topics"])
    for p, q in [(a, b), (b, c), (c, e)]: arrow(d, [R(p), L(q)])
    f = node(d, xs[3], r2, w, h, "Claim extraction", ["claims worth checking"])
    g = node(d, xs[2], r2, w, h, "Web research", ["references via search"])
    hh = node(d, xs[1], r2, w, h, "Research synthesis", ["structured insights"])
    i = node(d, xs[0], r2, w, h, "Final response", ["research-oriented output"], accent=True)
    arrow(d, [B(e), T(f)]); arrow(d, [L(f), R(g)]); arrow(d, [L(g), R(hh)]); arrow(d, [L(hh), R(i)])
    d.text((70, 705), "Also supports comparing two videos: claims and topics are extracted per video, then passed to a comparison agent.", font=inter(22), fill=MUTED)
    save(im, "video-intelligence.png")

def credit():
    im, d = canvas("SYSTEM DIAGRAM", "Credit Risk Assessment System", "Explainable loan-default prediction  ·  Home Credit Default Risk dataset")
    w, h, gap, x0, y = 310, 130, 80, 70, 245
    xs = [x0 + i*(w+gap) for i in range(4)]
    n = [node(d, xs[0], y, w, h, "Home Credit data", ["application · bureau", "previous applications"]),
         node(d, xs[1], y, w, h, "Cleaning + features", ["ratios · aggregations", "encoding · merging"]),
         node(d, xs[2], y, w, h, "Model comparison", ["RF · XGBoost", "CatBoost · LightGBM"]),
         node(d, xs[3], y, w, h, "Optuna + SHAP", ["tuning · explainability"], accent=True)]
    for p, q in zip(n, n[1:]): arrow(d, [R(p), L(q)])
    # ROC-AUC bars: values copied from the repository README
    d.text((70, 430), "ROC-AUC BY MODEL", font=mono(18, True), fill=ACCENT)
    d.text((70, 458), "bars start at 0.50 (random guess)", font=inter(19), fill=DIM)
    data = [("Random Forest", .698, "0.698"), ("XGBoost", .721, "0.721"), ("CatBoost", .733, "0.733"), ("LightGBM (selected)", .7405, "0.7405")]
    bx, bw_max, by = 330, 560, 515
    for i, (nm, v, txt) in enumerate(data):
        yy = by + i*52
        sel = nm.startswith("LightGBM")
        d.text((70, yy+4), nm, font=inter(22, "SemiBold" if sel else "Regular"), fill=TEXT if sel else MUTED)
        ln = int((v - .5) / .25 * bw_max)
        d.rounded_rectangle((bx, yy, bx+ln, yy+34), 6, fill=ACCENT if sel else (52, 61, 72))
        d.text((bx+ln+14, yy+4), txt, font=mono(22, sel), fill=TEXT if sel else MUTED)
    # serving chain
    sx = 1010
    a = node(d, sx, 545, 230, 120, "FastAPI", ["POST /predict"], tsz=26)
    b = node(d, sx+300, 545, 230, 120, "Streamlit", ["interactive UI"], tsz=26)
    arrow(d, [R(a), L(b)])
    d.text((sx, 695), "returns default probability and risk category", font=inter(21), fill=MUTED)
    bx3 = B(n[3])[0]
    arrow(d, [(bx3, y+h), (bx3, 500), (sx+115, 500), T(a)])
    save(im, "credit-risk.png")

def whatsapp():
    im, d = canvas("SYSTEM DIAGRAM", "WhatsApp Chat Analyzer", "Exported chat to interactive analytics dashboard")
    w, h = 400, 130
    a = node(d, 70, 245, w, h, "Exported chat (.txt)", ["WhatsApp export, no media"])
    b = node(d, 600, 245, w, h, "Regex preprocessing", ["dates · users · messages"])
    c = node(d, 1130, 245, w, h, "Feature extraction", ["words · media · links · emojis"], accent=True)
    arrow(d, [R(a), L(b)]); arrow(d, [R(b), L(c)])
    mods = ["Chat statistics", "User activity", "Daily / monthly timelines", "Weekly activity heatmap", "Word frequency", "Emoji analysis"]
    d.text((70, 430), "ANALYSIS MODULES", font=mono(18, True), fill=ACCENT)
    mw, mh = 440, 74
    for i, m in enumerate(mods):
        cx = 70 + (i % 3) * (mw + 55); cy = 475 + (i // 3) * (mh + 24)
        d.rounded_rectangle((cx, cy, cx+mw, cy+mh), 12, fill=PANEL, outline=BORDER, width=2)
        d.ellipse((cx+24, cy+mh/2-5, cx+34, cy+mh/2+5), fill=ACCENT)
        d.text((cx+52, cy+mh/2-15), m, font=inter(25, "Medium"), fill=TEXT)
    d.text((70, 690), "Charts rendered with Matplotlib and Seaborn inside a Streamlit app.", font=inter(22), fill=MUTED)
    save(im, "whatsapp-analyzer.png")

def flow_row(d, spec, y, h, w=252, gap=50, x0=70):
    prev = None
    for i, (t, s, acc) in enumerate(spec):
        b = node(d, x0 + i*(w+gap), y, w, h, t, s, accent=acc, tsz=26, ssz=20)
        if prev: arrow(d, [R(prev), L(b)])
        prev = b

def movie():
    im, d = canvas("SYSTEM DIAGRAM", "Movie Recommender", "Content-based filtering  ·  TMDB 5000 Movies dataset")
    flow_row(d, [("TMDB data", ["movies + credits"], False), ("Metadata merge", ["genres · cast · crew", "keywords · overview"], False),
                 ("CountVectorizer", ["text to vectors"], False), ("Cosine similarity", ["precomputed matrix"], True), ("Top matches", ["Streamlit UI"], False)], 330, 150)
    d.text((70, 560), "Pick a movie, get the most similar titles instantly.", font=inter(26), fill=MUTED)
    d.text((70, 604), "The similarity matrix and movie table are stored as pickles for fast lookup.", font=inter(22), fill=DIM)
    save(im, "movie-recommender.png")

def pizza(shot):
    W, H = 1600, 800
    im = dotted_bg(W, H); d = ImageDraw.Draw(im)
    d.text((70, 52), "DASHBOARD  ·  SCREENSHOT FROM REPOSITORY", font=mono(19, True), fill=ACCENT)
    d.text((70, 88), "Pizza Sales Dashboard", font=inter(46, "Bold"), fill=TEXT)
    d.text((70, 150), "MySQL KPIs  ·  Power BI + DAX  ·  2015 order data", font=inter(24), fill=MUTED)
    s = Image.open(shot).convert("RGB")
    th = 560; tw = int(s.width * th / s.height)
    s = s.resize((tw, th), Image.LANCZOS)
    x = (W - tw) // 2; y = 205
    d.rounded_rectangle((x-6, y-6, x+tw+6, y+th+6), 10, outline=BORDER, width=2)
    im.paste(s, (x, y))
    save(im, "pizza-dashboard.png")

def potato():
    im, d = canvas("SYSTEM DIAGRAM", "Potato Leaf Disease Classification", "CNN image classifier  ·  TensorFlow / Keras")
    flow_row(d, [("Image upload", ["leaf photo"], False), ("Streamlit", ["frontend"], False), ("FastAPI", ["POST /predict"], False),
                 ("CNN model", ["saved .keras model"], True), ("Prediction", ["class + confidence"], False)], 245, 140)
    d.text((70, 450), "THREE CLASSES", font=mono(18, True), fill=ACCENT)
    for i, c in enumerate(["Early Blight", "Late Blight", "Healthy"]):
        cx = 70 + i*330
        d.rounded_rectangle((cx, 490, cx+300, 560), 12, fill=PANEL, outline=BORDER, width=2)
        d.ellipse((cx+22, 520, cx+32, 530), fill=ACCENT)
        d.text((cx+50, 508), c, font=inter(26, "Medium"), fill=TEXT)
    d.text((70, 610), "TRAINING", font=mono(18, True), fill=ACCENT)
    d.text((70, 645), "Data augmentation (ImageDataGenerator)  ·  Adam optimizer  ·  categorical cross-entropy", font=inter(24), fill=MUTED)
    save(im, "potato-classification.png")

def rag():
    im, d = canvas("SYSTEM DIAGRAM", "RAG Technical Documentation Assistant", "Self-corrective retrieval with LangGraph  ·  FAISS  ·  Groq")
    w, h, gap, x0 = 310, 120, 80, 70
    xs = [x0 + i*(w+gap) for i in range(4)]
    r1, r2 = 245, 510
    a = node(d, xs[0], r1, w, h, "User question", ["+ chat history"])
    b = node(d, xs[1], r1, w, h, "Query analysis", ["concise search query"])
    c = node(d, xs[2], r1, w, h, "FAISS retrieval", ["top-5 chunks"])
    e = node(d, xs[3], r1, w, h, "Document grading", ["LLM relevance check"], accent=True)
    for p, q in [(a, b), (b, c), (c, e)]: arrow(d, [R(p), L(q)])
    rw = node(d, xs[3], r2, w, h, "Rewrite query", ["re-retrieve · max 3 retries"])
    ws = node(d, xs[2], r2, w, h, "Web search fallback", ["Tavily · after retries fail"])
    gn = node(d, xs[1], r2, w, h, "Generate answer", ["context-only, with sources"], accent=True)
    an = node(d, xs[0], r2, w, h, "Answer", ["+ source chunks"])
    nx = xs[3] + w - 70
    arrow(d, [(nx, r1+h), (nx, r2)]); fw = inter(19, "Medium").getlength("not relevant"); label(d, nx - 14 - fw, 396, "not relevant", MUTED, 19, False)
    arrow(d, [L(rw), R(ws)])
    arrow(d, [L(ws), R(gn)]); arrow(d, [L(gn), R(an)])
    ex = xs[3] + 70; gx = xs[1] + w/2
    arrow(d, [(ex, r1+h), (ex, 440), (gx, 440), (gx, r2)], col=ACCENT)
    label(d, (ex + gx)/2, 406, "relevant", ACCENT, 19)
    d.text((70, 690), "Answers are generated only from retrieved context, with source chunks returned alongside.", font=inter(22), fill=MUTED)
    save(im, "rag-assistant.png")

def expense():
    im, d = canvas("SYSTEM DIAGRAM", "Smart Expense Tracker & AI Bill Manager", "Full-stack finance app  ·  OCR, RAG Q&A and ML forecasting")
    fe = node(d, 70, 340, 300, 190, "Web dashboard", ["Chart.js charts", "budget alerts", "hosted on Vercel"], tsz=27)
    be = node(d, 470, 270, 300, 330, "FastAPI backend", ["REST API", "ML models", "hosted on Render"], accent=True, tsz=27)
    arrow(d, [R(fe), L(be)])
    mods = [("OCR bill scanner", "RapidOCR"), ("Bill Q&A (RAG)", "LangChain + Groq"), ("Expense categorizer", "TF-IDF + scikit-learn"),
            ("Spending forecast", "Linear Regression"), ("Recurring detector", "Pandas pattern matching"), ("AI assistant", "Groq LLM")]
    mw, mh = 340, 100
    for i, (t, s) in enumerate(mods):
        cx = 850 + (i % 2) * (mw + 20); cy = 235 + (i // 2) * (mh + 24)
        d.rounded_rectangle((cx, cy, cx+mw, cy+mh), 12, fill=PANEL, outline=BORDER, width=2)
        d.text((cx+22, cy+20), t, font=inter(24, "SemiBold"), fill=TEXT)
        d.text((cx+22, cy+56), s, font=inter(20), fill=MUTED)
    mid = be[1] + be[3] // 2
    d.line((R(be)[0], mid, 808, mid), fill=ARROW, width=3)
    d.line((808, 285, 808, 533), fill=ARROW, width=3)
    for yy in (285, 409, 533): arrow(d, [(808, yy), (842, yy)])
    d.text((70, 690), "Receipts become categorized expenses; questions about a bill are answered from its OCR text.", font=inter(22), fill=MUTED)
    save(im, "smart-expense-tracker.png")

# =====================================================================
#  Banner
# =====================================================================
def banner():
    W, H = 1800, 540
    im = dotted_bg(W, H, 44, (19, 24, 30))
    rnd = random.Random(7)
    pts = sorted((1180 + rnd.random()*540, 70 + rnd.random()*400) for _ in range(22))
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
    for p in pts:
        for q in sorted(pts, key=lambda q: (q[0]-p[0])**2 + (q[1]-p[1])**2)[1:3]:
            od.line((p, q), fill=(61, 220, 151, 38), width=2)
    for i, p in enumerate(pts):
        hot = i in (3, 9, 15)
        r = 7 if hot else 4
        od.ellipse((p[0]-r, p[1]-r, p[0]+r, p[1]+r), fill=(61, 220, 151, 230 if hot else 70))
    im.paste(ov, (0, 0), ov); d = ImageDraw.Draw(im)
    d.rectangle((110, 148, 186, 153), fill=ACCENT)
    spaced(d, (104, 178), "MEET GAJERA", inter(132, "Bold"), TEXT, tracking=5)
    d.text((112, 346), "DATA SCIENCE  |  AI ENGINEERING  |  GENERATIVE AI", font=inter(34, "Medium"), fill=MUTED)
    d.text((112, 412), "B.E. ARTIFICIAL INTELLIGENCE & MACHINE LEARNING   ·   AHMEDABAD, INDIA", font=mono(21), fill=DIM)
    d.rectangle((0, H-4, W, H), fill=ACCENT)
    p = ASSETS / "banner.png"; p.parent.mkdir(exist_ok=True); im.save(p, optimize=True); print("wrote", p.relative_to(ROOT))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--pizza", default=None, help="path to the genuine Pizza dashboard screenshot")
    a = ap.parse_args()
    build_chips(); banner(); video(); credit(); whatsapp(); movie(); potato(); rag(); expense()
    if a.pizza: pizza(a.pizza)
