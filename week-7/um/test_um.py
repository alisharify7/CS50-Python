import um

def test_valid_response():
    assert um.count("Um, Hello. How are You?") == 1
    assert um.count("my name is jeff") == 0
    assert um.count("Yummy Cake,!") == 0
    assert um.count("um, its nice to meet you emmy, um, i gotta go") == 2

def test_invalid_response():
    assert um.count("") == 1
    assert um.count("UMY YUM muy UMa umma") == 0