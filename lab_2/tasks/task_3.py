def unique(values):
    """
    Funkcja zwraca listę unikatowych wartości.
    Utrudnienie: Funkcja zwraca unikatowe wartości w kolejności wystąpienia.

    :param values: List of values to check.
    :type values: list
    :return: Unique values in order of appear.
    :rtype: list
    """

    unique_val = []

    while values:

        val = values[0]
        num_of_val = values.count(val)
        unique_val.append(val)

        for i in range(num_of_val):
            values.remove(val)

    return unique_val

    pass


if __name__ == "__main__":
     assert [1, 5, 3, 6, 7, 2, 4] == unique([1, 5, 3, 5, 6, 7, 2, 1, 4, 1, 5])