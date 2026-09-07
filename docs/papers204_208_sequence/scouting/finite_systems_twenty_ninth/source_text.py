"""Documentary HTML text extraction only; does not evaluate a finite map."""
from html.parser import HTMLParser
from pathlib import Path
import sys

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts=[]
        self.suppressed=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'):
            self.suppressed+=1
        if tag in ('p','div','section','h1','h2','h3','h4','h5','h6','li'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style'):
            self.suppressed-=1
        if tag in ('p','div','section','h1','h2','h3','h4','h5','h6','li'):
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.suppressed:
            self.parts.append(data)

parser=Text()
parser.feed(Path(sys.argv[1]).read_text())
print('\n'.join(line.strip() for line in ''.join(parser.parts).splitlines() if line.strip()))
