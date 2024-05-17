def solution(cards: list, slotSize: int) -> bool:
    def put_card_into_box(num: int) -> int:
        # 0 반환: 상자에 담았으나 꽉 채우지 못한 경우 / 1 반환: 상자에 담았고 꽉 채움 / -1 반환: 어떤 상자에도 담을 수 없음
        for i in range(box_count):
            if not box_list[i]:
                box_list[i].append(num)
                return 0

            if len(box_list[i]) < slotSize and box_list[i][-1] == num - 1:
                box_list[i].append(num)
                return 1 if len(box_list[i]) == slotSize else 0

        return -1

    box_count = len(cards) // slotSize
    box_list = [[] for _ in range(box_count)]

    cards.sort()
    result_count = 0
    for card_number in cards:
        result_count += put_card_into_box(card_number)

    return True if result_count == box_count else False


if __name__ == "__main__":
    result = solution(
        [5, 3, 2, 5],
        2
    )

    print(result)
