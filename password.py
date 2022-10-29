import random

lower_case = "abcdefghijklmnopqrstuvxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
number = "0123456789"
special_symbol = "@#$%&*?\/"

use_for = lower_case+upper_case+number+special_symbol
length_for_pass = 8
password = "".join(random.sample(use_for,length_for_pass))
print("you generted password is :", password)

