############################################
#                                          #
#             by : Ali Sharify             #
#        Dont copy currently Code          #
#          Github: alisharifyy             #
#                                          #
############################################



import sys

# Get input from user and strip it and force it to be lower case
user = input("File name: ").strip().lower()


image = ['.gif','.png']
app = ['.pdf','.zip']
jpeg = ['.jpg','jpeg']

# iterrate in each list and find file extensions

for i in image:
    if (i in user):
        print("image/" + i.replace(".","").strip())
        sys.exit(0)

for i in app:
    if (i in user):
        print("application/" + i.replace(".","").strip())
        sys.exit(0)


for i in jpeg:
    if (i in user):
        print("image/jpeg")
        sys.exit(0)

if ('.txt' in user):
    print("text/plain")
else:
    print("application/octet-stream")
