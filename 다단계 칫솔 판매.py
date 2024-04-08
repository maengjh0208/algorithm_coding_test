# https://school.programmers.co.kr/learn/courses/30/lessons/77486
# seller 에는 중복 판매자가 존재할 수 있음.
# 내 모든 이익을 합산해서 10퍼센트 매긴 값을 추천인에게 보내주는것이 아님. 따로따로 10퍼센트 먹여서 추천인에게 주어야 함.

def solution(enroll: list, referral: list, seller: list, amount: list) -> list:
    profits = {}
    recommend_info = {}  # 내가 추천한 사람들
    recommender = {}  # 나를 추천한 사람

    for name in enroll:
        recommend_info[name] = []
        recommender[name] = None
        profits[name] = 0

    for recommended, recommend in zip(enroll, referral):
        if recommend != "-":
            recommend_info[recommend].append(recommended)
            recommender[recommended] = recommend

    for name, money in zip(seller, amount):
        money *= 100
        ten_percent = int(money / 10)
        profits[name] += money - ten_percent
        next_name = recommender[name]

        while next_name is not None and ten_percent != 0:
            money = ten_percent
            ten_percent = int(money / 10)
            profits[next_name] += money - ten_percent
            next_name = recommender[next_name]

    return [profits[name] for name in enroll]


if __name__ == "__main__":
    result = solution(
        enroll=["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        referral=["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        seller=["sam", "emily", "jaimie", "edward"],
        amount=[2, 3, 5, 4]
    )

    print(result)
    print(result == [0, 110, 378, 180, 270, 450, 0, 0])