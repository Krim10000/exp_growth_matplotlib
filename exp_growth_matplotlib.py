print ("Starting")
from random import randrange
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, ion, show, draw
import time

class MyClass(object):
    def __init__(self, ID, BIRTH, X, Y):
        self.ID = ID
        self.BIRTH=BIRTH
        self.X =X
        self.Y=Y
#CADA CUANTO TIEMPO SE REPRODUCE LAS BACTERIAS
REP = 10


ID = 1
t=0
X=0
Y=0
my_objects = []
my_objects.append(MyClass(ID, t,X,Y))

#PLOT BACTERIA INICIAL
titulo ="Numero de bacterias:  " + str(ID) + "     tiempo: "+str(t)        
plt.title(titulo)
plt.plot( X,Y, 'go')
plt.axis([-50, 50, -50, 50])# tamaño grafico
plt.pause(0.5)

while t < 101: # DURACION DE LA "SIMULACION"
    
    
    for bacterias in my_objects:
        
        if  (t-bacterias.BIRTH)%REP ==0 and (t-bacterias.BIRTH)>0:
            ID = ID +1 # CADA BACTERIA TIENE UN ID UNICO
            
            X = bacterias.X + randrange(-10,10)
            Y = bacterias.Y + randrange(-10,10)
                        
            my_objects.append(MyClass(ID, t, X, Y))

            #PLOT, EL TIEMPO SE CONGELA Y APARECEN NUEVAS BACTERIAS
            titulo ="Numero de bacterias:  " + str(ID) + "     tiempo: "+str(t)        
            plt.title(titulo)
    
            plt.plot( X,Y, 'ro')
            plt.axis([-50, 50, -50, 50])# tamaño grafico
            plt.pause(1/pow(2,ID))


    # PLOT, EL TIEMPO PASA
    titulo ="Numero de bacterias:  " + str(ID) + "     tiempo: "+str(t)        
    plt.title(titulo)
    plt.axis([-50, 50, -50, 50])# tamaño grafico
    plt.pause(0.5)

            

   
    
    t = t +1    


#END WHILE   
#for obj in my_objects:
    #print ("ID es "+str(obj.ID) + ", tiempo de nacimiento es  "+str(obj.BIRTH) +"  posicion ("  +str(obj.X)+ "," +str(obj.Y)+  ")" )
    #print ("")
print("para terminar el programa cerrar el grafico")
plt.show()



             
