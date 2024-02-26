#Traigo las librerias que necesito
import numpy as np

#-------------------------------------------------------------------------------------------
#Defino una funcion para separar las covarianzas por cuadrantes
#-------------------------------------------------------------------------------------------
def calc_cuad(c, w, cov):
    c_w_c1 = np.where((c >= 0) & (w >= 0), cov, 0)
    c_w_c2 = np.where((c < 0) & (w > 0), cov, 0)
    c_w_c3 = np.where((c < 0) & (w < 0), cov, 0)
    c_w_c4 = np.where((c > 0) & (w < 0), cov, 0)
    return c_w_c1, c_w_c2, c_w_c3, c_w_c4

#-------------------------------------------------------------------------------------------
#Defino una funcion para calcular las Si,0 (H=0) por cuadrantes
#-------------------------------------------------------------------------------------------
def calc_S(cov_c1,cov_c2,cov_c3, cov_c4, cov):
    S_c1 = cov_c1/cov
    S_c2 = cov_c2/cov
    S_c3 = cov_c3/cov
    S_c4 = cov_c4/cov
    return S_c1, S_c2, S_c3, S_c4
