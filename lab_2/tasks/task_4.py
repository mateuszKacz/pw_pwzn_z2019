def count_letters(msg):
    """
    Zwraca pare (znak, liczba zliczeń) dla najczęściej występującego znaku w wiadomości.
    W przypadku równości zliczeń wartości sortowane są alfabetycznie.

    :param msg: Message to count chars in.
    :type msg: str
    :return: Most frequent pair char - count in message.
    :rtype: list
    """

    max_l = ('null', 0)

    for letter in msg:

        i = msg.count(letter)

        if i > max_l[1]:
            max_l = (letter, i)
        elif i == max_l[1]:
            if letter < max_l[0]:
                max_l = (letter, i)

    return max_l

    pass


if __name__ == '__main__':
    msg = 'Abrakadabra'
    assert count_letters(msg) == ('a', 4)
    assert count_letters('za') == ('a', 1)