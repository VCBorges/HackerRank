import textwrap

def wrap(string,max_width):
    a = textwrap.wrap(string,max_width)
    for i in a:
        print(i)
    return ('')

if __name__ == '__main__':
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)