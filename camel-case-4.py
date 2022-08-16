def splitter(type, txt):
    txt_len = len(txt)
    split = 0
    output = ''

    match type:
        case 'M':
            for i in range(1, txt_len):
                char = txt[i]
                if char.isupper():
                    output += txt[:i] + ' '
                    split = i
                elif not char.isalpha():
                    output += txt[split:i]
                    break

        case 'C' | 'V':
            for i in range(2, txt_len):
                char = txt[i]
                if char.isupper():
                    output += txt[split:i] + ' '
                    split = i
                elif i == txt_len - 1:
                    output += txt[split:txt_len]


    print(output.lower())


def combiner(type, txt):
    txt_len = len(txt)
    split = 0
    output = ''

    match type:
        case 'M':
            for i in range(1, txt_len):
                char = txt[i]
                if char.isupper():
                    output += txt[:i] + ' '
                    split = i
                if not char.isalpha():
                    output += txt[split:i]
                    break
        case 'C':
            for i in range(1, txt_len):
                char = txt[i]
                if char.isupper():
                    output += txt[:i] + ' '
                    split = i
                if not char.isalpha():
                    output += txt[split:i]
                    break
        case 'V':
            for i in range(1, txt_len):
                char = txt[i]
                if char.isupper():
                    output += txt[:i] + ' '
                    split = i
                if not char.isalpha():
                    output += txt[split:i]
                    break

    print(output)


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
camel_case(txt_in)
txt_in = 'S;C;LargeSoftwareBook'
camel_case(txt_in)
txt_in = 'S;V;pictureFrame'
camel_case(txt_in)
txt_in = 'C;V;mobile phone'
camel_case(txt_in)
txt_in = 'C;C;coffee machine'
camel_case(txt_in)
txt_in = 'C;M;white sheet of paper'
camel_case(txt_in)

