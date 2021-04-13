import psutil

# gives a single float value
cpu = psutil.cpu_percent()
print(cpu)
# gives an object with many fields
mem = psutil.virtual_memory()
print(mem)
# you can convert that object to a dictionary
mem_dict = dict(psutil.virtual_memory()._asdict())
print(mem_dict)
# you can have the percentage of used RAM
mem_percent = psutil.virtual_memory().percent
print(mem_percent)
# you can calculate percentage of available memory
mem_calc_percent = (
    psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
)
print(mem_calc_percent)