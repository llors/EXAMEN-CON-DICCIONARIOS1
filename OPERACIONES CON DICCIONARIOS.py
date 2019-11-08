# 10 EJEMPLOS DE CREACION
#1
D=dict()
print(D)
#2
d={}
print(d)
#3
DIC=dict(X=8)
print(DIC)
#4
D={1:5,2:10}
print(D)
#5
DC={"A":"a","B":"b","C":"c","D":5}
print(DC)
#6
DS=dict({1:"a",2:"e",3:"o"})
print(DS)
#7
P=[15,16]
Q=["LLORS","GINO"]
DCS=dict(zip(P,Q))
print(DCS)
#8
A={"LIMA":{"FRUTA","CIUDAD","HERRAMIENTA"},"e":{"VOCAL","N° epsilom"}}
print(A)
#9
DCSS=dict({0:"PORTAL ENTRE NUMEROS NEGATIVOS Y POSITIVOS"})
print(DCSS)
#10
dicc={"HOLA":"SALUDO","RESPETO":"VALOR","UVA":"FRUTA"}
print(dicc)

# 10 EJEMPLOS DE PERTENENCIA DE CLAVE
#1
D={}
print( 1 in D)
#2
S={1:2,3:4}
print(1 in S)
#3
S={"A":1,"E":2,"I":3,"O":4,"U":5}
print("A"in S)
print("U" in S)
#4
DC=dict({"X":"VARIABLE"})
print("Y" not in DC)
#5
DA={1:2,3:3,4:4}
print(3 not in DA)
#6
G={"MANZANA":"FRUTASA","ARROZ":"RICO","ACE":"DETERGENTE"}
print("FRUTASA" in G)
#7
SA=dict({"A":1,"E":2,"I":3})
print("A" in SA)
#8
B=dict()
print(1 not in B)
#9
A={1:2}
print(2 not in A)
#10
A={1:1,2:2,3:3}
print(1 in A)

# 10 EJEMPLOS DE COMPARACION
#1
D={1:2,2:3,3:4}
D1={2:1,3:2,4:3}
print(D==D1)
#2
D={1:2,2:3,3:4,4:5}
D1={2:1,3:2,4:3,5:4}
print(D!=D1)
#3
A={}
B=dict()
print(A==B)
#4
S={1:1,2:2,3:3}
Z={1:1,2:2,3:3}
print(S!=Z)
#5
Q={"A":"a","B":"b","C":"c"}
P={"A":"a","B":"b","C":"c"}
print(P==Q)
#6
Z={}
A=dict({1:1})
print(Z==A)
#7
X={1:"A",2:"E",3:"I",4:"O",5:"U"}
Y={"A":1,"E":2,"I":3,"O":4,"U":5}
print(X==Y)
#8
A=dict()
B=dict()
print(A!=B)
#9
P={}
Q={}
print(P==Q)
#10
A={1:2}
Z={2:1}
print(A==Z)

# 10 EJEMPLOS DE INDEXACION
#1
A={"REDONDO":"CIRULO","RECTANGULO":"CUADRADO"}
print(A["REDONDO"])
#2
D={1:2,2:3,3:4,4:5}
print(D[1])
#3
S=dict({"A":1,"E":2,"I":3})
print(S["A"])
#4
Z=dict({10:1000})
print(Z[10])
#5
D={1:"NUMERO","S":"SIMBOLO","A":"VOCAL"}
print(D["S"])
#6
SD=dict({1:"a",5:"u"})
print(SD[5])
#7
D={1:2,2:3,3:4,4:5}
print(D[2])
#8
Z={1:{"HOLA","MUNDO"},2:"ESTOY",4:"MEJOR"}
print(Z[1])
#9
SA=dict({"A":1,"E":2,"I":3})
print(SA["I"])
#10
A={1:2}
print(A[1])

