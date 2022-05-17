# def combiner(op, text):
#     match op:
#         case 'M':
#
#         case 'C':
#
#         case 'V':


def spliter(op, text):
    match op:
        case 'M':
            print(text)
        # case 'C':
        #
        # case 'V':



def camel_case(text_in):
    str_list = text_in.split(';')
    op1 = str_list[0]
    op2 = str_list[1]
    text = str_list[2]

    match op1:
        case 'S':
            spliter(op2, text)
        case 'C':
            # combiner(op2, text)



text_in = 'S;M;plasticCup()'
print(camel_case(text_in))
