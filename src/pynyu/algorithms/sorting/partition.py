from __future__ import annotations

from random import SystemRandom


class Partition(object):
    def lomuto(arr):
        return Partition.lomuto_range(arr, 0, len(arr) - 1)

    def lomuto_range(arr, start, end):
        if start > end:
            raise ValueError("start must be less than end")
        if start == end:
            raise ValueError("array cannot be empty")

        pivot = arr[end]
        j = start - 1

        for i in range(end):
            if arr[i] <= pivot:
                j = j + 1
                arr[j], arr[i] = arr[i], arr[j]

        arr[j + 1], arr[end] = arr[end], arr[j + 1]
        return j + 1

    def lomuto_range_index(arr, start, end, index):
        if index < start or index > end:
            raise ValueError("index must be within range of array")
        if start > end:
            raise ValueError("start must be less than end")
        if start == end:
            raise ValueError("array cannot be empty")
        arr[end], arr[index] = arr[index], arr[end]
        return Partition.lomuto_range(arr, start, end)

    def lomuto_index(arr, index):
        end = len(arr) - 1
        return Partition.lomuto_range_index(arr, 0, end, index)

    def lomuto_range_element(arr, start, end, element):
        index = arr.index(element)
        return Partition.lomuto_range_index(arr, start, end, index)

    def lomuto_element(arr, element):
        end = len(arr) - 1
        return Partition.lomuto_range_element(arr, 0, end, element)

    def lomuto_range_random(arr, start, end):
        random_index = SystemRandom().randint(start, end)
        return Partition.lomuto_range_index(arr, start, end, random_index)

    def lomuto_random(arr):
        end = len(arr) - 1
        return Partition.lomuto_range_random(arr, 0, end)


if __name__ == "__main__":
    pass
