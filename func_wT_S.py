import pandas as pd
import math

def flujo_wT_S(totales_wT_cuad,flujos_medios):

    val_medios = totales_wT_cuad.mean(axis=0,skipna=True)
# Creo lista para almacenar los datos
    S_cuad_wT = []
    S_1_5 = []
    S_3 = []
    S_5 = []
    S_7 = []
#Calculo S de cada cuadrante, como el promedio de cada cuadrante (H=0)
#dividido el promedio total (de todos los cuadrantes, H=0)
#para el nivel de 1.5 m
    cov_1_5 = flujos_medios['cov_wT_1.5m']
    cov_c1_1_5 = val_medios['cov_wT_c1_1.5m']
    cov_c2_1_5 = val_medios['cov_wT_c2_1.5m']
    cov_c3_1_5 = val_medios['cov_wT_c3_1.5m']
    cov_c4_1_5 = val_medios['cov_wT_c4_1.5m']

    S_wT_c1, S_wT_c2, S_wT_c3, S_wT_c4 = calc_S(cov_c1_1_5,cov_c2_1_5,cov_c3_1_5, cov_c4_1_5, cov_1_5)
    # Guardar los resultados en la variable 'cuad_inst_1_5'
    # S_1_5 = {'columnas': ['S_cuad1','S_cuad2','S_cuad3','S_cuad4'],
    # 'valores': [S_wT_c1[0], S_wT_c2[0], S_wT_c3[0], S_wT_c4[0]]}
    S_1_5 = ([S_wT_c1[0], S_wT_c2[0], S_wT_c3[0], S_wT_c4[0]])
    S_1_5_df = pd.DataFrame(S_1_5, index=['S_cuad1_1.5m','S_cuad2_1.5m','S_cuad3_1.5m','S_cuad4_1.5m']).T

#para el nivel de 3 m
    cov_3 = flujos_medios['cov_wT_3m']
    cov_c1_3 = val_medios['cov_wT_c1_3m']
    cov_c2_3 = val_medios['cov_wT_c2_3m']
    cov_c3_3 = val_medios['cov_wT_c3_3m']
    cov_c4_3 = val_medios['cov_wT_c4_3m']

    S_wT_c1, S_wT_c2, S_wT_c3, S_wT_c4 = calc_S(cov_c1_3,cov_c2_3,cov_c3_3, cov_c4_3, cov_3)
    S_3 = ([S_wT_c1[0], S_wT_c2[0], S_wT_c3[0], S_wT_c4[0]])
    S_3_df = pd.DataFrame(S_3, index=['S_cuad1_3m','S_cuad2_3m','S_cuad3_3m','S_cuad4_3m']).T

#para el nivel de 5 m
    cov_5 = flujos_medios['cov_wT_5m']
    cov_c1_5 = val_medios['cov_wT_c1_5m']
    cov_c2_5 = val_medios['cov_wT_c2_5m']
    cov_c3_5 = val_medios['cov_wT_c3_5m']
    cov_c4_5 = val_medios['cov_wT_c4_5m']

    S_wT_c1, S_wT_c2, S_wT_c3, S_wT_c4 = calc_S(cov_c1_5,cov_c2_5,cov_c3_5, cov_c4_5, cov_5)
    S_5 = ([S_wT_c1[0], S_wT_c2[0], S_wT_c3[0], S_wT_c4[0]])
    S_5_df = pd.DataFrame(S_5, index=['S_cuad1_5m','S_cuad2_5m','S_cuad3_5m','S_cuad4_5m']).T

#para el nivel de 7 m
    cov_7 = flujos_medios['cov_wT_7m']
    cov_c1_7 = val_medios['cov_wT_c1_7m']
    cov_c2_7 = val_medios['cov_wT_c2_7m']
    cov_c3_7 = val_medios['cov_wT_c3_7m']
    cov_c4_7 = val_medios['cov_wT_c4_7m']

    S_wT_c1, S_wT_c2, S_wT_c3, S_wT_c4 = calc_S(cov_c1_7,cov_c2_7,cov_c3_7,cov_c4_7, cov_7)
    S_7 = ([S_wT_c1[0], S_wT_c2[0], S_wT_c3[0], S_wT_c4[0]])
    S_7_df = pd.DataFrame(S_7,  index=['S_cuad1_7m','S_cuad2_7m','S_cuad3_7m','S_cuad4_7m']).T

#DataFrame con todos los niveles
#S de cada cuadrante para wT (H=0)
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    S_cuad_wT = pd.concat([S_1_5_df, S_3_df, S_5_df, S_7_df], axis=1)

    return S_cuad_wT


