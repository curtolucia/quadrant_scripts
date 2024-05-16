import os
import pandas as pd
import numpy as np

# from func_aux import calc_cuad, calc_S
from func_uw_cuad import flujo_uw_cuad, flujo_uw_cuad_nan
from func_wT_cuad import flujo_wT_cuad, flujo_wT_cuad_nan
from func_wc_cuad import flujo_wc_cuad, flujo_wc_cuad_nan
from func_uw_S import flujo_uw_S
from func_wT_S import flujo_wT_S
from func_wc_S import flujo_wc_S

# from flujo_wT_cuad import flujo_wT_cuad
# from flujo_wT_S_H import flujo_wT_S_H

ruta_entrada_faltantes = '.././faltantes/2021-2022/SM_140/2022/08/'
ruta_entrada_calidad = '.././calidad/2021-2022/SM_140/2022/08/'

ruta_entrada_desvios = '.././desvios/2021-2022/SM_140/2022/08/'
ruta_entrada_medios = '.././medios/2021-2022/SM_140/2022/08/'

ruta_salida_cuad_uw = '.././cuadrantes/flujo_uw/2021-2022/SM_140/2022/08/'
ruta_salida_S_uw = '.././SiH/Si0/flujo_uw/2021-2022/SM_140/2022/08/'

#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_cuad_uw):
    os.makedirs(ruta_salida_cuad_uw)
#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_S_uw):
    os.makedirs(ruta_salida_S_uw)

ruta_salida_cuad_wT = '.././cuadrantes/flujo_wT/2021-2022/SM_140/2022/08/'
ruta_salida_S_wT = '.././SiH/Si0/flujo_wT/2021-2022/SM_140/2022/08/'

#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_cuad_wT):
    os.makedirs(ruta_salida_cuad_wT)
#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_S_wT):
    os.makedirs(ruta_salida_S_wT)

ruta_salida_cuad_wc = '.././cuadrantes/flujo_wc/2021-2022/SM_140/2022/08/'
ruta_salida_S_wc = '.././SiH/Si0/flujo_wc/2021-2022/SM_140/2022/08/'

#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_cuad_wc):
    os.makedirs(ruta_salida_cuad_wc)
#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_S_wc):
    os.makedirs(ruta_salida_S_wc)

datos = 'SM_140_2022-08-'

