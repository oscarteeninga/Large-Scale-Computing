import random
import time

def montecarlo(event, context):
    start = time.time()
    data = str(event['data']).split(';')
    if len(data) != 4:
        return "Invalid arguments, should define: ';<from>;<to>;"
    a = float(data[1])
    b = float(data[2])
    n = 10000000

    integral = 0.0

    def f(x):
        return 2 * x * x * x - 3 * x * x + 8 * x - 12

    for i in range(n):
        integral += f(random.uniform(a, b))

    return str(time.time() - start)

    # return str((b - a) / float(n) * integral)
