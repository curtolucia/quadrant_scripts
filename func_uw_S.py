import pandas as pd
import math
import numpy as np

from func_aux import calc_S
#-------------------------------------------------------------------------------------------
#Defino funcion para calculo de los Si,0 para uw
#-------------------------------------------------------------------------------------------
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
def flujo_uw_S(totales_uw_cuad,flujos_medios):

    val_medios = totales_uw_cuad.mean(axis=0,skipna=True)
# Creo lista para almacenar los datos
    S_cuad_df = []
    # S_1_5 = []
    # S_3 = []
    # S_5 = []
    # S_7 = []

#Calculo S de cada cuadrante, como el promedio de cada cuadrante (H=0)
#dividido el promedio total (de todos los cuadrantes, H=0)
#para el nivel de 1.5 m
    cov = flujos_medios['cov_uw']
    cov_c1 = val_medios['cov_uw_c1']
    cov_c2 = val_medios['cov_uw_c2']
    cov_c3 = val_medios['cov_uw_c3']
    cov_c4 = val_medios['cov_uw_c4']

    S_c1, S_c2, S_c3, S_c4 = calc_S(cov_c1,cov_c2,cov_c3, cov_c4, cov)

    S_cuad_df = pd.DataFrame({
    'S_cuad1': [S_c1[0]],
    'S_cuad2': [S_c2[0]],
    'S_cuad3': [S_c3[0]],
    'S_cuad4': [S_c4[0]]})

    return S_cuad_df
#
# #para el nivel de 3 m
#     cov_3 = flujos_medios['cov_uw_3m']
#     cov_c1_3 = val_medios['cov_uw_c1_3m']
#     cov_c2_3 = val_medios['cov_uw_c2_3m']
#     cov_c3_3 = val_medios['cov_uw_c3_3m']
#     cov_c4_3 = val_medios['cov_uw_c4_3m']
#
#     S_uw_c1, S_uw_c2, S_uw_c3, S_uw_c4 = calc_S(cov_c1_3,cov_c2_3,cov_c3_3, cov_c4_3, cov_3)
# # Guardar los resultados en la variable 'S_inst_3'
#     S_3 = ([S_uw_c1[0], S_uw_c2[0], S_uw_c3[0], S_uw_c4[0]])
#     S_3_df = pd.DataFrame(S_3, index=['S_cuad1_3m','S_cuad2_3m','S_cuad3_3m','S_cuad4_3m']).T
#
# #para el nivel de 5 m
#     cov_5 = flujos_medios['cov_uw_5m']
#     cov_c1_5 = val_medios['cov_uw_c1_5m']
#     cov_c2_5 = val_medios['cov_uw_c2_5m']
#     cov_c3_5 = val_medios['cov_uw_c3_5m']
#     cov_c4_5 = val_medios['cov_uw_c4_5m']
#
#     S_uw_c1, S_uw_c2, S_uw_c3, S_uw_c4 = calc_S(cov_c1_5,cov_c2_5,cov_c3_5, cov_c4_5, cov_5)
# # Guardar los resultados en la variable 'S_inst_5'
#     S_5 = ([S_uw_c1[0], S_uw_c2[0], S_uw_c3[0], S_uw_c4[0]])
#     S_5_df = pd.DataFrame(S_5, index=['S_cuad1_5m','S_cuad2_5m','S_cuad3_5m','S_cuad4_5m']).T
#
# #para el nivel de 7 m
#     cov_7 = flujos_medios['cov_uw_7m']
#     cov_c1_7 = val_medios['cov_uw_c1_7m']
#     cov_c2_7 = val_medios['cov_uw_c2_7m']
#     cov_c3_7 = val_medios['cov_uw_c3_7m']
#     cov_c4_7 = val_medios['cov_uw_c4_7m']
#
#     S_uw_c1, S_uw_c2, S_uw_c3, S_uw_c4 = calc_S(cov_c1_7,cov_c2_7,cov_c3_7,cov_c4_7, cov_7)
# # Guardar los resultados en la variable 'S_inst_7'
#     S_7 = ([S_uw_c1[0], S_uw_c2[0], S_uw_c3[0], S_uw_c4[0]])
#     S_7_df = pd.DataFrame(S_7,  index=['S_cuad1_7m','S_cuad2_7m','S_cuad3_7m','S_cuad4_7m']).T
#
# #DataFrame con todos los niveles
# #S de cada cuadrante para uw (H=0)
# #para los niveles de 1.5 m, 3 m, 5 m y 7 m
#     S_cuad_uw = pd.concat([S_1_5_df, S_3_df, S_5_df, S_7_df], axis=1)
#     return S_cuad_uw
