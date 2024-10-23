import typing as tp


def mult_polynomials(f: tp.List[int], g: tp.List[int]) -> tp.List[int]:
    """
    Умножение полинома f на полином g (если степени полиномов разные, они дополняются нулями)
    Полиномы представляются в виде:
    f = [a0 + a1 * x + a2 * x^2 + ...], g = [b0 + b1 * x + b2 * x^2 + ...]
    :param f: [a0, a1, a2, ...]
    :param g: [b0, b1, b2, ...]
    :return: полином степени deg(f) + deg(g) - 1 в аналогичном виде
    """

    if not f or not g:
        raise ValueError("Empty polynomials")

    if len(f) < len(g):
        f.extend([0] * (len(g) - len(f)))
    elif len(f) > len(g):
        g.extend([0] * (len(f) - len(g)))

    if len(f) == 1:
        return [f[0] * g[0]]

    mid = len(f) // 2
    f_left, f_right = f[:mid], f[mid:]
    g_left, g_right = g[:mid], g[mid:]

    f_left_g_left = mult_polynomials(f_left, g_left)
    f_right_g_right = mult_polynomials(f_right, g_right)

    for i in range(mid):
        f_right[i] += f_left[i]
        g_right[i] += g_left[i]

    sum_f_sum_g = mult_polynomials(f_right, g_right)

    result = [0] * (len(f) * 2 - 1)

    for i in range(len(f_left_g_left)):
        result[i] += f_left_g_left[i]
        result[mid + i] -= f_left_g_left[i]

    for i in range(len(f_right_g_right)):
        result[mid * 2 + i] += f_right_g_right[i]
        result[mid + i] -= f_right_g_right[i]

    for i in range(len(sum_f_sum_g)):
        result[mid + i] += sum_f_sum_g[i]

    return result


#_______________________________________________
def mult_polynomials_naive(f: tp.List[int], g: tp.List[int]) -> tp.List[int]:
    """
    Умножение полинома f на полином g наивным способом (если степени полиномов разные, они дополняются нулями)
    Полиномы представляются в виде:
    f = [a0 + a1 * x + a2 * x^2 + ...], g = [b0 + b1 * x + b2 * x^2 + ...]
    :param f: [a0, a1, a2, ...]
    :param g: [b0, b1, b2, ...]
    :return: полином степени deg(f) + deg(g) - 1 в аналогичном виде
    """

    if not f or not g:
        raise ValueError("Empty polynomials")

    result = [0] * (max(len(f), len(g)) * 2 - 1)

    for k in range(len(result)):
        for i in range(k + 1):
            if i < len(f) and k - i < len(g):
                result[k] += f[i] * g[k - i]

    return result



