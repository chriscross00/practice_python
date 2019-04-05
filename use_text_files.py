file = open('test_text.txt', 'a')

def read_out(file):

    if file.mode == 'r':
        contents = file.read()
        print(contents)
    file.close()
    print('Done!')

read_out(file)