def solution(local_list):
    # 인자로 받은 가변 객체의 상태를 변경
    local_list = local_list.copy()
    local_list[0] = 100


global_list = [1, 2, 3, 4, 5]
solution(global_list)

print(global_list)


