############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################



from plates import is_valid

def main():
    test_one()
    test_two()
    test_three()
    test_four()


def test_one():
    assert is_valid("cs50") == True
    assert is_valid("cs05") == False


def test_two():
    assert is_valid("cs50p") == False
    assert is_valid("PI3.14") == False


def test_three():
    assert is_valid('O') == False
    assert is_valid('OUTATIMEasasasdasdasda') == False

def test_four():
    assert is_valid('5as5as0as5sdaf5da56d56a5d6a5d') == False
    assert is_valid('15050055454545454') == False


if __name__ == "__main__":
    main()
