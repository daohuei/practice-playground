import time
import setproctitle
import multiprocessing
import random
import json
import socket
from datetime import datetime

import numpy as np
from bokeh.client import pull_session, push_session
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import CustomJS, ServerSentDataSource
from flask import Flask, Response, make_response, request


# def crossdomain(f):
#     def wrapped_function(*args, **kwargs):
#         resp = make_response(f(*args, **kwargs))
#         h = resp.headers
#         h["Access-Control-Allow-Origin"] = "*"
#         h["Access-Control-Allow-Methods"] = "GET, OPTIONS, POST"
#         h["Access-Control-Max-Age"] = str(21600)
#         requested_headers = request.headers.get("Access-Control-Request-Headers")
#         if requested_headers:
#             h["Access-Control-Allow-Headers"] = requested_headers
#         return resp

#     return wrapped_function


# def get_free_port(host="127.0.0.1"):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind((host, 0))
#     port = sock.getsockname()[1]
#     sock.close()
#     return port


class Streamer(multiprocessing.Process):
    def __init__(self, streamer_id):
        self.streamer_id = streamer_id
        self.bokeh_connection = None
        # self.flask = Flask("streamer_id")
        # self.port = get_free_port()
        self.init_bokeh()
        super(Streamer, self).__init__()

    def init_flask(self):
        @self.flask.route("/data", methods=["GET", "OPTIONS"])
        @crossdomain
        def stream():
            def event_stream():
                """No global state used"""
                while True:
                    t = datetime.now().timestamp()
                    v = np.sin(t * 5) + 0.2 * np.random.random() + 3
                    x = v * np.sin(t)
                    y = v * np.cos(t)
                    data = [[x, y]]
                    yield "data: " + json.dumps(data) + "\n\n"
                    time.sleep(0.1)

            resp = Response(event_stream(), mimetype="text/event-stream")
            resp.headers["Cache-Control"] = "no-cache"
            return resp

    def init_bokeh(self):
        self.bokeh_connection = BokehConnection(self.streamer_id, self.port)
        self.bokeh_connection.start()

    def run(self):
        setproctitle.setproctitle(f"streamer_{self.streamer_id}")
        self.flask.run(port=self.port)


class BokehConnection(multiprocessing.Process):
    def __init__(self, streamer_id, port):
        self.session = None
        self.session_id = None
        self.streamer_id = streamer_id
        self.port = port
        super(BokehConnection, self).__init__()

    def bokeh_callback(self, session):
        adapter = CustomJS(
            code="""
        const result = {x: [], y: []}
        const pts = cb_data.response
        for (let i=0; i<pts.length; i++) {
            result.x.push(pts[i][0])
            result.y.push(pts[i][1])
        }
        return result
    """
        )

        source = ServerSentDataSource(
            data_url="http://localhost:5050/data",
            max_size=100,
            mode="append",
            adapter=adapter,
        )

        p = figure(
            height=800,
            width=800,
            background_fill_color="lightgrey",
            title="Streaming via Server Sent Events",
            x_range=[-5, 5],
            y_range=[-5, 5],
        )
        p.circle("x", "y", source=source)
        
        return session

    def check_status(self):
        return self.session.connected

    def run(self):
        setproctitle.setproctitle(f"bokeh_session_{self.streamer_id}")
        with pull_session(url="http://localhost:5006/stream-debugger") as session:
            doc = session.document
            source = ColumnDataSource({"x": [], "y": [], "color": []})

            def update():
                new = {
                    "x": [random.random()],
                    "y": [random.random()],
                    "color": [random.choice(["red", "blue", "green"])],
                }
                source.stream(new)

            doc.add_periodic_callback(update, 100)

            fig = figure(
                title="Streaming Circle Plot!",
                sizing_mode="scale_width",
                x_range=[0, 1],
                y_range=[0, 1],
            )
            fig.circle(source=source, x="x", y="y", color="color", size=10)
            print(f"http://localhost:5006/stream-debugger?session_id={session.id}")
            doc.title = "Now with live updating!"
            doc.add_root(fig)
            session = push_session(
                doc, session_id=session.id, url="http://localhost:5006/stream-debugger"
            )
            session.show()
            while True:
                print(self.port)
                time.sleep(1)