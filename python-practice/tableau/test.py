import numpy as np
from tabpy.tabpy_tools.client import Client


def multiply(x, y):
    return np.sum(x, y).tolist()


client = Client("http://localhost:9004/")
client.deploy("multiply", multiply, "Multiples two numbers x and y")
