def mult_polynomials(f: list, g: list) -> list:
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



