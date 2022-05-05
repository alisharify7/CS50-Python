# import sys

# user = input("File name: ").lower()

# image = ['.gif','.jpeg','.png']
# app = ['.pdf','.zip']

# for i in image:
#     if (i in user):
#         a = i.replace(".","")
#         print("image/" + a)
#         sys.exit(0)

# for i in app:
#     if (i in user):
#         a = i.replace(".","")
#         print("application/" + a)
#         sys.exit(0)

# if ('.txt' in user):
#     print("text/plain")
# elif('.jpg' in user):
#     print("image/jpeg")
# else:
#     print("application/octet-stream")


import sys

user = input("File name: ").strip().lower()

image = ['.gif','.png']
app = ['.pdf','.zip']
jpeg = ['.jpg','jpeg']


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
