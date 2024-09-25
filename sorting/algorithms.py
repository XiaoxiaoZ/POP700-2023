from sortableInterface import Sortable


def bubble_sort(data: Sortable):
    n = data.length()
    for i in range(n):
        for j in range(0, n-i-1):
            if data.get(j).compare(data.get(j+1)):
                data.swap(j, j+1)
    return data

def selection_sort(data: Sortable):
    n = data.length()
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if data.get(j).compare(data.get(min_index)):
                min_index = j
        data.swap(i, min_index)
    return data

def insertion_sort(data: Sortable):
    n = data.length()
    for i in range(1, n):
        key = data.get(i)
        j = i - 1
        while j >= 0 and data.get(j).compare(key):
            data.swap(j + 1, j)
            j -= 1
    return data

def heap_sort(data: Sortable):
    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data.get(left).compare(data.get(largest)):
            largest = left

        if right < n and data.get(right).compare(data.get(largest)):
            largest = right

        if largest != i:
            data.swap(i, largest)
            heapify(n, largest)

    n = data.length()

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extract elements from heap one by one
    for i in range(n-1, 0, -1):
        data.swap(0, i)
        heapify(i, 0)

    return data

def quick_sort(data: Sortable):
    def partition(low, high):
        pivot = data.get(high)
        i = low - 1
        for j in range(low, high):
            if data.get(j).compare(pivot):
                i += 1
                data.swap(i, j)
        data.swap(i + 1, high)
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, data.length() - 1)
    return data