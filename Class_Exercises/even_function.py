def even():
    even_numbers = []
    for count in range(0, 51, 2):
        if count == 20:
            break
        even_numbers.append(count)
    print(even_numbers)
    average = sum(even_numbers) / len(even_numbers)
    return average


print(even())
