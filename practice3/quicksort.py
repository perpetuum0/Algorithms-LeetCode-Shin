import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  # Индекс последнего элемента, который меньше или равен pivot

    for j in range(low, high):
        # Если текущий элемент меньше или равен опорному, отправляем его в левую часть
        if arr[j] <= pivot:
            i += 1
            
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    return i + 1

def randomized_partition(arr, low, high):
    # Выбираем случайный индекс в диапазоне [low, high]
    rand_pivot_idx = random.randint(low, high)
    
    # Меняем местами случайно выбранный элемент с последним arr[high]
    # Это позволяет нам использовать стандартную логику схемы Ломуто, 
    # где pivot всегда берется из конца, но по факту он был выбран случайно
    arr[rand_pivot_idx], arr[high] = arr[high], arr[rand_pivot_idx]
    
    return partition(arr, low, high)

def quick_sort(arr, low, high):
    if low < high:
        # Получаем индекс опорного элемента после разделения
        pi = randomized_partition(arr, low, high)

        # Рекурсивно сортируем левую часть (элементы меньше опорного)
        quick_sort(arr, low, pi - 1)
        # Рекурсивно сортируем правую часть (элементы больше опорного)
        quick_sort(arr, pi + 1, high)

arr1 = [10, 7, 8, 9, 1, 5]
print(f"До QuickSort: {arr1}")
quick_sort(arr1, 0, len(arr1) - 1)
print(f"После QuickSort: {arr1}")
