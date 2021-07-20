def solution(array, commands):
    answer = []
    slice_arr = []
    for i in commands:
        start, end, index = i
        slice_arr = array[start-1:end]
        slice_arr.sort()
        answer.append(slice_arr[index-1])
    
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))