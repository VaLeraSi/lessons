from sys import argv
# with open("bakery.csv", "r+", encoding="utf-8") as list_1:
with open("bakery.csv", "a", encoding="utf-8") as list_1:
    with open("bakery.csv", "r", encoding="utf-8") as list_2:
        if len(argv) == 1:
            print(list_2.read())
        elif len(argv) == 2:
            if "," in argv[1]:
                list_2.read()
                print(argv[1], file=list_1)
            else:
                print(*list_2.readlines()[int(argv[1]) - 1:], sep="")
        else:
            print(list_2.read().split()[int(argv[1]):int(argv[2]) + 1], sep="\n")
#
# from sys import argv
#
# with open("bakery.csv", "a", encoding="utf-8") as donut_a:
#     with open("bakery.csv", "r", encoding="utf-8") as donut_r:
#         if len(argv) > 1 and [i for i in argv[1:] if i.replace(".", "").isdigit()]:
#             if len(argv) == 3:
#                 print(*donut_r.read().split()[int(argv[1]) - 1:int(argv[2])], sep="\n")
#             if "," in argv[1] or "." in argv[1]:
#                 print(argv[1], file=donut_a)
#             else:
#                 print(*donut_r.readlines()[int(argv[1]) - 1:], sep="")
#         else:
#             print(donut_r.read())