import time
def init_word_list():
    r = open('words.txt')
    word_list = [line.strip() for line in r.readlines()]
    return word_list

def init_word_set(word_list):
    words = set(word_list)
    return words

def init_shortable(shortable, word_list):
    # for word in word_list:
    #     shortable[word] = 
    shortable['a'] = ''
    shortable['i'] = ''

def recursive_find(word):
    if word in shortable:
        return shortable[word] != False
    for i in range(0, len(word)):
        temp = word[:i] + word[i+1:]
        if temp in words_set:
            if recursive_find(temp):
                # shortable[word] = True
                shortable[word] = temp
                return True
    else:
        shortable[word] = False
        return False

def find():
    longest = ''
    for word in words_set:
        if recursive_find(word):
            # word_path[word].append(word)
            longest = word if len(word) > len(longest) else longest
    return longest

def print_path(word):
    temp = word
    while(len(temp) != 1):
        print(temp, end='->')
        temp = shortable[temp]
    print(temp)

if __name__ == '__main__':
    shortable = {}
    words_list = init_word_list()
    words_set = init_word_set(words_list)
    init_shortable(shortable,words_list)
    start = time.time()
    result = find()
    end = time.time() - start
    print(end)
    print(result)
    print_path(result)
    pass
# print_path(longest)
# print_path('is')
