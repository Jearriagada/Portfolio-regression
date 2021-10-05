import csv 
import numpy as np
from numpy.core.arrayprint import DatetimeFormat
from numpy.core.fromnumeric import mean, shape, sort
from numpy.core.records import array
from numpy import savetxt  

def menu():
    "Función que sirve para reciclar código del menú de opciones"
    print("Seleccione base de datos a importar:\n ",
        "'1': 'fama_french.csv'",",\n ",
        "'2': 'goog.csv'\n Una vez importadas ambas bases de datos,",
        " entrar '3' para continuar")

with open("fama_french.csv") as f: #fama.csv importacion de datos de fama
    fama_reader = list(csv.reader(f, delimiter=","))
    fama_array = np.array(fama_reader)
lend = len(fama_array) - 1

def data(x=-1):
    """
    Función que sirve para reciclar código de
    el manejo de datos de fama french

    """
    data = (np.delete(fama_array,0,axis=1))
    data = (np.delete(data,0,axis=0))
    data = data.astype(float)
    data = np.flip(data)
    return data[ :,x ]

def etiquetas():
    """
    Función que sirve para reciclar código de
    las etiquetas del archivo fama french
    
    """
    etiquetas_cf = (np.delete(fama_array,0,axis=1))
    etiquetas = etiquetas_cf[ 0 ]
    return etiquetas
etiquetasv = etiquetas()

def fechas():
    """
    Función que sirve para reciclar código 
    del ajuste al formato deseado de las fechas
    
    """
    fechas = (np.delete(fama_array, [ 1,2,3,4 ],axis=1))
    fechas = (np.delete(fechas,0,0))

    array_fechas = []
    for i in (fechas): 
        listasplit = i[ 0 ].split("-") #separamos las fechas por los guiónes
        if len(listasplit[ 0 ])<2: #generamos los 4 posibles casos para arreglar el formato (es necesario añadir ceros extra)
            if len(listasplit[ 1 ])<2:   
                fecha_nueva = (listasplit[ 2 ] 
                                + "-0"
                                + listasplit[ 0 ] 
                                + "-0" 
                                + listasplit[ 1 ])
                fecha2 = np.datetime64(fecha_nueva)
                array_fechas.append(fecha2)
            else:
                fecha_nueva = (listasplit[ 2 ] 
                                + "-0"
                                + listasplit[ 0 ] 
                                + "-" 
                                + listasplit[ 1 ])
                fecha2 = np.datetime64(fecha_nueva)
                array_fechas.append(fecha2)
        else:
            if len(listasplit[ 1 ])<2:   
                fecha_nueva = (listasplit[ 2 ] 
                                + "-" 
                                + listasplit[ 0 ] 
                                + "-0" 
                                + listasplit[ 1 ])
                fecha2 = np.datetime64(fecha_nueva)
                array_fechas.append(fecha2)
            else:
                fecha_nueva = (listasplit[ 2 ] 
                                + "-" 
                                + listasplit[ 0 ] 
                                + "-" 
                                + listasplit[ 1 ])
                fecha2 = np.datetime64(fecha_nueva)
                array_fechas.append(fecha2)

    array_fechas = np.array(array_fechas,dtype="datetime64") #cambiamos el formato al deseado una vez hechos los ajustes
    array_fechas = np.flip(array_fechas)
    return array_fechas

#-------------------------------------------------------------------------------------------------------------------------------

with open("goog.csv") as f: #importación de datos de google
    goog = list(csv.reader(f, delimiter=","))
    goog = np.array(goog)

def datag():
    """
    Función que sirve para reciclar código de
    el manejo de datos de google

    """
    datag = (np.delete(goog,0,axis=1))
    datag = (np.delete(datag,0,axis=0))
    datag = datag.astype(float)
    return datag

