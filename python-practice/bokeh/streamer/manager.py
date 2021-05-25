import typer
import time
import setproctitle
import multiprocessing
import signal
from base64 import b64decode
from tornado.ioloop import BaseAsyncIOLoop, IOLoop

from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Div, FileInput
from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.server.server import Server

import streamer

app = typer.Typer()


class GracefulDeath:
    """Catch signals to allow graceful shutdown."""

    def __init__(self):
        self.received_term_signal = False
        self.catch_signals = [
            signal.SIGINT,
            signal.SIGQUIT,
            signal.SIGTERM,
        ]
        for sig_num in self.catch_signals:
            signal.signal(sig_num, self.handler)

    def handler(self, sig_num, frame):
        self.last_signal = sig_num
        if sig_num in self.catch_signals:
            self.received_term_signal = True


class Mananger:
    def __init__(self):
        self.pool = {}
        super(Mananger, self).__init__()

    def run(self):
        setproctitle.setproctitle("stream_manager")
        io_loop = IOLoop.current()

        def modify_doc(doc):
            h_input = Div(text="""<h2>Upload your mp4 file</h2> """, max_height=40)

            file_input = FileInput()
            source = ColumnDataSource(dict())

            def value_changed(attr, old, new):
                # print(type(data))
                # with open("fake_video.mp4", "wb") as binary_file:
                # Write bytes to file
                # binary_file.write(data)
                print("init new process")
                # data = b64decode(new)
                print(file_input.filename)
                self.spawn_new_worker(file_input.filename)
                print(self.pool)

            file_input.on_change("filename", value_changed)
            doc.add_root(column(h_input, file_input))

        bokeh_app = Application(FunctionHandler(modify_doc))
        server = Server({"/": bokeh_app}, io_loop=io_loop, prefix="stream-debugger")
        server.start()
        server.show("/")
        io_loop.start()

    #     signal_handler = GracefulDeath()
    #     while True:
    #         if signal_handler.received_term_signal:
    #             print(
    #                 "Gracefully exiting due to receipt of signal {}".format(
    #                     signal_handler.last_signal
    #                 )
    #             )
    #             self.shutdown()
    #             return
    #         self.check_status()
    #         time.sleep(1.0)

    # def check_status(self):
    #     for _, p in self.pool.items():
    #         if p.bokeh_connection is not None:
    #             if p.bokeh_connection.session is not None:
    #                 print(p.bokeh_connection.check_status())

    def spawn_new_worker(self, new_id):
        streamer_id = new_id
        worker = streamer.Streamer(streamer_id)
        worker.start()
        self.pool[streamer_id] = worker

    def shutdown(self):
        print(self.pool)
        for _, p in self.pool.items():
            p.terminate()
            p.join()


@app.command()
def init():
    print("init manager")
    manager = Mananger()
    manager.run()


if __name__ == "__main__":
    app()
