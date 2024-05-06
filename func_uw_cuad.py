#Traigo las librerias que necesito
import pandas as pd
import numpy as np

from func_aux import calc_cuad
#-------------------------------------------------------------------------------------------
#Defino funcion para calculo de los cuadrantes para uw
#-------------------------------------------------------------------------------------------
#para los niveles de 1.5 m, 3 m, 5 m y 7 m

def flujo_uw_cuad(flujos_desvios):

    flujos_desvios = flujos_desvios.copy()

#leo de los archivos las columnas correspondientes a u
    u_desvio = flujos_desvios['u_desvio']
#leo de los archivos las columnas correspondientes a v
    # v_desvio = flujos_desvios['v_desvio']
#leo de los archivos las columnas correspondientes a w
    w_desvio = flujos_desvios['w_desvio']
# #leo las cov de cantidad de movimiento uw y vw
    cov_uw = flujos_desvios['cov_uw']
    # cov_vw = flujos_desvios['cov_vw']

# Creo lista para almacenar los datos
    cuad_inst = []
# Iterar para todos los valores instantaneos de uw
#para los niveles de 1.5 m, 3 m, 5 m y 7 m

    for u_d, w_d, cov_d in zip(u_desvio, w_desvio, cov_uw):

        if np.isnan(u_d) or np.isnan(w_d):
            cov_uw_c1 = cov_uw_c2 = cov_uw_c3 = cov_uw_c4 = np.nan
        else:
            cov_uw_c1, cov_uw_c2, cov_uw_c3, cov_uw_c4 = calc_cuad(u_d, w_d, cov_d)
# Guardar los resultados en la variable 'cuad_inst'
        cuad_inst.append([u_d, w_d, cov_uw_c1, cov_uw_c2, cov_uw_c3, cov_uw_c4])

    cuad_inst_df = pd.DataFrame(cuad_inst, columns=['u_desvio', 'w_desvio', \
    'cov_uw_c1', 'cov_uw_c2', 'cov_uw_c3', 'cov_uw_c4'])

    return cuad_inst_df

def flujo_uw_cuad_nan(flujos_desvios):

    cuad_inst_df = flujos_desvios[['u_desvio', 'w_desvio']].copy()

    nuevas_columnas = ['cov_uw_c1', 'cov_uw_c2', 'cov_uw_c3', 'cov_uw_c4']

    for columna in nuevas_columnas:
        cuad_inst_df[columna] = np.nan

    return cuad_inst_df

