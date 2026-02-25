def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False # ведем учет, была ли сделана хотя бы одна перестановка
    
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # если не было перестановок, массив отсортирован
        if not swapped:
            break
            
    return arr


a = [64, 34, 25, 12, 22, 11, 90]
print("Input:", a)

sa = optimized_bubble_sort(a)
print("Output:", sa)
