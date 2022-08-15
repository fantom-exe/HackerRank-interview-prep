def splitter(type, txt):
    text_list = []

    match type:
        case 'M' | 'V':
            for i in range(1, len(txt)):
                char = txt[i]
                if char.isupper():
                    text_list = txt[:i]
                elif not char.isalpha():
                    break
        # case 'C':
        #

    print(text_list)


def combiner(type, txt):
    text_list = []

    match type:
        case 'M':

        case 'C':

        case 'V':



    print(text_list)


def camel_case(txt_in):
    split_txt = txt_in.split(';')
    op = split_txt[0]
    type = split_txt[1]
    txt = split_txt[2]

    match op:
        case 'S':
            splitter(type, txt)
        case 'C':
            combiner(type, txt)



txt_in = 'S;M;plasticCup()'
print(camel_case(txt_in))
