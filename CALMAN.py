import numpy as np
import matplotlib.pyplot as plt
from my_funct import calman_filter, sigma_observation, filter_data, theory

ITERATIONS = 4.0       # Количество прогонов фильтра
MODULATION = 10.0       # Во сколько раз погрешность модели меньше погрешности измерений
DATA_file = "obs.txt"   # Имя файла с измерениями
RESULT_file = "result.txt" # Имя выходного файла
POLYNOM_degree = 9      # Степень аппроксимирующего полинома

Observations_x = []
Observations_y = []
Filtered_obs_y = []
Model_y = []

Result_filter = []
Result_obs = []

with open(DATA_file) as file_observation:
    for line in file_observation:
        Observations_x.append(float(line.split()[0]))
        Result_obs.append(float(line.split()[1]))
        Observations_y.append(float(line.split()[1]))

plt.plot(Observations_x, Observations_y, '.', color='Green', markersize=2, label='Observation')
plt.title('RANGE TO LAGEOS')
plt.legend()
plt.show()

coeff_polynom = np.polyfit(Observations_x, Observations_y, POLYNOM_degree)
theoretical_function = np.poly1d(coeff_polynom)
Model_y = theory(Observations_x, theoretical_function)

Sigma_obs = sigma_observation(Observations_y, Model_y)
Sigma_mod = Sigma_obs / MODULATION

Filtered_obs_y = calman_filter(Observations_x, Observations_y, Model_y, Sigma_obs, Sigma_mod)

Sigma_mod = sigma_observation(Filtered_obs_y, Model_y)
filter_data(Observations_y, Filtered_obs_y, Observations_x, Model_y, Result_obs, Sigma_mod*3.0)

for i in range (0, len(Observations_y)):
    Observations_y[i] -= Filtered_obs_y[i]

coeff_polynom = np.polyfit(Observations_x, Observations_y, POLYNOM_degree)
theoretical_function = np.poly1d(coeff_polynom)
Model_y = theory(Observations_x, theoretical_function)

Sigma_obs = sigma_observation(Observations_y, Model_y)
filter_data(Observations_y, Model_y, Observations_x, Filtered_obs_y, Result_obs, Sigma_obs)

for i in range (0, len(Filtered_obs_y)):
    Result_filter.append(Filtered_obs_y[i])

while ITERATIONS > 1:
    coeff_polynom = np.polyfit(Observations_x, Observations_y, POLYNOM_degree)
    theoretical_function = np.poly1d(coeff_polynom)
    Model_y = theory(Observations_x, theoretical_function)

    Sigma_obs = sigma_observation(Observations_y, Model_y)
    Sigma_mod = Sigma_obs / MODULATION

    Filtered_obs_y = calman_filter(Observations_x, Observations_y, Model_y, Sigma_obs, Sigma_mod)

    for i in range(0, len(Observations_y)):
        Observations_y[i] -= Filtered_obs_y[i]
        Result_filter[i] += Filtered_obs_y[i]

    ITERATIONS -= 1

with open(RESULT_file, "w") as file_result:
    for i in range(0, len(Result_obs)):
        file_result.write(str(Result_obs[i]) + '\t' + str(Result_filter[i]) + '\n')

for i in range(0, len(Result_obs)):
    Result_obs[i] -= Result_filter[i]

distribution_y = np.histogram(Result_obs, 30)
distribution_x = []
for i in range(len(distribution_y[1])-1):
    distribution_x.append((distribution_y[1][i]+distribution_y[1][i+1])/2)

plt.plot(distribution_x, distribution_y[0], '.', color='Blue', markersize=4, label='Distribution')
plt.title('DISTRIBUTION')
plt.legend()
plt.show()
    # Plot_x = np.linspace(min(Observations_x), max(Observations_x), 100)
plt.plot(Observations_x, Result_obs, '.', color='Red', markersize=2, label='Observations')
    # plt.plot(Observations_x, Filtered_obs_y, '.', color='Blue', markersize=2, label='Calman filtration')
    # plt.plot(Observations_x, theoretical_function(Observations_x), '.', color='Greenyellow', markersize=2, label='Theoretical approximation')
plt.title('CALMAN FILTER')
plt.legend()
plt.show()
