from flask import Flask, request

app = Flask(__name__)
const_str = "http-kit is a http server & client written from scrach for high performance clojure web applications, support async and websocket" * 200

@app.route('/')
def index():
    length = int(request.args.get("length"))
    return const_str[:length]

if __name__ == '__main__':
    app.run(port=3000, host='0.0.0.0')