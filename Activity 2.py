#Finding Frequency
test_dict = {'Codingal' : 2, 'is' : 2, 'the' : 2, 'for' : 2, 'Coding' : 1}
print(test_dict)

k = 2
result = 0

for key in test_dict:
    if test_dict[key] == k:
        result += 1
print("\nThe frequency of 'k' is :",result)