from sanic import Sanic, response
import sys


app = Sanic(__name__)

class config:
    KEEP_ALIVE_TIMEOUT = 6000

app.config.from_object(config)
const_str = "http-kit is a http server & client written from scrach for high performance clojure web applications, support async and websocket" * 200

@app.route("/")
async def index(request):
    length = int(request.args.get("length"))
    return response.text(const_str[:length])


if __name__ == '__main__':
    port = 3000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    app.run(host='0.0.0.0', port=port, workers=4)