def parse_to_roman(num_arabe):
    arabe = [1000,500,100,50,10,5,1]
    roman = ['M','D','C','L','X','V','I']
    result = ''

    if num_arabe > 5999:
        print("nombre trop grand")
    elif(num_arabe <= 0):
        print("nombre négatif")
    else:
        for ind in range(len(arabe)):
            while num_arabe >= arabe[ind]:
                result = result + roman[ind]
                num_arabe = num_arabe - arabe[ind]

        print(result)
