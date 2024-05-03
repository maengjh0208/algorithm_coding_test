# 개인정보 n개 (고객의 약관 동의를 얻어 수집됨)
# 약관 종류 다양, 각 약관별 보관 유효기간 따로따로 정해져 있음

def solution(today, terms, privacies):
    year, month, day = map(int, today.split("."))
    day += 1

    expiration_date = {}
    for term in terms:
        term_type, term_month = term.split()
        term_month = int(term_month)

        if day == 29:
            term_month += 1

        term_month = month - term_month
        term_year = year

        if term_month <= 0:
            term_year -= -term_month // 12 + 1
            term_month = 12 - (-term_month % 12)

        expiration_date[term_type] = f"{term_year}.{term_month:0>2}.{day:0>2}"

    # 파기해야 할 개인정보
    result = []
    for idx, privacy in enumerate(privacies):
        regist_date, regist_term = privacy.split()

        if regist_date < expiration_date[regist_term]:
            result.append(idx + 1)

    return result


if __name__ == "__main__":
    result = solution(
        today="2020.05.17",
        terms=["A 3", "B 12"],
        privacies=["2020.01.01 A", "2020.05.16 B"],
    )

    print(result)
