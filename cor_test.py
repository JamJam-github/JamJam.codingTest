import time


def coroutine_test():
    greeting = "good "
    text = (yield greeting)

    while True:
        # text = (yield greeting)
        print("text = ", end=""), print(text)
        # greeting += text
        text = yield greeting + text


if __name__ == "__main__":
    cr = coroutine_test()
    print("cr=", end=""), print(cr)

    next(cr)
    time.sleep(2)

    print("send 1")
    print(cr.send("morning"))
    time.sleep(2)

    print("send 2")
    print(cr.send("afternoon"))
    time.sleep(2)

    print("send 3")
    print(cr.send("evening"))
    time.sleep(2)