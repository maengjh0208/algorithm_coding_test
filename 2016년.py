import datetime


def solution(a: int, b: int) -> str:
    day = datetime.date(2016, a, b)

    weekday = {
        0: "MON", 1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN",
    }

    return weekday[day.weekday()]


if __name__ == "__main__":
    result = solution(5, 24)
    print(result)
