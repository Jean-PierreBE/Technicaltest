def parse_to_roman(num_arabe):
    arabe = [1000,500,100,50,10,5,1]
    roman = ['M','D','C','L','X','V','I']
    result = ''

    if num_arabe > 5999:
        print("nombre trop grand")
    elif(num_arabe < 0):
        print("nombre négatif")
    else:
        while num_arabe >= arabe[0]:
            result = result + roman[0]
            num_arabe = num_arabe - arabe[0]
        while num_arabe >= arabe[1]:
            result = result + roman[1]
            num_arabe = num_arabe - arabe[1]
        while num_arabe >= arabe[2]:
            result = result + roman[2]
            num_arabe = num_arabe - arabe[2]

        print(result)
