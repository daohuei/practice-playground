# from base64 import b64decode
# from tornado.ioloop import IOLoop
# import os
# import subprocess


# from bokeh.layouts import column
# from bokeh.models import ColumnDataSource, Div, FileInput
# from bokeh.application.handlers import FunctionHandler
# from bokeh.application import Application
# from bokeh.server.server import Server


# def modify_doc(doc):
#     h_input = Div(text="""<h2>Upload your mp4 file</h2> """, max_height=40)

#     file_input = FileInput()
#     source = ColumnDataSource(dict())

#     def value_changed(attr, old, new):
#         data = b64decode(new)
#         print(type(data))
#         with open("fake_video.mp4", "wb") as binary_file:
#             # Write bytes to file
#             # binary_file.write(data)
#             print("trigger os popen here")

#             cmd = "echo 'run command for stream debugger'"
#             output = subprocess.Popen(
#                 cmd,
#                 shell=True,
#                 stdout=subprocess.PIPE,
#                 stderr=subprocess.PIPE,
#                 universal_newlines=True,
#             )

#             exit_code = output.wait()
#             print(exit_code)
#             result = ""
#             if exit_code != 0:
#                 print("run failed")
#                 for line in output.stderr:
#                     result = result + line
#             else:
#                 print("run successfully")
#                 for line in output.stdout:
#                     print(f"line: {line}")
#                     result = result + line
#             print(f"result: {result}")

#     file_input.on_change("value", value_changed)
#     doc.add_root(column(h_input, file_input))


# def main():
#     """Launch the server and connect to it."""
#     print("Preparing a bokeh application.")
#     io_loop = IOLoop.current()
#     bokeh_app = Application(FunctionHandler(modify_doc))

#     server = Server({"/": bokeh_app}, io_loop=io_loop, prefix="mp4_upload")
#     server.start()
#     print("Opening Bokeh application on http://localhost:5006/")

#     io_loop.add_callback(server.show, "/")
#     io_loop.start()


# main()


import json
from datetime import datetime
from time import sleep

import numpy as np
from flask import Flask, Response, make_response, request

from bokeh.models import CustomJS, ServerSentDataSource
from bokeh.plotting import figure, output_file, show

# Bokeh related code

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
    data_url="http://localhost:5050/data", max_size=100, mode="append", adapter=adapter
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

# Flask related code

app = Flask(__name__)


def crossdomain(f):
    def wrapped_function(*args, **kwargs):
        resp = make_response(f(*args, **kwargs))
        h = resp.headers
        h["Access-Control-Allow-Origin"] = "*"
        h["Access-Control-Allow-Methods"] = "GET, OPTIONS, POST"
        h["Access-Control-Max-Age"] = str(21600)
        requested_headers = request.headers.get("Access-Control-Request-Headers")
        if requested_headers:
            h["Access-Control-Allow-Headers"] = requested_headers
        return resp

    return wrapped_function


@app.route("/data", methods=["GET", "OPTIONS"])
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
            sleep(0.1)

    resp = Response(event_stream(), mimetype="text/event-stream")
    resp.headers["Cache-Control"] = "no-cache"
    return resp


# show and run

output_file("plot.html", title="Bokeh Plot", mode="inline")
show(p)
app.run(port=5050)
