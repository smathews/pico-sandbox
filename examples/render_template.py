import io, sys
import utemplate.source

tpl_name = "templates/test.tpl.html"

f_out = io.StringIO()
with open(tpl_name) as f_in:
    c = utemplate.source.Compiler(f_in, f_out,
        loader=utemplate.source.Loader(None, tpl_name))
    c.compile()
ns = {}
exec(f_out.getvalue(), ns)

buf = ""
for x in ns["render"](n=10,foo="xyz"):
    buf = buf + x

print(buf)
