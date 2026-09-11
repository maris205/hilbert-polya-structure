"""Lossless-in-scope readable extraction: MathML alttext, selected sections.

The raw HTML is separately retained. This utility is not scientific evidence.
"""
from html.parser import HTMLParser
from pathlib import Path
import sys


class Extract(HTMLParser):
    def __init__(self, wanted):
        super().__init__()
        self.wanted = wanted
        self.depth = 0
        self.math = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section":
            if self.depth or attrs.get("id") in self.wanted:
                self.depth += 1
        if not self.depth:
            return
        if tag == "math":
            self.math += 1
            self.parts.append(" $" + attrs.get("alttext", "MISSING_ALTTEXT") + "$ ")
        elif tag in {"p", "tr", "h2", "h3", "h4", "h5", "li"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag == "math" and self.math:
            self.math -= 1
        if tag == "section" and self.depth:
            self.depth -= 1
        if self.depth and tag in {"p", "tr", "h2", "h3", "h4", "h5", "li"}:
            self.parts.append("\n")

    def handle_data(self, data):
        if self.depth and not self.math:
            self.parts.append(data)


source, target = map(Path, sys.argv[1:3])
parser = Extract(set(sys.argv[3:]))
parser.feed(source.read_text())
lines = [" ".join(line.split()) for line in "".join(parser.parts).splitlines()]
target.write_text("\n".join(line for line in lines if line) + "\n")
