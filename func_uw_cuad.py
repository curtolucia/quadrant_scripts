#Traigo las librerias que necesito
import pandas as pd
import math
import numpy as np

#Defino una funcion para separar las covarianzas por cuadrantes
# def calc_cuad(u, w, cov_uw):
#
#     u_w_c1 = np.where((u >= 0) & (w >= 0), cov_uw, 0)
#     u_w_c2 = np.where((u < 0) & (w > 0), cov_uw, 0)
#     u_w_c3 = np.where((u < 0) & (w < 0), cov_uw, 0)
#     u_w_c4 = np.where((u > 0) & (w < 0), cov_uw, 0)
#
#     return u_w_c1, u_w_c2, u_w_c3, u_w_c4


def flujo_uw_cuad(flujos_desvios):

    flujos_desvios = flujos_desvios.copy()

#leo de los archivos las columnas correspondientes a U
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    u_desvio_1_5 = flujos_desvios['u_desvio_1.5m']
    u_desvio_3 = flujos_desvios['u_desvio_3m']
    u_desvio_5 = flujos_desvios['u_desvio_5m']
    u_desvio_7 = flujos_desvios['u_desvio_7m']

#leo de los archivos las columnas correspondientes a v
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    v_desvio_1_5 = flujos_desvios['v_desvio_1.5m']
    v_desvio_3 = flujos_desvios['v_desvio_3m']
    v_desvio_5 = flujos_desvios['v_desvio_5m']
    v_desvio_7 = flujos_desvios['v_desvio_7m']

#leo de los archivos las columnas correspondientes a w
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    w_desvio_1_5 = flujos_desvios['w_desvio_1.5m']
    w_desvio_3 = flujos_desvios['w_desvio_3m']
    w_desvio_5 = flujos_desvios['w_desvio_5m']
    w_desvio_7 = flujos_desvios['w_desvio_7m']

#leo las cov de cantidad de movimiento u'w' y v'w'
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    cov_uw_1_5 = flujos_desvios['cov_uw_1.5m']
    cov_uw_3 = flujos_desvios['cov_uw_3m']
    cov_uw_5 = flujos_desvios['cov_uw_5m']
    cov_uw_7 = flujos_desvios['cov_uw_7m']

    cov_vw_1_5 = flujos_desvios['cov_vw_1.5m']
    cov_vw_3 = flujos_desvios['cov_vw_3m']
    cov_vw_5 = flujos_desvios['cov_vw_5m']
    cov_vw_7 = flujos_desvios['cov_vw_7m']

# # Creo lista para almacenar los datos
    cuad_inst = []
    cuad_inst_1_5 = []
    cuad_inst_3 = []
    cuad_inst_5 = []
    cuad_inst_7 = []


