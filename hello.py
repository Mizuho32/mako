import sys
import pathlib

from mako.template import Template
from mako.runtime import Context
from io import StringIO

text = \
"""
% if CONST:
for i in name:
    print("HI")
    "hello, ${name}!"
    "hi!, ${name}?"
% endif
"""

print("Original:")
print(text)
print("------")
print(text.__repr__())

mytemplate = Template(text)

buf = StringIO()
ctx = Context(buf, name="jack", CONST=True)
mytemplate.render_context(ctx)

print("After:")
print(buf.getvalue())
#print(buf.getvalue().__repr__())
print("---")
#print(mytemplate.render(name="jack"))
#print("---")
#print(mytemplate.render(name=False))
#print("---")

with open(sys.argv[1], "r") as h:
    text = h.read()

mytemplate = Template(text)
out = mytemplate.render(CONST=True)

path = pathlib.Path(sys.argv[1])
out_path = f"{path.stem}_out.py"
with open(out_path, "w") as h:
    h.write(out)

