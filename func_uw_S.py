import pandas as pd
import math

#Defino una funcion para separar las covarianzas por cuadrantes
def calc_S(cov_c1,cov_c2,cov_c3, cov_c4, cov):
    S_c1 = cov_c1/cov
    S_c2 = cov_c2/cov
    S_c3 = cov_c3/cov
    S_c4 = cov_c4/cov
    return S_c1, S_c2, S_c3, S_c4

def flujo_uw_S(totales_uw_cuad,flujos_medios):

    val_medios = totales_uw_cuad.mean(axis=0,skipna=True)
# Creo lista para almacenar los datos
    S_cuad_uw = []
    S_1_5 = []
    S_3 = []
    S_5 = []
    S_7 = []
#Calculo S de cada cuadrante, como el promedio de cada cuadrante (H=0)
#dividido el promedio total (de todos los cuadrantes, H=0)
#para el nivel de 1.5 m
    cov_1_5 = flujos_medios['cov_uw_1.5m']
    cov_c1_1_5 = val_medios['cov_uw_c1_1.5m']
    cov_c2_1_5 = val_medios['cov_uw_c2_1.5m']
    cov_c3_1_5 = val_medios['cov_uw_c3_1.5m']
    cov_c4_1_5 = val_medios['cov_uw_c4_1.5m']

    S_uw_c1, S_uw_c2, S_uw_c3, S_uw_c4 = calc_S(cov_c1_1_5,cov_c2_1_5,cov_c3_1_5, cov_c4_1_5, cov_1_5)
    # Guardar los resultados en la variable 'cuad_inst_1_5'
    # S_1_5 = {'columnas': ['S_cuad1','S_cuad2','S_cuad3','S_cuad4'],
    # 'valores': [S_uw_c1[0], S_uw_c2[0], S_uw_c3[0], S_uw_c4[0]]}
    S_1_5 = ([S_uw_c1[0], S_uw_c2[0], S_uw_c3[0], S_uw_c4[0]])
    S_1_5_df = pd.DataFrame(S_1_5, index=['S_cuad1_1.5m','S_cuad2_1.5m','S_cuad3_1.5m','S_cuad4_1.5m']).T

#para el nivel de 3 m
    cov_3 = flujos_medios['cov_uw_3m']
    cov_c1_3 = val_medios['cov_uw_c1_3m']
    cov_c2_3 = val_medios['cov_uw_c2_3m']
    cov_c3_3 = val_medios['cov_uw_c3_3m']
    cov_c4_3 = val_medios['cov_uw_c4_3m']

    S_uw_c1, S_uw_c2, S_uw_c3, S_uw_c4 = calc_S(cov_c1_3,cov_c2_3,cov_c3_3, cov_c4_3, cov_3)
    S_3 = ([S_uw_c1[0], S_uw_c2[0], S_uw_c3[0], S_uw_c4[0]])
    S_3_df = pd.DataFrame(S_3, index=['S_cuad1_3m','S_cuad2_3m','S_cuad3_3m','S_cuad4_3m']).T

#para el nivel de 5 m
    cov_5 = flujos_medios['cov_uw_5m']
    cov_c1_5 = val_medios['cov_uw_c1_5m']
    cov_c2_5 = val_medios['cov_uw_c2_5m']
    cov_c3_5 = val_medios['cov_uw_c3_5m']
    cov_c4_5 = val_medios['cov_uw_c4_5m']

    S_uw_c1, S_uw_c2, S_uw_c3, S_uw_c4 = calc_S(cov_c1_5,cov_c2_5,cov_c3_5, cov_c4_5, cov_5)
    S_5 = ([S_uw_c1[0], S_uw_c2[0], S_uw_c3[0], S_uw_c4[0]])
    S_5_df = pd.DataFrame(S_5, index=['S_cuad1_5m','S_cuad2_5m','S_cuad3_5m','S_cuad4_5m']).T

