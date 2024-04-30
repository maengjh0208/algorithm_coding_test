def solution(n, m, x, y, queries):
    left_up_location = [x, y]
    right_down_location = [x, y]

    for direction, distance in queries[::-1]:
        if direction == 0:
            # 끝지점에 있다면 영역을 넓히고
            if left_up_location[1] == 0:
                right_down_location[1] = min(right_down_location[1] + distance, m - 1)
            # 아니라면 옮긴다.
            elif left_up_location[1] + distance < m:
                left_up_location[1] += distance
                right_down_location[1] = min(right_down_location[1] + distance, m - 1)
            # 공을 굴려도 목적지에 닿을 수 없는 케이스
            else:
                break
        elif direction == 1:
            # 끝지점에 있다면 영역을 넓히고
            if right_down_location[1] == m - 1:
                left_up_location[1] = max(left_up_location[1] - distance, 0)
            # 아니라면 옮긴다.
            elif right_down_location[1] - distance >= 0:
                right_down_location[1] -= distance
                left_up_location[1] = max(left_up_location[1] - distance, 0)
            # 공을 굴려도 목적지에 닿을 수 없는 케이스
            else:
                break
        elif direction == 2:
            # 끝지점에 있다면 영역을 넓히고
            if left_up_location[0] == 0:
                right_down_location[0] = min(right_down_location[0] + distance, n - 1)
            # 아니라면 옮긴다.
            elif left_up_location[0] + distance < n:
                left_up_location[0] += distance
                right_down_location[0] = min(right_down_location[0] + distance, n - 1)
            # 공을 굴려도 목적지에 닿을 수 없는 케이스
            else:
                break
        else:
            # 끝지점에 있다면 영역을 넓히고
            if right_down_location[0] == n - 1:
                left_up_location[0] = max(left_up_location[0] - distance, 0)
            # 아니라면 옮긴다.
            elif right_down_location[0] - distance >= 0:
                right_down_location[0] -= distance
                left_up_location[0] = max(left_up_location[0] - distance, 0)
            # 공을 굴려도 목적지에 닿을 수 없는 케이스
            else:
                break
    else:
        return (right_down_location[0] - left_up_location[0] + 1) * (right_down_location[1] - left_up_location[1] + 1)

    return 0


if __name__ == "__main__":
    result = solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]])
    print(result)
