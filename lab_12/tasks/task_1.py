def generate_fibonacci(n=100):

    n_0 = 0
    n_1 = 1

    if isinstance(n, int) and (0 < n <= 100):

        for i in range(n):
            if i == 0:
                yield n_0
            elif i == 1:
                yield n_1
            else:
                n = n_1 + n_0
                yield n
                n_0 = n_1
                n_1 = n
    else:
        raise RuntimeError("n is not integer value")


if __name__ == '__main__':
    assert list(generate_fibonacci(1)) == [0]
    assert list(generate_fibonacci(2)) == [0, 1]
    assert sum(generate_fibonacci(10)) == 88
    ii = 0
    for ii in generate_fibonacci():
        pass
    assert ii == 218922995834555169026
    try:
        generate_fibonacci(0)
    except Exception as exc:
        assert isinstance(exc, RuntimeError)
