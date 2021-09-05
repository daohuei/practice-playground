from tornado.ioloop import IOLoop
from bokeh.layouts import column
from bokeh.models import Div
from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.server.server import Server


def modify_doc(doc):
    h_text = Div(text="<h1>This is the stress test for Bokeh</h1>")
    doc.title = "Stress Test Server"
    doc.add_root(column(h_text))


def main():
    """Launch the server and connect to it."""
    print("Preparing a bokeh application.")
    io_loop = IOLoop.current()
    bokeh_app = Application(FunctionHandler(modify_doc))

    server = Server(
        {"/": bokeh_app},
        io_loop=io_loop,
        prefix="stress-test",
        # keep_alive_milliseconds=60 * 60 * 1000,
    )
    server.start()
    print("Opening Bokeh application on http://localhost:5006/stress-test")

    io_loop.start()


main()