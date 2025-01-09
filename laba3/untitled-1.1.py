file = input('Ведите название файла: ')
try:
  my_file = open(file)
except FileNotFoundError:
  print(f"Этого файла не существует")
else:
  cont = my_file.read()
  print(cont)
  my_file.close()