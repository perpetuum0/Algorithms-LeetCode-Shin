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


# Алгоритм не сортирует весь массив, потому что после процедуры partition
# pivot уже стоит на своей окончательной позиции 'pi'.
# pi == k: ответ найден, останавливаем сортировку
# k < pi: искомый элемент в левой части, рекурсивно ищем только слева
# k < pi: искомый элемент в правой части, рекурсивно ищем только справа
def quick_select(arr, k):
    def select(low, high):
        # Базовый случай если в рассматриваемом подмассиве остался 1 элемент
        if low == high:
            return arr[low]

        # Разделяем подмассив и получаем точную позицию случайно выбранного опорного элемента
        pi = randomized_partition(arr, low, high)

        if pi == k:
            return arr[pi]  # Элемент найден
        elif k < pi:
            return select(low, pi - 1)  # Ищем в левой части
        else:
            return select(pi + 1, high) # Ищем в правой части

    # Запускаем вспомогательную функцию для всего массива
    return select(0, len(arr) - 1)


arr2 = [10, 4, 5, 8, 6, 11, 26]
k = 2 # Ищем 3-й наименьший элемент
print(f"\nМассив для QuickSelect: {arr2}")
result = quick_select(arr2, k)
print(f"{k}-й наименьший элемент: {result}")
print(f"Массив после QuickSelect: {arr2}")