import pandas as pd
import math

def flujo_wc_S(totales_wc_cuad,flujos_medios):

    val_medios = totales_wT_cuad.mean(axis=0,skipna=True)
# Creo lista para almacenar los datos
    S_cuad = []
    S_3_T = []
    S_3_CO2 = []
    S_3_q = []

#Calculo S de cada cuadrante, como el promedio de cada cuadrante (H=0)
#dividido el promedio total (de todos los cuadrantes, H=0)
#para el nivel de 3 m

#para el nivel de 3 m
    cov_T = flujos_medios['cov_wT_3m']
    cov_c1_3 = val_medios['cov_wT_c1_3m']
    cov_c2_3 = val_medios['cov_wT_c2_3m']
    cov_c3_3 = val_medios['cov_wT_c3_3m']
    cov_c4_3 = val_medios['cov_wT_c4_3m']

    S_wT_c1, S_wT_c2, S_wT_c3, S_wT_c4 = calc_S(cov_c1_3,cov_c2_3,cov_c3_3, cov_c4_3, cov_T)
    S_3_T = ([S_wT_c1[0], S_wT_c2[0], S_wT_c3[0], S_wT_c4[0]])
    S_3_T_df = pd.DataFrame(S_3, index=['S_T_cuad1_3m','S_T_cuad2_3m','S_T_cuad3_3m','S_T_cuad4_3m']).T


    cov_CO2 = flujos_medios['cov_wCO2_3m']
    cov_c1_CO2 = val_medios['cov_wCO2_c1_3m']
    cov_c2_CO2 = val_medios['cov_wCO2_c2_3m']
    cov_c3_CO2 = val_medios['cov_wCO2_c3_3m']
    cov_c4_CO2 = val_medios['cov_wCO2_c4_3m']

    S_wCO2_c1, S_wCO2_c2, S_wCO2_c3, S_wCO2_c4 = calc_S(cov_c1_CO2,cov_c2_CO2,cov_c3_CO2,cov_c4_CO2,cov_CO2)

    S_3_CO2 = ([S_wCO2_c1[0], S_wCO2_c2[0], S_wCO2_c3[0], S_wCO2_c4[0]])
    S_3_CO2_df = pd.DataFrame(S_3_CO2, index=['S_CO2_cuad1_3m','S_CO2_cuad2_3m','S_CO2_cuad3_3m','S_CO2_cuad4_3m']).T

#para el nivel de 3 m
    cov_q = flujos_medios['cov_wq_3m']
    cov_c1_q = val_medios['cov_wq_c1_3m']
    cov_c2_q = val_medios['cov_wq_c2_3m']
    cov_c3_q = val_medios['cov_wq_c3_3m']
    cov_c4_q = val_medios['cov_wq_c4_3m']

    S_wq_c1, S_wq_c2, S_wq_c3, S_wq_c4 = calc_S(cov_c1_q,cov_c2_q,cov_c3_q,cov_c4_q,cov_q)
    S_3_q = ([S_wq_c1[0], S_wq_c2[0], S_wq_c3[0], S_wq_c4[0]])
    S_3_q_df = pd.DataFrame(S_3, index=['S_q_cuad1_3m','S_q_cuad2_3m','S_q_cuad3_3m','S_q_cuad4_3m']).T

#DataFrame con todos los niveles
#S de cada cuadrante para wT (H=0)
#para los niveles de 1.5 m, 3 m, 5 m y 7 m
    S_cuad_wT = pd.concat([S_3_T_df,S_3_CO2_df, S_3_q_df,], axis=1)

    return S_cuad_wc
