from functions import function_to_test as ft

'''test parse to roman'''
ft.parse_to_roman(-1) # == "NONE
ft.parse_to_roman(1000) # == "M"
ft.parse_to_roman(2000) # == "MM"
ft.parse_to_roman(3500) # == "MMMD"
ft.parse_to_roman(4500) # == "MMMMD"
ft.parse_to_roman(4700) # == "MMMMDCC"

ft.parse_to_roman(4) # == "IV"
ft.parse_to_roman(5) # == "V"
ft.parse_to_roman(6) # == "VI"
ft.parse_to_roman(37) # === "XXXVII"
ft.parse_to_roman(143) # === "CXLIII"
ft.parse_to_roman(146) # === "CXLVI"
ft.parse_to_roman(1234) # == "MCCXXXIV"

