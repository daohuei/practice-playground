import os

output = os.popen(
    'docker exec -it streamrouter bash -c "python scripts/get_free_port.py 5555 5557"'
)
print(output.readline())
