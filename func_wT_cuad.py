from func_uw_cuad import calc_cuad
import pandas as pd

#-------------------------------------------------------------------------------------------
#Defino funcion para calculo de los cuadrantes para wT
#-------------------------------------------------------------------------------------------
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
def flujo_wT_cuad(flujos_desvios):

    flujos_desvios = flujos_desvios.copy()

#leo de los archivos las columnas correspondientes a T
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    T_desvio_1_5 = flujos_desvios['T_desvio_1.5m']
    T_desvio_3 = flujos_desvios['T_desvio_3m']
    T_desvio_5 = flujos_desvios['T_desvio_5m']
    T_desvio_7 = flujos_desvios['T_desvio_7m']

#leo de los archivos las columnas correspondientes a w
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    w_desvio_1_5 = flujos_desvios['w_desvio_1.5m']
    w_desvio_3 = flujos_desvios['w_desvio_3m']
    w_desvio_5 = flujos_desvios['w_desvio_5m']
    w_desvio_7 = flujos_desvios['w_desvio_7m']

#leo las cov de temperatura wT
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    cov_wT_1_5 = flujos_desvios['cov_wT_1.5m']
    cov_wT_3 = flujos_desvios['cov_wT_3m']
    cov_wT_5 = flujos_desvios['cov_wT_5m']
    cov_wT_7 = flujos_desvios['cov_wT_7m']

# Creo lista para almacenar los datos
    cuad_inst = []
    cuad_inst_1_5 = []
    cuad_inst_3 = []
    cuad_inst_5 = []
    cuad_inst_7 = []

# Iterar sobre los nombres de las columnas wT
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    for T_d, w_d, cov_d in zip(T_desvio_1_5, w_desvio_1_5, cov_wT_1_5):
        cov_wT_c1, cov_wT_c2, cov_wT_c3, cov_wT_c4 = calc_cuad(T_d, w_d, cov_d)
# Guardar los resultados en la variable 'cuad_inst_1_5'
        cuad_inst_1_5.append([w_d, T_d, cov_wT_c1.tolist(), cov_wT_c2.tolist(), cov_wT_c3.tolist(), cov_wT_c4.tolist()])
    cuad_inst_1_5_df = pd.DataFrame(cuad_inst_1_5, columns=['w_desvio_1.5m', 'T_desvio_1.5m', \
    'cov_wT_c1_1.5m', 'cov_wT_c2_1.5m', 'cov_wT_c3_1.5m', 'cov_wT_c4_1.5m'])


    for T_d, w_d, cov_d in zip(T_desvio_3, w_desvio_3, cov_wT_3):
        cov_wT_c1, cov_wT_c2, cov_wT_c3, cov_wT_c4 = calc_cuad(T_d, w_d, cov_d)
# Guardar los resultados en la variable 'cuad_inst_3'
        cuad_inst_3.append([w_d, T_d, cov_wT_c1.tolist(), cov_wT_c2.tolist(), cov_wT_c3.tolist(), cov_wT_c4.tolist()])
    cuad_inst_3_df = pd.DataFrame(cuad_inst_3, columns=['w_desvio_3m', 'T_desvio_3m', \
    'cov_wT_c1_3m', 'cov_wT_c2_3m', 'cov_wT_c3_3m', 'cov_wT_c4_3m'])

    for T_d, w_d, cov_d in zip(T_desvio_5, w_desvio_5, cov_wT_5):
        cov_wT_c1, cov_wT_c2, cov_wT_c3, cov_wT_c4 = calc_cuad(w_d, T_d, cov_d)
# Guardar los resultados en la variable 'cuad_inst_5'
        cuad_inst_5.append([T_d, w_d, cov_wT_c1.tolist(), cov_wT_c2.tolist(), cov_wT_c3.tolist(), cov_wT_c4.tolist()])
    cuad_inst_5_df = pd.DataFrame(cuad_inst_5, columns=['w_desvio_5m', 'T_desvio_5m', \
    'cov_wT_c1_5m', 'cov_wT_c2_5m', 'cov_wT_c3_5m', 'cov_wT_c4_5m'])

    for T_d, w_d, cov_d in zip(T_desvio_7, w_desvio_7, cov_wT_7):
        cov_wT_c1, cov_wT_c2, cov_wT_c3, cov_wT_c4 = calc_cuad(T_d, w_d, cov_d)
# Guardar los resultados en la variable 'cuad_inst_7'
        cuad_inst_7.append([w_d, T_d, cov_wT_c1.tolist(), cov_wT_c2.tolist(), cov_wT_c3.tolist(), cov_wT_c4.tolist()])
    cuad_inst_7_df = pd.DataFrame(cuad_inst_7, columns=['w_desvio_7m', 'T_desvio_7m', \
    'cov_wT_c1_7m', 'cov_wT_c2_7m', 'cov_wT_c3_7m', 'cov_wT_c4_7m'])

    cuad_inst_df = pd.concat([cuad_inst_1_5_df,cuad_inst_3_df,cuad_inst_5_df,cuad_inst_7_df], axis=1)
    return cuad_inst_df