for day in range(1, 2):
    for arch in range(30, 2400):
        if not os.path.isfile(ruta_entrada_medios + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv'):
            continue
        else:
            flujos_desvios = pd.read_csv(ruta_entrada_desvios + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + \
            '.csv',header=0,na_values='NAN') #lee el archivo guardado
            flujos_medios = pd.read_csv(ruta_entrada_medios + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + \
            '.csv',header=0,na_values='NAN') #lee el archivo guardado

            calidad = pd.read_csv(ruta_entrada_calidad + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + \
            '.csv',header=0,na_values='NAN')
            faltantes = pd.read_csv(ruta_entrada_faltantes + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + \
            '.csv',header=0,na_values='NAN')

            lim_calidad = 250
            lim_faltantes = 30

# #-------------------------------------------------------------------------------------------
# #proceso para uw en 1.5m
# #chequeo de calidad de datos y faltantes
# # metodo de los cuadrantes
# #-------------------------------------------------------------------------------------------
#
#             col_cov_uw_1_5 = ['cov_uw_1.5m']
#             check_calidad_uw_1_5 = (calidad[col_cov_uw_1_5] < lim_calidad).all(axis=1)
#
#             col_uw_1_5 = ['u_1.5m', 'w_1.5m']
#             check_faltantes_uw_1_5 = (faltantes[col_uw_1_5] < lim_faltantes).all(axis=1)
#
#             flujos_desvio_1_5 = pd.DataFrame({
#             'u_desvio': flujos_desvios['u_desvio_1.5m'],
#             'w_desvio': flujos_desvios['w_desvio_1.5m'],
#             'cov_uw': flujos_desvios['cov_uw_1.5m']})
#
#             flujos_medios_1_5 = pd.DataFrame({'cov_uw': flujos_medios['cov_uw_1.5m']})
#
#             if check_calidad_uw_1_5.all() & check_calidad_uw_1_5.all():
#
#                 totales_uw_cuad_1_5 = flujo_uw_cuad(flujos_desvio_1_5)
#
#                 S_uw_cuad_1_5 = flujo_uw_S(totales_uw_cuad_1_5,flujos_medios_1_5)
#                 S_uw_cuad_1_5 = pd.DataFrame({
#                 'S_cuad1_1.5m': S_uw_cuad_1_5['S_cuad1'].values,
#                 'S_cuad2_1.5m': S_uw_cuad_1_5['S_cuad2'].values,
#                 'S_cuad3_1.5m': S_uw_cuad_1_5['S_cuad3'].values,
#                 'S_cuad4_1.5m': S_uw_cuad_1_5['S_cuad4'].values})
#
#                 totales_uw_cuad_1_5.columns = ['u_desvio_1.5m', 'w_desvio_1.5m', \
#                 'cov_uw_c1_1.5m', 'cov_uw_c2_1.5m', 'cov_uw_c3_1.5m', 'cov_uw_c4_1.5m']
#
#             else:
#
#                 totales_uw_cuad_1_5 = flujo_uw_cuad_nan(flujos_desvio_1_5)
#                 totales_uw_cuad_1_5.columns = ['u_desvio_1.5m', 'w_desvio_1.5m', \
#                 'cov_uw_c1_1.5m', 'cov_uw_c2_1.5m', 'cov_uw_c3_1.5m', 'cov_uw_c4_1.5m']
#
#                 S_uw_cuad_1_5 = pd.DataFrame({
#                 'S_cuad1_1.5m': [np.nan],
#                 'S_cuad2_1.5m': [np.nan],
#                 'S_cuad3_1.5m': [np.nan],
#                 'S_cuad4_1.5m': [np.nan]})
#
# #-------------------------------------------------------------------------------------------
# #proceso para uw en 3m
# #chequeo de calidad de datos y faltantes
# # metodo de los cuadrantes
# #-------------------------------------------------------------------------------------------
#
#             col_cov_uw_3 = ['cov_uw_3m']
#             check_calidad_uw_3 = (calidad[col_cov_uw_3] < lim_calidad).all(axis=1)
#
#             col_uw_3 = ['u_3m', 'w_3m']
#             check_faltantes_uw_3 = (faltantes[col_uw_3] < lim_faltantes).all(axis=1)
#
#             flujos_desvio_3 = pd.DataFrame({
#             'u_desvio': flujos_desvios['u_desvio_3m'],
#             'w_desvio': flujos_desvios['w_desvio_3m'],
#             'cov_uw': flujos_desvios['cov_uw_3m']})
#
#             flujos_medios_3 = pd.DataFrame({'cov_uw': flujos_medios['cov_uw_3m']})
#
#             if check_calidad_uw_3.all() & check_calidad_uw_3.all():
#
#                 totales_uw_cuad_3 = flujo_uw_cuad(flujos_desvio_3)
#
#                 S_uw_cuad_3 = flujo_uw_S(totales_uw_cuad_3,flujos_medios_3)
#                 S_uw_cuad_3 = pd.DataFrame({
#                 'S_cuad1_3m': S_uw_cuad_3['S_cuad1'].values,
#                 'S_cuad2_3m': S_uw_cuad_3['S_cuad2'].values,
#                 'S_cuad3_3m': S_uw_cuad_3['S_cuad3'].values,
#                 'S_cuad4_3m': S_uw_cuad_3['S_cuad4'].values})
#
#                 totales_uw_cuad_3.columns = ['u_desvio_3m', 'w_desvio_3m', \
#                 'cov_uw_c1_3m', 'cov_uw_c2_3m', 'cov_uw_c3_3m', 'cov_uw_c4_3m']
#
#             else:
#
#                 totales_uw_cuad_3 = flujo_uw_cuad_nan(flujos_desvio_3)
#                 totales_uw_cuad_3.columns = ['u_desvio_3m', 'w_desvio_3m', \
#                 'cov_uw_c1_3m', 'cov_uw_c2_3m', 'cov_uw_c3_3m', 'cov_uw_c4_3m']
#
#                 S_uw_cuad_3 = pd.DataFrame({
#                 'S_cuad1_3m': [np.nan],
#                 'S_cuad2_3m': [np.nan],
#                 'S_cuad3_3m': [np.nan],
#                 'S_cuad4_3m': [np.nan]})
#
# #-------------------------------------------------------------------------------------------
# #proceso para uw en 5m
# #chequeo de calidad de datos y faltantes
# # metodo de los cuadrantes
# #-------------------------------------------------------------------------------------------
#
#             col_cov_uw_5 = ['cov_uw_5m']
#             check_calidad_uw_5 = (calidad[col_cov_uw_5] < lim_calidad).all(axis=1)
#
#             col_uw_5 = ['u_5m', 'w_5m']
#             check_faltantes_uw_5 = (faltantes[col_uw_5] < lim_faltantes).all(axis=1)
#
#             flujos_desvio_5 = pd.DataFrame({
#             'u_desvio': flujos_desvios['u_desvio_5m'],
#             'w_desvio': flujos_desvios['w_desvio_5m'],
#             'cov_uw': flujos_desvios['cov_uw_5m']})
#
#             flujos_medios_5 = pd.DataFrame({'cov_uw': flujos_medios['cov_uw_5m']})
#
#             if check_calidad_uw_5.all() & check_calidad_uw_5.all():
#
#                 totales_uw_cuad_5 = flujo_uw_cuad(flujos_desvio_5)
#
#                 S_uw_cuad_5 = flujo_uw_S(totales_uw_cuad_5,flujos_medios_5)
#                 S_uw_cuad_5 = pd.DataFrame({
#                 'S_cuad1_5m': S_uw_cuad_5['S_cuad1'].values,
#                 'S_cuad2_5m': S_uw_cuad_5['S_cuad2'].values,
#                 'S_cuad3_5m': S_uw_cuad_5['S_cuad3'].values,
#                 'S_cuad4_5m': S_uw_cuad_5['S_cuad4'].values})
#
#                 totales_uw_cuad_5.columns = ['u_desvio_5m', 'w_desvio_5m', \
#                 'cov_uw_c1_5m', 'cov_uw_c2_5m', 'cov_uw_c3_5m', 'cov_uw_c4_5m']
#
#             else:
#
#                 totales_uw_cuad_5 = flujo_uw_cuad_nan(flujos_desvio_5)
#                 totales_uw_cuad_5.columns = ['u_desvio_5m', 'w_desvio_5m', \
#                 'cov_uw_c1_5m', 'cov_uw_c2_5m', 'cov_uw_c3_5m', 'cov_uw_c4_5m']
#
#                 S_uw_cuad_5 = pd.DataFrame({
#                 'S_cuad1_5m': [np.nan],
#                 'S_cuad2_5m': [np.nan],
#                 'S_cuad3_5m': [np.nan],
#                 'S_cuad4_5m': [np.nan]})
#
# #-------------------------------------------------------------------------------------------
# #proceso para uw en 7m
# #chequeo de calidad de datos y faltantes
# # metodo de los cuadrantes
# #-------------------------------------------------------------------------------------------
#
#             col_cov_uw_7 = ['cov_uw_7m']
#             check_calidad_uw_7 = (calidad[col_cov_uw_7] < lim_calidad).all(axis=1)
#
#             col_uw_7 = ['u_7m', 'w_7m']
#             check_faltantes_uw_7 = (faltantes[col_uw_7] < lim_faltantes).all(axis=1)
#
#             flujos_desvio_7 = pd.DataFrame({
#             'u_desvio': flujos_desvios['u_desvio_7m'],
#             'w_desvio': flujos_desvios['w_desvio_7m'],
#             'cov_uw': flujos_desvios['cov_uw_7m']})
#
#             flujos_medios_7 = pd.DataFrame({'cov_uw': flujos_medios['cov_uw_7m']})
#
#             if check_calidad_uw_7.all() & check_calidad_uw_7.all():
#
#                 totales_uw_cuad_7 = flujo_uw_cuad(flujos_desvio_7)
#
#                 S_uw_cuad_7 = flujo_uw_S(totales_uw_cuad_7,flujos_medios_7)
#                 S_uw_cuad_7 = pd.DataFrame({
#                 'S_cuad1_7m': S_uw_cuad_7['S_cuad1'].values,
#                 'S_cuad2_7m': S_uw_cuad_7['S_cuad2'].values,
#                 'S_cuad3_7m': S_uw_cuad_7['S_cuad3'].values,
#                 'S_cuad4_7m': S_uw_cuad_7['S_cuad4'].values})
#
#                 totales_uw_cuad_7.columns = ['u_desvio_7m', 'w_desvio_7m', \
#                 'cov_uw_c1_7m', 'cov_uw_c2_7m', 'cov_uw_c3_7m', 'cov_uw_c4_7m']
#
#             else:
#
#                 totales_uw_cuad_7 = flujo_uw_cuad_nan(flujos_desvio_7)
#                 totales_uw_cuad_7.columns = ['u_desvio_7m', 'w_desvio_7m', \
#                 'cov_uw_c1_7m', 'cov_uw_c2_7m', 'cov_uw_c3_7m', 'cov_uw_c4_7m']
#
#                 S_uw_cuad_7 = pd.DataFrame({
#                 'S_cuad1_7m': [np.nan],
#                 'S_cuad2_7m': [np.nan],
#                 'S_cuad3_7m': [np.nan],
#                 'S_cuad4_7m': [np.nan]})
#
# #-------------------------------------------------------------------------------------------
# #resultados de uw en 1.5m, 3m, 5m, 7m
# # metodo de los cuadrantes
# #Si
# #-------------------------------------------------------------------------------------------
#
#             totales_uw_cuad = pd.concat([totales_uw_cuad_1_5,\
#             totales_uw_cuad_3,totales_uw_cuad_5,totales_uw_cuad_7], axis=1)
#
#             totales_uw_cuad.to_csv (ruta_salida_cuad_uw + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False, na_rep='NAN')
#
#             S_uw_cuad = pd.concat([S_uw_cuad_1_5,\
#             S_uw_cuad_3,S_uw_cuad_5,S_uw_cuad_7], axis=1)
#
#             S_uw_cuad.to_csv (ruta_salida_S_uw + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False, na_rep='NAN')
#
# # #-------------------------------------------------------------------------------------------
# # #proceso para wT en 1.5m
# # #chequeo de calidad de datos y faltantes
# # # metodo de los cuadrantes
# # #-------------------------------------------------------------------------------------------
#
#             col_cov_wT_1_5 = ['cov_wT_1.5m']
#             check_calidad_wT_1_5 = (calidad[col_cov_wT_1_5] < lim_calidad).all(axis=1)
#
#             col_wT_1_5 = ['T_1.5m', 'w_1.5m']
#             check_faltantes_wT_1_5 = (faltantes[col_wT_1_5] < lim_faltantes).all(axis=1)
#
#             flujos_desvio_1_5 = pd.DataFrame({
#             'T_desvio': flujos_desvios['T_desvio_1.5m'],
#             'w_desvio': flujos_desvios['w_desvio_1.5m'],
#             'cov_wT': flujos_desvios['cov_wT_1.5m']})
#
#             flujos_medios_1_5 = pd.DataFrame({'cov_wT': flujos_medios['cov_wT_1.5m']})
#
#             if check_calidad_wT_1_5.all() & check_calidad_wT_1_5.all():
#
#                 totales_wT_cuad_1_5 = flujo_wT_cuad(flujos_desvio_1_5)
#
#                 S_wT_cuad_1_5 = flujo_wT_S(totales_wT_cuad_1_5,flujos_medios_1_5)
#                 S_wT_cuad_1_5 = pd.DataFrame({
#                 'S_cuad1_1.5m': S_wT_cuad_1_5['S_cuad1'].values,
#                 'S_cuad2_1.5m': S_wT_cuad_1_5['S_cuad2'].values,
#                 'S_cuad3_1.5m': S_wT_cuad_1_5['S_cuad3'].values,
#                 'S_cuad4_1.5m': S_wT_cuad_1_5['S_cuad4'].values})
#
#                 totales_wT_cuad_1_5.columns = ['T_desvio_1.5m', 'w_desvio_1.5m', \
#                 'cov_wT_c1_1.5m', 'cov_wT_c2_1.5m', 'cov_wT_c3_1.5m', 'cov_wT_c4_1.5m']
#
#             else:
#
#                 totales_wT_cuad_1_5 = flujo_wT_cuad_nan(flujos_desvio_1_5)
#                 totales_wT_cuad_1_5.columns = ['T_desvio_1.5m', 'w_desvio_1.5m', \
#                 'cov_wT_c1_1.5m', 'cov_wT_c2_1.5m', 'cov_wT_c3_1.5m', 'cov_wT_c4_1.5m']
#
#                 S_wT_cuad_1_5 = pd.DataFrame({
#                 'S_cuad1_1.5m': [np.nan],
#                 'S_cuad2_1.5m': [np.nan],
#                 'S_cuad3_1.5m': [np.nan],
#                 'S_cuad4_1.5m': [np.nan]})
#
# # #-------------------------------------------------------------------------------------------
# # #proceso para wT en 3m
# # #chequeo de calidad de datos y faltantes
# # # metodo de los cuadrantes
# # #-------------------------------------------------------------------------------------------
#
#             col_cov_wT_3 = ['cov_wT_3m']
#             check_calidad_wT_3 = (calidad[col_cov_wT_3] < lim_calidad).all(axis=1)
#
#             col_wT_3 = ['T_3m', 'w_3m']
#             check_faltantes_wT_3 = (faltantes[col_wT_3] < lim_faltantes).all(axis=1)
#
#             flujos_desvio_3 = pd.DataFrame({
#             'T_desvio': flujos_desvios['T_desvio_3m'],
#             'w_desvio': flujos_desvios['w_desvio_3m'],
#             'cov_wT': flujos_desvios['cov_wT_3m']})
#
#             flujos_medios_3 = pd.DataFrame({'cov_wT': flujos_medios['cov_wT_3m']})
#
#             if check_calidad_wT_3.all() & check_calidad_wT_3.all():
#
#                 totales_wT_cuad_3 = flujo_wT_cuad(flujos_desvio_3)
#
#                 S_wT_cuad_3 = flujo_wT_S(totales_wT_cuad_3,flujos_medios_3)
#                 S_wT_cuad_3 = pd.DataFrame({
#                 'S_cuad1_3m': S_wT_cuad_3['S_cuad1'].values,
#                 'S_cuad2_3m': S_wT_cuad_3['S_cuad2'].values,
#                 'S_cuad3_3m': S_wT_cuad_3['S_cuad3'].values,
#                 'S_cuad4_3m': S_wT_cuad_3['S_cuad4'].values})
#
#                 totales_wT_cuad_3.columns = ['T_desvio_3m', 'w_desvio_3m', \
#                 'cov_wT_c1_3m', 'cov_wT_c2_3m', 'cov_wT_c3_3m', 'cov_wT_c4_3m']
#
#             else:
#
#                 totales_wT_cuad_3 = flujo_wT_cuad_nan(flujos_desvio_3)
#                 totales_wT_cuad_3.columns = ['T_desvio_3m', 'w_desvio_3m', \
#                 'cov_wT_c1_3m', 'cov_wT_c2_3m', 'cov_wT_c3_3m', 'cov_wT_c4_3m']
#
#                 S_wT_cuad_3 = pd.DataFrame({
#                 'S_cuad1_3m': [np.nan],
#                 'S_cuad2_3m': [np.nan],
#                 'S_cuad3_3m': [np.nan],
#                 'S_cuad4_3m': [np.nan]})
#
# # #-------------------------------------------------------------------------------------------
# # #proceso para wT en 5m
# # #chequeo de calidad de datos y faltantes
# # # metodo de los cuadrantes
# # #-------------------------------------------------------------------------------------------
#
#             col_cov_wT_5 = ['cov_wT_5m']
#             check_calidad_wT_5 = (calidad[col_cov_wT_5] < lim_calidad).all(axis=1)
#
#             col_wT_5 = ['T_5m', 'w_5m']
#             check_faltantes_wT_5 = (faltantes[col_wT_5] < lim_faltantes).all(axis=1)
#
#             flujos_desvio_5 = pd.DataFrame({
#             'T_desvio': flujos_desvios['T_desvio_5m'],
#             'w_desvio': flujos_desvios['w_desvio_5m'],
#             'cov_wT': flujos_desvios['cov_wT_5m']})
#
#             flujos_medios_5 = pd.DataFrame({'cov_wT': flujos_medios['cov_wT_5m']})
#
#             if check_calidad_wT_5.all() & check_calidad_wT_5.all():
#
#                 totales_wT_cuad_5 = flujo_wT_cuad(flujos_desvio_5)
#
#                 S_wT_cuad_5 = flujo_wT_S(totales_wT_cuad_5,flujos_medios_5)
#                 S_wT_cuad_5 = pd.DataFrame({
#                 'S_cuad1_5m': S_wT_cuad_5['S_cuad1'].values,
#                 'S_cuad2_5m': S_wT_cuad_5['S_cuad2'].values,
#                 'S_cuad3_5m': S_wT_cuad_5['S_cuad3'].values,
#                 'S_cuad4_5m': S_wT_cuad_5['S_cuad4'].values})
#
#                 totales_wT_cuad_5.columns = ['T_desvio_5m', 'w_desvio_5m', \
#                 'cov_wT_c1_5m', 'cov_wT_c2_5m', 'cov_wT_c3_5m', 'cov_wT_c4_5m']
#
#             else:
#
#                 totales_wT_cuad_5 = flujo_wT_cuad_nan(flujos_desvio_5)
#                 totales_wT_cuad_5.columns = ['T_desvio_5m', 'w_desvio_5m', \
#                 'cov_wT_c1_5m', 'cov_wT_c2_5m', 'cov_wT_c3_5m', 'cov_wT_c4_5m']
#
#                 S_wT_cuad_5 = pd.DataFrame({
#                 'S_cuad1_5m': [np.nan],
#                 'S_cuad2_5m': [np.nan],
#                 'S_cuad3_5m': [np.nan],
#                 'S_cuad4_5m': [np.nan]})
#
# # #-------------------------------------------------------------------------------------------
# # #proceso para wT en 7m
# # #chequeo de calidad de datos y faltantes
# # # metodo de los cuadrantes
# # #-------------------------------------------------------------------------------------------
#
#             col_cov_wT_7 = ['cov_wT_7m']
#             check_calidad_wT_7 = (calidad[col_cov_wT_7] < lim_calidad).all(axis=1)
#
#             col_wT_7 = ['T_7m', 'w_7m']
#             check_faltantes_wT_7 = (faltantes[col_wT_7] < lim_faltantes).all(axis=1)
#
#             flujos_desvio_7 = pd.DataFrame({
#             'T_desvio': flujos_desvios['T_desvio_7m'],
#             'w_desvio': flujos_desvios['w_desvio_7m'],
#             'cov_wT': flujos_desvios['cov_wT_7m']})
#
#             flujos_medios_7 = pd.DataFrame({'cov_wT': flujos_medios['cov_wT_7m']})
#
#             if check_calidad_wT_7.all() & check_calidad_wT_7.all():
#
#                 totales_wT_cuad_7 = flujo_wT_cuad(flujos_desvio_7)
#
#                 S_wT_cuad_7 = flujo_wT_S(totales_wT_cuad_7,flujos_medios_7)
#                 S_wT_cuad_7 = pd.DataFrame({
#                 'S_cuad1_7m': S_wT_cuad_7['S_cuad1'].values,
#                 'S_cuad2_7m': S_wT_cuad_7['S_cuad2'].values,
#                 'S_cuad3_7m': S_wT_cuad_7['S_cuad3'].values,
#                 'S_cuad4_7m': S_wT_cuad_7['S_cuad4'].values})
#
#                 totales_wT_cuad_7.columns = ['T_desvio_7m', 'w_desvio_7m', \
#                 'cov_wT_c1_7m', 'cov_wT_c2_7m', 'cov_wT_c3_7m', 'cov_wT_c4_7m']
#
#             else:
#
#                 totales_wT_cuad_7 = flujo_wT_cuad_nan(flujos_desvio_7)
#                 totales_wT_cuad_7.columns = ['T_desvio_7m', 'w_desvio_7m', \
#                 'cov_wT_c1_7m', 'cov_wT_c2_7m', 'cov_wT_c3_7m', 'cov_wT_c4_7m']
#
#                 S_wT_cuad_7 = pd.DataFrame({
#                 'S_cuad1_7m': [np.nan],
#                 'S_cuad2_7m': [np.nan],
#                 'S_cuad3_7m': [np.nan],
#                 'S_cuad4_7m': [np.nan]})
#
# #-------------------------------------------------------------------------------------------
# #resultados de wT en 1.5m, 3m, 5m, 7m
# # metodo de los cuadrantes
# #Si
# #-------------------------------------------------------------------------------------------
#
#             totales_wT_cuad = pd.concat([totales_wT_cuad_1_5,\
#             totales_wT_cuad_3,totales_wT_cuad_5,totales_wT_cuad_7], axis=1)
#
#             totales_wT_cuad.to_csv (ruta_salida_cuad_wT + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False, na_rep='NAN')
#
#             S_wT_cuad = pd.concat([S_wT_cuad_1_5,\
#             S_wT_cuad_3,S_wT_cuad_5,S_wT_cuad_7], axis=1)
#
#             S_wT_cuad.to_csv (ruta_salida_S_wT + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False, na_rep='NAN')

#-------------------------------------------------------------------------------------------
#proceso para wc (wT, wCO2 y wq) en 3m
#chequeo de calidad de datos y faltantes
# metodo de los cuadrantes
#-------------------------------------------------------------------------------------------

            col_cov_wc = ['cov_wT_3m', 'cov_wCO2_3m', 'cov_wq_3m']
            check_calidad_wc = (calidad[col_cov_wc] < lim_calidad).all(axis=1)

            col_wc = ['T_3m', 'w_3m', 'CO2_3m', 'H2O_3m']
            check_faltantes_wc = (faltantes[col_wc] < lim_faltantes).all(axis=1)

            flujos_desvio_3 = pd.DataFrame({
            'T_desvio': flujos_desvios['T_desvio_3m'],
            'w_desvio': flujos_desvios['w_desvio_3m'],
            'q_desvio': flujos_desvios['q_desvio_3m'],
            'CO2_desvio': flujos_desvios['CO2_desvio_3m'],
            'cov_wT': flujos_desvios['cov_wT_3m'],
            'cov_wq': flujos_desvios['cov_wq_3m'],
            'cov_wCO2': flujos_desvios['cov_wCO2_3m']})

            flujos_medios_3 = pd.DataFrame({
            'cov_wT': flujos_medios['cov_wT_3m'],
            'cov_wCO2': flujos_medios['cov_wCO2_3m'],
            'cov_wq': flujos_medios['cov_wq_3m']})

            if check_calidad_wc.all() & check_calidad_wc.all():

                totales_wc_cuad_3 = flujo_wc_cuad(flujos_desvio_3)

                S_wc_cuad_3 = flujo_wc_S(totales_wc_cuad_3,flujos_medios_3)
                S_wc_cuad_3 = pd.DataFrame({
                'S_T_cuad1_3m': S_wc_cuad_3['S_T_cuad1'].values,
                'S_T_cuad2_3m': S_wc_cuad_3['S_T_cuad2'].values,
                'S_T_cuad3_3m': S_wc_cuad_3['S_T_cuad3'].values,
                'S_T_cuad4_3m': S_wc_cuad_3['S_T_cuad4'].values,
                'S_CO2_cuad1_3m': S_wc_cuad_3['S_CO2_cuad1'].values,
                'S_CO2_cuad2_3m': S_wc_cuad_3['S_CO2_cuad2'].values,
                'S_CO2_cuad3_3m': S_wc_cuad_3['S_CO2_cuad3'].values,
                'S_CO2_cuad4_3m': S_wc_cuad_3['S_CO2_cuad4'].values,
                'S_q_cuad1_3m': S_wc_cuad_3['S_q_cuad1'].values,
                'S_q_cuad2_3m': S_wc_cuad_3['S_q_cuad2'].values,
                'S_q_cuad3_3m': S_wc_cuad_3['S_q_cuad3'].values,
                'S_q_cuad4_3m': S_wc_cuad_3['S_q_cuad4'].values})

                totales_wc_cuad_3.columns = ['w_desvio_3m', \
                'T_desvio_3m', 'CO2_desvio_3m', 'q_desvio_3m', \
                'cov_wT_c1_3m', 'cov_wT_c2_3m', 'cov_wT_c3_3m', 'cov_wT_c4_3m', \
                'cov_wCO2_c1_3m', 'cov_wCO2_c2_3m', 'cov_wCO2_c3_3m', 'cov_wCO2_c4_3m', \
                'cov_wq_c1_3m', 'cov_wq_c2_3m', 'cov_wq_c3_3m', 'cov_wq_c4_3m']

            else:

                totales_wc_cuad_3 = flujo_wc_cuad_nan(flujos_desvio_3)
                totales_wc_cuad_3.columns = ['w_desvio_3m', \
                'T_desvio_3m', 'CO2_desvio_3m', 'q_desvio_3m', \
                'cov_wT_c1_3m', 'cov_wT_c2_3m', 'cov_wT_c3_3m', 'cov_wT_c4_3m', \
                'cov_wCO2_c1_3m', 'cov_wCO2_c2_3m', 'cov_wCO2_c3_3m', 'cov_wCO2_c4_3m', \
                'cov_wq_c1_3m', 'cov_wq_c2_3m', 'cov_wq_c3_3m', 'cov_wq_c4_3m']

                S_wc_cuad_3 = pd.DataFrame({
                'S_T_cuad1_3m': [np.nan],
                'S_T_cuad2_3m': [np.nan],
                'S_T_cuad3_3m': [np.nan],
                'S_T_cuad4_3m': [np.nan],
                'S_CO2_cuad1_3m': [np.nan],
                'S_CO2_cuad2_3m': [np.nan],
                'S_CO2_cuad3_3m': [np.nan],
                'S_CO2_cuad4_3m': [np.nan],
                'S_q_cuad1_3m': [np.nan],
                'S_q_cuad2_3m': [np.nan],
                'S_q_cuad3_3m': [np.nan],
                'S_q_cuad4_3m': [np.nan]})

#-------------------------------------------------------------------------------------------
#resultados para wc (wT, wCO2 y wq) en 3m
# metodo de los cuadrantes
#Si
#-------------------------------------------------------------------------------------------

            totales_wc_cuad_3.to_csv (ruta_salida_cuad_wc + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False, na_rep='NAN')

            S_wc_cuad_3.to_csv (ruta_salida_S_wc + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False, na_rep='NAN')

# #-------------------------------------------------------------------------------------------
# # metodo de los cuadrantes para wc (wCO2 y wq)
# #-------------------------------------------------------------------------------------------
# # para el nivel de 3 m
#             if check_calidad_wc.all() & check_faltantes_wc.all():
#
#                 totales_wc_cuad = flujo_wc_cuad(flujos_desvios)
#                 totales_wc_cuad.to_csv (ruta_salida_cuad_wc + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False)
#
#                 S_wc_cuad = flujo_wc_S(totales_wc_cuad,flujos_medios)
#                 S_wc_cuad.to_csv (ruta_salida_S_wc + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False)
#
#             else:
#                 continue


# #-------------------------------------------------------------------------------------------
# #chequeo de calidad de datos y faltantes para uw
# #-------------------------------------------------------------------------------------------
#             col_cov_uw = ['cov_uw_1.5m', 'cov_uw_3m', 'cov_uw_5m', 'cov_uw_7m']
#             check_calidad_uw = (calidad[col_cov_uw] < lim_calidad).all(axis=1)
#
#             col_uw = ['u_1.5m', 'w_1.5m', 'u_3m', 'w_3m', 'u_5m', 'w_5m', \
#             'u_7m', 'w_7m']
#             check_faltantes_uw = (faltantes[col_uw] < lim_faltantes).all(axis=1)
#
#
# #-------------------------------------------------------------------------------------------
# # metodo de los cuadrantes para uw
# #-------------------------------------------------------------------------------------------
# #para los niveles de 1.5 m, 3 m, 5 m y 7 m
#             if check_calidad_uw.all() & check_faltantes_uw.all():
#
#                 totales_uw_cuad = flujo_uw_cuad(flujos_desvios)
#                 totales_uw_cuad.to_csv (ruta_salida_cuad_uw + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False)
#
#                 S_uw_cuad = flujo_uw_S(totales_uw_cuad,flujos_medios)
#                 S_uw_cuad.to_csv (ruta_salida_S_uw + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False)
#
#             else:
#                 continue
#
# #-------------------------------------------------------------------------------------------
# #chequeo de calidad de datos y faltantes para wT
# #-------------------------------------------------------------------------------------------
#             col_cov_wT = ['cov_wT_1.5m', 'cov_wT_3m', 'cov_wT_5m', 'cov_wT_7m']
#             check_calidad_wT = (calidad[col_cov_wT] < lim_calidad).all(axis=1)
#
#             col_wT = ['T_1.5m', 'w_1.5m', 'T_3m', 'w_3m', 'T_5m', 'w_5m', \
#             'T_7m', 'w_7m']
#             check_faltantes_wT = (faltantes[col_wT] < lim_faltantes).all(axis=1)
#
# #-------------------------------------------------------------------------------------------
# # metodo de los cuadrantes para wT
# #-------------------------------------------------------------------------------------------
# #para los niveles de 1.5 m, 3 m, 5 m y 7 m
#             if check_calidad_wT.all() & check_faltantes_wT.all():
#
#                 totales_wT_cuad = flujo_wT_cuad(flujos_desvios)
#                 totales_wT_cuad.to_csv (ruta_salida_cuad_wT + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False)
#
#                 S_wT_cuad = flujo_wT_S(totales_wT_cuad,flujos_medios)
#                 S_wT_cuad.to_csv (ruta_salida_S_wT + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False)
#
#             else:
#                 continue
#
# #-------------------------------------------------------------------------------------------
# #chequeo de calidad de datos y faltantes para wc (wCO2 y wq)
# #-------------------------------------------------------------------------------------------
#             col_cov_wc = ['cov_wT_3m', 'cov_wCO2_3m', 'cov_wq_3m']
#             check_calidad_wc = (calidad[col_cov_wc] < lim_calidad).all(axis=1)
#
#             col_wc = ['T_3m', 'w_3m', 'CO2_3m', 'H2O_3m']
#             check_faltantes_wc = (faltantes[col_wc] < lim_faltantes).all(axis=1)
#
# #-------------------------------------------------------------------------------------------
# # metodo de los cuadrantes para wc (wCO2 y wq)
# #-------------------------------------------------------------------------------------------
# # para el nivel de 3 m
#             if check_calidad_wc.all() & check_faltantes_wc.all():
#
#                 totales_wc_cuad = flujo_wc_cuad(flujos_desvios)
#                 totales_wc_cuad.to_csv (ruta_salida_cuad_wc + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False)
#
#                 S_wc_cuad = flujo_wc_S(totales_wc_cuad,flujos_medios)
#                 S_wc_cuad.to_csv (ruta_salida_S_wc + datos + str(day).zfill(2) + '_' + str(arch).zfill(4) + '.csv', index=False)
#
#             else:
#                 continue
