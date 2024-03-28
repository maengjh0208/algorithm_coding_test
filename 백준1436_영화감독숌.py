def function():
    N = int(input())

    movie_name = 666
    movie_num = 1

    while(1):
        # 종료 조건
        if N == movie_num:
            print(movie_name)
            break

        movie_name += 1
        movie_num = movie_num + 1 if "666" in str(movie_name) else movie_num


if __name__ == "__main__":
    function()