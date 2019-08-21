def is_pangram(sentence):
    sent = sentence.lower()

    # alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # comp_sent = []

    # for i in range(len(sent)):
    #     if sent[i].isalpha() and sent[i] not in comp_sent:
    #       comp_sent.append(sent[i])

    # comp_sent.sort()
    # return alph == comp_sent

    letters = set()

    for i in range(len(sent)):
        if sent[i].isalpha() and sent[i] not in letters:
            letters.add(sent[i])

    return len(letters) == 26

    #set() == []
    #list ordered, set is not.