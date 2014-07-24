import re
def checkio(text):
    k = g = s = 0
    text = text.lower()
    text = re.split('[., ]+', text)
    gl = list('aeiouy')
    for tx in text:
        if len(tx) <= 1:
            continue
        if tx.isalpha():
            i=g=s=0
            tx=list(tx)
            for pr in tx:
                i=i+1
                if pr in gl:
                    s=0
                    g=g+1
                    if g>1:
                        break
                else:
                    g=0
                    s=s+1
                    if s>1: break 
                    
            else:
                k=k+1
    
    
    
    return k

print(checkio("A quantity of striped words."))