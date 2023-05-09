#ama=1 azu=2 rojo=3 verde=4
def son_listas_diferentes(lista1, lista2):
    for i in range(len(lista1)):
        if lista1[i] == lista2[i]:
            return False
    return True
def es_lista_diferente_de_todas(lista, lista_de_listas):
    for otra_lista in lista_de_listas:
        if not son_listas_diferentes(lista, otra_lista):
            return False
    return True


comb_c1=[(1,1,2,3),(1,4,2,3),(1,4,3,3),
         (3,1,1,2),(3,1,4,2),(3,1,4,3),
         (2,3,1,1),(2,3,1,4),(3,3,1,4),
         (1,2,3,1),(4,2,3,1),(4,3,3,1)]

comb_c2=[(1,4,4,3),(1,2,4,3),(4,2,3,3),
         (3,1,4,4),(3,1,2,4),(3,4,2,3),
         (4,3,1,4),(4,3,1,2),(3,3,4,2),
         (4,4,3,1),(2,4,3,1),(2,3,3,4)]

comb_c3=[(2,2,1,3),(2,4,1,4),(2,4,3,4),
         (3,2,2,1),(4,2,4,1),(4,2,4,3),
         (1,3,2,2),(1,4,2,4),(3,4,2,4),
         (2,1,3,2),(4,1,4,2),(4,3,4,2)]

comb_c4=[(1,1,2,3),(1,4,2,3),(2,4,3,1),
         (3,1,1,2),(3,1,4,2),(1,2,4,3),
         (2,3,1,1),(2,3,1,4),(3,1,2,4),
         (1,2,3,1),(4,2,3,1),(4,3,1,2)]

q=12
o=0
u=0
for i in range(q):
    for j in range(q):
        for k in range(q):
            for l in range(q):
                u+=1
                if es_lista_diferente_de_todas(comb_c1[i], [comb_c2[j], comb_c3[k], comb_c4[l]]) and \
                   es_lista_diferente_de_todas(comb_c2[j], [comb_c3[k], comb_c4[l]]) and \
                   es_lista_diferente_de_todas(comb_c3[k], [comb_c4[l]]):
                    #comb_c1[i][0] != comb_c2[j][0] and comb_c1[i][0] != comb_c3[k][0] and comb_c1[i][0] != comb_c4[l][0] and \
                    #comb_c1[i][1] != comb_c2[j][1] and comb_c1[i][1] != comb_c3[k][1] and comb_c1[i][1] != comb_c4[l][1] and \
                    #comb_c1[i][2] != comb_c2[j][2] and comb_c1[i][2] != comb_c3[k][2] and comb_c1[i][2] != comb_c4[l][2] and \
                    #comb_c1[i][3] != comb_c2[j][3] and comb_c1[i][3] != comb_c3[k][3] and comb_c1[i][3] != comb_c4[l][3] and \
                    #comb_c2[j][0] != comb_c3[k][0] and comb_c2[j][0] != comb_c4[l][0] and\
                    #comb_c2[j][1] != comb_c3[k][1] and comb_c2[j][1] != comb_c4[l][1] and\
                    #comb_c2[j][2] != comb_c3[k][2] and comb_c2[j][2] != comb_c4[l][2] and\
                    #comb_c2[j][3] != comb_c3[k][3] and comb_c2[j][3] != comb_c4[l][3] and\
                    #comb_c3[k][0] != comb_c4[l][0] and\
                    #comb_c3[k][1] != comb_c4[l][1] and\
                    #comb_c3[k][2] != comb_c4[l][2] and\
                    #comb_c3[k][3] != comb_c4[l][3]  :#and\

                    
                    #comb_c1[i][0] != comb_c2[j][1] and comb_c1[i][0] != comb_c3[k][2] and comb_c1[i][0] != comb_c4[l][3] and\
                    #comb_c2[j][1] != comb_c3[k][2] and comb_c2[j][1] != comb_c4[l][3] and\
                    #comb_c3[k][2] != comb_c4[l][3]:
                    
                    
                    
                    print(comb_c1[i][0],comb_c2[j][0],comb_c3[k][0],comb_c4[l][0],comb_c1[i][0]+comb_c2[j][0]+comb_c3[k][0]+comb_c4[l][0])
                    print(comb_c1[i][1],comb_c2[j][1],comb_c3[k][1],comb_c4[l][1],comb_c1[i][1]+comb_c2[j][1]+comb_c3[k][1]+comb_c4[l][1])
                    print(comb_c1[i][2],comb_c2[j][2],comb_c3[k][2],comb_c4[l][2],comb_c1[i][2]+comb_c2[j][2]+comb_c3[k][2]+comb_c4[l][2])
                    print(comb_c1[i][3],comb_c2[j][3],comb_c3[k][3],comb_c4[l][3],comb_c1[i][3]+comb_c2[j][3]+comb_c3[k][3]+comb_c4[l][3])
                    o+=1
                    print(comb_c1[i])
                    print(comb_c2[j])
                    print(comb_c3[k])
                    print(comb_c4[l])
                    print('------------------')
print(o)
print(u)


