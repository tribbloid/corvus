import ray
from datetime import datetime

# a simple MapReduce example
ray.init()

@ray.remote
class Reducer(object):
    def __init__(self, sum: int = 0):
        self.sum = sum

    def add(self, v: int):
        self.sum += v

    def result(self):
        return self.sum

@ray.remote
def plus(a: int, b: int):
    return a + b

@ray.remote
def morph(a: int):
    v =  a * a
    return v

reducer = Reducer.remote()

@ray.remote
def add(a: int, reducer: Reducer):
    morphed = morph.remote(a)
    reducer.add.remote(morphed)

rr = range(1, 10000)
result = []

start_time = datetime.now()
for i in rr:
    result.append(add.remote(i, reducer))
ready, notReady = ray.wait(result, len(rr))
print(ray.get(reducer.result.remote()))
print('time elapsed: ', datetime.now() - start_time)

start_time = datetime.now()
sum2 = 0
for i in rr:
    sum2 += i * i
print(sum2)
print('time elapsed: ', datetime.now() - start_time)
