def splitter(type, txt):
    output = ''
    split = 0

    match type:
        case 'M':
            for i in range(1, len(txt)):
                char = txt[i]
                if char.isupper():
                    output += txt[:i].lower() + ' '
                    split = i
                if not char.isalpha():
                    output += txt[split:i].lower()
                    break
        case 'C':
            for i in range(1, len(txt)):
                char = txt[i]
                if char.isupper():
                    output += txt[:i].lower() + ' '
                    split = i
                if not char.isalpha():
                    output += txt[split:i].lower()
                    break
        case 'V':
            for i in range(1, len(txt)):
                char = txt[i]
                if char.isupper():
                    output += txt[:i].lower() + ' '
                    split = i
                if not char.isalpha():
                    output += txt[split:i].lower()
                    break


    return output


def combiner(type, txt):
    output = ''
    split = 0

    match type:
        case 'M':
            for i in range(1, len(txt)):
                char = txt[i]
                if char.isupper():
                    output += txt[:i].lower() + ' '
                    split = i
                if not char.isalpha():
                    output += txt[split:i].lower()
                    break
        case 'C':
            for i in range(1, len(txt)):
                char = txt[i]
                if char.isupper():
                    output += txt[:i].lower() + ' '
                    split = i
                if not char.isalpha():
                    output += txt[split:i].lower()
                    break
        case 'V':
            for i in range(1, len(txt)):
                char = txt[i]
                if char.isupper():
                    output += txt[:i].lower() + ' '
                    split = i
                if not char.isalpha():
                    output += txt[split:i].lower()
                    break


    return output


def camel_case(txt_in):
    split_txt = txt_in.split(';')
    op = split_txt[0]
    type = split_txt[1]
    txt = split_txt[2]

    match op:
        case 'S':
            return splitter(type, txt)
        case 'C':
            combiner(type, txt)



txt_in = 'S;M;plasticCup()'
print(camel_case(txt_in))