# 10 EJEMPLOS DE LONGITUD
#1
A={1:2}
print(len(A))
#2
Z={1:{"HOLA","MUNDO"},2:"ESTOY",4:"MEJOR"}
print(len(Z))
#3
A=dict()
print(len(A))
#4
Q={1:1,2:2,3:3}
print(len(Q))
#5
P=[12,13,14,19,19]
Q=["LENYS","LUIS","ANGELA","SANSON","JUAN"]
DCS=dict(zip(P,Q))
print(len(DCS))
#6
X={1:3}
S=len(X)
print(S)
#7
Q={"LENYS":12,"LUIS":13,"ANGELA":14,"SANSON":19,"JUAN":20}
print(len(Q))
#8
Z={1:1,2:2,3:3}
print(len(Z))
#9
Z1={1:1,2:2,3:3,4:3,5:3}
print(len(Z1))
#10
S=dict({1:1})
print(len(S))

# 10 EJEMPLOS DE ITERACION
#1
Z={1:1,2:2,3:3}
for k in Z:
    print(k)
#2
Q={"JORGE":12,"LUIS":13,"ANGELA":14,"SANSON":19,"JUAN":20}
for k in Q:
    print(k)
#3
A={1:2,"A":2,"B":1,"S":1}
for k in A:
    print(k)
#4
Z=dict({1:"W"})
for k in Z:
    print(k)
#5
D={"HOLA":"MUNDO","BB":"HHH","JJJ":"LLLL"}
for k in D:
    print(k)
#6
A={1:2,2:3,3:4,4:5,5:6,7:8}
for k,v in zip(A.keys(),A.values()):
    print(k,v)
#7
v={"NOMBRE":"FERIHA","APELLIDO":"VILMAZ","DNI":567844}
for k, v in zip(v.keys(), v.values()):
    print(k, v)
#8
A={"LORENZO":16,"JUAN":17,"MARLOM":17,"PERCY":19}
for k, v in zip(A.keys(), A.values()):
    print(k, v)
#9
q = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 7: 8}
for k, v in zip(q.keys(), q.values()):
    print(k, v)
#10
R={1:"HOLA",2:"QUE",3:"ESTAS",4:"HACIENDO"}
for k, v in zip(R.keys(), R.values()):
    print(k, v)

# 10 EJEMPLOS DE BUSQUEDA
#1
A={1:2}
print(A.get(1))
#2
D={"MANZANA":"FRUTA"}
print(D.get("MANZANA"))
#3
A=dict({1:2,2:2,3:3})
print(A.get(2))
#4
S={"W":"Y","Z":"W","A":"1"}
print(S.get("W"))
#5
X={"!":"#","$>":"F"}
print(X.get("!"))
#6
Z={1:{1,2,3,4},2:8}
print(Z.get(1))
#7
CANDIDATOS={10:"LUIS ESPERANZA",20:"JOSE BARATA",30:"MARCO OCRAM"}
print(CANDIDATOS.get(10))
#8
CANDIDATOS={10:"LUIS ESPERANZA",20:"JOSE BARATA",30:"MARCO OCRAM"}
print(CANDIDATOS.get(20))
#9
C={1:2,2:3}
print(C.get(2))
#10
S=dict({1:"HOLA",2:"COMO",3:"ESTAS"})
print(S.get(1))
print(S.get(2))
print(S.get(3))

# 10 EJEMPLOS DE ELIMINACION
#1
P={1:2,3:4,5:5}
del P[1]
print(P)
#2
Q={"A":"a","E":"e","I":"i","O":"o","U":"u"}
del Q["A"]
print(Q)
#3
A={1:2,3:4,5:6}
del A[5]
print(A)
#4
P={1:2,3:4,5:5}
del P[3]
print(P)
#5
S={"HOLA":1,"MUNDO":2}
del S["MUNDO"]
print(S)
#6
P={10:20,30:4,5:50}
del P[10]
print(P)
#7
A=dict({1:"!"})
del A[1]
print(A)
#8
X={1:2,2:3,4:5,6:3}
del X
#9
X={1:2,2:3,4:5,6:3}
del X[4]
print(X)
#10
Y={6:3}
del Y[6]
print(Y)

