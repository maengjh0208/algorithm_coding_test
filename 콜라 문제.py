def solution(a, b, n):
    count = 0
    while n >= a:
        new_cola = (n // a) * b
        n = n % a + new_cola
        count += new_cola

    return count


if __name__ == "__main__":
    result = solution(3, 1, 20)
    print(result)