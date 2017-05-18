import random
class StrTrie:
    def __newnode(self, s):
        self.ns.append({})
        self.cnt.append(1)
        self.tot += 1
        return self.tot - 1

    def __init__(self):
        self.tot = 0
        self.ns = []
        self.cnt = []
        self.root = self.__newnode('');
    
    def insert(self, prefix):
        assert(isinstance(prefix, list))
        p = self.root
        for i in prefix:
            if i not in self.ns[p]:
                self.ns[p][i] = self.__newnode(i)
                p = self.ns[p][i]
            else:
                p = self.ns[p][i]
                self.cnt[p] += 1
        return p
    '''\'cause the prefix has indicated the length of markov predication length, the predication depth k is not defined'''
    def getkth(self, prefix):
        assert(isinstance(prefix, list))
        p = self.root
        for i in prefix:
            p = self.ns[p][i]
            
        range_of_nex = sum(self.cnt[v] for v in self.ns[p].values())
        tar_index = random.randint(0, range_of_nex - 1)
        for v in self.ns[p].items():
            if tar_index < self.cnt[v[1]]:
                return v[0]
            tar_index -= self.cnt[v[1]]
        

class MarkovText:
    maxk =0
    def __init__(self):
        self.qwrapped = StrTrie()
        self.bwrapped = StrTrie()
        self.xbwrapped = StrTrie()
        self.plain = StrTrie()
        self.f = ''
        self.p = 0
        self.flen = 0
    def __quote_wrapped_ins(self, quote, k):
        pp = 0
        quote = quote.replace('\n"', ' ')
        lenpp = len(quote) - 1
        lister = []
        while pp < lenpp:
            while quote[pp] == '\n':
                pp += 1
            if quote[pp].isalnum():
                spp = pp
                while pp < lenpp and quote[pp].isalnum():
                    pp += 1
                lister.append(quote[spp: pp])
            else:
                spp = pp
                while pp < lenpp and not quote[pp].isalnum():
                    pp += 1
                lister.append(quote[spp: pp])
        lister.append('"')
        lilen = len(lister)
        for i in range(lilen - k):
            self.qwrapped.insert(lister[i: i + k])
        for i in range(lilen - k, lilen - 1):
            self.qwrapped.insert(lister[i:])
    def __bracket_wrapped_ins(self, quote, k):
        pp = 0
        lenpp = len(quote) - 1
        lister = []
        while pp < lenpp:
            while quote[pp] == '\n':
                pp += 1
            if quote[pp].isalnum():
                spp = pp
                while pp < lenpp and quote[pp].isalnum():
                    pp += 1
                lister.append(quote[spp: pp])
            else:
                spp = pp
                while pp < lenpp and not quote[pp].isalnum():
                    pp += 1
                lister.append(quote[spp: pp])
        lister.append(')')
        lilen = len(lister)
        for i in range(lilen - k):
            self.bwrapped.insert(lister[i: i - k])
        for i in range(lilen - k, lilen - 1):
            self.bwrapped.insert(lister[i:])
    def __xbrack_wrapped_ins(self, quote, k):
        pp = 0
        lenpp = len(quote) - 1
        lister = []
        while pp < lenpp:
            while quote[pp] == '\n':
                pp += 1
            if quote[pp].isalnum():
                spp = pp
                while pp < lenpp and quote[pp].isalnum():
                    pp += 1
                lister.append(quote[spp: pp])
            else:
                spp = pp
                while pp < lenpp and not quote[pp].isalnum():
                    pp += 1
                lister.append(quote[spp: pp])
        lister.append(']')
        lilen = len(lister)
        for i in range(lilen - k):
            self.xbwrapped.insert(lister[i: i + k])
        for i in range(lilen - k, lilen - 1):
            self.xbwrapped.insert(lister[i:])
    def __next_word(self, k):
        if (self.f[self.p] == '\n'):
            while self.p < self.flen and self.f[self.p] == '\n':
                self.p += 1
            return ' '
        if self.f[self.p].isalnum():
            sp = self.p
            while self.p < self.flen and self.f[self.p].isalnum():
                self.p += 1
            return self.f[sp:self.p]
        if self.f[self.p] == ' ':
            sp = self.p
            while self.p < self.flen and self.f[self.p] == ' ':
                self.p += 1
            return ' '
            return self.f[sp: self.p]
        if self.f[self.p] == '"':
            self.p += 1
            sp = self.p
            while not (self.f[self.p] == '"' and self.f[self.p - 1] != '\n'):
                self.p += 1
            self.p += 1
            self.__quote_wrapped_ins(self.f[sp:self.p], k)
            return '"'
        if self.f[self.p] == '(':
            self.p += 1
            sp = self.p
            while self.f[self.p] != ')':
                self.p += 1
            self.p += 1
            self.__bracket_wrapped_ins(self.f[sp: self.p], k)
            return '('
        if self.f[self.p] == '[':
            self.p += 1
            sp = self.p
            while self.f[self.p] != ']':
                self.p += 1
            self.p += 1
            self.__xbrack_wrapped_ins(self.f[sp: self.p], k)
            return '['
        self.p += 1
        return self.f[self.p - 1]
        sp = self.p
        while self.p < self.flen and not self.f[self.p].isalnum():
            self.p += 1
        return self.f[sp: self.p]
    def __gen_q_wrapped(self, k):
        Q = []
        for i in range(k):
            try:
                to_append = self.qwrapped.getkth(Q)
            except KeyError:
                to_append = self.qwrapped.getkth([])
            if to_append == '"':
                return ''.join(Q)
            Q.append(to_append)
        while True:
            to_append = self.qwrapped.getkth(Q[len(Q) - k:])
            if to_append == '"':
                return ''.join(Q)
            Q.append(to_append)

    def __gen_b_wrapped(self, k):
        Q = []
        for i in range(k):
            to_append = self.bwrapped.getkth(Q)
            if to_append == ')':
                return ''.join(Q)
            Q.append(to_append)
        while True:
            try:
                to_append = self.bwrapped.getkth(Q[len(Q) - k:])
            except KeyError:
                to_append = self.bwrapped.getkth([])
            if to_append == ')':
                return ''.join(Q)
            Q.append(to_append)
    def __gen_xb_wrapped(self, k):
        Q = []
        for i in range(k):
            to_append = self.xbwrapped.getkth(Q)
            if to_append == ']':
                return ''.join(Q)
            Q.append(to_append)
        while True:
            try:
                to_append = self.xbwrapped.getkth(Q[len(Q) - k:])
            except KeyError:
                to_append = self.xbwrapped.getkth([])
            if to_append == ']':
                return ''.join(Q)
            Q.append(to_append)
    def Build(self, txtpath):
        assert(isinstance(txtpath, str))
        self.f = open(txtpath).read()
        self.p = 0
        self.flen = len(self.f)
        lister = []
        while(self.p < self.flen):
            wd = self.__next_word(MarkovText.maxk)
            lister.append(wd)
        lislen = len(lister)
        #maxk = MarkovText.maxk
        for i in range(lislen - MarkovText.maxk):
            self.plain.insert(lister[i: i + MarkovText.maxk])
    def Write(self, k, n):
        Q = []
        for i in range(k):
            Q.append(self.plain.getkth(Q))
        while n:
            try:
                tmp = self.plain.getkth(Q[len(Q) - k:])
            except KeyError:
                tmp = self.plain.getkth([])
            if tmp in '.?!':
                n -= 1
            Q.append(tmp)

        for i, ss in enumerate(Q):
            if ss == '"':
                Q[i] = '"' + self.__gen_q_wrapped(k) + '"'
            elif ss == '[':
                Q[i] = '[' + self.__gen_xb_wrapped(k) + ']'
            elif ss == '(':
                Q[i] = '(' + self.__gen_b_wrapped(k) + ')'
        for i, ss in enumerate(Q):
            if ss[0].isalpha():
                Q[i] = ss[0].upper() + ss[1:]
                break
        return ''.join(Q)

