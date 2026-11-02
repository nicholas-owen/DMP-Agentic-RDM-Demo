#!/usr/bin/env python3
"""Two-way traceability check between the findings register and the panel report.

Usage:
    python3 tools/check_trace.py register/round2.json report/report.md

Checks:
  invented          IDs cited in the report that are not in the register
  cites_withdrawn   withdrawn findings cited in the body of the report
  dropped           findings that are not withdrawn but never cited
  withdrawn_unlisted  withdrawn findings missing from "Withdrawn during discussion"
  uncited_lines     lines in the issue sections that cite no finding

Exit status is 1 if anything other than withdrawn_unlisted is found, else 0.
"""
import json
import re
import sys

ID = r"(?:STW|IG|BIO|ETH|TRE)-\d+"
ID_RE = re.compile(rf"\b{ID}\b")
BRACKET_RE = re.compile(r"\[([^\]]*)\]")
ISSUE_SECTIONS = ("major issues", "minor issues", "points of disagreement")


def load_register(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    live, withdrawn = set(), set()
    for review in data.get("reviews", []):
        for finding in review.get("findings", []):
            target = withdrawn if finding.get("status") == "withdrawn" else live
            target.add(finding["id"])
    return live, withdrawn


def sections(text):
    """Split the report into (heading, lines) pairs at level-2 headings."""
    out, heading, lines = [], "", []
    for line in text.splitlines():
        if line.startswith("## "):
            out.append((heading, lines))
            heading, lines = line[3:].strip().lower(), []
        else:
            lines.append(line)
    out.append((heading, lines))
    return out


def bracket_ids(line):
    ids = set()
    for group in BRACKET_RE.findall(line):
        ids.update(ID_RE.findall(group))
    return ids


def main(register_path, report_path):
    live, withdrawn = load_register(register_path)
    with open(report_path, encoding="utf-8") as fh:
        text = fh.read()

    cited_body, listed_withdrawn, uncited = set(), set(), []
    for heading, lines in sections(text):
        if heading.startswith("withdrawn during discussion"):
            for line in lines:
                listed_withdrawn.update(ID_RE.findall(line))
            continue
        for line in lines:
            cited_body.update(bracket_ids(line))
            body = line.strip()
            if (
                heading in ISSUE_SECTIONS
                and body
                and not body.startswith("#")
                and body.rstrip(".").lower() != "none"
                and not bracket_ids(line)
            ):
                uncited.append(f"[{heading}] {body}")

    results = {
        "invented": sorted(cited_body - live - withdrawn),
        "cites_withdrawn": sorted(cited_body & withdrawn),
        "dropped": sorted(live - cited_body),
        "withdrawn_unlisted": sorted(withdrawn - listed_withdrawn),
        "uncited_lines": uncited,
    }

    print(f"Findings in register: {len(live)} live, {len(withdrawn)} withdrawn")
    print(f"Live findings cited in report: {len(live & cited_body)} of {len(live)}")
    for name, items in results.items():
        print(f"\n{name}: {len(items)}")
        for item in items:
            print(f"  {item}")

    failed = any(results[k] for k in results if k != "withdrawn_unlisted")
    print("\nRESULT:", "PROBLEMS FOUND" if failed else "PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
