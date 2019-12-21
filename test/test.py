import unittest
import random
import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi, fabs
from my_funct import sigma_observation, calman_filter, theory


class MyTestCase(unittest.TestCase):
    def test_Calman_sin(self):
        observations_x = []
        observations_y = []
        epsilon = 0.8
        polynom_degree = 3
        mod_x = []

        random.seed(888)
        x = 0.0
        h = 0.001
        while True:
            y = sin(x) + random.normalvariate(0, 2.0)
            mod_x.append(sin(x))
            observations_x.append(x)
            observations_y.append(y)
            x += h
            if x > (pi * 2.0):
                break

        coeff_polynom = np.polyfit(observations_x, observations_y, polynom_degree)
        theoretical_function = np.poly1d(coeff_polynom)
        model_y = theory(observations_x, theoretical_function)

        sigma_obs = sigma_observation(observations_y, model_y)
        sigma_mod = sigma_observation(mod_x, model_y)

        filtered_obs_y = calman_filter(observations_x, observations_y, model_y, sigma_obs, sigma_mod)

        result = True
        max_residual = 0.0
        for i in range(0, len(observations_x)):
            substruct = filtered_obs_y[i] - sin(observations_x[i])
            if max_residual < substruct:
                max_residual = substruct
                if max_residual > epsilon:
                    result = False

        if not result:
            plt.plot(observations_x, observations_y, '.', color='Red', markersize=2, label='Observations')
            plt.plot(observations_x, filtered_obs_y, '.', color='Blue', markersize=2, label='Calman filtration')
            plt.plot(observations_x, mod_x, '.', color='Yellow', markersize=1, label='Model function')
            plt.title(' Filtration of sin(x) ')
            plt.legend()
            plt.show()

        self.assertTrue(result, " Фильтр Калмана работает неверно ")

    def test_sigma(self):
        test_x = []
        test_y = []
        sigma = 2.0
        epsilon = 0.05

        random.seed(888)

        count = 0
        while True:
            y = random.normalvariate(0, sigma)
            test_y.append(y)
            test_x.append(0.0)

            count += 1
            if count > 7000:
                break

        def zero(x):
            return 0.0

        test_model = theory(test_x, zero)

        new_sigma = sigma_observation(test_y, test_model)
        result = True
        if fabs(new_sigma - sigma) > epsilon:
            result = False

        self.assertTrue(result, " Ошибка в функции расчёта дисперсии ")


if __name__ == '__main__':
    unittest.main()
