#!/usr/bin/env python3
"""Check protected Markdown content in the bundled evaluation cases.

This is a preservation check, not a Korean grammar or semantic quality grader.
Only the Markdown forms documented in evals/README.md are covered.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

FENCE_START = re.compile(r"^ {0,3}(\x60{3,}|~{3,})(.*)$")
INLINE = re.compile(r"(?<!\x60)(\x60+)(?!\x60)(.+?)(?<!\x60)\1(?!\x60)", re.DOTALL)
MARKDOWN_LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
WIKI_LINK = re.compile(r"!?\[\[([^\]\n]+)\]\]")


def protected(text):
    blocks, prose, block = [], [], []
    marker = None
    for line in text.splitlines(keepends=True):
        if marker is None:
            match = FENCE_START.match(line)
            if match:
                marker = match[1]
                block = [line]
            else:
                prose.append(line)
        else:
            block.append(line)
            if re.fullmatch(r" {0,3}" + re.escape(marker[0]) +
                            "{" + str(len(marker)) + r",}[ \t]*\r?\n?", line):
                blocks.append("".join(block).rstrip("\r\n"))
                block, marker = [], None
    if marker is not None:
        raise ValueError("Unclosed fenced code block")
    body = "".join(prose)
    inline = [match[2] for match in INLINE.finditer(body)]
    body = INLINE.sub("", body)
    return {
        "fenced_code": blocks,
        "inline_code": Counter(inline),
        "markdown_targets": Counter(MARKDOWN_LINK.findall(body)),
        "wiki_targets": Counter(WIKI_LINK.findall(body)),
    }


def indexed(document, label, output=False):
    if not isinstance(document, dict) or not isinstance(document.get("cases"), list):
        raise ValueError(f"{label}: expected an object with a cases array")
    result = {}
    for row in document["cases"]:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            raise ValueError(f"{label}: each case requires a string id")
        case_id = row["id"]
        if case_id in result:
            raise ValueError(f"{label}: duplicate id {case_id}")
        fields = ("corrected", "notes") if output else ("text",)
        if any(not isinstance(row.get(key), str) for key in fields):
            raise ValueError(f"{label}: {case_id} requires string fields {fields}")
        result[case_id] = row
    return result


def audit(inputs, outputs):
    original = indexed(inputs, "inputs")
    revised = indexed(outputs, "outputs", output=True)
    errors = []
    if original.keys() != revised.keys():
        errors.append(f"IDs differ: missing={sorted(original.keys() - revised.keys())}, "
                      f"extra={sorted(revised.keys() - original.keys())}")
    for case_id in original.keys() & revised.keys():
        before = protected(original[case_id]["text"])
        after = protected(revised[case_id]["corrected"])
        for name in before:
            if before[name] != after[name]:
                errors.append(f"{case_id}: {name} changed")
    return sorted(errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    parser.add_argument("outputs", type=Path)
    args = parser.parse_args()
    try:
        inputs = json.loads(args.inputs.read_text(encoding="utf-8"))
        outputs = json.loads(args.outputs.read_text(encoding="utf-8"))
        errors = audit(inputs, outputs)
    except (OSError, ValueError) as exc:
        print(f"Invalid input: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(inputs['cases'])} cases; protected content preserved. "
          "Semantic review is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
