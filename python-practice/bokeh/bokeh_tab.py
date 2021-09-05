from bokeh.models import (
    Button,
    FileInput,
    Div,
    Tabs,
    Panel,
    TextInput,
)
from bokeh.plotting import curdoc
from bokeh.layouts import column

local_title_text = "<h2>Upload video clip (mp4 only)</h2>"
local_invalid_text = "<h4>Please input valid mp4 file</h4>"
remote_title_text = "<h2>Debugging with online cameras</h2>"
remote_invalid_text = "<h4>Please input Jumbo ID and VD Instance Public IP</h4>"

local_input_title = Div(text=local_title_text)
file_input = FileInput(accept=".mp4")


def local_event():
    print(file_input.mime_type)
    print(file_input.filename)
    if file_input.mime_type != "video/mp4":
        local_input_title.update(text=f"{local_title_text}{local_invalid_text}")
        return
    local_input_title.update(text=local_title_text)


local_start_button = Button(label="Start StreamDebugger", button_type="success")
local_start_button.on_click(local_event)


remote_input_title = Div(text=remote_title_text)
jumbo_id_input = TextInput(value="", title="Jumbo ID:")
public_ip_input = TextInput(value="", title="Public IP:")


def remote_event():
    # empty case
    if not jumbo_id_input.value or not public_ip_input.value:
        remote_input_title.update(text=f"{remote_title_text}{remote_invalid_text}")
        return
    remote_input_title.update(text=remote_title_text)


remote_start_button = Button(label="Start StreamDebugger", button_type="success")
remote_start_button.on_click(remote_event)

input_tab = Tabs(
    tabs=[
        Panel(
            child=column(local_input_title, file_input, local_start_button),
            title="Local Mode",
        ),
        Panel(
            child=column(
                remote_input_title, jumbo_id_input, public_ip_input, remote_start_button
            ),
            title="Remote Mode",
        ),
    ],
)

curdoc().add_root(input_tab)
