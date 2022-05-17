# def combiner(op, text):
#     match op:
#         case 'M':
#
#         case 'C':
#
#         case 'V':


def splitter(op, text):
    text_list = []
    match op:
        case 'M' | 'V':
            for i in range(1, len(text)):
                char = text[i]
                if char.isupper():
                    text_list = text[:i]
                elif not char.isalpha():
                    break
        # case 'C':
        #

    print(text_list)


def camel_case(text_in):
    str_list = text_in.split(';')
    op1 = str_list[0]
    op2 = str_list[1]
    text = str_list[2]

    match op1:
        case 'S':
            splitter(op2, text)
        # case 'C':
            # combiner(op2, text)



text_in = 'S;M;plasticCup()'
print(camel_case(text_in))
