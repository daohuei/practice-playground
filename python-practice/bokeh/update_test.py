from functools import partial
from random import random
from threading import Thread
import time

from bokeh.models import ColumnDataSource
from bokeh.plotting import curdoc, figure

import cv2
import numpy as np

from tornado import gen


def extract_video(video: str):
    cap = cv2.VideoCapture(video)
    video_meta = {}
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    video_meta["width"] = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_meta["height"] = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_meta["fps"] = int(cap.get(cv2.CAP_PROP_FPS))

    video_frames = np.empty(
        (frame_count, video_meta["height"], video_meta["width"], 3), np.dtype("uint8")
    )
    i = 0
    ret = True
    while i < frame_count and ret:
        ret, video_frames[i] = cap.read()
        i += 1
    cap.release()
    return video_frames, video_meta


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


frames, meta = extract_video(
    "video_path"
)

width = meta["width"]
height = meta["height"]
p = figure(
    tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")],
    plot_width=600,
    plot_height=(int(600 / width * height)),
)
p.axis.visible = False
p.x_range.range_padding = p.y_range.range_padding = 0

# must give a vector of images
image_data = p.image_rgba(image=[], x=0, y=0, dw=width, dh=height)

# only modify from a Bokeh session callback
source = image_data.data_source

# This is important! Save curdoc() to make sure all threads
# see the same document.
doc = curdoc()


@gen.coroutine
def update(frame):
    new_data = dict(image=[frame])
    source.data = new_data


def blocking_task():
    i = 0
    while True:
        # do some blocking computation
        time.sleep(0.1)
        if i == len(frames):
            i = 0
        display_frame_rgb = cv2.cvtColor(frames[i], cv2.COLOR_BGR2RGB)
        disp_frame = convert_rgb_to_bokehrbga(display_frame_rgb)
        i += 1
        # but update the document from a callback
        doc.add_next_tick_callback(partial(update, frame=disp_frame))


doc.add_root(p)

thread = Thread(target=blocking_task)
thread.start()