# 10 EJEMPLOS DE REEMPLAZO
#1
Y={6:3}
Y[6]=12
print(Y)
#2
Z={1:2,3:5,4:9,0:1}
Z[1]=9
print(Z)
#3
I={"A":1,"E":2,"I":3}
I["A"]=10
print(I)
#4
W=dict({1:"Q"})
W[1]="A"
print(W)
#5
SA={12:1,7:0}
SA[7]=13
print(SA)
#6
X={1:2,3:5,4:9,0:1}
X[0]="A"
print(X)
#7
OP={1:0,0:1}
OP[0]=9
print(OP)
#8
A=dict({"W":"Q","O":"P"})
A["W"]="K"
print(A)
#9
W=dict({1:2})
W[1]="A"
print(W)
#10
F={1:"O",2:"U"}
F[1]="I"
print(F)
# 10 EJEMPLOS DE AGREGADO
#1
D={}
A="EDUARDO"
T="TRACY"
D.setdefault(A,T)
print(D)
#2
A=dict()
Y="HOLA"
Z=["SALUDO","ESENCIAL"]
A.setdefault(Y,Z)
print(A)
#3
A={1:2}
A.setdefault(0,8)
print(A)
#4
S=dict({2:4})
S.setdefault(1,0)
print(S)
#5
W=dict()
A="HOLA"
B="MUNDO"
W.setdefault(A,B)
W.setdefault(1,3)
print(W)
#6
SA={}
SA.setdefault(1,0)
SA.setdefault(2,9)
SA.setdefault(5,6)
SA.setdefault(3,9)
print(SA)
#7
D=dict()
D.setdefault("a","b")
D.setdefault("c","d")
D.setdefault("e","f")
D.setdefault("g","h")
D.setdefault("i","e")
print(D)
#8
X={1:0,2:9}
X.setdefault(8,0)
X.setdefault(100,19)
print(X)
#9
SA=dict({1:9})
SA.setdefault(3,0)
SA.setdefault("W","E")
SA.setdefault("#","%")
SA.setdefault(11,12)
print(SA)
#10
O={1:10}
O.setdefault(100,120)
print(O)

# 10 EJEMPLOS DE ANULACION
#1
A={1:2,2:0,3:0,11:9}
A.clear()
print(A)
#2
D=dict({1:9})
D.clear()
print(D)
#3
D1={}
D1.clear()
print(D1)
#4
A1={1:2,2:0,3:0,11:9}
A1.clear()
print(A1)
#5
SA=dict()
SA.clear()
print(SA)
#6
Z=dict({1:9})
Z.clear()
print(Z)
#7
XZ={1:9,"W":"K","G":"J"}
XZ.clear()
print(XZ)
#8
A={"S":2}
A.clear()
print(A)
#9
C={"AA":"HOLA","BB":"AYUDA","CC":"ESTOY ACA"}
C.clear()
print(C)
#10
Z=dict({"W":"X"})
Z.clear()
print(Z)

# 10 EJEMPLOS DE CLONADO
#1
XZ={1:9,"W":"K","G":"J"}
x=XZ.copy()
print(x)
#2
X={}
Z=X.copy()
print(Z)
#3
A=dict()
F=A.copy()
print(F)
#4
CX={1:2,3:0,4:0}
B=CX.copy()
print(B)
#5
Z={1:0}
C=Z.copy()
print(C)
#6
SA=dict({1:9,5:0,3:2,12:90})
D=SA.copy()
print(D)
#7
XZ={1:9,10:0,2:6,"G":"g"}
x=XZ.copy()
print(x)
#8
I={"NUMER0":12,"DNI":1234567,"NOMBRE":"ALEX"}
S=I.copy()
print(S)
#9
XZO=dict({1:9,"A":"W",1:4})
R=XZO.copy()
print(R)
#10
X={"F":"E","W":"K","G":"J"}
x=X.copy()
print(x)

