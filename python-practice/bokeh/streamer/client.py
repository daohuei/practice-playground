# import random
# from bokeh.server.server import Server
# from bokeh.application import Application
# from bokeh.application.handlers.function import FunctionHandler
# from bokeh.plotting import figure, ColumnDataSource


# def make_document(doc):
#     source = ColumnDataSource({"x": [], "y": [], "color": []})

#     def update():
#         new = {
#             "x": [random.random()],
#             "y": [random.random()],
#             "color": [random.choice(["red", "blue", "green"])],
#         }
#         source.stream(new)

#     doc.add_periodic_callback(update, 100)

#     fig = figure(
#         title="Streaming Circle Plot!",
#         sizing_mode="scale_width",
#         x_range=[0, 1],
#         y_range=[0, 1],
#     )
#     fig.circle(source=source, x="x", y="y", color="color", size=10)

#     doc.title = "Now with live updating!"
#     doc.add_root(fig)


# apps = {"/": Application(FunctionHandler(make_document))}

# server = Server(apps, port=5006)
# server.start()

from base64 import b64decode
from tornado.ioloop import IOLoop
import asyncio
import os
import subprocess


from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Div, FileInput
from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.server.server import Server


def modify_doc(doc):
    h_input = Div(text="""<h2>Upload your mp4 file</h2> """, max_height=40)

    file_input = FileInput()
    source = ColumnDataSource(dict())

    def value_changed(attr, old, new):
        data = b64decode(new)
        print(type(data))
        with open("fake_video.mp4", "wb") as binary_file:
            # Write bytes to file
            # binary_file.write(data)
            print("trigger os popen here")

            cmd = "echo 'run command for stream debugger'"
            output = subprocess.Popen(
                cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            )

            exit_code = output.wait()
            print(exit_code)
            result = ""
            if exit_code != 0:
                print("run failed")
                for line in output.stderr:
                    result = result + line
            else:
                print("run successfully")
                for line in output.stdout:
                    print(f"line: {line}")
                    result = result + line
            print(f"result: {result}")

    file_input.on_change("value", value_changed)
    doc.add_root(column(h_input, file_input))

def init_static_event_loop():
    static_loop = asyncio.get_event_loop()

def main():
    """Launch the server and connect to it."""
    print("Preparing a bokeh application.")
    io_loop = IOLoop.current()
    bokeh_app = Application(FunctionHandler(modify_doc))

    server = Server({"/": bokeh_app}, io_loop=io_loop, prefix="stream-debugger")
    server.start()
    print("Opening Bokeh application on http://localhost:5006/")

    io_loop.add_callback(server.show, "/")
    io_loop.start()


main()