############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################


from bank import value


def test_20():
    assert value("HY MIKE") == 20
    assert value("HOW ?") == 20


def test_100():
    assert value("very nice") == 100
    assert value("zodiac") == 100


def test_0():
    assert value("Hello Temp") == 0
    assert value("HelLo temp") == 0
    assert value("HELLO temp") == 0
