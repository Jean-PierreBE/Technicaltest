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

def rot_text(text, sens, iter):
    alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    trans_text = ''
    for ind in range(len(text)):
        if text[ind] != ' ':
            value_index = alph.index(text[ind])
            if sens == 'C':
                value_sel = value_index + iter
                if value_sel > len(alph) - 1:
                    value_sel = value_sel - len(alph)
            elif(sens == 'D'):
                value_sel = value_index - iter
                if value_sel < 0:
                    value_sel = value_sel + len(alph)
            trans_text = trans_text + alph[value_sel]
        else:
            trans_text = trans_text + ' '

    return trans_text

def binary_gap(number):

    bin_num = "{0:b}".format(number)
    print(bin_num)
    num_zero = []
    num = 0
    for char in bin_num:
        if char == '0':
                num += 1
        elif(char == '1'):
            if num > 0:
                num_zero.append(num)
                num = 0
    print(num_zero)
    if len(num_zero) < 1:
        return 0
    else:
        return max(num_zero)