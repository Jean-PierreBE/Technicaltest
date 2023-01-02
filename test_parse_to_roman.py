from functions import function_to_test as ft

'''test parse to roman'''
ft.parse_to_roman(1000) # == "M"
#ft.parse_to_roman(2000) # == "MM"



ft.parse_to_roman(4) # == "IV"
ft.parse_to_roman(37) # === "XXXVII"
ft.parse_to_roman(143) # === "CXLIII"
#ft.parse_to_roman(1234) # == "MCCXXXIV"

