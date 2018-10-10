from algorithm.QuickSort import *

vector = [10, 7, 8, 9, 1, 5]

try:
    quicksort = QuickSort(vector)
    length = len(vector)
    print(quicksort.sort(0, length-1))
except Exception as e:
    print(e)

vector = [] 

try:
    quicksort = QuickSort(vector)
    length = len(vector)
    print(quicksort.sort(0, length-1))
except Exception as e:
    print(e)


vector = None

try:
    quicksort = QuickSort(vector)
    length = len(vector)
    print(quicksort.sort(0, length-1))
except Exception as e:
    print(e)


vector = [6]

try:
    quicksort = QuickSort(vector)
    length = len(vector)
    print('Vetor Ordenado: '+quicksort.sort(0, length-1))
except Exception as e:
    print(e)