numbers = [1,2,3,4,5, 100]
for number in numbers:
    print(number)
    numbers.append(number+1)
    if number > 100:
        break
