test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}
print(test_dict)

user = int(input('What number do you want to check the frequency of? '))
freq = 0

for value in test_dict.values():
  if value == user:
    freq += 1

print('The number' ,user, 'appears', freq, 'times in the dictionary.')