import os
import pandas as pd

from func_uw_cuad import flujo_uw_cuad
from func_uw_S import flujo_uw_S
#
# from flujo_wT_cuad import flujo_wT_cuad
# from flujo_wT_S_H import flujo_wT_S_H

ruta_entrada_faltantes = '.././faltantes/2021-2022/SM_140/2021/03/'
ruta_entrada_calidad = '.././calidad/2021-2022/SM_140/2021/03/'

ruta_entrada_desvios = '.././desvios/2021-2022/SM_140/2021/03/'
ruta_entrada_medios = '.././medios/2021-2022/SM_140/2021/03/'

ruta_salida_cuad = '.././cuadrantes/flujo_uw/2021-2022/SM_140/2021/03/'
ruta_salida_S = '.././SiH/Si0/flujo_uw/2021-2022/SM_140/2021/03/'

#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_cuad):
    os.makedirs(ruta_salida_cuad)
#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_S):
    os.makedirs(ruta_salida_S)

datos = 'SM_140_2021-03-'

for day in range(31, 32):
    for arch in range(1430, 1500):
        if not os.path.isfile(ruta_entrada_desvios + datos + str(day) + '_' + str(arch).zfill(4) + '.csv'):
            continue
        else:
            flujos_desvios = pd.read_csv(ruta_entrada_desvios + datos + str(day) + '_' + str(arch).zfill(4) + \
            '.csv',header=0,na_values='NAN') #lee el archivo guardado
            flujos_medios = pd.read_csv(ruta_entrada_medios + datos + str(day) + '_' + str(arch).zfill(4) + \
            '.csv',header=0,na_values='NAN') #lee el archivo guardado

            calidad = pd.read_csv(ruta_entrada_calidad + datos + str(day) + '_' + str(arch).zfill(4) + \
            '.csv',header=0,na_values='NAN')
            faltantes = pd.read_csv(ruta_entrada_faltantes + datos + str(day) + '_' + str(arch).zfill(4) + \
            '.csv',header=0,na_values='NAN')

            lim_calidad = 250
            lim_faltantes = 30

            col_cov_uw = ['cov_uw_1.5m', 'cov_uw_3m', 'cov_uw_5m', 'cov_uw_7m']
            check_calidad = (calidad[col_cov_uw] < lim_calidad).all(axis=1)

            col_uw = ['u_1.5m', 'w_1.5m', 'u_3m', 'w_3m', 'u_5m', 'w_5m', \
            'u_7m', 'w_7m']
            check_faltantes = (faltantes[col_uw] < lim_faltantes).all(axis=1)

            totales_uw_cuad = flujo_uw_cuad(flujos_desvios)
            # totales_uw_cuad.to_csv (ruta_salida_cuad + datos + str(day) + '_' + str(arch) + '.csv', index=False)

            # if check_calidad.all() & check_faltantes.all():
            #
            #     totales_uw_cuad = flujo_uw_cuad(flujos_desvios)
            #     totales_uw_cuad.to_csv (ruta_salida_cuad + datos + str(day) + '_' + str(arch) + '.csv', index=False)
            #
            #     # S_uw_cuad = flujo_uw_S(totales_uw_cuad,flujos_medios)
            #     # S_uw_cuad.to_csv (ruta_salida_S + datos + str(day) + '_' + str(arch) + '.csv', index=False)
            #
            # else:
            #     continue

            # if check_calidad.all() & check_faltantes.all():
            #     print('true')
            # else:
            #     print('false')


#
# #Creo el directorio de salida (ruta_salida) si no existe
# if not os.path.exists(ruta_salida):
#     os.makedirs(ruta_salida)
# #Separo los flujos (U'w') por cuadrantes en 4 columnas
#
# flujo_uw_cuad(ruta_entrada, ruta_entrada_validos, ruta_salida, datos)
#
# #Separo los flujos (w'T') por cuadrantes
# ruta_entrada = './desvios/140/2021/03/'
# ruta_entrada_validos = './flujos_validos/140/2021/03/'
# ruta_salida = './cuadrantes/flujo_wT/140/2021/03/'
# datos = 'SM_140_2021-03-'
#
# #Creo el directorio de salida (ruta_salida) si no existe
# if not os.path.exists(ruta_salida):
#     os.makedirs(ruta_salida)
# #Separo los flujos (U'w') por cuadrantes en 4 columnas
#
# flujo_wT_cuad(ruta_entrada, ruta_entrada_validos, ruta_salida, datos)
#
# # Calculo S de cada cuadrante, la fraccion de las tensiones de Reynolds por cuadrante
# ruta_entrada_totales = './cuadrantes/flujo_uw/140/2021/03/'
# ruta_entrada_medios = './flujos_validos/140/2021/03/'
# ruta_salida = './SiH/Si0/flujo_uw/140/2021/03/'
# datos = 'SM_140_2021-03-'
# #Creo el directorio de salida (ruta_salida) si no existe
# if not os.path.exists(ruta_salida):
#     os.makedirs(ruta_salida)
# #Calculo S de cada cuadrante en 4 columnas
#
# flujo_uw_S_H(ruta_entrada_totales,ruta_entrada_medios,ruta_salida,datos)
#
# # Guardo los datos anteriores en una lista
# ruta_entrada = './SiH/Si0/flujo_uw/140/2021/03/'
# ruta_salida = './SiH/Si0/flujo_uw/140/2021/03/'
# datos = 'SM_140_2021-03-'
# #Creo el directorio de salida (ruta_salida) si no existe
# if not os.path.exists(ruta_salida):
#     os.makedirs(ruta_salida)
# #Calculo S de cada cuadrante en 4 columnas
# from list_flujo_uw_S_H import list_flujo_uw_S_H
# list_flujo_uw_S_H(ruta_entrada,ruta_salida,datos)
#
# #Calculo S de cada cuadrante, la fraccion de las tensiones de Reynolds por cuadrante
# ruta_entrada_totales = './cuadrantes/flujo_wT/140/2021/03/'
# ruta_entrada_medios = './flujos_validos/140/2021/03/'
# ruta_salida = './SiH/Si0/flujo_wT/140/2021/03/'
# datos = 'SM_140_2021-03-'
# #Creo el directorio de salida (ruta_salida) si no existe
# if not os.path.exists(ruta_salida):
#     os.makedirs(ruta_salida)
# #Calculo S de cada cuadrante en 4 columnas
#
# flujo_wT_S_H(ruta_entrada_totales,ruta_entrada_medios,ruta_salida,datos)
#
# # Guardo los datos anteriores en una lista
# ruta_entrada = './SiH/Si0/flujo_wT/140/2021/03/'
# ruta_salida = './SiH/Si0/flujo_wT/140/2021/03/'
# datos = 'SM_140_2021-03-'
# #Creo el directorio de salida (ruta_salida) si no existe
# if not os.path.exists(ruta_salida):
#     os.makedirs(ruta_salida)
# #Calculo S de cada cuadrante en 4 columnas
# from list_flujo_wT_S_H import list_flujo_wT_S_H
# list_flujo_wT_S_H(ruta_entrada,ruta_salida,datos)
