#!/usr/bin/env python3
"""Compile manuscripts and validate committed PDF snapshots."""

from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf"
MANIFEST = OUTPUT / "manifest.json"
BUILD = ROOT / ".build"

README_ALLOWED_COMMANDS = {
    "Phi", "Rightarrow", "Theta", "frac", "infty", "kappa", "lambda", "le",
    "left", "log", "longrightarrow", "mathbb", "mathcal", "mathrm", "qquad",
    "rho", "right", "sigma", "sim", "sqrt", "text", "to", "varphi",
}

DOCUMENTS = [
    ("papers/01-luce-boundary-cycle-laws/luce-boundary-cycle-laws.tex", "luce-boundary-cycle-laws.pdf"),
    ("papers/02-mesoscopic-luce-cycles/mesoscopic-luce-cycles.tex", "mesoscopic-luce-cycles.pdf"),
    ("papers/03-luce-erdos-turan/luce-erdos-turan.tex", "luce-erdos-turan.pdf"),
    ("papers/04-luce-edgeworth/luce-edgeworth.tex", "luce-edgeworth.pdf"),
    ("papers/05-one-shuffle-universality/one-shuffle-universality.tex", "one-shuffle-universality.pdf"),
    ("papers/06-radial-lru-extremality/radial-lru-extremality.tex", "radial-lru-extremality.pdf"),
    ("papers/07-residual-mass-transform-order/residual-mass-transform-order.tex", "residual-mass-transform-order.pdf"),
    ("papers/08-thorp-cycle-universality/thorp-cycle-universality.tex", "thorp-cycle-universality.pdf"),
    ("notes/working/functional-luce-erdos-turan.tex", "functional-luce-erdos-turan.pdf"),
    ("notes/working/one-shuffle-edgeworth-optimality.tex", "one-shuffle-edgeworth-optimality.pdf"),
    ("third_party/openai-thorp/main.tex", "openai-thorp-mixing.pdf"),
]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def source_digest(path: Path) -> str:
    h = hashlib.sha256(path.read_bytes())
    if path == ROOT / "third_party/openai-thorp/main.tex":
        for name in ("conditional-flow.tex", "references.tex"):
            q = path.parent / name
            h.update(("\0" + name + "\0").encode())
            h.update(q.read_bytes())
    return h.hexdigest()

def check_readme_math() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (r"\(", r"\)", r"\[", r"\]", r"\!", r"\left[", r"\right]", r"\newcommand", r"\renewcommand", r"\def"):
        if token in text:
            raise RuntimeError("README contains forbidden TeX syntax: " + token)
    for macro in (r"\Ee",r"\Pp",r"\TV",r"\Kol",r"\ord",r"\lcm",r"\dd",
                  r"\PD",r"\GEM",r"\cL",r"\R",r"\N",r"\one",r"\Pois"):
        if re.search(re.escape(macro) + r"(?![A-Za-z])", text):
            raise RuntimeError("README contains unexpanded manuscript macro: " + macro)
    commands = set(re.findall(r"\\([A-Za-z]+)", text))
    unsupported = sorted(commands - README_ALLOWED_COMMANDS)
    if unsupported:
        raise RuntimeError(
            "README contains unsupported/unreviewed TeX command(s): " + ", ".join(unsupported)
        )
    if text.count("$$") % 2:
        raise RuntimeError("README has unmatched display-math delimiter")
    in_display = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "$":
            raise RuntimeError("README has a standalone single-dollar delimiter")
        if "$$" in line and stripped != "$$":
            raise RuntimeError("README display delimiter must occupy its own line: " + line)
        if stripped == "$$":
            in_display = not in_display
            continue
        if in_display:
            if re.fullmatch(r"=+", stripped) or re.fullmatch(r"-+", stripped):
                raise RuntimeError(
                    "README display contains a Markdown structural line: " + line
                )
            if re.match(r"^[+*-]\s+", stripped):
                raise RuntimeError(
                    "README display contains a Markdown list marker: " + line
                )

def check_readme_links() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith("#") or re.match(r"[A-Za-z][A-Za-z0-9+.-]*:", target):
            continue
        local = target.split("#",1)[0]
        if local and not (ROOT / local).exists():
            raise RuntimeError("Broken README link: " + local)

def check_authors() -> None:
    for rel,_ in DOCUMENTS[:-1]:
        if "Christopher D. Long" not in (ROOT / rel).read_text(encoding="utf-8"):
            raise RuntimeError("Missing Christopher D. Long attribution: " + rel)
    if r"\author{OpenAI}" not in (ROOT / "third_party/openai-thorp/main.tex").read_text(encoding="utf-8"):
        raise RuntimeError("Pinned Thorp source lost OpenAI attribution")

