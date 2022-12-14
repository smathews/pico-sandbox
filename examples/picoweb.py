import picoweb
import network
import logger
import utemplate.source
import os

ap = network.WLAN(network.AP_IF)
ap.config(essid="foobar", password="foobarfoobar")
ap.active(True)

while ap.active() == False:
    pass

print(ap.ifconfig())

app = picoweb.WebApp("Foobar")

# Delete cached templates before loading the directory
# Needed during testing, maybe not for prod
for file in os.listdir("templates"):
    if file[-3:] == ".py":
        print("Deleteing template cache file: %s" % file)
        os.remove("templates/%s" % file)

# Override the template loader in pico, this is because it
# expects the templates to be in its lib directory, dumb
app.template_loader = utemplate.source.Loader(None, "templates")

@app.route("/")
def index(req, resp):
    data = {"name": "Pico"}

    if req.method == "POST":
        yield from req.read_form_data()
        data["name"] = req.form["name"]

    yield from picoweb.start_response(resp)
    yield from app.render_template(resp, "hello.tpl.html", (data,))

# Send our logger in, ulogger is the default (its dependencies are too large for rpico)
app.run(log=logger, debug=True, host="0.0.0.0", port=80)
