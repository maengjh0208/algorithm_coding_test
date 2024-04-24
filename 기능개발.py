# 기능은 진도가 100퍼 되어야 서비스에 반영 가능
# 기능의 개발속도는 모두 다름
# 뒤에 있는 기능이 앞의 기능보다 먼저 개발될 수 있음. 그래도 앞에 있는 기능이 배포될때 같이 배포될 수 있음


def solution(progresses, speeds):
    # 남은 작업 진도에 대하여, 배포 가능한 일자 구하기
    publish = []
    for i in range(len(progresses)):
        remain_work = 100 - progresses[i]

        if remain_work % speeds[i] != 0:
            publish.append(remain_work // speeds[i] + 1)
        else:
            publish.append(remain_work // speeds[i])

    # 배포마다 몇 개의 기능이 배포되는지 구하기
    result = []
    day = publish[0]
    count = 1
    for i in range(1, len(publish)):
        if publish[i] > day:
            result.append(count)
            count = 1
            day = publish[i]
        else:
            count += 1

        if i == (len(publish) - 1):
            result.append(count)

    return result


if __name__ == "__main__":
    result = solution(
        progresses=[93, 30, 55],
        speeds=[1, 30, 5],
    )
    print(result)