def check_log(log: str, source: Path) -> None:
    patterns=(r"^!",r"LaTeX Warning:.*undefined",r"Citation .* undefined",
              r"Reference .* undefined",r"multiply defined",r"Overfull ")
    bad=[line for line in log.splitlines() if any(re.search(p,line) for p in patterns)]
    if bad:
        raise RuntimeError("LaTeX diagnostics in %s:\n%s" % (source, "\n".join(bad[:30])))

def pdf_text(path: Path) -> str:
    return subprocess.check_output(["pdftotext","-layout",str(path),"-"], text=True, encoding="utf-8")

def build_one(source: Path, output_name: str, env: dict[str,str]):
    work = BUILD / output_name.removesuffix(".pdf")
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)
    cmd=["latexmk","-pdf","-g","-interaction=nonstopmode","-halt-on-error",
         "-file-line-error","-latexoption=-no-shell-escape","-outdir="+str(work),source.name]
    result=subprocess.run(cmd,cwd=source.parent,env=env,capture_output=True,text=True,timeout=300)
    (work/"build-console.txt").write_text(result.stdout+result.stderr,encoding="utf-8")
    if result.returncode:
        raise RuntimeError("LaTeX failed for %s; see %s" % (source, work/"build-console.txt"))
    built=work/(source.stem+".pdf")
    log=(work/(source.stem+".log")).read_text(errors="replace")
    check_log(log,source)
    info=subprocess.check_output(["pdfinfo",str(built)],text=True)
    pages=int(re.search(r"^Pages:\s+(\d+)",info,re.M).group(1))
    return built,pages,[x for x in log.splitlines() if "Underfull " in x]

def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    for command in ("latexmk","pdflatex","pdftotext","pdfinfo"):
        if shutil.which(command) is None:
            raise RuntimeError("Missing dependency: "+command)
    for rel,_ in DOCUMENTS:
        if not (ROOT/rel).exists():
            raise RuntimeError("Missing manuscript source: "+rel)
    for name in ("conditional-flow.tex","references.tex"):
        if not (ROOT/"third_party/openai-thorp"/name).exists():
            raise RuntimeError("Missing Thorp companion source: "+name)
    check_authors()
    check_readme_math()

    old={}
    if args.check:
        if not MANIFEST.exists():
            raise RuntimeError("Missing PDF manifest; run make pdf")
        records=json.loads(MANIFEST.read_text(encoding="utf-8"))["documents"]
        old={r["source"]:r for r in records}
        if set(old)!={rel for rel,_ in DOCUMENTS}:
            raise RuntimeError("Manifest/source list mismatch; run make pdf")
        for rel,name in DOCUMENTS:
            source=ROOT/rel; pdf=OUTPUT/name; rec=old[rel]
            if rec["source_sha256"] != source_digest(source):
                raise RuntimeError("Source changed; run make pdf: "+rel)
            if not pdf.exists() or rec["pdf_sha256"] != digest(pdf):
                raise RuntimeError("Missing or modified PDF; run make pdf: "+name)

    env=dict(os.environ,SOURCE_DATE_EPOCH="1791504000",FORCE_SOURCE_DATE="1",TZ="UTC")
    records=[]; copies=[]
    for rel,name in DOCUMENTS:
        source=ROOT/rel
        print("Building "+rel,flush=True)
        built,pages,underfull=build_one(source,name,env)
        for line in underfull[:8]:
            print("  Nonfatal typography diagnostic: "+line)
        committed=OUTPUT/name
        if args.check:
            freshhash=digest(built)
            committedhash=digest(committed)
            if freshhash != committedhash:
                if pdf_text(built) != pdf_text(committed):
                    raise RuntimeError("Rebuilt PDF content differs; run make pdf: "+name)
                raise RuntimeError(
                    "Rebuilt PDF bytes differ despite matching extracted text; "
                    "refresh the deterministic snapshot with make pdf: "+name
                )
            if freshhash != old[rel]["pdf_sha256"]:
                raise RuntimeError("Rebuilt PDF hash disagrees with manifest: "+name)
            pdfhash=freshhash
        else:
            pdfhash=digest(built); copies.append((built,committed))
        records.append({"source":rel,"source_sha256":source_digest(source),
                        "pdf":str(committed.relative_to(ROOT)),
                        "pdf_sha256":pdfhash,"pages":pages})
    if not args.check:
        OUTPUT.mkdir(parents=True,exist_ok=True)
        for built,committed in copies:
            shutil.copyfile(built,committed)
        MANIFEST.write_text(json.dumps({"schema_version":1,"documents":records},indent=2)+"\n",encoding="utf-8")
    check_readme_links()
    check_readme_math()
    print("Verified %d documents, README links, and README math syntax." % len(DOCUMENTS))

if __name__ == "__main__":
    try:
        main()
    except (RuntimeError,subprocess.SubprocessError,OSError,ValueError,KeyError,AttributeError) as exc:
        print(str(exc),file=sys.stderr); sys.exit(1)
