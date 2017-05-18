
import markov


if __name__ == '__main__':
    m = markov.MarkovText()
    Tpath = r"C:\spring17\EXP4\emma.txt"#r"C:\spring17\EXP4\emma.txt"
    k = 5
    n = 10
    markov.MarkovText.maxk = k + 1
    m.Build(Tpath)
    #m.Build(r"C:\spring17\EXP4\emma.txt")
    print(m.Write(k, n))
