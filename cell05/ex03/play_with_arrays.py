#!/usr/bin/env python3

original_array = [2, 4, 9, 48, 8, 22, -12, 2]

new_array = {num + 2 for num in original_array if (num) > 5}

print(original_array)
print(new_array)
