def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # вычисляем середину
        mid = (left + right) // 2

        # элемент найден
        if arr[mid] == target:
            return mid

        # Искомый элемент больше центрального, тогда ищем в правой части
        if arr[mid] < target:
            left = mid + 1
        # искомый элемент меньше центрального, тогда ищем в левой части
        else:
            right = mid - 1

    # элемент не найден
    return -1
