import pandas as pd
import numpy as np

from func_aux import calc_cuad

#-------------------------------------------------------------------------------------------
#Defino funcion para calculo de los Si,0 para wc
#-------------------------------------------------------------------------------------------
#para el nivel de 3 m
def flujo_wc_cuad(flujos_desvios):

    flujos_desvios = flujos_desvios.copy()

#leo de los archivos las columnas correspondientes a w
#para el nivel de 3 m
    w_desvio_3 = flujos_desvios['w_desvio']

#leo de los archivos las columnas correspondientes a CO2 y q
#para el nivel de 3m
    CO2_desvio_3 = flujos_desvios['CO2_desvio']
    q_desvio_3 = flujos_desvios['q_desvio']
    T_desvio_3 = flujos_desvios['T_desvio']

#leo las cov de los escalares wCO2 y wq
#para el nivel de 3m
    cov_wCO2_3 = flujos_desvios['cov_wCO2']
    cov_wq_3 = flujos_desvios['cov_wq']
    cov_wT_3 = flujos_desvios['cov_wT']

# Creo lista para almacenar los datos
    cuad_inst_T = []
    cuad_inst_CO2 = []
    cuad_inst_q = []

    for T_d, w_d, cov_d in zip(T_desvio_3, w_desvio_3, cov_wT_3):
        if np.isnan(T_d) or np.isnan(w_d):
            cov_wT_c1 = cov_wT_c2 = cov_wT_c3 = cov_wT_c4 = np.nan
        else:
            cov_wT_c1, cov_wT_c2, cov_wT_c3, cov_wT_c4 = calc_cuad(T_d, w_d, cov_d)
# Guardar los resultados en la variable 'cuad_inst_T'
        cuad_inst_T.append([w_d, T_d, cov_wT_c1, cov_wT_c2, cov_wT_c3, cov_wT_c4])
    cuad_inst_T_df = pd.DataFrame(cuad_inst_T, columns=['w_desvio', 'T_desvio', \
    'cov_wT_c1', 'cov_wT_c2', 'cov_wT_c3', 'cov_wT_c4'])

    # Iterar sobre los nombres de las columnas
    for CO2_d, w_d, cov_d in zip(CO2_desvio_3, w_desvio_3, cov_wCO2_3):
        if np.isnan(CO2_d) or np.isnan(w_d):
            cov_wCO2_c1 = cov_wCO2_c2 = cov_wCO2_c3 = cov_wCO2_c4 = np.nan
        else:
            cov_wCO2_c1, cov_wCO2_c2, cov_wCO2_c3, cov_wCO2_c4 = calc_cuad(CO2_d, w_d, cov_d)
# Guardar los resultados en la variable 'cuad_inst_CO2'
        cuad_inst_CO2.append([w_d, CO2_d, cov_wCO2_c1, cov_wCO2_c2, cov_wCO2_c3, cov_wCO2_c4])
    cuad_inst_CO2_df = pd.DataFrame(cuad_inst_CO2, columns=['CO2_desvio', \
    'cov_wCO2_c1', 'cov_wCO2_c2', 'cov_wCO2_c3', 'cov_wCO2_c4'])

    for q_d, w_d, cov_d in zip(q_desvio_3, w_desvio_3, cov_wq_3):
        if np.isnan(q_d) or np.isnan(w_d):
            cov_wq_c1 = cov_wq_c2 = cov_wq_c3 = cov_wq_c4 = np.nan
        else:
            cov_wq_c1, cov_wq_c2, cov_wq_c3, cov_wq_c4 = calc_cuad(q_d, w_d, cov_d)
# Guardar los resultados en la variable 'cuad_inst_q'
        cuad_inst_q.append([w_d, q_d, cov_wq_c1, cov_wq_c2, cov_wq_c3, cov_wq_c4])
    cuad_inst_q_df = pd.DataFrame(cuad_inst_q, columns=['q_desvio', \
    'cov_wq_c1', 'cov_wq_c2', 'cov_wq_c3', 'cov_wq_c4'])

    cuad_inst_df = pd.concat([cuad_inst_T_df,cuad_inst_CO2_df,cuad_inst_q_df], axis=1)
    return cuad_inst_df


def flujo_wc_cuad_nan(flujos_desvios):

    cuad_inst_df = flujos_desvios[['w_desvio','T_desvio', 'CO2_desvio', 'q_desvio']].copy()

    nuevas_columnas = ['cov_wT_c1', 'cov_wT_c2', 'cov_wT_c3', 'cov_wT_c4',\
    'cov_wCO2_c1', 'cov_wCO2_c2', 'cov_wCO2_c3', 'cov_wCO2_c4',\
    'cov_wq_c1', 'cov_wq_c2', 'cov_wq_c3', 'cov_wq_c4']

    for columna in nuevas_columnas:
        cuad_inst_df[columna] = np.nan

    return cuad_inst_df
