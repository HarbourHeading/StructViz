"""Module to implement algorithms"""

import time
from typing import List


def bubble_sort(data: list[int], draw_data: any, speed: float) -> None:
    """Bubble sort algorithm"""

    data_len = len(data)

    for i in range(data_len):
        for j in range(0, data_len - i - 1):

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                draw_data(data, ['Green' if x == j + 1 else 'Red' for x in range(len(data))])
                time.sleep(speed)


def quick_sort(data: list[int], draw_data: any, low: int, high: int, speed: float) -> None:
    """Quick sort algorithm"""

    if low < high:
        pivot_index = partition(data, draw_data, low, high, speed)

        quick_sort(data, draw_data, low, pivot_index - 1, speed)    # Left-side of pivot
        quick_sort(data, draw_data, pivot_index + 1, high, speed)   # Right-side of pivot


def get_color(data: list[int], low: int, high: int, border: int, cur_i: int, is_swapping: bool = False) -> List[str]:
    """Quick sort: Get color for data"""

    color_list: list[str] = []
    data_len = len(data)

    for i in range(data_len):

        if high <= i <= low:
            color_list.append('Grey')   # Grey: Unsorted elements
        else:
            color_list.append('White')  # White: Sorted half/partition

        if i == low:
            color_list[i] = 'Blue'      # Blue: Pivot point element
        elif i == border:
            color_list[i] = 'Red'       # Red: Starting pointer
        elif i == cur_i:
            color_list[i] = 'Yellow'    # Yellow: Ending pointer

        if is_swapping and (i == border or i == cur_i):
            color_list[i] = 'Green'     # Green: Sort complete

    return color_list


def partition(data: list[int], draw_data: any, low: int, high: int, speed: float) -> int:
    """Quick sort: Find partition position"""

    pivot: int = data[high]
    i: int = low - 1

    draw_data(data, get_color(data, low, high, i, i))

    time.sleep(speed)

    for j in range(low, high):

        if data[j] <= pivot:
            draw_data(data, get_color(data, low, high, i, j, True))

            i += 1

            data[i], data[j] = data[j], data[i]

        draw_data(data, get_color(data, low, high, i, j))

        time.sleep(speed)

    draw_data(data, get_color(data, low, high, i, low, True))

    time.sleep(speed)

    data[i + 1], data[high] = data[high], data[i + 1]

    return i + 1
