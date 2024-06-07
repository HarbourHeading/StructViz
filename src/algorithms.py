"""Module to implement the algorithms"""


def bubble(data, draw_data):
    """Bubble sort algorithm"""

    data_length = len(data)

    for i in range(data_length):
        for j in range(0, data_length - i - 1):

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                draw_data(data, ['Green' if x == j + 1 else 'Red' for x in range(len(data))])
                yield

    draw_data(data, ['Green' for _ in range(len(data))])
