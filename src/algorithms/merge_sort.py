"""Merge sort algorithm"""

import time


def merge_sort_algorithm(data: list[int], draw_data: callable, low: int, high: int, speed: float) -> None:
    """Merge sort algorithm"""
    if low < high:
        mid = low + (high - low) // 2

        merge_sort_algorithm(data, draw_data, low, mid, speed)  # Left list
        merge_sort_algorithm(data, draw_data, mid + 1, high, speed)  # Right list
        merging(data, draw_data, low, mid, high, speed)  # Merge lists


def merging(data: list[int], draw_data: callable, low: int, mid: int, high: int, speed: float) -> None:
    """Merge sort: Merge sublists"""

    left_side = mid - low + 1
    right_side = high - mid

    left_list = [0] * left_side
    right_list = [0] * right_side

    for i in range(0, left_side):
        left_list[i] = data[low + i]
        draw_data(data, ['Grey' for _ in range(len(data))])
        time.sleep(speed)

    for j in range(0, right_side):
        right_list[j] = data[mid + 1 + j]
        draw_data(data, ['Grey' for _ in range(len(data))])
        time.sleep(speed)

    i = 0  # Left index
    j = 0  # Right index
    k = low  # Merged list index

    while i < left_side and j < right_side:
        if left_list[i] <= right_list[j]:
            data[k] = left_list[i]
            draw_data(data, ['Grey' for _ in range(len(data))])
            i += 1
        else:
            data[k] = right_list[j]
            draw_data(data, ['Grey' for _ in range(len(data))])
            j += 1
        k += 1
        time.sleep(speed)

    while i < left_side:
        data[k] = left_list[i]
        draw_data(data, ['Grey' for _ in range(len(data))])
        i += 1
        k += 1
        time.sleep(speed)

    while j < right_side:
        data[k] = right_list[j]
        draw_data(data, ['Grey' for _ in range(len(data))])
        j += 1
        k += 1
        time.sleep(speed)
