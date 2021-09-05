import zipfile
from base64 import b64decode
from io import BytesIO
from tornado.ioloop import IOLoop

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
            binary_file.write(data)

    file_input.on_change("value", value_changed)
    doc.add_root(column(h_input, file_input))


def main():
    """Launch the server and connect to it."""
    print("Preparing a bokeh application.")
    io_loop = IOLoop.current()
    bokeh_app = Application(FunctionHandler(modify_doc))

    server = Server({"/": bokeh_app}, io_loop=io_loop)
    server.start()
    print("Opening Bokeh application on http://localhost:5006/")

    io_loop.add_callback(server.show, "/")
    io_loop.start()


main()