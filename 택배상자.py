# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    origin_container = [i for i in range(len(order), 0, -1)]
    secondary_container = []
    count = 0

    while count != len(order):
        delivery = order[count]

        # 보조 컨테이너 마지막으로 올려놓은 택배와 일치하면 꺼낸다.
        if secondary_container and secondary_container[-1] == delivery:
            count += 1
            secondary_container.pop()
        elif origin_container:
            # 기존 컨테이너의 택배와 일치하면 꺼낸다.
            if origin_container[-1] == delivery:
                count += 1
                origin_container.pop()
            # 보조 컨테이너에 넣는다.
            else:
                secondary_container.append(origin_container.pop())
        # 더이상 진행 불가능
        else:
            break

    return count


if __name__ == "__main__":
    result = solution([5, 4, 3, 2, 1])
    print(result)