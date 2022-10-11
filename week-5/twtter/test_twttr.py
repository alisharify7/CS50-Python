############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################


from twttr import shorten

def test_strings():
    assert shorten("twitter") == 'twttr'


def test_names():
    assert shorten("TWITTER") == 'TWTTR'


def test_numbers():
    assert shorten("123987") == '123987'
    assert shorten("123456879") == '123456879'


def test_uppercase():
    assert shorten("hello twitter") == 'hll twttr'

