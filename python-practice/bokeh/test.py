# from random import random

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.plotting import figure, curdoc
import numpy as np
import cv2


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


frames, meta = extract_video(
    "/home/ken/umbocv/video_clips/rain/20201228_080235_Demo.mp4"
)
print(len(frames), meta)
sample_frame = frames[20]
print(sample_frame.shape)

frame_rgba = np.dstack((sample_frame, np.zeros(sample_frame.shape[:-1])))
print(frame_rgba.shape)

# N = 500
# x = np.linspace(0, 10, N)
# y = np.linspace(0, 10, N)
# xx, yy = np.meshgrid(x, y)
# d = np.sin(xx) * np.cos(yy)

# print(d.shape)

# p = figure(tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")])
# p.x_range.range_padding = p.y_range.range_padding = 0

# i = 0
# print(frames[i].shape)
# frame_rgba = np.dstack((frames[i], np.zeros(frames[i].shape[:-1])))
# print(frame_rgba.shape)
# # must give a vector of image data for image parameter
# r = p.image_rgba(image=[frame_rgba])
# ds = r.data_source
# # create a callback that adds a number in a random location
# def callback():
#     # BEST PRACTICE --- update .data in one step with a new dict
#     global i, frames
#     # new_x = np.linspace(10, 20, N)
#     # new_y = np.linspace(10, 20, N)
#     # new_xx, new_yy = np.meshgrid(new_x, new_y)
#     # new_d = np.sin(new_xx) * np.cos(new_yy)
#     i += 1
#     frame_rgba = np.dstack((frames[i], np.zeros(frames[i].shape[:-1])))
#     print(frame_rgba.shape)
#     new_data = dict(image=[frame_rgba])
#     ds.data = new_data


# # add a button widget and configure with the call back
# button = Button(label="Press Me")
# button.on_click(callback)

# # put the button and plot in a layout and add to the document
# curdoc().add_root(column(p, button))


N = 20
img = np.empty((N, N), dtype=np.uint32)
# view = img.view(dtype=np.uint8).reshape((N, N, 4))
# for i in range(N):
#     for j in range(N):
#         view[i, j, 0] = int(i / N * 255)
#         view[i, j, 1] = 158
#         view[i, j, 2] = int(j / N * 255)
#         view[i, j, 3] = 255

p = figure(tooltips=[("x", "$x"), ("y", "$y"), ("value", "@image")])
p.x_range.range_padding = p.y_range.range_padding = 0
print(img.shape)
# must give a vector of images
p.image_rgba(image=[img], x=0, y=0, dw=10, dh=10)

# put the button and plot in a layout and add to the document
curdoc().add_root(column(p))