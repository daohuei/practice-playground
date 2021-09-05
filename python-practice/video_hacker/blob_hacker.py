import requests
import subprocess
import threading
import time
from Crypto.Cipher import AES


def decrypt(data, key):
    """Decrypt using AES CBC"""
    decryptor = AES.new(key, AES.MODE_CBC)
    return decryptor.decrypt(data)


# for downloading ts file
def download_job(url, ts_id, key):
    def download_callback():
        output_video_ts = f"video/{ts_id}.ts"
        f = open(output_video_ts, "wb")
        # make request and download the file
        chunk_size = 1024
        res = requests.get(url, stream=True)
        for chunk in res.iter_content(chunk_size=chunk_size):
            print(type(chunk))
            dec_data = decrypt(
                chunk.encode("utf-8"),
                key,
            )
            f.write(dec_data)
        f.close()
        print(ts_id)

    return download_callback


thread_list = []
# read the m3u8 file
m3u8_file_path = input("input m3u8 file please: ")
m3u8_key = input("input key: ")
with open(m3u8_file_path) as f:
    index = 0
    # load every url
    for line in f.readlines():
        if "ts" in line and "EXT" not in line:
            url = line.strip()
            download_thread = threading.Thread(
                target=download_job(url, index, m3u8_key)
            )
            download_thread.start()
            thread_list.append(download_thread)
            index += 1
            time.sleep(0.1)

for t in thread_list:
    t.join()
print("Done")

# # 建立一個子執行緒

# # 執行該子執行緒
# t.start()

# # 主執行緒繼續執行自己的工作
# for i in range(3):
#     print("Main thread:", i)
#     time.sleep(1)

# # 等待 t 這個子執行緒結束
# t.join()

# print("Done.")
# url_source = input("video url")
# file_num = input("file number")
# url = url_source[0:-6]
# print(url_source)
# num = ""
# output_video_ts = f"./video/{file_num}.ts"
# f = open(output_video_ts, "wb")
# output_video_mp4 = f"./video/{file_num}.mp4"
# chunk_size = 1024
# for number in range(0, 613):
#     # 1 digit
#     if len(str(number)) == 1:
#         num = f"00{number}"
#     # 2 digit
#     elif len(str(number)) == 2:
#         num = f"0{number}"
#     # 3 digit
#     elif len(str(number)) == 3:
#         num = f"{number}"
#     url_list = f"{url}{num}.ts"
#     print(url_list)
#     res = requests.get(url_list, stream=True)
#     for chunk in res.iter_content(chunk_size=chunk_size):
#         f.write(chunk)
# # TODO: run ffmpeg here
# # subprocess.run("")
# f.close()
# print("Video Downloading Completed! Enjoy!")