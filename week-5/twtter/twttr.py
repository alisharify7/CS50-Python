############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################


def main():
    answer = shorten("twitter")
    print(answer)


def shorten(str_in):
    for each in str_in:
        if(each.upper() in ['A', 'E', 'I', 'O', 'U']):
            str_in = str_in.replace(each,"")
    return str_in


if __name__ == "__main__":
    main()