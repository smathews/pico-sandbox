import picoweb
import network
import logger

ap = network.WLAN(network.AP_IF)
ap.config(essid="foobar", password="foobarfoobar")
ap.active(True)

while ap.active() == False:
    pass

print(ap.ifconfig())

app = picoweb.WebApp("Foobar")

@app.route("/")
def index(req, resp):
    print(req)
    yield from picoweb.start_response(resp)
    yield from resp.awrite("<html><body><h1>Pico</h1></body></html>")

app.run(log=logger, debug=True, host="0.0.0.0", port=80)
