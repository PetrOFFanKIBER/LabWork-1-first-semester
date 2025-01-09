i = input('Напишите "r"')
file = open('example.txt', i)
content = file.read()
print (content)
file.close