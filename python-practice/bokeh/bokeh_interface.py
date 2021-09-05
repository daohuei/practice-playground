import random
import json

from tornado.ioloop import IOLoop
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler
from bokeh.plotting import figure, ColumnDataSource
from bokeh.layouts import column, row, gridplot
from bokeh.models import Select, TextInput, CheckboxGroup, Slider, Div


def init_image_win(name, width=320, height=180):
    image_win = figure(
        title=name, aspect_ratio=width / height, sizing_mode="scale_width"
    )
    image_win.axis.visible = False
    image_win.x_range.range_padding = 0
    image_win.y_range.range_padding = 0
    image_win.toolbar_location = None
    image_data = image_win.image_rgba(image=[], x=0, y=0, dw=width, dh=height)
    return image_win


def make_document(doc):

    frame_ratio = 320 / 180

    # Frames from Pipelines
    raw_image_win = init_image_win("Raw Image")
    motion_mask_win = init_image_win("Motion Mask")
    cv_mask_win = init_image_win("CV Mask")
    new_alert_win = init_image_win("New Alert Snapshot")

    pipeline_win_height = 225
    pipeline_grid_plot = gridplot(
        [
            raw_image_win,
            motion_mask_win,
            cv_mask_win,
            new_alert_win,
        ],
        ncols=1,
        plot_width=int(pipeline_win_height * frame_ratio),
        plot_height=pipeline_win_height,
        toolbar_location=None,
    )
    pipeline_col = column(pipeline_grid_plot)

    # Frames from Motion
    h264_win = init_image_win("H.264")
    fd_win = init_image_win("FD")
    mog2_win = init_image_win("MOG2")
    amf_win = init_image_win("AMF")
    display_detection_win = init_image_win("Motion Detection")

    motion_win_height = 225
    motion_grid_plot = gridplot(
        children=[
            [h264_win, fd_win],
            [mog2_win, amf_win],
        ],
        plot_width=int(motion_win_height * frame_ratio),
        plot_height=motion_win_height,
        toolbar_location=None,
    )

    motion_col = column(display_detection_win, motion_grid_plot)

    # Motion Control Panel
    motion_checkbox_group = CheckboxGroup(
        labels=["H.264", "FD", "MOG2", "AMF", "Show Motion Detections"]
    )
    motion_select = Select(
        title="Motion Filter Type", value="h264", options=["h264", "fd", "mog2", "amf"]
    )
    motion_interval_slider = Slider(
        start=0.05, end=30, value=1.5, step=0.01, title="Motion Interval"
    )
    motion_threshold_slider = Slider(
        start=0, end=200, value=50, step=1, title="Motion Threshold(H.264 only)"
    )
    motion_bbx_area_threshold_slider = Slider(
        start=25,
        end=200,
        value=200,
        step=1,
        title="Motion BBX Area Threshold(OpenCV only)",
    )

    # AMF only configs
    variance_threshold_slider = Slider(
        start=10, end=500, value=500, step=1, title="Variance Threshold(AMF only)"
    )
    amf_checkbox_group = CheckboxGroup(
        labels=["History Variance(AMF only)", "Frame Reduction(AMF only)"], active=[1]
    )

    # Config Control Panel
    show_configs_checkbox_group = CheckboxGroup(
        labels=["Show CV Config", "Show Event Config"]
    )
    override_cv_config_input = TextInput(
        value=json.dumps({}), title="Override CV Config"
    )
    override_event_config_input = TextInput(
        value=json.dumps({}), title="Override Event Config"
    )
    env_select = Select(
        title="Environment", value="staging", options=["staging", "rc", "production"]
    )
    jumbo_id_input = TextInput(value="", title="Jumbo ID")
    api_token_input = TextInput(value="", title="API Token")

    panel_col = column(
        Div(text="<h4> Config Control Panel </h4>"),
        show_configs_checkbox_group,
        override_cv_config_input,
        override_event_config_input,
        env_select,
        jumbo_id_input,
        api_token_input,
        Div(text="<h4> Motion Control Panel </h4>"),
        motion_checkbox_group,
        motion_select,
        motion_interval_slider,
        motion_threshold_slider,
        motion_bbx_area_threshold_slider,
        variance_threshold_slider,
        amf_checkbox_group,
        sizing_mode="scale_width",
    )

    main_row = row(
        pipeline_col,
        panel_col,
        motion_col,
    )

    doc.title = "StreamDebugger"
    doc.add_root(main_row)


io_loop = IOLoop.current()
apps = {"/": Application(FunctionHandler(make_document))}

server = Server(apps, port=5006, io_loop=io_loop)
server.start()
io_loop.start()
