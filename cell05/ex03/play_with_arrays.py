original_array = [2, 8, 9, 48, 8, 22, -12, 2]
temp_array2 = [value + 2 for value in original_array if value > 5]
new_array2 = sorted(list(set(temp_array2)))
print("Original array:", original_array)
print("New array:", new_array2)