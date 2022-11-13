def readBook(filepath):
    with open(filepath, 'r') as f:
        cnt = 1
        while f.readline():
            print("Line {}: {}".format(cnt, f.readline()))
            cnt += 1

    # with open(filepath,"r") as f:
    #     for lines in f:
    #         print(lines)
    #     f.close()

    # with open(filepath,"r") as fp:
    #     linem = fp.readlines()
    #     print(linem)

    # with open(filepath, "r") as f:
    #     # for line in f.read(): kelime kelime okudu
    #     # for line in f.readlines():  # hepsini okudu f veya f.readlines() aynı işi görüyor.
    #     # for line in f.readline(): kelime kelime okudu
    #     # for line in f:f.readlines():  # hepsini okudu f veya f.readlines() aynı işi görüyor.
    #     for line in f.readline():
    #         print(line)

    # with open(filepath) as fnp:
    #     line = fnp.readline()
    #     count = 1
    #     while line:
    #         print(f"Line {count}: {line}")
    #         line = fnp.readline()
    #         count += 1


filepath = "illiad.txt"
readBook(filepath)
print()
readBook(filepath)
