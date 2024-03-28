# 팀은 6명으로 구성. 상위 4명의 점수를 합산.
# 자격을 갖춘 사람(6명 미만인 팀은 제외)은 결승점을 통과한 순서대로 점수를 받음
# 가장 낮은 점수를 받은 팀이 우승. 점수가 동일할 경우 다섯번 째 주자가 더 빨리 들어온 팀이 우승
import sys


def function():
    # T: 테스트 케이스
    T = int(input())

    for _ in range(T):
        num = int(sys.stdin.readline().rstrip())
        arrivals = sys.stdin.readline().split()

        # key: 팀 번호 / value: [인원 수, 상위 4명 점수, 5번째 주자 점수, 상위 4명 점수 합산하기 위애 필요한 카운트 수]
        team_info = dict()

        # 팀 인원수 확인
        for i in range(len(arrivals)):
            if arrivals[i] not in team_info:
                # 첫 주자 들어올 때 초기 세팅
                team_info[arrivals[i]] = [1, 0, 0, 0]
            else:
                team_info[arrivals[i]][0] += 1

        # 팀 별 점수 합산
        score = 1
        for i in range(len(arrivals)):
            if team_info[arrivals[i]][0] == 6:
                team_info[arrivals[i]][3] += 1

                if team_info[arrivals[i]][3] <= 4:
                    team_info[arrivals[i]][1] += score
                elif team_info[arrivals[i]][3] == 5:
                    team_info[arrivals[i]][2] = score

                score += 1

        # 우승자 정보: [우승팀 번호, 우승팀 상위 4명 점수, 우승팀 5번째 주자 점수]
        winner = [0, 6 * num, 0]

        for key, value in team_info.items():
            # 팀원이 6명이 아닌 경우 탈락
            if value[0] != 6:
                continue

            # 우승자 교체
            if winner[1] > value[1] or (winner[1] == value[1] and winner[2] > value[2]):
                winner = [key, value[1], value[2]]

        print(winner[0])


if __name__ == "__main__":
    function()