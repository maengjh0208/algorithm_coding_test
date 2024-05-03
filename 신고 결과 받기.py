def solution(id_list, report, k):
    # 유저: 해당 유저가 신고한 유저들
    reporter_dict = {name: set() for name in id_list}

    # 유저: 신고당한 횟수
    reportee_dict = {name: 0 for name in id_list}

    for report_content in report:
        reporter, reportee = report_content.split(" ")

        if reportee not in reporter_dict[reporter]:
            reporter_dict[reporter].add(reportee)
            reportee_dict[reportee] += 1

    # 각 유저별 처리 결과 메일 받은 횟수 확인
    result = []
    for id in id_list:
        count = 0
        for reportee in reporter_dict[id]:
            if reportee_dict[reportee] >= k:
                count += 1

        result.append(count)

    return result


if __name__ == "__main__":
    result = solution(
        id_list=["muzi", "frodo", "apeach", "neo"],
        report=["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        k=2,
    )

    print(result)
