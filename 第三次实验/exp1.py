def make_table():
    for i in range(11):
        if i%5==0:
            print('+','—'*3,'+','—'*3,'+')
            #print('+————+————+')
        else:
            print('|',' '*3,'|',' '*3,'|')
make_table()