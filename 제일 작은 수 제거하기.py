def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        idx = arr.index(min(arr))
        return arr[:idx] + arr[idx + 1:]


if __name__ == "__main__":
    result = solution([4, 3, 2, 1])
    print(result)
