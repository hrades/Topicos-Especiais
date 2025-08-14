def change_letter(texto):
  result = ''
  for i, char in enumerate(texto):
    if i % 2 == 0:
      result += char.upper()
    else:
      result += char.lower()
  return result

user = input('Say something: ')
user = change_letter(user)
print(user)
