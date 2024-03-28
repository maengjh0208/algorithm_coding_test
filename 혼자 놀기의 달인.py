def solution(cards):
    is_used_cards = [0 for _ in range(len(cards))]
    link_counts = []

    for i in range(len(cards)):
        if is_used_cards[i] == 0:
            link_cards = [i + 1]
            is_used_cards[i] = 1

            next = cards[i]
            while next not in link_cards:
                link_cards.append(next)
                is_used_cards[next - 1] = 1

                next = cards[next - 1]

            link_counts.append(len(link_cards))

    link_counts.sort(reverse=True)

    if len(link_counts) == 1:
        return 0
    else:
        return link_counts[0] * link_counts[1]


if __name__ == "__main__":
    result = solution([8,6,3,7,2,5,1,4])  #  12
    print(result)