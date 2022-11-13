# first lets create a file
f = open('lets_ReadFile.txt', 'w+')
for i in range(20):
    f.write("Lets start new life %d\r\n" % (i + 1))
f.close()

# now lets read it
with open('lets_ReadFile.txt', 'r') as f:
    content = f.readlines()
    count = 0
    while count < len(content):
        print(content[count])
        count += 1

#
# file = open("testfile.txt", "w")
#
# file.write("Hello World\t")
# file.write('This is our new text file\t')
# file.write('and this is another line.\t')
# file.write('Why? Because we can.')
#
# file.close()
#
# f=open("testfile.txt", "r")
# cont=f.read()
# print(cont)
