def flujo_wT_cuad(ruta_entrada, ruta_entrada_validos, ruta_salida, datos):

#Traigo las librerias que necesito
    import pandas as pd
    import math
    import os
    import numpy as np

    for day in range(21, 32):
        for arch in range(1, 2500):
            if not os.path.isfile(ruta_entrada_validos + datos + str(day) + '_' + str(arch) + '.csv'):
                continue
            else:
                datos_flujos_totales = pd.read_csv(ruta_entrada + datos + str(day) + '_' + \
                str(arch) + '.csv',header=0)

#Leo los datos de U', w' y T'
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
                u_desvio_1_5 = datos_flujos_totales['u_desvio_1.5m'].values
                u_desvio_3 = datos_flujos_totales['u_desvio_3m'].values
                u_desvio_5 = datos_flujos_totales['u_desvio_5m'].values
                u_desvio_7 = datos_flujos_totales['u_desvio_7m'].values

                w_desvio_1_5 = datos_flujos_totales['w_desvio_1.5m'].values
                w_desvio_3 = datos_flujos_totales['w_desvio_3m'].values
                w_desvio_5 = datos_flujos_totales['w_desvio_5m'].values
                w_desvio_7 = datos_flujos_totales['w_desvio_7m'].values

                T_desvio_1_5 = datos_flujos_totales['T_desvio_1.5m'].values
                T_desvio_3 = datos_flujos_totales['T_desvio_3m'].values
                T_desvio_5 = datos_flujos_totales['T_desvio_5m'].values
                T_desvio_7 = datos_flujos_totales['T_desvio_7m'].values
#leo u'w'
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
                flujo_uw_1_5 = datos_flujos_totales['flujo_uw_1.5m'].values
                flujo_uw_3 = datos_flujos_totales['flujo_uw_3m'].values
                flujo_uw_5 = datos_flujos_totales['flujo_uw_5m'].values
                flujo_uw_7 = datos_flujos_totales['flujo_uw_7m'].values

#leo w'T'
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
                flujo_wT_1_5 = datos_flujos_totales['flujo_wT_1.5m'].values
                flujo_wT_3 = datos_flujos_totales['flujo_wT_3m'].values
                flujo_wT_5 = datos_flujos_totales['flujo_wT_5m'].values
                flujo_wT_7 = datos_flujos_totales['flujo_wT_7m'].values

                resultados = (ruta_salida + datos + str(day) + '_' + str(arch) + '.csv')

#Creo una lista para los resultados
                resultados = [[],[],[],[],[],[],\
                [],[],[],[],[],[],\
                [],[],[],[],[],[],\
                [],[],[],[],[],[]]

                for i in range(0, len(T_desvio_1_5)):

#Separo por cuadrantes segun signo de U' y w'
#El archivo de salida (resultados) tiene 4 columnas, 1 por cuadrante, y pone el valor
#del flujo segun el cuadrante, y nan a los otros 3 cuadrantes, eso por cada fila de datos
                    if T_desvio_1_5[i] >= 0 and w_desvio_1_5[i] >= 0:
                        flujo_wT_c1_1_5 = flujo_wT_1_5[i]
                        flujo_wT_c2_1_5 = 0
                        flujo_wT_c3_1_5 = 0
                        flujo_wT_c4_1_5 = 0

                    elif T_desvio_1_5[i] < 0 and w_desvio_1_5[i] > 0:
                        flujo_wT_c1_1_5 = 0
                        flujo_wT_c2_1_5 = flujo_wT_1_5[i]
                        flujo_wT_c3_1_5 = 0
                        flujo_wT_c4_1_5 = 0

                    elif T_desvio_1_5[i] < 0 and w_desvio_1_5[i] < 0:
                        flujo_wT_c1_1_5 = 0
                        flujo_wT_c2_1_5 = 0
                        flujo_wT_c3_1_5 = flujo_wT_1_5[i]
                        flujo_wT_c4_1_5 = 0

                    elif T_desvio_1_5[i] > 0 and w_desvio_1_5[i] < 0:
                        flujo_wT_c1_1_5 = 0
                        flujo_wT_c2_1_5 = 0
                        flujo_wT_c3_1_5 = 0
                        flujo_wT_c4_1_5 = flujo_wT_1_5[i]

                    resultados[0].append(w_desvio_1_5[i])
                    resultados[1].append(T_desvio_1_5[i])
                    resultados[2].append(flujo_wT_c1_1_5)
                    resultados[3].append(flujo_wT_c2_1_5)
                    resultados[4].append(flujo_wT_c3_1_5)
                    resultados[5].append(flujo_wT_c4_1_5)

                for i in range(0, len(T_desvio_3)):

#Separo por cuadrantes segun signo de U' y w'
#El archivo de salida (resultados) tiene 4 columnas, 1 por cuadrante, y pone el valor
#del flujo segun el cuadrante, y nan a los otros 3 cuadrantes, eso por cada fila de datos
                    if T_desvio_3[i] >= 0 and w_desvio_3[i] >= 0:
                        flujo_wT_c1_3 = flujo_wT_3[i]
                        flujo_wT_c2_3 = 0
                        flujo_wT_c3_3 = 0
                        flujo_wT_c4_3 = 0

                    elif T_desvio_3[i] < 0 and w_desvio_3[i] > 0:
                        flujo_wT_c1_3 = 0
                        flujo_wT_c2_3 = flujo_wT_3[i]
                        flujo_wT_c3_3 = 0
                        flujo_wT_c4_3 = 0

                    elif T_desvio_3[i] < 0 and w_desvio_3[i] < 0:
                        flujo_wT_c1_3 = 0
                        flujo_wT_c2_3 = 0
                        flujo_wT_c3_3 = flujo_wT_3[i]
                        flujo_wT_c4_3 = 0

                    elif T_desvio_3[i] > 0 and w_desvio_3[i] < 0:
                        flujo_wT_c1_3 = 0
                        flujo_wT_c2_3 = 0
                        flujo_wT_c3_3 = 0
                        flujo_wT_c4_3 = flujo_wT_3[i]

                    resultados[6].append(w_desvio_3[i])
                    resultados[7].append(T_desvio_3[i])
                    resultados[8].append(flujo_wT_c1_3)
                    resultados[9].append(flujo_wT_c2_3)
                    resultados[10].append(flujo_wT_c3_3)
                    resultados[11].append(flujo_wT_c4_3)

                for i in range(0, len(T_desvio_5)):