# 10 EJEMPLOS DE INSERCION
#1
XZ={1:9,"W":"K","G":"J"}
XZ[1]=90
print(XZ)
#2
A={1:8}
A[1]=9
print(A)
#3
B=dict({2:9,4:0})
B[4]=78
print(B)
#4
S={1:9,4:0,12:0,11:0}
S[11]=908
print(S)
#5
SA=dict({1:9,2:0,3:12})
SA[2]=1234
print(SA)
#6
XZ={1:9,"W":"K","G":"J"}
XZ["K"]=90
print(XZ)
#7
AD={1:0,2:0,8:9}
AD[8]=56
print(AD)
#8
X1={"Q":"D","J":"A","AS":"AD"}
X1["J"]="WR"
print(X1)
#9
SZ=dict({1:0})
SZ[1]="SA"
print(SZ)
#10
ZX={1:"O",2:"U",3:"I"}
ZX[1]="III"
print(ZX)

# 10 EJEMPLOS DE EXTRACCION
#1
A={1:2,3:0,4:0}
Z=A.pop(1)
print(Z)
#2
S={1:0}
ZZ=S.pop(1)
print(ZZ)
#3
SA=dict({0:1,3:9})
S=SA.pop(3)
print(S)
#4
CX={"A":"E","I":"O","U":"W"}
C=CX.pop("I")
print(C)
#5
WA={1:"W",2:"QW",3:"AS"}
V=WA.pop(3)
print(V)
#6
D={"A":1,"B":2,"C":8}
SA=D.pop("A")
print(SA)
#7
D1={2:3,"A":22,"J":29}
S=D1.pop("A")
print(S)
#8
S=dict({"Q":"A"})
DS=S.pop("Q")
print(DS)
#9
CX={"A":"E","I":"O","U":"W"}
C=CX.pop("I")
X=CX.pop("A")
print(X)
print(C)
#10
X={1:0,2:9}
A=X.pop(1)
A1=X.pop(2)
print(A)
print(A1)

# 10 EJEMPLOS DE CLAVES
#1
A={1:9,11:23}
print(A.keys())
#2
X={1:0,2:9}
print(X.keys())
#3
D={1:7}
print(D.keys())
#4
X={1:3,2:4,3:5}
print(X.keys())
#5
a={1:0}
print(a.keys())
#6
b={1:2,3:4,5:9}
print(b.keys())
#7
c={"Q":"A"}
print(c.keys())
#8
X={1:0,2:5,4:8,3:9}
print(X.keys())
#9
n={"W":"X"}
print(n.keys())
#10
p={1:0}
print(p.keys())

# 10 EJEMPLOS DE VALORES
#1
n={"W":"X"}
print(d.values())
#2
d={1:1,"a":"c"}
print(d.values())
#3
d={0:1,3:9}
print(d.values())
#4
d={1:0,2:0,8:9}
print(d.values())
#5
d={2:4}
print(d.values())
#6
d={"MANZANA":"FRUTA"}
print(d.values())
#7
d={"nombre":"GINO"}
print(d.values())
#8
d={1:2,3:4,5:6}
print(d.values())
#9
d={"A":"E","I":"O","U":"W"}
print(d.values())
#10
d={"PROFESOR":"DOCTOR"}
print(d.values())

# 10 EJEMPLOS DE COMVERSION
#1
D={1:"mundo","a":"tierra"}
print(tuple(D.values()))
#2
m={1:"grande",2:"fuerte"}
print(tuple(m.values()))
#3
n={"frtas":1.50,"mandarina":1.76}
print(tuple(n))
#4
n=dict(x=2,y=3)
print(list(n))
#5
x=dict({"m":3})
print(set(x.values()))
#6
y={1:"figura","m":"hermosa"}
print(tuple(y.values()))
#7
d=dict({"numero":10})
print(set(d.values()))
#8
d={"PROFESOR","DOCTOR"}
print(list(d))
#9
d={1:1,"a":"c"}
print(tuple(d.values()))
#10
e=dict({"misterios":1})
print(set(e.values()))