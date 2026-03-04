

# Task 1: Importing math_utils in two ways
import math_utils
from math_utils import square

print("---- Math Utils ----")
print("Addition:", math_utils.add(10, 5))
print("Subtraction:", math_utils.subtract(10, 5))
print("Square:", square(4))

# Task 2: Import string_utils
import string_utils

print("\n---- String Utils ----")
text = "hello world from python"

print("Capitalized:", string_utils.capitalize_words(text))
print("Reversed:", string_utils.reverse_string(text))
print("Word Count:", string_utils.word_count(text))

# Task 3 & 4: Importing Package
import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package import apply_tax

print("\n---- Shop Package ----")

print("Discounted Price:", disc.apply_discount(1000, 10))
print("Flat Discount:", disc.flat_discount(1000))

total = calculate_total([100, 200, 300])
print("Total Bill:", total)

print("Total with Tax:", apply_tax(total))