from math import sqrt, fabs

data_obs = __file__[:-11]+'data\\obs.txt'

def sigma_observation(y_obs, model):
    """Вычисление дисперсии

    :param y_obs:   список измерений
    :param model:   список модели измерений
    :return:        среднеквадратическое отклонение
    """
    x = 0.0
    for i in range(0, len(y_obs)):
        x += (y_obs[i] - model[i]) * (y_obs[i] - model[i])
    x /= (len(y_obs) - 1.0)
    x = sqrt(x)
    return x


def k_cal(s_obs, s_mod):
    """Вычисление коэффициента фильтра Калмана

    :param s_obs:   среднеквадратическое отклонение измерений
    :param s_mod:   среднеквадратическое отклонение модели
    :return:        Коэффициент Калмана
    """
    sigma_obs2 = s_obs * s_obs
    sigma_mod2 = s_mod * s_mod
    e = sigma_obs2
    k = 1.0
    while True:
        mem_k = k
        e = sigma_obs2 * (e + sigma_mod2) / (e + sigma_obs2 + sigma_mod2)
        k = e / sigma_obs2
        if sqrt((k - mem_k) * (k - mem_k)) < 0.0000001:
            break
    return k


def calman_filter(x_obs, y_obs, model, sigma_obs, sigma_mod):
    """Фильтр Калмана

    :param x_obs:       список x - координаты измерений
    :param y_obs:       список y - координаты измерений
    :param model:       список модели измерений
    :param sigma_obs:   среднеквадратическое отклонение измерений
    :param sigma_mod:   среднеквадратическое отклонение модели
    :return:            список с отфильтрованными измерениями
    """
    filter_obs = []

    k = k_cal(sigma_obs, sigma_mod)

    x0 = model[0]
    filter_obs.append(x0)

    for i in range(1, len(x_obs)):
        x0 = k * y_obs[i] + (1.0 - k) * (x0 + model[i] - model[i-1])
        filter_obs.append(x0)

    return filter_obs


def filter_data(sub1, sub2, m1, m2, m3, sigma):
    """Фильтрация ложных измерений

    Вычисляется разница между измерениями и моделью,
    если она больше среднеквадратическое отклонения, то данное измерение
    удаляется из измерений и модели, а также из всех списков для фильтрации

    :param sub1:    список измерений
    :param sub2:    список модели
    :param m1:      список для фильтрации
    :param m2:      список для фильтрации
    :param m3:      список для фильтрации
    :param sigma:   среднеквадратическое отклонение измерений
    :return:
    """
    length = len(sub1)
    i = 0
    while i < length:
        if fabs(sub1[i] - sub2[i]) > sigma:
            del sub1[i]
            del sub2[i]
            del m1[i]
            del m2[i]
            del m3[i]
            length -= 1
        else:
            i += 1
