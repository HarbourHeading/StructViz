"""Bubble sort algorithm"""

import time


def bubble_sort_algorithm(data: list[int], draw_data: callable, speed: float) -> None:
    """Bubble sort algorithm"""

    data_len = len(data)

    for i in range(data_len):
        for j in range(0, data_len - i - 1):

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                draw_data(data, ['Green' if x == j + 1 else 'Red' for x in range(len(data))])
                time.sleep(speed)
