def select_type(survey_info: dict, indicator: int) -> str:
    answer = ""

    if indicator == 1:
        answer = "T" if survey_info["R"] < survey_info["T"] else "R"
    elif indicator == 2:
        answer = "F" if survey_info["C"] < survey_info["F"] else "C"
    elif indicator == 3:
        answer = "M" if survey_info["J"] < survey_info["M"] else "J"
    elif indicator == 4:
        answer = "N" if survey_info["A"] < survey_info["N"] else "A"

    return answer


def solution(survey: list, choices: list) -> str:
    # 점수판
    survey_dict = {
        "R": 0, "T": 0,
        "C": 0, "F": 0,
        "J": 0, "M": 0,
        "A": 0, "N": 0,
    }

    # 점수 합산
    score_list = [3, 2, 1, 0, 1, 2, 3]
    for i in range(len(choices)):
        if choices[i] < 4:
            survey_dict[survey[i][0]] += score_list[choices[i] - 1]
        elif choices[i] > 4:
            survey_dict[survey[i][1]] += score_list[choices[i] - 1]

    # 성격 유형
    first = select_type(survey_dict, 1)
    second = select_type(survey_dict, 2)
    third = select_type(survey_dict, 3)
    fourth = select_type(survey_dict, 4)

    return f"{first}{second}{third}{fourth}"


if __name__ == "__main__":
    result = solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
    print(result)