# Definir los nombres de las columnas de u_desvio y w_desvio
    columnas_u_desvio = ['u_desvio_1.5m', 'u_desvio_3m', 'u_desvio_5m', 'u_desvio_7m']
    columnas_w_desvio = ['w_desvio_1.5m', 'w_desvio_3m', 'w_desvio_5m', 'w_desvio_7m']
    columnas_cov_desvio = ['cov_uw_1.5m', 'cov_uw_3m', 'cov_uw_5m', 'cov_uw_7m']

    # Iterar sobre los nombres de las columnas
    for u_desvio_1_5, w_desvio_1_5, cov_vw_1_5 in zip(u_desvio_1_5, w_desvio_1_5, cov_vw_1_5):
        # Extraer las columnas de u_desvio y w_desvio
        # u_desvio = u_desvio_1_5
        # w_desvio = w_desvio_1_5
        # cov_uw = flujos_desvios[col_uw]

        # Calcular los cuadrantes para las columnas de u_desvio y w_desvio
        cov_uw_c1 = np.where((u_desvio_1_5 >= 0) & (w_desvio_1_5 >= 0), cov_uw_1_5, 0)
        cov_uw_c2 = np.where((u_desvio_1_5 < 0) & (w_desvio_1_5 > 0), cov_uw_1_5, 0)
        cov_uw_c3 = np.where((u_desvio_1_5 < 0) & (w_desvio_1_5 < 0), cov_uw_1_5, 0)
        cov_uw_c4 = np.where((u_desvio_1_5 > 0) & (w_desvio_1_5 < 0), cov_uw_1_5, 0)
        # Guardar los resultados en 'resultados'
        # cov_uw_c = pd.concat([pd.DataFrame(cov_uw_c1),pd.DataFrame(cov_uw_c2),pd.DataFrame(cov_uw_c3),pd.DataFrame(cov_uw_c4)])

        cuad_inst_1_5.append([cov_uw_c1,cov_uw_c2,cov_uw_c3,cov_uw_c4])

    # for u_desvio_3, w_desvio_3, cov_vw_3 in zip(u_desvio_3, w_desvio_3, cov_vw_3):
    #     # Extraer las columnas de u_desvio y w_desvio
    #     u_desvio = pd.Series(u_desvio_3)
    #     w_desvio = pd.Series(w_desvio_3)
    #     # cov_uw = flujos_desvios[col_uw]
    #
    #     # Calcular los cuadrantes para las columnas de u_desvio y w_desvio
    #     cov_uw_c1 = pd.Series(np.where((u_desvio_3 >= 0) & (w_desvio_3 >= 0), cov_uw_3, 0))
    #     cov_uw_c2 = pd.Series(np.where((u_desvio_3 < 0) & (w_desvio_3 > 0), cov_uw_3, 0))
    #     cov_uw_c3 = pd.Series(np.where((u_desvio_3 < 0) & (w_desvio_3 < 0), cov_uw_3, 0))
    #     cov_uw_c4 = pd.Series(np.where((u_desvio_3 > 0) & (w_desvio_3 < 0), cov_uw_3, 0))
    #
    #     # Guardar los resultados en 'resultados'
    #     cov_uw_c = pd.DataFrame({
    #     'u_desvio_1.5m': u_desvio, # Incluir la columna 'u_desvio'
    #     'w_desvio_1.5m': w_desvio,
    #     'cov_uw_c1_1.5m': cov_uw_c1,
    #     'cov_uw_c2_1.5m': cov_uw_c2,
    #     'cov_uw_c3_1.5m': cov_uw_c3,
    #     'cov_uw_c4_1.5m': cov_uw_c4,
    #       # Incluir la columna 'w_desvio'
    # }u_desvio, w_desvio,cov_uw_c1,cov_uw_c2,cov_uw_c3,cov_uw_c4)
    #     cuad_inst_3.append(cov_uw_c)

    # resultado_final = pd.concat(cuad_inst_1_5, axis=0)
    print(cuad_inst_1_5)
    return resultado_final
#Con el for recorro los datos de u'w' separando por cuadrantes
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    # for u_1_5, w_1_5, u_3, w_3, u_5, w_5, u_7, w_7\
    #  in zip(u_desvio_1_5, w_desvio_1_5, u_desvio_3, w_desvio_3, u_desvio_5, w_desvio_5, u_desvio_7, w_desvio_7):
    #
    #     cov_uw_c1_1_5, cov_uw_c2_1_5, cov_uw_c3_1_5, cov_uw_c4_1_5 = calc_cuad(u_1_5,w_1_5,cov_uw_1_5)
    #     cuad_inst_1_5.append([u_1_5, w_1_5, cov_uw_c1_1_5, cov_uw_c2_1_5, cov_uw_c3_1_5, cov_uw_c4_1_5])
    #
    # # for u_3, w_3 in zip(u_desvio_3, w_desvio_3):
    #     cov_uw_c1_3, cov_uw_c2_3, cov_uw_c3_3, cov_uw_c4_3 = calc_cuad(u_3,w_3,cov_uw_3)
    #     cuad_inst_3.append([u_3, w_3, cov_uw_c1_3, cov_uw_c2_3, cov_uw_c3_3, cov_uw_c4_3)]
    #
    # # for u_5, w_5 in zip(u_desvio_5, w_desvio_5):
    #     cov_uw_c1_5, cov_uw_c2_5, cov_uw_c3_5, cov_uw_c4_5 = calc_cuad(u_5,w_5,cov_uw_5)
    #     cuad_inst_5.append([u_5, w_5, cov_uw_c1_5, cov_uw_c2_5, cov_uw_c3_5, cov_uw_c4_5])
    #
    # # for u_7, w_7 in zip(u_desvio_7, w_desvio_7):
    #     cov_uw_c1_7, cov_uw_c2_7, cov_uw_c3_7, cov_uw_c4_7 = calc_cuad(u_7,w_7,cov_uw_7)
    #     cuad_inst_7.append([u_7, w_7, cov_uw_c1_7, cov_uw_c2_7, cov_uw_c3_7, cov_uw_c4_7])
    #
    # cuad_inst = pd.concat([cuad_inst_1_5, cuad_inst_3, cuad_inst_5, cuad_inst_7])
    #
    #
    # cuad_inst_df = pd.DataFrame(cuad_inst, columns=['u_desvio_1.5m', 'w_desvio_1.5m', \
    # 'cov_uw_c1_1.5m', 'cov_uw_c2_1.5m', 'cov_uw_c3_1.5m', 'cov_uw_c4_1.5m', \
    # 'u_desvio_3m', 'w_desvio_3m', \
    # 'cov_uw_c1_3m', 'cov_uw_c2_3m', 'cov_uw_c3_3m', 'cov_uw_c4_3m', \
    # 'u_desvio_5m', 'w_desvio_5m', \
    # 'cov_uw_c1_5m', 'cov_uw_c2_5m', 'cov_uw_c3_5m', 'cov_uw_c4_5m', \
    # 'u_desvio_7m', 'w_desvio_7m', \
    # 'cov_uw_c1_7m', 'cov_uw_c2_7m', 'cov_uw_c3_7m', 'cov_uw_c4_7m'])
    #
    # return cuad_inst_df
    # return cuad_inst_1_5


