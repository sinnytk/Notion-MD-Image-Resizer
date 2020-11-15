
import re
import sys
from os import path
headings3 = re.compile(r'(### .+)')

assert (len(sys.argv) > 1),"File destination missing"

md_file = sys.argv[1]

f = open(md_file,mode='r')
matches = re.findall(headings3, f.read())
print("### Index")
for match in matches:
    text = match[4:]
    hyperlink = match.replace(' ','\ ')
    print(f"\t - [{text}]({hyperlink})")