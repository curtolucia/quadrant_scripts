def flujo_wT_cuad(flujos_desvios):

    flujos_desvios = flujos_desvios.copy()

#leo de los archivos las columnas correspondientes a w
#para el nivel de 3 m
    w_desvio_3 = flujos_desvios['w_desvio_3m']

#leo de los archivos las columnas correspondientes a CO2' y q
#para el nivel de 3m
    CO2_desvio_3 = flujos_desvios['CO2_3m']
    q_desvio_3 = flujos_desvios['q_3m']
    T_desvio_3 = flujos_desvios['T_desvio_3m']

#leo las cov de los escalares wCO2 y wq
#para el nivel de 3m
    cov_wCO2_3 = flujos_desvios['cov_wCO2_3m']
    cov_wq_3 = flujos_desvios['cov_wq_3m']
    cov_wT_3 = flujos_desvios['cov_wT_3m']

# Creo lista para almacenar los datos
    cuad_inst_T = []
    cuad_inst_CO2 = []
    cuad_inst_q = []

    for T_d, w_d, cov_d in zip(T_desvio_3, w_desvio_3, cov_wT_3):
        cov_wT_c1, cov_wT_c2, cov_wT_c3, cov_wT_c4 = calc_cuad(T_d, w_d, cov_d)
    # Guardar los resultados en la variable 'cuad_inst_1_5'
        cuad_inst_T.append([w_d, T_d, cov_wT_c1.tolist(), cov_wT_c2.tolist(), cov_wT_c3.tolist(), cov_wT_c4.tolist()])
    cuad_inst_T_df = pd.DataFrame(cuad_inst_3, columns=['w_desvio_3m', 'T_desvio_3m', \
    'cov_wT_c1_3m', 'cov_wT_c2_3m', 'cov_wT_c3_3m', 'cov_wT_c4_3m'])

    # Iterar sobre los nombres de las columnas
    for CO2_d, w_d, cov_d in zip(CO2_desvio_3, w_desvio_3, cov_wCO2_3):
        cov_wCO2_c1, cov_wCO2_c2, cov_wCO2_c3, cov_wCO2_c4 = calc_cuad(CO2_d, w_d, cov_d)
    # Guardar los resultados en la variable 'cuad_inst_CO2'
        cuad_inst_CO2.append([w_d, CO2_d, cov_wCO2_c1.tolist(), cov_wCO2_c2.tolist(), cov_wCO2_c3.tolist(), cov_wCO2_c4.tolist()])
    cuad_inst_CO2_df = pd.DataFrame(cuad_inst_CO2, columns=['w_desvio_3m', 'CO2_desvio_3m', \
    'cov_wCO2_c1_3m', 'cov_wCO2_c2_3m', 'cov_wCO2_c3_3m', 'cov_wCO2_c4_3m'])

    for q_d, w_d, cov_d in zip(q_desvio_3, w_desvio_3, cov_wq_3):
        cov_wq_c1, cov_wq_c2, cov_wq_c3, cov_wq_c4 = calc_cuad(q_d, w_d, cov_d)
    # Guardar los resultados en la variable 'cuad_inst_1_5'
        cuad_inst_q.append([w_d, q_d, cov_wq_c1.tolist(), cov_wq_c2.tolist(), cov_wq_c3.tolist(), cov_wq_c4.tolist()])
    cuad_inst_q_df = pd.DataFrame(cuad_inst_q, columns=['w_desvio_3m', 'q_desvio_3m', \
    'cov_wq_c1_3m', 'cov_wq_c2_3m', 'cov_wq_c3_3m', 'cov_wq_c4_3m'])

    cuad_inst_df = pd.concat([cuad_inst_T_df,cuad_inst_CO2_df,cuad_inst_q_df], axis=1)
    return cuad_inst_df
