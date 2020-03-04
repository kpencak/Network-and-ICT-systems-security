tekst = "P?A S?YV% +?XV?+NE L+NZK M%$%?SZ?WQYNE+$N $TQ PQLY VE?SQ WQ+HTQE+$N H%$TQV?+ +RK?R+? E/?K?AYQKNLYNAQ PQ+NA%V? YQALYX +?L+NZK%V?$Q*%"
alfabet = "$%*+/?ABCDEFGHIJKLMNOPRSTUVWXYZ"

def litera(i):
    switch={'?':'A', 'M':'M', '%':'O', '$':'N', 'S':'L', 'Z':'F', 'W':'B', 'Q':'E', 'Y':'T', 'N':'Y', 'E':'C', '+':'Z', 'T':'I', ' ':' ', 'V':'W', 'X':'U', 'L':'S', 'K':'R', '*':'G', 'P':'J', 'A':'K', 'H':'P', '/':'H', 'R':'D'} 
    if(i in switch):
        return switch.get(i)
    else:
        return 'xxxxxxxxxxxxxxxxx'

haslo = [None]*len(tekst)
for i in tekst:
    print(litera(i))