# #leo de los archivos las columnas correspondientes a u
#     u_desvio_1_5 = flujos_desvios['u_desvio_1.5m']
#     u_desvio_3 = flujos_desvios['u_desvio_3m']
#     u_desvio_5 = flujos_desvios['u_desvio_5m']
#     u_desvio_7 = flujos_desvios['u_desvio_7m']
#
# #leo de los archivos las columnas correspondientes a v
#     v_desvio_1_5 = flujos_desvios['v_desvio_1.5m']
#     v_desvio_3 = flujos_desvios['v_desvio_3m']
#     v_desvio_5 = flujos_desvios['v_desvio_5m']
#     v_desvio_7 = flujos_desvios['v_desvio_7m']
#
# #leo de los archivos las columnas correspondientes a w
#     w_desvio_1_5 = flujos_desvios['w_desvio_1.5m']
#     w_desvio_3 = flujos_desvios['w_desvio_3m']
#     w_desvio_5 = flujos_desvios['w_desvio_5m']
#     w_desvio_7 = flujos_desvios['w_desvio_7m']
#
# #leo las cov de cantidad de movimiento uw y vw
# #para los niveles de 1.5 m, 3 m, 5 m y 7 m
#     cov_uw_1_5 = flujos_desvios['cov_uw_1.5m']
#     cov_uw_3 = flujos_desvios['cov_uw_3m']
#     cov_uw_5 = flujos_desvios['cov_uw_5m']
#     cov_uw_7 = flujos_desvios['cov_uw_7m']
#
#     cov_vw_1_5 = flujos_desvios['cov_vw_1.5m']
#     cov_vw_3 = flujos_desvios['cov_vw_3m']
#     cov_vw_5 = flujos_desvios['cov_vw_5m']
#     cov_vw_7 = flujos_desvios['cov_vw_7m']
#
# # Creo lista para almacenar los datos
#     cuad_inst = []
#     cuad_inst_1_5 = []
#     cuad_inst_3 = []
#     cuad_inst_5 = []
#     cuad_inst_7 = []
#
# # Iterar para todos los valores instantaneos de uw
# #para los niveles de 1.5 m, 3 m, 5 m y 7 m
#     for u_d, w_d, cov_d in zip(u_desvio_1_5, w_desvio_1_5, cov_uw_1_5):
#         cov_uw_c1, cov_uw_c2, cov_uw_c3, cov_uw_c4 = calc_cuad(u_d, w_d, cov_d)
# # Guardar los resultados en la variable 'cuad_inst_1_5'
#         cuad_inst_1_5.append([u_d, w_d, cov_uw_c1.tolist(), cov_uw_c2.tolist(), cov_uw_c3.tolist(), cov_uw_c4.tolist()])
#     cuad_inst_1_5_df = pd.DataFrame(cuad_inst_1_5, columns=['u_desvio_1.5m', 'w_desvio_1.5m', \
#     'cov_uw_c1_1.5m', 'cov_uw_c2_1.5m', 'cov_uw_c3_1.5m', 'cov_uw_c4_1.5m'])
#
#
#     for u_d, w_d, cov_d in zip(u_desvio_3, w_desvio_3, cov_uw_3):
#         cov_uw_c1, cov_uw_c2, cov_uw_c3, cov_uw_c4 = calc_cuad(u_d, w_d, cov_d)
# # Guardar los resultados en la variable 'cuad_inst_3'
#         cuad_inst_3.append([u_d, w_d, cov_uw_c1.tolist(), cov_uw_c2.tolist(), cov_uw_c3.tolist(), cov_uw_c4.tolist()])
#     cuad_inst_3_df = pd.DataFrame(cuad_inst_3, columns=['u_desvio_3m', 'w_desvio_3m', \
#     'cov_uw_c1_3m', 'cov_uw_c2_3m', 'cov_uw_c3_3m', 'cov_uw_c4_3m'])
#
#     for u_d, w_d, cov_d in zip(u_desvio_5, w_desvio_5, cov_uw_5):
#         cov_uw_c1, cov_uw_c2, cov_uw_c3, cov_uw_c4 = calc_cuad(u_d, w_d, cov_d)
# # Guardar los resultados en la variable 'cuad_inst_5'
#         cuad_inst_5.append([u_d, w_d, cov_uw_c1.tolist(), cov_uw_c2.tolist(), cov_uw_c3.tolist(), cov_uw_c4.tolist()])
#     cuad_inst_5_df = pd.DataFrame(cuad_inst_5, columns=['u_desvio_5m', 'w_desvio_5m', \
#     'cov_uw_c1_5m', 'cov_uw_c2_5m', 'cov_uw_c3_5m', 'cov_uw_c4_5m'])
#
#     for u_d, w_d, cov_d in zip(u_desvio_7, w_desvio_7, cov_uw_7):
#         cov_uw_c1, cov_uw_c2, cov_uw_c3, cov_uw_c4 = calc_cuad(u_d, w_d, cov_d)
# # Guardar los resultados en la variable 'cuad_inst_7'
#         cuad_inst_7.append([u_d, w_d, cov_uw_c1.tolist(), cov_uw_c2.tolist(), cov_uw_c3.tolist(), cov_uw_c4.tolist()])
#     cuad_inst_7_df = pd.DataFrame(cuad_inst_7, columns=['u_desvio_7m', 'w_desvio_7m', \
#     'cov_uw_c1_7m', 'cov_uw_c2_7m', 'cov_uw_c3_7m', 'cov_uw_c4_7m'])
#
#     cuad_inst_df = pd.concat([cuad_inst_1_5_df,cuad_inst_3_df,cuad_inst_5_df,cuad_inst_7_df], axis=1)
#     return cuad_inst_df