def etiquetasg():
    """
    Función que sirve para reciclar código de
    las etiquetas del archivo google
    
    """
    etiquetas_cf2 = (np.delete(goog,0,axis=1))
    etiquetasg = etiquetas_cf2[ 0 ]
    etiquetasg = (list(etiquetasg))
    return (etiquetasg)
etiquetasgv = etiquetasg()

def fechasg():
    """
    Función que sirve para reciclar código 
    del ajuste al formato deseado de las fechas
    
    """
    fechasg = (np.delete(goog,1,axis=1))
    fechasg = (np.delete(fechasg,0,0))

    array_fechasg = []
    for i in (fechasg):
        listasplitg = i[0].split("/") #separamos las fechas por los slash
        if len(listasplitg[0])<2: #generamos los 4 posibles casos para arreglar el formato (es necesario añadir ceros extra)
            if len(listasplitg[1])<2: 
                fecha_nuevag = (listasplitg[ 2 ] 
                                + "-0"
                                + listasplitg[ 0 ] 
                                + "-0" 
                                + listasplitg[ 1 ])
                fecha2g = np.datetime64(fecha_nuevag)
                array_fechasg.append(fecha2g)
            else:
                fecha_nuevag = (listasplitg[ 2 ] 
                                + "-0"
                                + listasplitg[ 0 ] 
                                + "-" 
                                + listasplitg[ 1 ])
                fecha2g = np.datetime64(fecha_nuevag)
                array_fechasg.append(fecha2g)
        else:
            if len(listasplitg[ 1 ])<2:   
                fecha_nuevag = (listasplitg[ 2 ] 
                                + "-" 
                                + listasplitg[ 0 ] 
                                + "-0" 
                                + listasplitg[ 1 ])
                fecha2g = np.datetime64(fecha_nuevag)
                array_fechasg.append(fecha2g)
            else:
                fecha_nuevag = (listasplitg[ 2 ] 
                                + "-"
                                + listasplitg[ 0 ] 
                                + "-" 
                                + listasplitg[ 1 ])
                fecha2g = np.datetime64(fecha_nuevag) 
                array_fechasg.append(fecha2g)

    array_fechasg = np.array(array_fechasg,dtype="datetime64") #cambiamos el formato al deseado una vez hechos los ajustes
    return array_fechasg
    
#-------------------------------------------------------------------------------------------------------------------------------

def importar_serie():
    """
    Función que llama a las funciones anteriores realizando el formateo de los datos de cada una de las bases solicitadas
    
    """
    continuar = True
    while continuar == True:
        menu()
        serie=input("Ingrese su opcion ")
        if serie == "1":
            data()
            etiquetas()
            fechas()
            print("'fama_french.csv' importado\n")
        elif serie == "2":
            datag()
            etiquetasg()
            fechasg()
            print("'goog.csv' importado\n")
        elif serie == "3":
            continuar = False

if __name__ == '__main__':
    importar_serie()

#-------------------------------------------------------------------------------------------------------------------------------

#calculo de los datos menos su promedio 

