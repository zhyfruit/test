def n_markov(n, seq):
    """
    对输入序列做n阶马尔科夫分析
    """
    m_map = {}
    for i in range(len(seq) - n):
        preset = tuple(word for word in seq[i:i + n])
        if preset not in m_map:
            m_map[preset] = [seq[i + n]]
        else:
            m_map[preset].append(seq[i + n])
    return m_map


def genarate_sentence(m_map, n, m):
    """
    根据马尔科夫分析结果生成n句
    """
    import random
    result = [[] for i in range(n)]
    i = 0
    while i != n:
        if len(result[i]) == 0:
            first = random.choice(list(m_map.keys()))
            while not first[0].istitle() or not first[0].isalpha():
                first = random.choice(list(m_map.keys()))
            result[i].extend(first)
        else:
            last = tuple(result[i][-m:])
            if last[-1] in '.?!':
                i += 1
            else:
                if len(result[i]) >= 50:
                    result[i].append('.')
                    i += 1
                else:
                    if last in m_map:
                        t = random.choice(m_map[last])
                        result[i].append(t)
                        if t in '.?!':
                            i += 1
                    else:
                        result[i].extend(random.choice(list(m_map.keys())))
    return result


def read_text(fin, word_list):
    """
    读取文本，分割文本生成单词字符列表
    """
    for line in fin:
        words = []
        word = ''
        for i in range(len(line)):
            alpha = line[i]
            if alpha.isalpha():
                word += alpha
            else:
                if word != '':
                    if alpha == '.':
                        if line[i - 2] == 'M' or line[i - 3] == 'M':
                            word += '.'
                            continue
                        else:
                            words.append(word)
                            word = ''
                            words.append(alpha)
                    elif alpha in ',?\"!':
                        words.append(word)
                        word = ''
                        words.append(alpha)
                    elif alpha == ' ':
                        words.append(word)
                        word = ''
                    elif alpha == '-' and line[i + 1] == '-':
                        words.append(word)
                        word = ''
                        words.append('--')
                    elif alpha == '\'' and i != 0:
                        if line[i - 1] == 's':
                            word += '\''
                        elif line[i + 1] == 's':
                            word += '\''
                        else:
                            words.append(word)
                            words.append(alpha)
                            word = ''
        word_list.extend(words)


if __name__ == '__main__':
    fin = open('emma.txt')
    word_list = []
    read_text(fin, word_list)

    n = 2
    m_map = n_markov(n, word_list)
    result = genarate_sentence(m_map, 5, n)

    for sentence in result:
        for word in sentence:
            if word in ',.?!\"':
                print(word, end="")
            else:
                print(' ' + word, end="")
        print()
        print()
