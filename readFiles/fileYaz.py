# yaz
def writeToFile(path, content):
    file = open('./testYaz.txt', "w")
    file.write(yaz)
    file.close()


yaz = input("Yazıyı giriniz: ")
writeToFile('./testYaz.txt', yaz)


# oku
def okuyazi():
    count = 1
    with open('./testYaz.txt', 'r') as file:
        line = file.readlines()
        count = 1
        while line:
            print("{}. satır: {}".format(count, line))
            line = file.readline()
            count += 1


okuyazi()
"""Peace, factious monster, born to vex the state, With wrangling talents form'd for foul debate Curb that impetuous tongue, nor rashly vain. """