def regresa(dependiente,independiente,mudo="0"):
    """
    Esta funcion tiene por objetivo realizar dos regresiones lineales distintas
    dependiendo de lo que le solicitemos en el menú de elección.
    
    Pámetros
    --------
    dependiente : np.ndarray
        base de datos con las observaciones de nuestra variable dependiente
    independiente : np.ndarray
        base de datos con las observaciones de nuestra(s) variable(s) independiente(s)
    mudo : boolean
        variable binaria que determina si se activa o no el modo mudo el cual no imprime la regresión final
    
    Resultado
    ---------
    coeff : np.ndarray
        matriz con los coeficientes de la regresión
    r2 : float
        r cuadrado de la regresión
    
    """
    if dependiente == "1" and isinstance(datag(),np.ndarray) == True: #validación de datos ingresados
        y = datag()
        y = np.reshape(y,len(y))  
        ymean = (np.mean(y))
        y_ymean = (y-ymean) #cálculo de y - y promedio para cada y
    elif isinstance(datag(),np.ndarray) == False:
        raise ValueError("Error, Asegurese de que los datos ",
        "estén en formato numpy ndarray") #error por no cumplir el formato solicitado de los datos
    else:
        raise ValueError("Error, ingrese una de las opciones anteriores") #error por no ingresar ninguna de las opciones anteriores

    if independiente == "1" and mudo =="0" and isinstance(
                                                datag(),np.ndarray) == True: #validación de datos ingresados
        x = (data(x=-1))
        xmean = (np.mean(x))
        x_xmean = (x-xmean) #cálculo de x - x promedio para cada x
        x_2 = x_xmean**2 #cálculo de x cuadrado 
        d = (y_ymean * x_xmean) 

        e = np.sum(d)

        f = np.sum(x_2)

        beta1 = e/f 
        beta0 = ymean - (beta1*xmean)
        coeff = np.append(beta0,beta1) #matriz de coeficientes
        yj = beta0 + (beta1*x)

        sec = np.sum((yj - ymean)**2) #cálculo del r2
        stc = np.sum((y-ymean)**2)
        r_2 = sec/stc
        return coeff, r_2, print(
                f"\nResumen de la regresion",
                f"\n-----------------------\n\n",
                f"Numero de observaciones: {len(y)}\n",
                f"R-cuadrado:              {round(r_2,4)}\n\n",
                f"Nombre  |  coef.  |  error std  |",
                f"\n=================================\nb0       | ",
                f"{round(beta0,5)}|\n{etiquetasv[0]}   |  {round(beta1,5)}|")  
    elif independiente == "1" and mudo =="1" and isinstance(
                                                datag(),np.ndarray) == True: #validación de datos ingresados
        x = (data(x=-1))
        xmean = (np.mean(x))
        x_xmean = (x-xmean) #cálculo de x - x promedio para cada x
        x_2 = x_xmean**2 #cálculo de x cuadrado 
        d = (y_ymean * x_xmean)

        e = np.sum(d)

        f = np.sum(x_2)

        beta1 = e/f
        beta0 = ymean - (beta1*xmean)
        coeff = np.append(beta0,beta1) #matriz de coeficientes
        yj = beta0 + (beta1*x)

        sec = np.sum((yj - ymean)**2) #cálculo del r2
        stc = np.sum((y-ymean)**2)
        r_2 = sec/stc
        return coeff, r_2
    elif independiente == "2" and mudo == "0" and isinstance(
                                                datag(),np.ndarray) == True: #validación de datos ingresados
        
        x1 = (data([-2,-3,-4])) #traemos las columnas que necesitamos de la matriz de datos 
        
        shape = len(x1) #codigo para crear una matriz de 1s para despues añadir a los datos y obtener el b0
        value = 1

        unos = np.empty(shape, dtype=np.int)
        unos.fill(value)

        m_unos = (np.resize(unos,[ lend,1 ]))
        
        x1 = (np.flip(x1)) #codigo que añade los 1
        x1 = np.append(x1,m_unos,axis=1)
        x1 = np.flip(x1)
        x1_t = x1.T 
      
        x1_x1T = x1_t @ x1 #calculos para obtener el b0

        xflip = np.linalg.inv(x1_x1T)

        y_t = y.T
        x1_t_y = (x1_t @ y_t)

        betas = (xflip @ x1_t_y) 
        betasr = np.round(betas,4)
        betasT = betas.T
        coeff = betas #matriz de coeficientes

        numerador = betasT @ x1_t @ x1 @ betas 

        denominador = y_t @ y

        r_2_multi = numerador/denominador
        r_2 = r_2_multi
        r_2_multir = round(r_2_multi,4)
        return coeff, r_2, print(
                f"\nResumen de la regresion",
                "\n-----------------------\n\n",
                f"Numero de observaciones: {len(x1)}\n",
                f"R-cuadrado:              {r_2_multir}\n\n",
                "Nombre  |  coef.  |  error std  |",
                "\n=================================\nb0       |",
                f" {betasr[ 0 ]}|\n{etiquetasv[ 1 ]}      |",
                f" {betasr[ 1 ]}|\n{etiquetasv[ 2 ]}      |",
                f" {betasr[ 2 ]}|\n{etiquetasv[ 3 ]}       |",
                f" {betasr[ 3 ]}|")
    elif independiente == "2" and mudo == "1" and isinstance(
                                                datag(),np.ndarray) == True: #validación de datos ingresados
        
        x1 = (data([ -2,-3,-4 ])) #traemos las columnas que necesitamos de la matriz de datos 

        shape = len(x1) #codigo para crear una matriz de 1s para despues añadir a los datos y obtener el b0
        value = 1

        unos = np.empty(shape, dtype=np.int)
        unos.fill(value)

        m_unos = (np.resize(unos,[ lend,1 ]))
      
        x1 = (np.flip(x1)) #codigo que añade los 1
        x1 = np.append(x1,m_unos,axis=1)
        x1 = np.flip(x1)
        x1_t = x1.T 
       
        x1_x1T = x1_t @ x1 #calculos para obtener el b0

        xflip = np.linalg.inv(x1_x1T)

        y_t = y.T
        x1_t_y = (x1_t @ y_t)

        betas = (xflip @ x1_t_y) 
        betasr = np.round(betas,4)
        betasT = betas.T
        coeff = betas #matriz de coeficientes

        numerador = betasT @ x1_t @ x1 @ betas 

        denominador = y_t @ y

        r_2_multi = numerador/denominador
        r_2_multir = round(r_2_multi,4)
        r_2 = r_2_multi
        return betas, r_2
    elif isinstance(datag(),np.ndarray) == False:
        raise ValueError("Error, Asegurese de que los datos",
                                " estén en formato numpy ndarray") #error por no cumplir el formato solicitado de los datos
    else:
        raise ValueError("Error, ingrese una de las opciones ") #error por no ingresar ninguna de las opciones anteriores

    
