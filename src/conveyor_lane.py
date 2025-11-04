import heapq

"""
HW03 — Conveyor Lane: Nearly-Sorted Packages

Implement sort_k_sorted(arr, k) -> list
"""

def sort_k_sorted(arr, k):
    # If array is empty or k is 0, no sorting needed
    if not arr or k == 0:
        return arr

    result = []
    heap = []

    # 1) Push first k+1 items into the heap
    for i in range(min(k + 1, len(arr))):
        heapq.heappush(heap, arr[i])

    # 2) Process the rest of the items
    for i in range(k + 1, len(arr)):
        # Pop smallest and append to result
        result.append(heapq.heappop(heap))
        # Push next item
        heapq.heappush(heap, arr[i])

    # 3) Drain remaining heap items
    while heap:
        result.append(heapq.heappop(heap))

    return result