#para el nivel de 7 m
    cov_7 = flujos_medios['cov_uw_7m']
    cov_c1_7 = val_medios['cov_uw_c1_7m']
    cov_c2_7 = val_medios['cov_uw_c2_7m']
    cov_c3_7 = val_medios['cov_uw_c3_7m']
    cov_c4_7 = val_medios['cov_uw_c4_7m']

    S_uw_c1, S_uw_c2, S_uw_c3, S_uw_c4 = calc_S(cov_c1_7,cov_c2_7,cov_c3_7,cov_c4_7, cov_7)
    S_7 = ([S_uw_c1[0], S_uw_c2[0], S_uw_c3[0], S_uw_c4[0]])
    S_7_df = pd.DataFrame(S_7,  index=['S_cuad1_7m','S_cuad2_7m','S_cuad3_7m','S_cuad4_7m']).T

#DataFrame con todos los niveles
#S de cada cuadrante para uw (H=0)
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    S_cuad_uw = pd.concat([S_1_5_df, S_3_df, S_5_df, S_7_df], axis=1)

    return S_cuad_uw

#     S_cuad1_1_5 = float(val_medios['cov_uw_c1_1.5m'] / flujos_medios['cov_uw_1.5m'])
#     S_cuad2_1_5 = float(val_medios['cov_uw_c2_1.5m'] / flujos_medios['cov_uw_1.5m'])
#     S_cuad3_1_5 = float(val_medios['cov_uw_c3_1.5m'] / flujos_medios['cov_uw_1.5m'])
#     S_cuad4_1_5 = float(val_medios['cov_uw_c4_1.5m'] / flujos_medios['cov_uw_1.5m'])
#
# #para el nivel de 3 m
#     S_cuad1_3 = float(val_medios['cov_uw_c1_3m'] / flujos_medios['cov_uw_3m'])
#     S_cuad2_3 = float(val_medios['cov_uw_c2_3m'] / flujos_medios['cov_uw_3m'])
#     S_cuad3_3 = float(val_medios['cov_uw_c3_3m'] / flujos_medios['cov_uw_3m'])
#     S_cuad4_3 = float(val_medios['cov_uw_c4_3m'] / flujos_medios['cov_uw_3m'])
#
# #para el nivel de 5 m
#     S_cuad1_5 = float(val_medios['cov_uw_c1_5m'] / flujos_medios['cov_uw_5m'])
#     S_cuad2_5 = float(val_medios['cov_uw_c2_5m'] / flujos_medios['cov_uw_5m'])
#     S_cuad3_5 = float(val_medios['cov_uw_c3_5m'] / flujos_medios['cov_uw_5m'])
#     S_cuad4_5 = float(val_medios['cov_uw_c4_5m'] / flujos_medios['cov_uw_5m'])
#
# #para el nivel de 7 m
#     S_cuad1_7 = float(val_medios['cov_uw_c7_5m'] / flujos_medios['cov_uw_7m'])
#     S_cuad2_7 = float(val_medios['cov_uw_c7_5m'] / flujos_medios['cov_uw_7m'])
#     S_cuad3_7 = float(val_medios['cov_uw_c7_5m'] / flujos_medios['cov_uw_7m'])
#     S_cuad4_7 = float(val_medios['cov_uw_c7_5m'] / flujos_medios['cov_uw_7m'])
#
#     S_cuad_uw = pd.concat([S_cuad1_1_5, S_cuad2_1_5, S_cuad3_1_5, S_cuad4_1_5, \
#     S_cuad1_3, S_cuad2_3, S_cuad3_3, S_cuad4_3, \
#     S_cuad1_5, S_cuad2_5, S_cuad3_5, S_cuad4_5, \
#     S_cuad1_7, S_cuad2_7, S_cuad3_7, S_cuad4_7], \
#     axis=1, keys=['S_cuad1_1.5m', 'S_cuad2_1.5m', 'S_cuad3_1.5m', 'S_cuad4_1.5m', \
#     'S_cuad1_3m', 'S_cuad2_3m', 'S_cuad3_3m', 'S_cuad4_3m', \
#     'S_cuad1_5m', 'S_cuad2_5m', 'S_cuad3_5m', 'S_cuad4_5m', \
#     'S_cuad1_7m', 'S_cuad2_7m', 'S_cuad3_7m', 'S_cuad4_7m'])
    # 'u_desvio_5m', 'v_desvio_5m', 'w_desvio_5m', 'T_desvio_5m', 'cov_uw_5m', 'cov_vw_5m', 'cov_wT_5m', \
    # 'u_desvio_7m', 'v_desvio_7m', 'w_desvio_7m', 'T_desvio_7m', 'cov_uw_7m', 'cov_vw_7m', 'cov_wT_7m', \
    # 'CO2_desvio_3m', 'H2O_desvio_3m', 'q_desvio_3m', 'cov_wCO2_3m', 'cov_wH2O_3m','cov_wq_3m','cov_qCO2_3m','cov_qT_3m','cov_CO2T_3m'])
    #
    # return S_cuad_uw

