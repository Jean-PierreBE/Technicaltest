from functions import function_to_test as ft

text = 'je m appelle nili stein'
sens = 'C'
iter = 1
str1 = ft.rot_text(text.upper(), sens, iter)
print(str1)

str2 = ft.rot_text(str1.upper(), 'D', iter)
print(str2)