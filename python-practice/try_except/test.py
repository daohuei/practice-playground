def test(x):
    try:
        if x:
            print(x)
        else:
            raise (Exception)
    except:
        print("wrong")
    finally:
        print("finally")

    print("after finally")


if __name__ == "__main__":
    test(None)
    test("hello")
