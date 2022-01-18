import unittest
import time
import random


class SequentialTest(unittest.TestCase):

    def test_sequential_montecarlo(self):
        start = time.time()
        a = 0.0
        b = 2.0
        n = 10000000

        integral = 0.0

        def f(x):
            return 2 * x * x * x - 3 * x * x + 8 * x - 12

        for i in range(n):
            integral += f(random.uniform(a, b))

        print(str((b - a) / float(n) * integral))
        print("TIME: ", time.time() - start)


if __name__ == '__main__':
    unittest.main()
