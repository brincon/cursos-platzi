numbers = [1, 2, 3, 4, 5]

# solo los numeros que tienen residuo 0, van a pertenecer 
# a la nueva lista
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
print(numbers)
