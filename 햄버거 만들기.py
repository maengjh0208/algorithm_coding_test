# def solution(ingredients):
#     # 정해진 햄버거 구성 순서
#     burger_pattern = [1, 2, 3, 1]
#
#     stack = []  # 재료를 쌓을 스택
#     burger_count = 0  # 포장된 햄버거 수
#
#     for ingredient in ingredients:
#         stack.append(ingredient)  # 재료를 스택에 쌓음
#
#         # 스택에 쌓인 재료가 햄버거 구성 순서와 일치하는지 확인
#         if len(stack) >= len(burger_pattern) and stack[-len(burger_pattern):] == burger_pattern:
#             # 햄버거 구성 순서와 일치하면 해당 재료들을 스택에서 제거
#             for _ in range(len(burger_pattern)):
#                 stack.pop()
#             burger_count += 1  # 포장된 햄버거 수 증가
#
#     return burger_count

def solution(ingredients):
    # 햄버거 구성 순서
    bugger_pattern = [1, 2, 3, 1]
    stack = []
    count = 0

    for num in ingredients:
        # 스택에 재료 쌓음
        stack.append(num)

        # 스택에 쌓인 재료가 햄버거 구성 순서와 일치하는지 확인
        if len(stack) >= len(bugger_pattern) and stack[-len(bugger_pattern):] == bugger_pattern:
            # 햄버거 구성과 일치하면 스택에서 해당 재료들 제거
            for _ in range(len(bugger_pattern)):
                stack.pop()

            # 햄버거 카운트 증가
            count += 1

    return count


if __name__ == "__main__":
    result = solution([1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1])

    print(result)
    print(result == 3)

