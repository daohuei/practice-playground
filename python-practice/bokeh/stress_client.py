import random
import time

import cv2
import numpy as np
from bokeh.client import pull_session, push_session
from bokeh.embed import server_session
from bokeh.plotting import figure, ColumnDataSource
from tornado.ioloop import PeriodicCallback


def convert_rgb_to_bokehrbga(img):
    """
    convert RGB image to two-dimensional array of RGBA values (encoded as 32-bit integers)
    Bokeh require rbga
    :param img: (N,M, 3) array (dtype = uint8)
    :return: (K, R, dtype=uint32) array
    """
    if img.dtype != np.uint8:
        raise NotImplementedError

    if img.ndim != 3:
        raise NotImplementedError

    bokeh_img = np.dstack([img, 255 * np.ones(img.shape[:2], np.uint8)])
    final_rgba_image = np.squeeze(bokeh_img.view(dtype=np.uint32))
    final_rgba_image = np.flipud(final_rgba_image)
    return final_rgba_image


def init_raw_image_window():
    width = 320
    height = 180
    raw_image_win = figure(
        name="stress_image",
        title="Streaming Window RGB #1",
        plot_width=600,
        plot_height=(int(600 / width * height)),
    )
    raw_image_win.axis.visible = False
    raw_image_win.x_range.range_padding = 0
    raw_image_win.y_range.range_padding = 0
    raw_image_data = raw_image_win.image_rgba(image=[], x=0, y=0, dw=width, dh=height)
    return raw_image_win, raw_image_data


session = None
stress_image = None
stress_data = None
count = 0

black_frame = np.zeros((180, 320, 3), np.uint8)
white_frame = 255 * np.ones((180, 320, 3), np.uint8)
black_frame_rgb = cv2.cvtColor(black_frame, cv2.COLOR_BGR2RGB)
white_frame_rgb = cv2.cvtColor(white_frame, cv2.COLOR_BGR2RGB)
disp_black_frame = convert_rgb_to_bokehrbga(black_frame_rgb)
disp_white_frame = convert_rgb_to_bokehrbga(white_frame_rgb)


def session_health_check():
    print("health check")
    global stress_image, stress_data, session, count
    doc = session.document
    if stress_image is None:
        stress_image, stress_data = init_raw_image_window()
        doc.clear()
        doc.add_root(stress_image)
        doc.title = "Now with live updating!"
    if count % 2 == 0:
        stress_data.data_source.data = dict(image=[disp_black_frame])
    else:
        stress_data.data_source.data = dict(image=[disp_white_frame])
    count += 1


# scheduler for health check
scheduler = PeriodicCallback(session_health_check, 1000.0)
scheduler.start()
session = pull_session(
    url="http://localhost:5006/stress-test",
    session_id="test_session",
    io_loop=scheduler.io_loop,
)
scheduler.io_loop.start()
