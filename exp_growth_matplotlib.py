print ("Starting")
from random import randrange
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show, draw
import time
import math

class MyClass(object):
    def __init__(self, ID,BIRTH,X0,Y0,X1,Y1,DEATH):
        self.ID = ID
        self.BIRTH = BIRTH
        self.X0 = X0
        self.Y0 = Y0
        self.X1 = X1
        self.Y1 = Y1
        self.VEL = VEL
        self.DEATH = DEATH

t=0 # TIEMPO INICIAL      
tf = 201# DURACION DE LA SIMULACION
NIB = 1 #NUMERO INCIAL DE BACTERIAS

#DEATH, despues de cierta cantidad de tiempo la bacteria muere
#DEATH = 0, bacteria viva.
#DEATH = 1, bacteria muerta.



REP = 10 #CADA CUANTO TIEMPO SE REPRODUCE LAS BACTERIAS


#datos de la bacteria incial


ID = 1 # ID DE LA PRIMERA BACTERIA


X0=0 # PUNTO DE INICIO EN EL EJE X DE LA BACTERIA
Y0=0 # PUNTO DE INICIO EN EL EJE Y DE LA BACTERIA
X1=0 # DESTINO EN EL EJE X
Y1=0 # DESTINO EN EL EJE Y
VEL=2 # ESPACIO QUE LA BACTERIA AVANZA POR TIEMPO
R =50 # RADIO ALEATORIO DESDE EL LUGAR DE ORIGEN HASTA DONDE AVANZARA LA BACTERIA
Rmin = R*-1



my_objects = []


#crea a las bacterias incial, todas las bacterias se crean en la misma posicion
count = 1
while count <= NIB :
    
    my_objects.append(MyClass(ID,t,X0,Y0,X1,Y1,0))
    ID = ID+1
    count = count +1

print(" El numero inicial de bacterias es " + str(len(my_objects)) )
  
K=0
L=0

while t < tf: # DURACION DE LA "SIMULACION"
    #print("tiempo" +str(t))

#####################################################################################
    #NACIMIENTO DE BACTERIAS
    for bacterias in my_objects:
        
        if  (t-bacterias.BIRTH)%REP ==0 and (t-bacterias.BIRTH)>0: #and bacterias.DEATH ==0

            #nace en el mismo lugar que la bacteria original    
            X0= bacterias.X0
            Y0=bacterias.Y0
            ID = bacterias.ID +1 # CADA BACTERIA TIENE UN ID UNICO
          
            #destino de la bacteria     
            X1 = bacterias.X0 + randrange(Rmin,R)  # RADIO ALEATORIO DESDE EL LUGAR DE ORIGEN HASTA DONDE AVANZARA LA BACTERIA

            Y1 = bacterias.Y0 + randrange(Rmin,R) # RADIO ALEATORIO DESDE EL LUGAR DE ORIGEN HASTA DONDE AVANZARA LA BACTERIA


            X1 = round(X1,2)
            Y1 = round(Y1,2)

            #agregar bacteria a la lista                        
            my_objects.append(MyClass(ID, t , X0, Y0, X1, Y1, 0))

            #print("La bacteria " +str(bacterias.ID) + " se reprodujo")

