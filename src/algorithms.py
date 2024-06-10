"""Module to implement algorithms"""

import time


def bubble_sort(data, draw_data, speed):
    """Bubble sort algorithm"""

    size = len(data)

    for i in range(size):
        for j in range(0, size - i - 1):

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                draw_data(data, ['Green' if x == j + 1 else 'Red' for x in range(len(data))])
                time.sleep(speed)


def partition(data, draw_data, low, high, speed):
    """Quick sort: Find partition position"""

    pivot = data[high]
    i = low - 1

    draw_data(data, get_color(len(data), low, high, i, i))

    time.sleep(speed)

    for j in range(low, high):

        if data[j] <= pivot:
            draw_data(data, get_color(len(data), low, high, i, j, True))

            i += 1

            data[i], data[j] = data[j], data[i]

        draw_data(data, get_color(len(data), low, high, i, j))

        time.sleep(speed)

    draw_data(data, get_color(len(data), low, high, i, low, True))

    time.sleep(speed)

    data[i + 1], data[high] = data[high], data[i + 1]

    return i + 1


def quick_sort(data, draw_data, low, high, speed):
    """Quick sort algorithm"""

    if low < high:
        pivot_index = partition(data, draw_data, low, high, speed)

        quick_sort(data, draw_data, low, pivot_index - 1, speed)  # Left-side of pivot
        quick_sort(data, draw_data, pivot_index + 1, high, speed)  # Right-side of pivot


# Grey - Unsorted elements
# Blue - Pivot point element
# White - Sorted half/partition
# Red - Starting pointer
# Yellow - Ending pointer
# Green - All elements are sorted
def get_color(data_len, low, high, border, cur_i, is_swapping=False):
    """Quick sort: Get color for data"""

    color_array = []
    for i in range(data_len):

        if high <= i <= low:
            color_array.append('Grey')
        else:
            color_array.append('White')

        if i == low:
            color_array[i] = 'Blue'
        elif i == border:
            color_array[i] = 'Red'
        elif i == cur_i:
            color_array[i] = 'Yellow'

        if is_swapping:
            if i == border or i == cur_i:
                color_array[i] = 'Green'

    return color_array