# def flujo_uw_S_H(ruta_entrada_totales,ruta_entrada_medios,ruta_salida,datos):
#
# #Traigo las librerias que necesito
#     import pandas as pd
#     import os
#     import math
#     import numpy as np
#
#     #for n in range(180, 181):
#     #for n in range(936, 937):
#     #for n in range(1363, 1364):
#     for day in range(21, 32):
#         for arch in range(1, 2500):
#             if not os.path.isfile(ruta_entrada_totales + datos + str(day) + '_' + str(arch) + '.csv'):
#                 continue
#             else:
#                 datos_flujos_cuad = pd.read_csv(ruta_entrada_totales + datos + str(day) + '_' + \
#                 str(arch) + '.csv',header=0)
#                 datos_flujos_medios = pd.read_csv(ruta_entrada_medios + datos + str(day) + '_' + \
#                 str(arch) + '.csv',header=0)
#
# #PAra los niveles de 1,5 m, 3m, 5m y 7m
# #Leo los datos medios de U'w'
#                 flujo_uw_medio_1_5 = float(datos_flujos_medios['T_medio_1.5m'])
#
# #Calculo valores medios de U'w' de cada cuadrante
#                 flujo_cuad1_medio_1_5  = datos_flujos_cuad['flujo_uw_c1_1.5m'].mean(axis=0,skipna=True)
#                 flujo_cuad2_medio_1_5  = datos_flujos_cuad['flujo_uw_c2_1.5m'].mean(axis=0, skipna=True)
#                 flujo_cuad3_medio_1_5  = datos_flujos_cuad['flujo_uw_c3_1.5m'].mean(axis=0, skipna=True)
#                 flujo_cuad4_medio_1_5  = datos_flujos_cuad['flujo_uw_c4_1.5m'].mean(axis=0, skipna=True)
#
# #Calculo S de cada cuadrante, como el promedio de cada cuadrante (datos fuera de H)
# #dividido el promedio total (de todos los cuadrantes, con datos dentro y fuera de H)
#                 S_cuad1_1_5 = flujo_cuad1_medio_1_5 /flujo_uw_medio_1_5
#                 S_cuad2_1_5 = flujo_cuad2_medio_1_5 /flujo_uw_medio_1_5
#                 S_cuad3_1_5 = flujo_cuad3_medio_1_5 /flujo_uw_medio_1_5
#                 S_cuad4_1_5 = flujo_cuad4_medio_1_5 /flujo_uw_medio_1_5
#
# #Convierto los resultados a flotantes para guardarlos en un .csv (sino guarda los valores entre [])
# #Los valores de S_c son los mismos que en S_cuad, pero sino aparecen entre []
#                 S_c1_1_5  = float(S_cuad1_1_5)
#                 S_c2_1_5  = float(S_cuad2_1_5)
#                 S_c3_1_5  = float(S_cuad3_1_5)
#                 S_c4_1_5  = float(S_cuad4_1_5)
#
# #PAra los niveles de 1,5 m, 3m, 5m y 7m
# #Leo los datos medios de U'w'
#                 flujo_uw_medio_3 = float(datos_flujos_medios['T_medio_3m'])
#
# #Calculo valores medios de U'w' de cada cuadrante
#                 flujo_cuad1_medio_3  = datos_flujos_cuad['flujo_uw_c1_3m'].mean(axis=0,skipna=True)
#                 flujo_cuad2_medio_3  = datos_flujos_cuad['flujo_uw_c2_3m'].mean(axis=0, skipna=True)
#                 flujo_cuad3_medio_3  = datos_flujos_cuad['flujo_uw_c3_3m'].mean(axis=0, skipna=True)
#                 flujo_cuad4_medio_3  = datos_flujos_cuad['flujo_uw_c4_3m'].mean(axis=0, skipna=True)
#
# #Calculo S de cada cuadrante, como el promedio de cada cuadrante (datos fuera de H)
# #dividido el promedio total (de todos los cuadrantes, con datos dentro y fuera de H)
#                 S_cuad1_3 = flujo_cuad1_medio_3 /flujo_uw_medio_3
#                 S_cuad2_3 = flujo_cuad2_medio_3 /flujo_uw_medio_3
#                 S_cuad3_3 = flujo_cuad3_medio_3 /flujo_uw_medio_3
#                 S_cuad4_3 = flujo_cuad4_medio_3 /flujo_uw_medio_3
#
# #Convierto los resultados a flotantes para guardarlos en un .csv (sino guarda los valores entre [])
# #Los valores de S_c son los mismos que en S_cuad, pero sino aparecen entre []
#                 S_c1_3  = float(S_cuad1_3)
#                 S_c2_3  = float(S_cuad2_3)
#                 S_c3_3  = float(S_cuad3_3)
#                 S_c4_3  = float(S_cuad4_3)
#
# #PAra los niveles de 1,5 m, 3m, 5m y 7m
# #Leo los datos medios de U'w'
#                 flujo_uw_medio_5 = float(datos_flujos_medios['T_medio_5m'])
#
# #Calculo valores medios de U'w' de cada cuadrante
#                 flujo_cuad1_medio_5  = datos_flujos_cuad['flujo_uw_c1_5m'].mean(axis=0,skipna=True)
#                 flujo_cuad2_medio_5  = datos_flujos_cuad['flujo_uw_c2_5m'].mean(axis=0, skipna=True)
#                 flujo_cuad3_medio_5  = datos_flujos_cuad['flujo_uw_c3_5m'].mean(axis=0, skipna=True)
#                 flujo_cuad4_medio_5  = datos_flujos_cuad['flujo_uw_c4_5m'].mean(axis=0, skipna=True)
#
# #Calculo S de cada cuadrante, como el promedio de cada cuadrante (datos fuera de H)
# #dividido el promedio total (de todos los cuadrantes, con datos dentro y fuera de H)
#                 S_cuad1_5 = flujo_cuad1_medio_5 /flujo_uw_medio_5
#                 S_cuad2_5 = flujo_cuad2_medio_5 /flujo_uw_medio_5
#                 S_cuad3_5 = flujo_cuad3_medio_5 /flujo_uw_medio_5
#                 S_cuad4_5 = flujo_cuad4_medio_5 /flujo_uw_medio_5
#
# #Convierto los resultados a flotantes para guardarlos en un .csv (sino guarda los valores entre [])
# #Los valores de S_c son los mismos que en S_cuad, pero sino aparecen entre []
#                 S_c1_5  = float(S_cuad1_5)
#                 S_c2_5  = float(S_cuad2_5)
#                 S_c3_5  = float(S_cuad3_5)
#                 S_c4_5  = float(S_cuad4_5)
#
# #PAra los niveles de 1,5 m, 3m, 5m y 7m
# #Leo los datos medios de U'w'
#                 flujo_uw_medio_7 = float(datos_flujos_medios['T_medio_7m'])
#
# #Calculo valores medios de U'w' de cada cuadrante
#                 flujo_cuad1_medio_7  = datos_flujos_cuad['flujo_uw_c1_7m'].mean(axis=0,skipna=True)
#                 flujo_cuad2_medio_7  = datos_flujos_cuad['flujo_uw_c2_7m'].mean(axis=0, skipna=True)
#                 flujo_cuad3_medio_7  = datos_flujos_cuad['flujo_uw_c3_7m'].mean(axis=0, skipna=True)
#                 flujo_cuad4_medio_7  = datos_flujos_cuad['flujo_uw_c4_7m'].mean(axis=0, skipna=True)
#
# #Calculo S de cada cuadrante, como el promedio de cada cuadrante (datos fuera de H)
# #dividido el promedio total (de todos los cuadrantes, con datos dentro y fuera de H)
#                 S_cuad1_7 = flujo_cuad1_medio_7 /flujo_uw_medio_7
#                 S_cuad2_7 = flujo_cuad2_medio_7 /flujo_uw_medio_7
#                 S_cuad3_7 = flujo_cuad3_medio_7 /flujo_uw_medio_7
#                 S_cuad4_7 = flujo_cuad4_medio_7 /flujo_uw_medio_7
#
# #Convierto los resultados a flotantes para guardarlos en un .csv (sino guarda los valores entre [])
# #Los valores de S_c son los mismos que en S_cuad, pero sino aparecen entre []
#                 S_c1_7  = float(S_cuad1_7)
#                 S_c2_7  = float(S_cuad2_7)
#                 S_c3_7  = float(S_cuad3_7)
#                 S_c4_7  = float(S_cuad4_7)
#
# #Guardo los resultados en un .csv
#                 resultados = (ruta_salida + datos + str(day) + '_' + str(arch) + '.csv')
#
#                 resultados_forma = "{dat1},{dat2},{dat3},{dat4},{dat5},{dat6},{dat7},{dat8},{dat9},{dat10},{dat11},{dat12},{dat13},{dat14},{dat15},{dat16},\n"
#
# #Escribo el encabezado del archivo (1er fila con los nombres de las variables de cada columna)
#                 f = open(resultados, 'w') #abro arch resultados como escritura
#                 head = 'S_c1_uw_1.5m,S_c2_uw_1.5m,S_cuad3_uw_1.5m,S_cuad4_uw_1.5m,S_c1_uw_3m,S_c2_uw_3m,S_cuad3_uw_3m,S_cuad4_uw_3m,S_c1_uw_5m,S_c2_uw_5m,S_cuad3_uw_5m,S_cuad4_uw_5m,S_c1_uw_7m,S_c2_uw_7m,S_cuad3_uw_7m,S_cuad4_uw_7m,\n' #encabezado
#                 f.write(head) #escribe el encabezado en el archivo
#                 f.close()
#
# #Agrego datos abajo del encabezado
#                 f = open(resultados, 'a') #abro de nuevo resultados pero como append
#                 dato = resultados_forma.format(dat1=S_c1_1_5,dat2=S_c2_1_5,dat3=S_c3_1_5,dat4=S_c4_1_5,\
#                 dat5=S_c1_3,dat6=S_c2_3,dat7=S_c3_3,dat8=S_c4_3,\
#                 dat9=S_c1_5,dat10=S_c2_5,dat11=S_c3_5,dat12=S_c4_5,\
#                 dat13=S_c1_7,dat14=S_c2_7,dat15=S_c3_7,dat16=S_c4_7)
#                 f.write(dato)
#                 f.close()