# Iterar sobre los datos
# para el nivel de 1.5 m
#     for u_1_5, w_1_5 in zip(u_desvio_1_5, w_desvio_1_5):
#
#         if u_1_5 >= 0 and w_1_5 >= 0:
#             cov_uw_c1_1_5 = cov_uw_1_5
#             cov_uw_c2_1_5 = 0
#             cov_uw_c3_1_5 = 0
#             cov_uw_c4_1_5 = 0
#
#         elif u_1_5 < 0 and w_1_5 > 0:
#             cov_uw_c1_1_5 = 0
#             cov_uw_c2_1_5 = cov_uw_1_5
#             cov_uw_c3_1_5 = 0
#             cov_uw_c4_1_5 = 0
#
#         elif u_1_5 < 0 and w_1_5 < 0:
#             cov_uw_c1_1_5 = 0
#             cov_uw_c2_1_5 = 0
#             cov_uw_c3_1_5 = cov_uw_1_5
#             cov_uw_c4_1_5 = 0
#
#         elif u_1_5 > 0 and w_1_5 < 0:
#             cov_uw_c1_1_5 = 0
#             cov_uw_c2_1_5 = 0
#             cov_uw_c3_1_5 = 0
#             cov_uw_c4_1_5 = cov_uw_1_5
#
#         cuad_inst_1_5.append([u_1_5, w_1_5, cov_uw_c1_1_5, cov_uw_c2_1_5, cov_uw_c3_1_5, cov_uw_c4_1_5])
#         cuad_inst_1_5_df = pd.DataFrame(cuad_inst_1_5)
#
#
# # Iterar sobre los datos
# # para el nivel de 3 m
#     for u_3, w_3 in zip(u_desvio_3, w_desvio_3):
#
#         if u_3 >= 0 and w_3 >= 0:
#             cov_uw_c1_3 = cov_uw_3
#             cov_uw_c2_3 = 0
#             cov_uw_c3_3 = 0
#             cov_uw_c4_3 = 0
#
#         elif u_3 < 0 and w_3 > 0:
#             cov_uw_c1_3 = 0
#             cov_uw_c2_3 = cov_uw_3
#             cov_uw_c3_3 = 0
#             cov_uw_c4_3 = 0
#
#         elif u_3 < 0 and w_3 < 0:
#             cov_uw_c1_3 = 0
#             cov_uw_c2_3 = 0
#             cov_uw_c3_3 = cov_uw_3
#             cov_uw_c4_3 = 0
#
#         elif u_3 > 0 and w_3 < 0:
#             cov_uw_c1_3 = 0
#             cov_uw_c2_3 = 0
#             cov_uw_c3_3 = 0
#             cov_uw_c4_3 = cov_uw_3
#
#         cuad_inst_3.append([u_3, w_3, cov_uw_c1_3, cov_uw_c2_3, cov_uw_c3_3, cov_uw_c4_3])
#         cuad_inst_3_df = pd.DataFrame(cuad_inst_3)
#
# # Iterar sobre los datos
# # para el nivel de 5 m
#     for u_5, w_5 in zip(u_desvio_5, w_desvio_5):
#
#         if u_5 >= 0 and w_5 >= 0:
#             cov_uw_c1_5 = cov_uw_5
#             cov_uw_c2_5 = 0
#             cov_uw_c3_5 = 0
#             cov_uw_c4_5 = 0
#
#         elif u_5 < 0 and w_5 > 0:
#             cov_uw_c1_5 = 0
#             cov_uw_c2_5 = cov_uw_5
#             cov_uw_c3_5 = 0
#             cov_uw_c4_5 = 0
#
#         elif u_5 < 0 and w_5 < 0:
#             cov_uw_c1_5 = 0
#             cov_uw_c2_5 = 0
#             cov_uw_c3_5 = cov_uw_5
#             cov_uw_c4_5 = 0
#
#         elif u_5 > 0 and w_5 < 0:
#             cov_uw_c1_5 = 0
#             cov_uw_c2_5 = 0
#             cov_uw_c3_5 = 0
#             cov_uw_c4_5 = cov_uw_5
#
#         cuad_inst_5.append([u_5, w_5, cov_uw_c1_5, cov_uw_c2_5, cov_uw_c3_5, cov_uw_c4_5])
#         cuad_inst_5_df = pd.DataFrame(cuad_inst_5)
#
# # Iterar sobre los datos
# # para el nivel de 5 m
#     for u_7, w_7 in zip(u_desvio_7, w_desvio_7):
#
#         if u_7 >= 0 and w_7 >= 0:
#             cov_uw_c1_7 = cov_uw_7
#             cov_uw_c2_7 = 0
#             cov_uw_c3_7 = 0
#             cov_uw_c4_7 = 0
#
#         elif u_7 < 0 and w_7 > 0:
#             cov_uw_c1_7 = 0
#             cov_uw_c2_7 = cov_uw_7
#             cov_uw_c3_7 = 0
#             cov_uw_c4_7 = 0
#
#         elif u_7 < 0 and w_7 < 0:
#             cov_uw_c1_7 = 0
#             cov_uw_c2_7 = 0
#             cov_uw_c3_7 = cov_uw_7
#             cov_uw_c4_7 = 0
#
#         elif u_7 > 0 and w_7 < 0:
#             cov_uw_c1_7 = 0
#             cov_uw_c2_7 = 0
#             cov_uw_c3_7 = 0
#             cov_uw_c4_7 = cov_uw_7
#
#         cuad_inst_7.append([u_7, w_7, cov_uw_c1_7, cov_uw_c2_7, cov_uw_c3_7, cov_uw_c4_7])
#         cuad_inst_7_df = pd.DataFrame(cuad_inst_7)
#
#     cuad_inst = pd.concat([cuad_inst_1_5_df, cuad_inst_3_df, cuad_inst_5_df, cuad_inst_7_df])
#
#     # Agregar los resultados a la lista de resultados
#     # cuad_inst.append((u_1_5, w_1_5, cov_uw_c1_1_5, cov_uw_c2_1_5, cov_uw_c3_1_5, cov_uw_c4_1_5,\
#     # u_3, w_3, cov_uw_c1_3, cov_uw_c2_3, cov_uw_c3_3, cov_uw_c4_3,\
#     # u_5, w_5, cov_uw_c1_5, cov_uw_c2_5, cov_uw_c3_5, cov_uw_c4_5,\
#     # u_7, w_7, cov_uw_c1_7, cov_uw_c2_7, cov_uw_c3_7, cov_uw_c4_7))
#     #voy por aca, tengo que hacer los otros niveles y los v'w'
#     cuad_inst_df = pd.DataFrame(cuad_inst, columns=['u_desvio_1.5m', 'w_desvio_1.5m', \
#     'cov_uw_c1_1.5m', 'cov_uw_c2_1.5m', 'cov_uw_c3_1.5m', 'cov_uw_c4_1.5m', \
#     'u_desvio_3m', 'w_desvio_3m', \
#     'cov_uw_c1_3m', 'cov_uw_c2_3m', 'cov_uw_c3_3m', 'cov_uw_c4_3m', \
#     'u_desvio_5m', 'w_desvio_5m', \
#     'cov_uw_c1_5m', 'cov_uw_c2_5m', 'cov_uw_c3_5m', 'cov_uw_c4_5m', \
#     'u_desvio_7m', 'w_desvio_7m', \
#     'cov_uw_c1_7m', 'cov_uw_c2_7m', 'cov_uw_c3_7m', 'cov_uw_c4_7m'])
#
# #    cuad_inst_df = pd.DataFrame(cuad_inst, columns=['u_desvio_1_5', 'w_desvio_1_5', 'flujo_uw_c1_1_5', 'flujo_uw_c2_1_5', 'flujo_uw_c3_1_5', 'flujo_uw_c4_1_5'])
#     return cuad_inst_df
#

