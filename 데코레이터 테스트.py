def test_decorator_2(func):
    def wrapper(*args, **kwargs):
        print("test_decorator_2 실행 중")
        func(*args, **kwargs)
        print("test_decorator_2 실행 완료")

    return wrapper


def test_decorator_1(func):
    def wrapper(*args, **kwargs):
        print("test_decorator_1 실행 중")
        func(*args, **kwargs)
        print("test_decorator_1 실행 완료")

    return wrapper


@test_decorator_1
@test_decorator_2
def say_hello():
    print("say_hello 함수 실행!")

say_hello()