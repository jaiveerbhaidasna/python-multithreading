import multiprocessing as mp    

def main():
    dict = {}
    word = ""
    prev_word = ""
    with open('test.txt', mode='r') as f:
        contents = f.read()

    for i in range(len(contents)):
        if contents[i] == " ":
            if word in dict.keys():
                if prev_word in dict[word].keys():
                    dict[word][prev_word] += 1
                else:
                    dict[word][prev_word] = 1
            else:
                dict[word] = {}
            prev_word = word
            word = ""
        else:
            word = word + contents[i]

    print(dict)

if __name__ == "__main__":
    main()

