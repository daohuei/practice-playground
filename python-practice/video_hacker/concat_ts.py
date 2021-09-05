import os

dir_name = "video"

dirs = os.listdir(dir_name)
output_video_ts = "video/all.ts"
output = open(output_video_ts, "wb")
for ts_path in dirs:
    video_part = open(f"video/{ts_path}", "rb")
    output.write(video_part.read())
    video_part.close()
output.close()