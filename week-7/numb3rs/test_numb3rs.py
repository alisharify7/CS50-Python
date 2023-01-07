import numb3rs


def test_four():
    assert numb3rs.validate("127.0.0.1") == True
    assert numb3rs.validate("500.000.000.50000") == False
    assert numb3rs.validate("192.50.50.60") == True
    assert numb3rs.validate("192.58.1.1000") == False
    assert numb3rs.validate("asdqasdasdad") == False


def test_one():
    assert numb3rs.validate("hello") == False
    assert numb3rs.validate("10.554544.56454.") == False
    assert numb3rs.validate("10.10.10.10") == True
    assert numb3rs.validate("...") == False


def test_two():
    assert numb3rs.validate("-50.50.1.1") == False
    assert numb3rs.validate("-5454.874.1.1") == False
    assert numb3rs.validate("0.0.-100.01000..") == False
    assert numb3rs.validate("192.168.1.44") == False
    assert numb3rs.validate("...dasda.. 192.168.1.1") == False



def test_three():
    assert numb3rs.validate("asdasdasd") == False
    assert numb3rs.validate("asdasd") == False
    assert numb3rs.validate("80.50.50.50") == True
    assert numb3rs.validate("asdasda!@#!@") == False
    assert numb3rs.validate("  ") == False
    assert numb3rs.validate("1....1") == False


def main():
    test_one()
    test_two()
    test_three()
    test_four()



if __name__ == "__main__":
    main()
