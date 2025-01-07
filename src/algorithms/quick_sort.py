"""Quick sort algorithm"""

import time


def quick_sort_algorithm(data: list[int], draw_data: callable, low: int, high: int, speed: float) -> None:
    """Quick sort algorithm"""

    if low < high:
        pivot_index = partition(data, draw_data, low, high, speed)

        quick_sort_algorithm(data, draw_data, low, pivot_index - 1, speed)  # Left-side of pivot
        quick_sort_algorithm(data, draw_data, pivot_index + 1, high, speed)  # Right-side of pivot


def get_color(data: list[int], low: int, border: int, cur_i: int, is_swapping: bool = False) -> list[str]:
    """Quick sort: Get color for data"""

    color_list = []
    data_len = len(data)

    for i in range(data_len):

        color_list.append('White')  # White: Sorted half/partition

        if i == low:
            color_list[i] = 'Blue'  # Blue: Pivot point element
        elif i == border:
            color_list[i] = 'Grey'  # Grey: Starting pointer
        elif i == cur_i:
            color_list[i] = 'Yellow'  # Yellow: Ending pointer

        if is_swapping and (i == border or i == cur_i):
            color_list[i] = 'Green'  # Green: Sort complete

    return color_list


def partition(data: list[int], draw_data: callable, low: int, high: int, speed: float) -> int:
    """Quick sort: Find partition position"""

    pivot = data[high]
    i = low - 1

    draw_data(data, get_color(data, high, i, i))

    time.sleep(speed)

    for j in range(low, high):

        if data[j] <= pivot:
            draw_data(data, get_color(data, high, i, j, True))

            i += 1

            data[i], data[j] = data[j], data[i]

        draw_data(data, get_color(data, high, i, j))

        time.sleep(speed)

    draw_data(data, get_color(data, high, i, low, True))

    time.sleep(speed)

    data[i + 1], data[high] = data[high], data[i + 1]

    return i + 1