#####################################################################################
    #MOVIMIENTO DE BACTERIAS      
           
    for bacterias in my_objects:
        #Se mueven si no estan en su destino final, no se mueven el turno en que nacen
        if ((round(bacterias.X1,2) != round(bacterias.X0,2)) or (round(bacterias.Y1,2) != round(bacterias.Y0,2))) and bacterias.BIRTH != t:
            
            DISTANCIAX = round((bacterias.X1-bacterias.X0),2)#vector
            DISTANCIAY = round((bacterias.Y1-bacterias.Y0),2)#vector

            D  = round(VEL,2)
            X0 = round(bacterias.X0,2)
            Y0 = round(bacterias.Y0,2)
            X1 = round(bacterias.X1,2)
            Y1 = round(bacterias.Y1,2)
            
            
            if DISTANCIAX != 0:
                
                M = (bacterias.Y1-bacterias.Y0)/(bacterias.X1-bacterias.X0) # M PENDIENTE:
                C = bacterias.Y0 - M* bacterias.X0 # C CONSTANTE:
                J = pow(M,2)+1 # POR COMODIDAD
                
               
                XNA = (X0 + D * J**(-0.5)) # OBTENIDO AL DESPEJAR A**2 + B**2 = C**2

                XNB = (X0 - D * J**(-0.5)) # OBTENIDO AL DESPEJAR A**2 + B**2 = C**2

                YNA = M*XNA +C # Y = MX+C

                YNB = M*XNB +C # Y = MX+C

                #DA = (((XNA-X0)**2 + (YNA-Y0)**2)**0.5) COMPROBACION A
                #DB = (((XNB-X0)**2 + (YNB-Y0)**2)**0.5) COMPROBACION B

                XN=XNA
                YN=YNA
                                           
                XN = round(XN,2)
                YN = round(YN,2)

                #caso particular cuando la distacia que puede avanzar la bacteria es menor a la distancia que falta
                if DISTANCIAX<(XN-X0):
                    XN = round(X1,2)

                if DISTANCIAX<(YN-Y0):
                    YN = round(Y1,2)
                    
                #print("La bacteria " +str(bacterias.ID) + " se movio, desde " +str(bacterias.X0)+","+str(bacterias.Y0)+ "  hasta  "+str(XN)+","+str(YN) )
                #print("destino : " + str(round(bacterias.X1,2)) +"," +str(round(bacterias.Y1,2)))

                bacterias.X0 = XN
                bacterias.Y0 = YN
                
                
#######################################################################
                
            else:
                XN = X1
                if DISTANCIAY > 0:
                    YN = VEL
                else:
                    YN = -1*VEL
                
                                
                XN = round(XN,2)
                YN = round(YN,2)

                #caso particular cuando la distacia que puede avanzar la bacteria es menor a la distancia que falta
                if DISTANCIAX<(XN-X0):
                    XN = round(X1,2)

                if DISTANCIAY<(YN-Y0):
                    YN = round(Y1,2)

                #print("La bacteria " +str(bacterias.ID) + " se movio, desde " +str(bacterias.X0)+","+str(bacterias.Y0)+ "  hasta  "+str(XN)+","+str(YN) )
                #print("destino : " + str(round(bacterias.X1,2)) +"," +str(round(bacterias.Y1,2)))

                bacterias.X0= XN
                bacterias.Y0 = YN

#####################################################################################
    

        
    #GRAFICO
    
    K =[]
    L=[]
    S =[]
    DID = []
    for bacterias in my_objects:
        ki = bacterias.X0
        K.append(ki)
        li = bacterias.Y0
        L.append(li)
        si = ((t-bacterias.BIRTH)%REP+1)
        S.append(si)
        idi = str(bacterias.ID)
        DID.append(idi)

    #print(my_objects[0].X0)
    #print(my_objects[0].Y0)
    
    
    # PLOT, EL TIEMPO PASA
    titulo ="Numero de bacterias:  " + str(len (my_objects)) + "     tiempo: "+str(t)        
    plt.title(titulo)
    
    plt.plot( K,L, 'go',linewidth=2, markersize=5, data =DID)

    MINX= -100
    MAXX= 100
    MINY= -100
    MAXY= 100

    plt.axis([MINX, MAXX,MINY, MAXY])# tamaño grafico  -X,+X,-Y,+Y
    if min(K)<MINX  or max(K) > MAXX or min(L) < MINY or max(L)>MAXY:
        list1 = [max(K), max(L), abs(min(K)), abs(min(L))]
        coord=max(list1)
        coord= 10*((coord//10)+2) 
        plt.axis([-1*coord, coord,-1*coord, coord])
        
    
    plt.pause(0.5)
    

    plt.clf()
    
    
    t = t +1  #EL TIEMPO PASA


#END WHILE
DESTINO =0
for bacterias in my_objects:
    if (bacterias.X1 == bacterias.X0 and bacterias.Y1 == bacterias.Y0):
        DESTINO = DESTINO +1
print(  str(DESTINO)+ " bacterias llegaron a su destino, de un total de " + str(len (my_objects)))




print("para terminar el programa cerrar el grafico")



             