print("##################################",
                "############################################",
                "\n############################################",
                "##################################\n       A continuación",
                " se le pedirán las variables de la regresión lineal\n",
                "#######################################################",
                "#######################\n################################",
                "##############################################")
regresa(
                dependiente=input("ingrese una opcion una variable dependiente \n 1 - retornos de google\n "),
                independiente=input("ingrese una(s) variable(s) independiente(s) \n 1 - 'premio por riesgo de mercado' \n 2- 'retornos de los 3 factores de fama french'\n "),
                mudo=input("¿desea activar el modo mudo?\n 0 - No\n 1 - Si\n "))



####### Analisis y Conclusiones finales:
### REGRESIÓN LINEAL 
# La regresión lineal nos dice que cuando el premio por riesgo mercado es 0, la rentabilidad de una acción de google es de 0,0006674,
# y que por cada punto que aumente el premio por riesgo mercado, la rentabilidad de google crecerá un 0,966552; 
# el r2 nos dice que esta variable es capaz de explicar el 38,66% de la dispersión de la rentabilidad de google. 

#### REGRESIÓN MÚLTIPLE
# Los datos obtenidos en la regresión mulitvariable nos dicen que cuando estas 3 variables son 0, entonces la rentabilidad de google es de 0,001060295. 
# Si la variable SMB aumenta en 1 unidad, la rentabilidad de google aumenta en 0,26827, Si la variable HML aumenta en 1 unidad, la rentabilidad de google aumenta en 0,092544, Si la variable RF aumenta en 1 unidad, la rentabilidad de google aumenta en 0,643467. El R2 nos dice que en conjunto, estas 3 variables forman un modelo que explica el 0,93% de la dispersión de la rentabilidad de google. ------ al comparar estos modelos, podemos ver que la variabilidad de MKT-RF explica notoriamente mejor la dispersión de google que las otras 3 variables que se usaron en la regresión multivariable.
#
#-------------------------------------------------------------------------------------------------------------------------------