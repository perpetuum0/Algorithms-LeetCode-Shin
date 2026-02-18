def binary_search_recursive(arr, left, right, target):
    # base case - элемент не найден
    if left > right:
        return -1

    mid = (left + right) // 2

    # base case - элемент найден
    if arr[mid] == target:
        return mid

    # recursive call - ищем в правой или левой части
    if arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, right, target)
    else:
        return binary_search_recursive(arr, left, mid - 1, target)
