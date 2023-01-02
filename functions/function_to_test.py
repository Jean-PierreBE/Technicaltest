def parse_to_roman(num_arabe):
    arabe = [1000,500,100,50,10,5,1]
    roman = ['M','D','C','L','X','V','I']
    result = ''

    if num_arabe > 5999:
        print("nombre trop grand")
    elif(num_arabe < 0):
        print("nombre négatif")
    else:
        ind = 0
        while num_arabe >= arabe[0]:
            result[ind] = roman[0]
            ind += 1
            num_arabe = num_arabe - arabe[0]
        print(result)
