'''Дан файл. Определите сколько в нем букв (латинского алфавита), слов, строк.
Выведите три найденных числа в формате, приведенном в примере.
'''
with open("input.txt", "r") as f:
    ALL = list()
    for line in f.readlines():
        if line[0] == "\n":
            continue
        L = list(line.strip('.\n').split())
        ALL.append(L)
    count_words = 0
    count_letters = 0
    for line in ALL:
        count_words += len(line)
        for word in line:
            count_letters += len(word)
    print(count_letters, "letters")
    print(count_words, "words")
    print(len(ALL), "lines")
