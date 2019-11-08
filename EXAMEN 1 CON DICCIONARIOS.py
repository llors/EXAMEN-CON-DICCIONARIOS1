# PROCESO DE VOTACION VASICO
n=0
m=0
p=0
x=1
while x!=4:
    print("###############################")
    print("+          votacion           +")
    print("+#############################+")
    print("+   1. ver candidato          +")
    print("+   2. registrar voto         +")
    print("+   3. flash informativo      +")
    print("+   4. salir                  +")
    print("+##############################+")
    s = int(input("ingrese la opcion deseada:"))
    a = {1: "ver candidato", 2: "registrar votos",
         3: "flash informativo", 4: "salir"}
    for k, a in a.items():
        print("+", k, a)
    if s==1:
         print("###############################")
         print("ver candidato")
         print("###############################")
         print("+ 1. luis esperanaza          +")
         print("+ 2. jose barata              +")
         print("+ 3. marco ocram              +")
         print("+==========================================+")
         input("presione enter para volver al menu principal")
         d = {1: "luis esperanza", 2: "jose barata", 3: "marco ocram"}
         for k, d in d.items():
             print("+", k, d)
    if s == 2:
         print("registre su voto")
         y = int(input("ingrese el numero del candidato deseado:"))
         if y >= 1 and y <= 3:
            if y == 1:
                n=n+1
            if y == 2:
                m=m+1
            if y == 3:
                p=p + 1
            t=p+m+n
         else:
               print("error: la opcion no es coorrecta")
         input("su voto se registro correctamente/ presione enter para volver al menu")
    if s == 3:
        print("+=========================+")
        print("flash informativo")
        print("+=========================+")
        print("+ # candidato       votos +")
        print("+luis esperanza      ",n,"+")
        print("+jose baratra       ",m, "+")
        print("+marco ocram        ",p, "+")
        print("+=========================+")
        print("+total de votos:     ",t,"+")
        print("+=========================+")
        input("PULSE ENTER PARA VOLVER AL MENU PRINCIPAL:")

    if s == 4:
        print("+=========================+")
        print("+        GANADOR          +")
        print("+=========================+")
        if n>=m and n>=p:
            z = []
            for i in range(7):
                z.append(["*"]*6)
            print("+      ", z[0][0])
            print("+      ", z[1][0])
            print("+      ", z[2][0])
            print("+      ", z[3][0])
            print("+      ", z[4][0])
            print("+      ", z[5][0])
            print("+      ", z[6][0],z[6][1],z[6][2],z[6][3],z[6][4])
            print("+===============================================+")
            print("luis esperanza:",w,"vts")
            print("+===============================================+")
            break
    if m >= n and m >= p:
                    i=[]
    for f in range(7):
                    i.append(["*"]*6)
                    print("+========================+")
                    print("+        GANADOR         +")
                    print("+========================+")
                    print(i[0][1], i[0][2], i[0][3], i[0][4], i[0][5])
                    print(i[0][1],"   ", i[1][3])
                    print(i[2][1],"   ", i[2][3])
                    print(i[3][1],"   ", i[3][3])
                    print(i[4][1],"   ", i[4][3])
                    print(i[5][1],"   ", i[5][3])
                    print(i[6][1],"   ", i[6][3])
                    print(i[6][0], i[6][1], i[6][2])
                    print("+========================+")
                    print("+ jose baratra", m, "vts")
                    print("+========================+")
                    break
                    if p >= n and p >= m:
                           j = []
                    for r in range(7):
                           j.append(["*"] * 6)
                    print("+========================+")
                    print("+        GANADOR         +")
                    print("+========================+")
                    print(j[0][1], "       ", j[0][5])
                    print(j[1][1], j[1][2], "  ", j[1][4], "", j[1][5])
                    print(j[2][1], "  ", j[2][3], "  ", j[2][5])
                    print(j[3][1], "       ", j[3][5])
                    print(j[4][1], "       ", j[4][5])
                    print(j[5][1], "       ", j[5][5])
                    print(j[6][1], "       ", j[6][5])
                    print("+========================+")
                    print("+ marco ocran:", p, "vts")
                    print("+========================+")
                    break