#Separo por cuadrantes segun signo de U' y w'
#El archivo de salida (resultados) tiene 4 columnas, 1 por cuadrante, y pone el valor
#del flujo segun el cuadrante, y nan a los otros 3 cuadrantes, eso por cada fila de datos
                    if T_desvio_5[i] >= 0 and w_desvio_5[i] >= 0:
                        flujo_wT_c1_5 = flujo_wT_5[i]
                        flujo_wT_c2_5 = 0
                        flujo_wT_c3_5 = 0
                        flujo_wT_c4_5 = 0

                    elif T_desvio_5[i] < 0 and w_desvio_5[i] > 0:
                        flujo_wT_c1_5 = 0
                        flujo_wT_c2_5 = flujo_wT_5[i]
                        flujo_wT_c3_5 = 0
                        flujo_wT_c4_5 = 0

                    elif T_desvio_5[i] < 0 and w_desvio_5[i] < 0:
                        flujo_wT_c1_5 = 0
                        flujo_wT_c2_5 = 0
                        flujo_wT_c3_5 = flujo_wT_5[i]
                        flujo_wT_c4_5 = 0

                    elif T_desvio_5[i] > 0 and w_desvio_5[i] < 0:
                        flujo_wT_c1_5 = 0
                        flujo_wT_c2_5 = 0
                        flujo_wT_c3_5 = 0
                        flujo_wT_c4_5 = flujo_wT_5[i]

                    resultados[12].append(w_desvio_5[i])
                    resultados[13].append(T_desvio_5[i])
                    resultados[14].append(flujo_wT_c1_5)
                    resultados[15].append(flujo_wT_c2_5)
                    resultados[16].append(flujo_wT_c3_5)
                    resultados[17].append(flujo_wT_c4_5)

                for i in range(0, len(T_desvio_7)):

#Separo por cuadrantes segun signo de U' y w'
#El archivo de salida (resultados) tiene 4 columnas, 1 por cuadrante, y pone el valor
#del flujo segun el cuadrante, y nan a los otros 3 cuadrantes, eso por cada fila de datos
                    if T_desvio_7[i] >= 0 and w_desvio_7[i] >= 0:
                        flujo_wT_c1_7 = flujo_wT_7[i]
                        flujo_wT_c2_7 = 0
                        flujo_wT_c3_7 = 0
                        flujo_wT_c4_7 = 0

                    elif T_desvio_7[i] < 0 and w_desvio_7[i] > 0:
                        flujo_wT_c1_7 = 0
                        flujo_wT_c2_7 = flujo_wT_7[i]
                        flujo_wT_c3_7 = 0
                        flujo_wT_c4_7 = 0

                    elif T_desvio_7[i] < 0 and w_desvio_7[i] < 0:
                        flujo_wT_c1_7 = 0
                        flujo_wT_c2_7 = 0
                        flujo_wT_c3_7 = flujo_wT_7[i]
                        flujo_wT_c4_7 = 0

                    elif T_desvio_7[i] > 0 and w_desvio_7[i] < 0:
                        flujo_wT_c1_7 = 0
                        flujo_wT_c2_7 = 0
                        flujo_wT_c3_7 = 0
                        flujo_wT_c4_7 = flujo_wT_7[i]

                    resultados[18].append(w_desvio_7[i])
                    resultados[19].append(T_desvio_7[i])
                    resultados[20].append(flujo_wT_c1_7)
                    resultados[21].append(flujo_wT_c2_7)
                    resultados[22].append(flujo_wT_c3_7)
                    resultados[23].append(flujo_wT_c4_7)

            resultados_frame = pd.DataFrame({'w_desvio_1.5m':resultados[0],'T_desvio_1.5m':resultados[1],'flujo_wT_c1_1.5m':resultados[2],'flujo_wT_c2_1.5m':resultados[3],'flujo_wT_c3_1.5m':resultados[4],'flujo_wT_c4_1.5m':resultados[5],\
            'w_desvio_3m':resultados[6],'T_desvio_3m':resultados[7],'flujo_wT_c1_3m':resultados[8],'flujo_wT_c2_3m':resultados[9],'flujo_wT_c3_3m':resultados[10],'flujo_wT_c4_3m':resultados[11],\
            'w_desvio_5m':resultados[12],'T_desvio_5m':resultados[13],'flujo_wT_c1_5m':resultados[14],'flujo_wT_c2_5m':resultados[15],'flujo_wT_c3_5m':resultados[16],'flujo_wT_c4_5m':resultados[17],\
            'w_desvio_7m':resultados[18],'T_desvio_7m':resultados[19],'flujo_wT_c1_7m':resultados[20],'flujo_wT_c2_7m':resultados[21],'flujo_wT_c3_7m':resultados[22],'flujo_wT_c4_7m':resultados[23]})

            resultados_frame.to_csv(ruta_salida + datos + str(day) + '_' + str(arch) + '.csv', index=False)
