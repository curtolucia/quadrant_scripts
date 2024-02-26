import os
import pandas as pd

# from func_aux import calc_cuad, calc_S
from func_uw_cuad import flujo_uw_cuad
from func_wT_cuad import flujo_wT_cuad
from func_wc_cuad import flujo_wc_cuad
from func_uw_S import flujo_uw_S
from func_wT_S import flujo_wT_S
from func_wc_S import flujo_wc_S

# from flujo_wT_cuad import flujo_wT_cuad
# from flujo_wT_S_H import flujo_wT_S_H

ruta_entrada_faltantes = '.././faltantes/2021-2022/SM_140/2021/03/'
ruta_entrada_calidad = '.././calidad/2021-2022/SM_140/2021/03/'

ruta_entrada_desvios = '.././desvios/2021-2022/SM_140/2021/03/'
ruta_entrada_medios = '.././medios/2021-2022/SM_140/2021/03/'

ruta_salida_cuad_uw = '.././cuadrantes/flujo_uw/2021-2022/SM_140/2021/03/'
ruta_salida_S_uw = '.././SiH/Si0/flujo_uw/2021-2022/SM_140/2021/03/'

#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_cuad_uw):
    os.makedirs(ruta_salida_cuad_uw)
#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_S_uw):
    os.makedirs(ruta_salida_S_uw)

ruta_salida_cuad_wT = '.././cuadrantes/flujo_wT/2021-2022/SM_140/2021/03/'
ruta_salida_S_wT = '.././SiH/Si0/flujo_wT/2021-2022/SM_140/2021/03/'

#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_cuad_wT):
    os.makedirs(ruta_salida_cuad_wT)
#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_S_wT):
    os.makedirs(ruta_salida_S_wT)

ruta_salida_cuad_wc = '.././cuadrantes/flujo_wc/2021-2022/SM_140/2021/03/'
ruta_salida_S_wc = '.././SiH/Si0/flujo_wc/2021-2022/SM_140/2021/03/'

#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_cuad_wc):
    os.makedirs(ruta_salida_cuad_wc)
#Creo el directorio de salida (ruta_salida) si no existe
if not os.path.exists(ruta_salida_S_wc):
    os.makedirs(ruta_salida_S_wc)

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

#-------------------------------------------------------------------------------------------
#chequeo de calidad de datos y faltantes para uw
#-------------------------------------------------------------------------------------------
            col_cov_uw = ['cov_uw_1.5m', 'cov_uw_3m', 'cov_uw_5m', 'cov_uw_7m']
            check_calidad_uw = (calidad[col_cov_uw] < lim_calidad).all(axis=1)

            col_uw = ['u_1.5m', 'w_1.5m', 'u_3m', 'w_3m', 'u_5m', 'w_5m', \
            'u_7m', 'w_7m']
            check_faltantes_uw = (faltantes[col_uw] < lim_faltantes).all(axis=1)

#-------------------------------------------------------------------------------------------
# metodo de los cuadrantes para uw
#-------------------------------------------------------------------------------------------
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
            if check_calidad_uw.all() & check_faltantes_uw.all():

                totales_uw_cuad = flujo_uw_cuad(flujos_desvios)
                totales_uw_cuad.to_csv (ruta_salida_cuad_uw + datos + str(day) + '_' + str(arch) + '.csv', index=False)

                S_uw_cuad = flujo_uw_S(totales_uw_cuad,flujos_medios)
                S_uw_cuad.to_csv (ruta_salida_S_uw + datos + str(day) + '_' + str(arch) + '.csv', index=False)

            else:
                continue

#-------------------------------------------------------------------------------------------
#chequeo de calidad de datos y faltantes para wT
#-------------------------------------------------------------------------------------------
            col_cov_wT = ['cov_wT_1.5m', 'cov_wT_3m', 'cov_wT_5m', 'cov_wT_7m']
            check_calidad_wT = (calidad[col_cov_wT] < lim_calidad).all(axis=1)

            col_wT = ['T_1.5m', 'w_1.5m', 'T_3m', 'w_3m', 'T_5m', 'w_5m', \
            'T_7m', 'w_7m']
            check_faltantes_wT = (faltantes[col_wT] < lim_faltantes).all(axis=1)

#-------------------------------------------------------------------------------------------
# metodo de los cuadrantes para wT
#-------------------------------------------------------------------------------------------
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
            if check_calidad_wT.all() & check_faltantes_wT.all():

                totales_wT_cuad = flujo_wT_cuad(flujos_desvios)
                totales_wT_cuad.to_csv (ruta_salida_cuad_wT + datos + str(day) + '_' + str(arch) + '.csv', index=False)

                S_wT_cuad = flujo_wT_S(totales_wT_cuad,flujos_medios)
                S_wT_cuad.to_csv (ruta_salida_S_wT + datos + str(day) + '_' + str(arch) + '.csv', index=False)

            else:
                continue

#-------------------------------------------------------------------------------------------
#chequeo de calidad de datos y faltantes para wc (wCO2 y wq)
#-------------------------------------------------------------------------------------------
            col_cov_wc = ['cov_wT_3m', 'cov_wCO2_3m', 'cov_wq_3m']
            check_calidad_wc = (calidad[col_cov_wc] < lim_calidad).all(axis=1)

            col_wc = ['T_3m', 'w_3m', 'CO2_3m', 'H2O_3m']
            check_faltantes_wc = (faltantes[col_wc] < lim_faltantes).all(axis=1)

#-------------------------------------------------------------------------------------------
# metodo de los cuadrantes para wc (wCO2 y wq)
#-------------------------------------------------------------------------------------------
# para el nivel de 3 m
            if check_calidad_wc.all() & check_faltantes_wc.all():

                totales_wc_cuad = flujo_wc_cuad(flujos_desvios)
                totales_wc_cuad.to_csv (ruta_salida_cuad_wc + datos + str(day) + '_' + str(arch) + '.csv', index=False)

                S_wc_cuad = flujo_wc_S(totales_wc_cuad,flujos_medios)
                S_wc_cuad.to_csv (ruta_salida_S_wc + datos + str(day) + '_' + str(arch) + '.csv', index=False)

            else:
                continue
