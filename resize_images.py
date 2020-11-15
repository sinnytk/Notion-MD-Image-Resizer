
import re
import sys
from os import path
OLD_IMG_TAG = re.compile(r'!\[Lecture.+\]\((.+)\)')

assert (len(sys.argv) > 1),"File destination missing"

md_file = sys.argv[1]

f = open(md_file,mode='r+')
new_text = re.sub(OLD_IMG_TAG,r'<img src="\1" width="500"/>',f.read())
f.write(new_text)