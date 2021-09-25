"""
def test1():
    assert "Green" == "Blue", "There is an error No.1"
    print("Pass 1")
"""


def test2():
    assert "Green" == "green", "There is an error No.2"
    print("It is working")


def main():
    test2()
    #test1()

main()