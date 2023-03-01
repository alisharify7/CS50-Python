############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharify7             #
#                                          #
############################################


import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    """
        this function take an youtube iframe like and return short version of link
    """

    #  - using walrus  -  
    # if src_link := re.search(r"^<iframe(?:.+)? src=\"(?:https?://)?(?:www\.)?youtube.com/embed/(\w+)\".?(?:.+)?></iframe>$", s):
    #     return f"https://youtu.be/{src_link.group(1)}"
    # return None

    
    #  - normal way -
    src_link = re.search(r"^<iframe(?:.+)? src=\"(?:https?://)?(?:www\.)?youtube.com/embed/(\w+)\".?(?:.+)?></iframe>$", s):
    if src_link:
         return f"https://youtu.be/{src_link.group(1)}"
    return None


if __name__ == "__main__":
    main()
