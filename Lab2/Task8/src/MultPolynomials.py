import typing as tp
from utils import read, write


def mult_polynomials(f: tp.List[int], g: tp.List[int]) -> tp.List[int]:
    if not f or not g:
        raise ValueError("Empty polynomials")

    if len(f) < len(g):
        f = ([0] * (len(g) - len(f))) + f
    elif len(f) > len(g):
        g = ([0] * (len(f) - len(g))) + g


    def mult_polynomials_recursion(f: tp.List[int], g: tp.List[int],
                                   f_start: int, f_end: int,
                                   g_start: int, g_end: int) -> tp.List[int]:
        len_f = f_end - f_start
        len_g = g_end - g_start
        assert len_f == len_g

        if len_f == 1:
            return [f[f_start] * g[g_start]]

        mid = len_f // 2
        f_mid = f_start + mid
        g_mid = g_start + mid

        f_left_g_left = mult_polynomials_recursion(f, g, f_start, f_mid, g_start, g_mid)
        f_right_g_right = mult_polynomials_recursion(f, g, f_mid, f_end, g_mid, g_end)

        f_left_plus_f_right = f[f_mid:f_end]
        g_left_plus_g_right = g[g_mid:g_end]
        for i in range(f_start, f_mid):
            f_left_plus_f_right[i - f_start] += f[i]
        for i in range(g_start, g_mid):
            g_left_plus_g_right[i - g_start] += g[i]

        sum_f_sum_g = mult_polynomials_recursion(f_left_plus_f_right, g_left_plus_g_right,
                                                 0, f_end - f_mid,
                                                 0, g_end - g_mid)

        result = [0] * (len_f * 2 - 1)

        for i in range(len(f_left_g_left)):
            result[i] += f_left_g_left[i]
            result[mid + i] -= f_left_g_left[i]

        for i in range(len(f_right_g_right)):
            result[mid * 2 + i] += f_right_g_right[i]
            result[mid + i] -= f_right_g_right[i]

        for i in range(len(sum_f_sum_g)):
            result[mid + i] += sum_f_sum_g[i]

        return result

    return mult_polynomials_recursion(f, g, 0, len(f), 0, len(g))


#_______________________________________________
def mult_polynomials_naive(f: tp.List[int], g: tp.List[int]) -> tp.List[int]:
    if not f or not g:
        raise ValueError("Empty polynomials")

    result = [0] * (max(len(f), len(g)) * 2 - 1)

    for k in range(len(result)):
        for i in range(k + 1):
            if i < len(f) and k - i < len(g):
                result[k] += f[i] * g[k - i]

    return result


def main():
    f, g = read()
    write(*mult_polynomials(f, g))


if __name__ == "__main__":
    main()

