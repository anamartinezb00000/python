import random

def display_map(M,d):
    m=len(M[0])
    n=len(M)
    for x in range(n):
        for y in range(m):
            if M[x][y]==0:
                print(d[0],end="")
            if M[x][y]==1:
                print(d[1],end="")
        print('')
    return ''

"""M=[[0,0,0,1,1],
   [0,0,0,0,1],
   [1,1,0,0,0],
   [0,0,0,0,0]]"""
d={0:' ',1:'#'}


def create_perso(c,a):
    x=c[0]
    y=c[1]
    d={'char':a,'x':x,'y':y,'score':0}
    return d

def display_map_and_char(M,d,p):
    m=len(M[0])
    n=len(M)
    a=p['x']
    b=p['y']
    for x in range(n):
        for y in range(m):
            if b==x and a==y:
                print(p['char'],end="")
            elif M[x][y]==0:
                print(d[0],end="")
            elif M[x][y]==1:
                print(d[1],end="")
        print('')
    return ''



def update(letter,M,p):
    m=len(M)
    n=len(M[0])
    possibilités=['s','z','q','d','E']
    if letter not in possibilités:
        print("Reessayez avec une lettre parmis s,z,q,d et E")
    else :
        if letter=='s' and p['y']<m-1 and M[p['y']+1][p['x']]!=1:
            p['y']+=1
            
        if letter =='z' and M[p['y']-1][p['x']]!=1:
            if p['y']!=0:
                p['y']-=1
                
        if letter=='d' and p['x']<n-1 and M[p['y']][p['x']+1]!=1:
            p['x']+=1
        
        if letter=='q' and M[p['y']][p['x']-1]!=1:
            if p['x']!=0:
                p['x']-=1
        if letter=='E':
            pos= (p['x'],p['y'])
            delete_all_walls(M,pos)
    return ''


    
def create_objects(nb_objects,M):
    d=set()
    v=0
    n=len(M)
    m=len(M[0])
    for i in range(nb_objects):
        while v!=nb_objects:
            y=random.randint(0,n-1)
            x=random.randint(1,m-1)
            if M[y][x]==0 :
                    v+=1
                    d.add((x,y))
    return d

def display_map_and_char_and_objects(M,d,p,objects):
    m=len(M[0])
    n=len(M)
    a=p['x']
    b=p['y']
    for x in range(n):
        for y in range(m):
            if b==x and a==y:
                print(p['char'],end="")
            elif M[x][y]==3:
                print('X',end="")
            elif (y,x) in objects:
                if M[x][y]==1 or M[x][y]==4:
                    M[x][y]=0
                print('.',end="")
            elif M[x][y]==0:
                print(d[0],end="")
            elif M[x][y]==1:
                print(d[1],end="")
            elif M[x][y]==4:
                print("O", end="")
        print('')
    return ''


    
def update_objects(p,objects):
    a=p['x']
    b=p['y']
    objects2=objects.copy()
    for i in objects2:
        if (a,b)==i:
            objects.remove(i)
            p['score']+=1
    return objects

#géneration d'une nouvelle matrice   
def generate_random_map(size_map,proportion_wall):
    n=size_map[0]
    m=size_map[1]
    taille=n*m
    M=[[0]*n for i in range(m)]
    v=0
    murs=proportion_wall*taille
    murs=int(murs)
    sortie=0
    troue=0
    troues=random.randint(0,5)
    while v!=murs:
        y=random.randint(2,n-1)
        x=random.randint(1,m-1)
        if M[x][y]!=1:
            M[x][y]=1
            v+=1
    
    while sortie!=3:
        y=random.randint(2,n-1)
        x=random.randint(1,m-1)
        if M[x][y]==0:
            M[x][y]=3
            sortie+=3
    
    while troue!=troues:
        y=random.randint(2,n-1)
        x=random.randint(1,m-1)
        if M[x][y]==0:
            M[x][y]=4
            troue+=1
    
    return M

#géneration d'une nouvelle map
def create_new_level(p,M,objects,size_map,proportion_wall):
    size_map[0]+=1
    size_map[1]+=1
    global m
    m=generate_random_map(size_map, proportion_wall)
    global obj
    global nbobjets
    nbobjets=random.randint(0,7)
    obj=create_objects(nbobjets, M)
    global perso
    perso=create_perso((0,0),apparence)
    return ""

#supprime les murs  
def delete_all_walls(M,pos):
    x,y= pos
    valeursupx=max(0,x-1)
    valeurinfx=min(len(M[0]),x+2)
    valeursupy=max(0,y-1)
    valeurinfy=min(len(M),y+2)
    for i in range(valeursupy,valeurinfy):
        for j in range(valeursupx,valeurinfx):
            if M[i][j]==1:
                M[i][j] = 0
    return M
     
 
     
size=[7,4]
proportion=0.3
m=generate_random_map(size,proportion)
nbobjets=random.randint(0,4)
obj=create_objects(nbobjets,m)
niveau=0
print("Bonjour, bienvenue dans un mini jeu d'arcade, \nl'objectif etant de passer le plus de niveau possible. \nVoici les commandes :  entrer s pour se déplacer vers le bas, z pour se déplacer vers le haut, d pour se déplacer vers la droite, et q pour se déplacer vers la gauche. \nAttention aux troues !!")
apparence=input("Choisissez l'apparence de votre joueur :")
while type(apparence)!=str:
    apparence=input("réessayez avec une lettre de l'alphabet :")
perso=create_perso((0,0),apparence)
print(display_map_and_char_and_objects(m,d,perso,obj))
 
while True :
    lettre=input("Quel déplacement souhaitez vous effectuer ? :")
    update(lettre,m,perso)
    update_objects(perso, obj)
    if m[perso['y']][perso['x']]==3:
        create_new_level(perso,m,obj,size,proportion)
        niveau+=1
    if m[perso['y']][perso['x']]==4:
        print("GAME OVER :( try again...")
        break
    if niveau==5:
        print("VOUS AVEZ GAGNEEE!!")
        break
    print(display_map_and_char_and_objects(m,d,perso,obj))
    print('le score du joeur est de :',perso['score']," sur ", nbobjets)
    print('Vous avez atteint le niveau :', niveau)

