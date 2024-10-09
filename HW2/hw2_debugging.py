import rand


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    leftArr = mergeSort(arr[:half])
    rightArr = mergeSort(arr[half:])
    return recombine(leftArr, rightArr)

def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = []

    # Merge arrays while both have elements.
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr.append(leftArr[leftIndex])
            leftIndex += 1
        else:
            mergeArr.append(rightArr[rightIndex])
            rightIndex += 1

    # Append remaining elements from leftArr.
    while leftIndex < len(leftArr):
        mergeArr.append(leftArr[leftIndex])
        leftIndex += 1

    # Append remaining elements from rightArr
    while rightIndex < len(rightArr):
        mergeArr.append(rightArr[rightIndex])
        rightIndex += 1

    return mergeArr

arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)
