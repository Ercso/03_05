
with open('./teszt.txt', 'r', encoding='utf-8') as forrasfajl, \
    open('./teszt_masolata.txt', 'w', encoding='utf-8') as celfajl:
    for sor in forrasfajl:
        print(sor.strip(), file=celfajl)