# def flujo_uw_cuad(flujos_desvios, calidad, cuad_inst):
#
#
#
#     for day in range(21, 32):
#         for arch in range(1, 2500):
#             if not os.path.isfile(ruta_entrada_validos + datos + str(day) + '_' + str(arch) + '.csv'):
#                 continue
#             else:
#                 datos_flujos_totales = pd.read_csv(ruta_entrada + datos + str(day) + '_' + \
#                 str(arch) + '.csv',header=0)
#
# #Leo los datos de U', w' y T'
# #para los niveles de 1.5 m, 3 m, 5 m y 7 m
#                 u_desvio_1_5 = datos_flujos_totales['u_desvio_1.5m'].values
#                 u_desvio_3 = datos_flujos_totales['u_desvio_3m'].values
#                 u_desvio_5 = datos_flujos_totales['u_desvio_5m'].values
#                 u_desvio_7 = datos_flujos_totales['u_desvio_7m'].values
#
#                 w_desvio_1_5 = datos_flujos_totales['w_desvio_1.5m'].values
#                 w_desvio_3 = datos_flujos_totales['w_desvio_3m'].values
#                 w_desvio_5 = datos_flujos_totales['w_desvio_5m'].values
#                 w_desvio_7 = datos_flujos_totales['w_desvio_7m'].values
#
#                 T_desvio_1_5 = datos_flujos_totales['T_desvio_1.5m'].values
#                 T_desvio_3 = datos_flujos_totales['T_desvio_3m'].values
#                 T_desvio_5 = datos_flujos_totales['T_desvio_5m'].values
#                 T_desvio_7 = datos_flujos_totales['T_desvio_7m'].values
# #leo u'w'
# #para los niveles de 1.5 m, 3 m, 5 m y 7 m
#                 flujo_uw_1_5 = datos_flujos_totales['flujo_uw_1.5m'].values
#                 flujo_uw_3 = datos_flujos_totales['flujo_uw_3m'].values
#                 flujo_uw_5 = datos_flujos_totales['flujo_uw_5m'].values
#                 flujo_uw_7 = datos_flujos_totales['flujo_uw_7m'].values
#
# #leo w'T'
# #para los niveles de 1.5 m, 3 m, 5 m y 7 m
#                 flujo_wT_1_5 = datos_flujos_totales['flujo_wT_1.5m'].values
#                 flujo_wT_3 = datos_flujos_totales['flujo_wT_3m'].values
#                 flujo_wT_5 = datos_flujos_totales['flujo_wT_5m'].values
#                 flujo_wT_7 = datos_flujos_totales['flujo_wT_7m'].values
#
#
# #Creo una lista para los resultados
#                 resultados = [[],[],[],[],[],[],\
#                 [],[],[],[],[],[],\
#                 [],[],[],[],[],[],\
#                 [],[],[],[],[],[]]
#
#                 for i in range(0, len(u_desvio_1_5)):
#
# #Separo por cuadrantes segun signo de U' y w'
# #El archivo de salida (resultados) tiene 4 columnas, 1 por cuadrante, y pone el valor
# #del flujo segun el cuadrante, y nan a los otros 3 cuadrantes, eso por cada fila de datos
#                     if u_desvio_1_5[i] >= 0 and w_desvio_1_5[i] >= 0:
#                         flujo_uw_c1_1_5 = flujo_uw_1_5[i]
#                         flujo_uw_c2_1_5 = 0
#                         flujo_uw_c3_1_5 = 0
#                         flujo_uw_c4_1_5 = 0
#
#                     elif u_desvio_1_5[i] < 0 and w_desvio_1_5[i] > 0:
#                         flujo_uw_c1_1_5 = 0
#                         flujo_uw_c2_1_5 = flujo_uw_1_5[i]
#                         flujo_uw_c3_1_5 = 0
#                         flujo_uw_c4_1_5 = 0
#
#                     elif u_desvio_1_5[i] < 0 and w_desvio_1_5[i] < 0:
#                         flujo_uw_c1_1_5 = 0
#                         flujo_uw_c2_1_5 = 0
#                         flujo_uw_c3_1_5 = flujo_uw_1_5[i]
#                         flujo_uw_c4_1_5 = 0
#
#                     elif u_desvio_1_5[i] > 0 and w_desvio_1_5[i] < 0:
#                         flujo_uw_c1_1_5 = 0
#                         flujo_uw_c2_1_5 = 0
#                         flujo_uw_c3_1_5 = 0
#                         flujo_uw_c4_1_5 = flujo_uw_1_5[i]
#
#                     resultados[0].append(u_desvio_1_5[i])
#                     resultados[1].append(w_desvio_1_5[i])
#                     resultados[2].append(flujo_uw_c1_1_5)
#                     resultados[3].append(flujo_uw_c2_1_5)
#                     resultados[4].append(flujo_uw_c3_1_5)
#                     resultados[5].append(flujo_uw_c4_1_5)
#
#
#                 for i in range(0, len(u_desvio_3)):
#
# #Separo por cuadrantes segun signo de U' y w'
# #El archivo de salida (resultados) tiene 4 columnas, 1 por cuadrante, y pone el valor
# #del flujo segun el cuadrante, y nan a los otros 3 cuadrantes, eso por cada fila de datos
#                     if u_desvio_3[i] >= 0 and w_desvio_3[i] >= 0:
#                         flujo_uw_c1_3 = flujo_uw_3[i]
#                         flujo_uw_c2_3 = 0
#                         flujo_uw_c3_3 = 0
#                         flujo_uw_c4_3 = 0
#
#                     elif u_desvio_3[i] < 0 and w_desvio_3[i] > 0:
#                         flujo_uw_c1_3 = 0
#                         flujo_uw_c2_3 = flujo_uw_3[i]
#                         flujo_uw_c3_3 = 0
#                         flujo_uw_c4_3 = 0
#
#                     elif u_desvio_3[i] < 0 and w_desvio_3[i] < 0:
#                         flujo_uw_c1_3 = 0
#                         flujo_uw_c2_3 = 0
#                         flujo_uw_c3_3 = flujo_uw_3[i]
#                         flujo_uw_c4_3 = 0
#
#                     elif u_desvio_3[i] > 0 and w_desvio_3[i] < 0:
#                         flujo_uw_c1_3 = 0
#                         flujo_uw_c2_3 = 0
#                         flujo_uw_c3_3 = 0
#                         flujo_uw_c4_3 = flujo_uw_3[i]
#
#                     resultados[6].append(u_desvio_3[i])
#                     resultados[7].append(w_desvio_3[i])
#                     resultados[8].append(flujo_uw_c1_3)
#                     resultados[9].append(flujo_uw_c2_3)
#                     resultados[10].append(flujo_uw_c3_3)
#                     resultados[11].append(flujo_uw_c4_3)
#
#                 for i in range(0, len(u_desvio_5)):
#
# #Separo por cuadrantes segun signo de U' y w'
# #El archivo de salida (resultados) tiene 4 columnas, 1 por cuadrante, y pone el valor
# #del flujo segun el cuadrante, y nan a los otros 3 cuadrantes, eso por cada fila de datos
#                     if u_desvio_5[i] >= 0 and w_desvio_5[i] >= 0:
#                         flujo_uw_c1_5 = flujo_uw_5[i]
#                         flujo_uw_c2_5 = 0
#                         flujo_uw_c3_5 = 0
#                         flujo_uw_c4_5 = 0
#
#                     elif u_desvio_5[i] < 0 and w_desvio_5[i] > 0:
#                         flujo_uw_c1_5 = 0
#                         flujo_uw_c2_5 = flujo_uw_5[i]
#                         flujo_uw_c3_5 = 0
#                         flujo_uw_c4_5 = 0
#
#                     elif u_desvio_5[i] < 0 and w_desvio_5[i] < 0:
#                         flujo_uw_c1_5 = 0
#                         flujo_uw_c2_5 = 0
#                         flujo_uw_c3_5 = flujo_uw_5[i]
#                         flujo_uw_c4_5 = 0
#
#                     elif u_desvio_5[i] > 0 and w_desvio_5[i] < 0:
#                         flujo_uw_c1_5 = 0
#                         flujo_uw_c2_5 = 0
#                         flujo_uw_c3_5 = 0
#                         flujo_uw_c4_5 = flujo_uw_5[i]
#
#                     resultados[12].append(u_desvio_5[i])
#                     resultados[13].append(w_desvio_5[i])
#                     resultados[14].append(flujo_uw_c1_5)
#                     resultados[15].append(flujo_uw_c2_5)
#                     resultados[16].append(flujo_uw_c3_5)
#                     resultados[17].append(flujo_uw_c4_5)
#
#                 for i in range(0, len(u_desvio_7)):
#
# #Separo por cuadrantes segun signo de U' y w'
# #El archivo de salida (resultados) tiene 4 columnas, 1 por cuadrante, y pone el valor
# #del flujo segun el cuadrante, y nan a los otros 3 cuadrantes, eso por cada fila de datos
#                     if u_desvio_7[i] >= 0 and w_desvio_7[i] >= 0:
#                         flujo_uw_c1_7 = flujo_uw_7[i]
#                         flujo_uw_c2_7 = 0
#                         flujo_uw_c3_7 = 0
#                         flujo_uw_c4_7 = 0
#
#                     elif u_desvio_7[i] < 0 and w_desvio_7[i] > 0:
#                         flujo_uw_c1_7 = 0
#                         flujo_uw_c2_7 = flujo_uw_7[i]
#                         flujo_uw_c3_7 = 0
#                         flujo_uw_c4_7 = 0
#
#                     elif u_desvio_7[i] < 0 and w_desvio_7[i] < 0:
#                         flujo_uw_c1_7 = 0
#                         flujo_uw_c2_7 = 0
#                         flujo_uw_c3_7 = flujo_uw_7[i]
#                         flujo_uw_c4_7 = 0
#
#                     elif u_desvio_7[i] > 0 and w_desvio_7[i] < 0:
#                         flujo_uw_c1_7 = 0
#                         flujo_uw_c2_7 = 0
#                         flujo_uw_c3_7 = 0
#                         flujo_uw_c4_7 = flujo_uw_7[i]
#
#                     resultados[18].append(u_desvio_7[i])
#                     resultados[19].append(w_desvio_7[i])
#                     resultados[20].append(flujo_uw_c1_7)
#                     resultados[21].append(flujo_uw_c2_7)
#                     resultados[22].append(flujo_uw_c3_7)
#                     resultados[23].append(flujo_uw_c4_7)
#
#
#                 resultados_frame = pd.DataFrame({'u_desvio_1.5m':resultados[0],'w_desvio_1.5m':resultados[1],'flujo_uw_c1_1.5m':resultados[2],'flujo_uw_c2_1.5m':resultados[3],'flujo_uw_c3_1.5m':resultados[4],'flujo_uw_c4_1.5m':resultados[5],\
#                 'u_desvio_3m':resultados[6],'w_desvio_3m':resultados[7],'flujo_uw_c1_3m':resultados[8],'flujo_uw_c2_3m':resultados[9],'flujo_uw_c3_3m':resultados[10],'flujo_uw_c4_3m':resultados[11],\
#                 'u_desvio_5m':resultados[12],'w_desvio_5m':resultados[13],'flujo_uw_c1_5m':resultados[14],'flujo_uw_c2_5m':resultados[15],'flujo_uw_c3_5m':resultados[16],'flujo_uw_c4_5m':resultados[17],\
#                 'u_desvio_7m':resultados[18],'w_desvio_7m':resultados[19],'flujo_uw_c1_7m':resultados[20],'flujo_uw_c2_7m':resultados[21],'flujo_uw_c3_7m':resultados[22],'flujo_uw_c4_7m':resultados[23]})
#
#                 resultados_frame.to_csv(ruta_salida + datos + str(day) + '_' + str(arch) + '.csv', index=False)
