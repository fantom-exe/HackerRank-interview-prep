# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


def splitter(txt_type, txt):
    txt_len = len(txt)
    split = 0
    output = ''

    if txt_type == 'M':
        for i in range(1, txt_len):
            char = txt[i]
            if char.isupper():
                output += txt[:i] + ' '
                split = i
            elif not char.isalpha():
                output += txt[split:i]
                break
    elif txt_type in ['C', 'V']:
        for i in range(1, txt_len):
            char = txt[i]
            if char.isupper():
                output += txt[split:i] + ' '
                split = i
            elif i == txt_len - 1:
                output += txt[split:txt_len]

    print(output.lower())


def combiner(txt_type, txt):
    words = txt.split(' ')
    num_of_words = len(words)
    output = ''

    if txt_type == 'M':
        output += words[0]
        for i in range(1, num_of_words):
            output += words[i][0].upper() + words[i][1:]

        print(output + '()')
    elif txt_type == 'C':
        for i in range(0, num_of_words):
            output += words[i][0].upper() + words[i][1:]

        print(output)
    elif txt_type == 'V':
        output += words[0]
        for i in range(1, num_of_words):
            output += words[i][0].upper() + words[i][1:]

        print(output)


def camel_case(txt_in):
    split_txt = txt_in.split(';')
    op = split_txt[0]
    txt_type = split_txt[1]
    txt = split_txt[2]

    if op == 'S':
        splitter(txt_type, txt)
    elif op == 'C':
        combiner(txt_type, txt)


if __name__ == '__main__':
    # Read input lines and remove '\n' and '\r' characters to avoid bugs
    inputData = [line.rstrip('\n\r') for line in sys.stdin.readlines()]

    for txt_in in inputData:
        camel_case(txt_in)

