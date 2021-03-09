"""
For testing if md5sum checking is concurrent
when other users are modifying the checking text file
"""
import time
import hashlib

original_md5 = ""


file_name = "text.txt"
while True:
    # Open,close, read file and calculate MD5 on its contents
    with open(file_name, "rb") as file_to_check:
        # read contents of the file
        data = file_to_check.read()
        # pipe contents of the file through
        md5_returned = hashlib.md5(data).hexdigest()

    # Finally compare original MD5 with freshly calculated
    if original_md5 == md5_returned:
        print("MD5 verified.")
    else:
        print("MD5 verification failed!.")
    time.sleep(0.1)
