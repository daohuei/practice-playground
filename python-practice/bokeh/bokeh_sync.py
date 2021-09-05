from bokeh.client import push_session
from bokeh.models.widgets import CheckboxGroup
from bokeh.document import Document
from bokeh.plotting import curdoc, figure, show
import asyncio
from tornado.platform.asyncio import BaseAsyncIOLoop, AsyncIOMainLoop
from tornado.ioloop import IOLoop

doc = Document()


def my_radio_handler(new):
    doc.title = str(new)
    print("Radio button " + str(new) + " option selected.")


radio_button_group = CheckboxGroup(
    labels=["Option 1", "Option 2", "Option 3"], active=[]
)
radio_button_group.on_click(my_radio_handler)

doc.add_root(radio_button_group)

loop = asyncio.get_event_loop()
io_loop = BaseAsyncIOLoop(asyncio_loop=loop)
# io_loop = IOLoop._ioloop_for_asyncio[loop]
# io_loop = IOLoop.current()
# Open a session to keep our local document in sync with server
session = push_session(doc, session_id="123", io_loop=io_loop)

# Run forever (this is crucial to retrive callback's data)
session._connection._loop.spawn_callback(session._connection._next)
loop.run_forever()
print("hw")