#     #for n in range(180, 181):
#     #for n in range(936, 937):
#     #for n in range(1363, 1364):
#     for day in range(21, 32):
#         for arch in range(1100, 1110):
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
#                 flujo_wT_medio_1_5 = float(datos_flujos_medios['flujo_uw_medio_1.5m'])
#
# #Calculo valores medios de U'w' de cada cuadrante
#                 flujo_cuad1_medio_1_5  = datos_flujos_cuad['flujo_wT_c1_1.5m'].mean(axis=0,skipna=True)
#                 flujo_cuad2_medio_1_5  = datos_flujos_cuad['flujo_wT_c2_1.5m'].mean(axis=0, skipna=True)
#                 flujo_cuad3_medio_1_5  = datos_flujos_cuad['flujo_wT_c3_1.5m'].mean(axis=0, skipna=True)
#                 flujo_cuad4_medio_1_5  = datos_flujos_cuad['flujo_wT_c4_1.5m'].mean(axis=0, skipna=True)
#
#                 print(flujo_cuad4_medio_1_5)
#
# #Calculo S de cada cuadrante, como el promedio de cada cuadrante (datos fuera de H)
# #dividido el promedio total (de todos los cuadrantes, con datos dentro y fuera de H)
#                 S_cuad1_1_5 = flujo_cuad1_medio_1_5 /flujo_wT_medio_1_5
#                 S_cuad2_1_5 = flujo_cuad2_medio_1_5 /flujo_wT_medio_1_5
#                 S_cuad3_1_5 = flujo_cuad3_medio_1_5 /flujo_wT_medio_1_5
#                 S_cuad4_1_5 = flujo_cuad4_medio_1_5 /flujo_wT_medio_1_5
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
#                 flujo_wT_medio_3 = float(datos_flujos_medios['flujo_uw_medio_3m'])
#
# #Calculo valores medios de U'w' de cada cuadrante
#                 flujo_cuad1_medio_3  = datos_flujos_cuad['flujo_wT_c1_3m'].mean(axis=0,skipna=True)
#                 flujo_cuad2_medio_3  = datos_flujos_cuad['flujo_wT_c2_3m'].mean(axis=0, skipna=True)
#                 flujo_cuad3_medio_3  = datos_flujos_cuad['flujo_wT_c3_3m'].mean(axis=0, skipna=True)
#                 flujo_cuad4_medio_3  = datos_flujos_cuad['flujo_wT_c4_3m'].mean(axis=0, skipna=True)
#
# #Calculo S de cada cuadrante, como el promedio de cada cuadrante (datos fuera de H)
# #dividido el promedio total (de todos los cuadrantes, con datos dentro y fuera de H)
#                 S_cuad1_3 = flujo_cuad1_medio_3 /flujo_wT_medio_3
#                 S_cuad2_3 = flujo_cuad2_medio_3 /flujo_wT_medio_3
#                 S_cuad3_3 = flujo_cuad3_medio_3 /flujo_wT_medio_3
#                 S_cuad4_3 = flujo_cuad4_medio_3 /flujo_wT_medio_3
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
#                 flujo_wT_medio_5 = float(datos_flujos_medios['flujo_uw_medio_5m'])
#
# #Calculo valores medios de U'w' de cada cuadrante
#                 flujo_cuad1_medio_5  = datos_flujos_cuad['flujo_wT_c1_5m'].mean(axis=0,skipna=True)
#                 flujo_cuad2_medio_5  = datos_flujos_cuad['flujo_wT_c2_5m'].mean(axis=0, skipna=True)
#                 flujo_cuad3_medio_5  = datos_flujos_cuad['flujo_wT_c3_5m'].mean(axis=0, skipna=True)
#                 flujo_cuad4_medio_5  = datos_flujos_cuad['flujo_wT_c4_5m'].mean(axis=0, skipna=True)
#
# #Calculo S de cada cuadrante, como el promedio de cada cuadrante (datos fuera de H)
# #dividido el promedio total (de todos los cuadrantes, con datos dentro y fuera de H)
#                 S_cuad1_5 = flujo_cuad1_medio_5 /flujo_wT_medio_5
#                 S_cuad2_5 = flujo_cuad2_medio_5 /flujo_wT_medio_5
#                 S_cuad3_5 = flujo_cuad3_medio_5 /flujo_wT_medio_5
#                 S_cuad4_5 = flujo_cuad4_medio_5 /flujo_wT_medio_5
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
#                 flujo_wT_medio_7 = float(datos_flujos_medios['flujo_uw_medio_7m'])
#
#
# #Calculo valores medios de U'w' de cada cuadrante
#                 flujo_cuad1_medio_7  = datos_flujos_cuad['flujo_wT_c1_7m'].mean(axis=0,skipna=True)
#                 flujo_cuad2_medio_7  = datos_flujos_cuad['flujo_wT_c2_7m'].mean(axis=0, skipna=True)
#                 flujo_cuad3_medio_7  = datos_flujos_cuad['flujo_wT_c3_7m'].mean(axis=0, skipna=True)
#                 flujo_cuad4_medio_7  = datos_flujos_cuad['flujo_wT_c4_7m'].mean(axis=0, skipna=True)
#
# #Calculo S de cada cuadrante, como el promedio de cada cuadrante (datos fuera de H)
# #dividido el promedio total (de todos los cuadrantes, con datos dentro y fuera de H)
#                 S_cuad1_7 = flujo_cuad1_medio_7 /flujo_wT_medio_7
#                 S_cuad2_7 = flujo_cuad2_medio_7 /flujo_wT_medio_7
#                 S_cuad3_7 = flujo_cuad3_medio_7 /flujo_wT_medio_7
#                 S_cuad4_7 = flujo_cuad4_medio_7 /flujo_wT_medio_7
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
#                 head = 'S_c1_wT_1.5m,S_c2_wT_1.5m,S_cuad3_wT_1.5m,S_cuad4_wT_1.5m,S_c1_wT_3m,S_c2_wT_3m,S_cuad3_wT_3m,S_cuad4_wT_3m,S_c1_wT_5m,S_c2_wT_5m,S_cuad3_wT_5m,S_cuad4_wT_5m,S_c1_wT_7m,S_c2_wT_7m,S_cuad3_wT_7m,S_cuad4_wT_7m,\n' #encabezado
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
