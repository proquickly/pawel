import gc

numbers = list(range(10_000_000))
del numbers
gc.collect()


c = 0
for i in range(10_000):
    c = c + 1
