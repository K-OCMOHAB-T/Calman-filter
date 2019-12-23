import unittest
import numpy as np
from my_modul import sigma_observation, calman_filter


class MyTestCase(unittest.TestCase):
    def test_calman_filter(self):
        observations_x = []
        observations_y = []
        model_y = []
        mod_x = []
        filtered_obs_y = []

        with open("test_file") as file_observation:
            for line in file_observation:
                observations_x.append(float(line.split()[0]))
                observations_y.append(float(line.split()[1]))
                model_y.append(float(line.split()[2]))
                mod_x.append(float(line.split()[3]))
                filtered_obs_y.append(float(line.split()[4]))

        sigma_obs = sigma_observation(observations_y, model_y)
        sigma_mod = sigma_observation(mod_x, model_y)

        new_filtered_obs_y = calman_filter(observations_x, observations_y, model_y, sigma_obs, sigma_mod)
        np.testing.assert_array_almost_equal(new_filtered_obs_y, filtered_obs_y, 20, "Фильтр Калмана работает неверно")

    def test_sigma_observation(self):
        test_x = [1, 2, 3, 2, 1, 2, 3]
        test_y = [3, 2, 1, 2, 3, 2, 1]
        sigma = sigma_observation(test_x, test_y)
        np.testing.assert_allclose(sigma, 1.632993161855452, rtol=1e-14, atol=0)


if __name__ == '__main__':
    unittest.main()
