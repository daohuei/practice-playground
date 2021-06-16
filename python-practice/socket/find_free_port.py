import socket


def find_free_port(start=1024, end=65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while start <= end:
        try:
            sock.bind(("", start))
            sock.close()
            return start
        except OSError:
            start += 1
    raise IOError("no free ports")


print(find_free_port(5555, 5557))