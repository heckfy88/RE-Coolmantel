from typing import List, Any
import math as mt
import matplotlib.pyplot as plt
import math


def teplyom_gor(t):
    f = 0
    t_spis = [100, 110, 120, 140, 160, 180, 190, 200, 225, 250, 275, 300, 325, 350, 375, 400, 450, 500, 550, 600]
    c_spis = [1890, 1900, 1950, 2000, 2050, 2100, 2200, 2280, 2360, 2440, 2550, 2660, 2800, 2900, 3060]
    #c_spis_egor = [3273, 3306, 3340, 3408, 3500, 3636, 3722, 3817, 3046, 3099, 3876, 3556, 3308, 3158, 3081, 3054, 3086, 3188, 3305, 3444]
    m = t_spis[0]
    for j in t_spis:
        r = abs(t - j)
        if r <= m:
            m = r
            f = j
        # elif r > m:
        #   m = r
        #  f = j

    if t < f:
        b = t_spis.index(f)
        if b != 0:
            a = t_spis.index(f) - 1
        else:
            a = 0
        c = c_spis[a] + (c_spis[b] - c_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    elif f < t <= t_spis[-1]:
        b = t_spis.index(f) + 1
        a = t_spis.index(f)
        c = c_spis[a] + (c_spis[b] - c_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    else:
        c = c_spis[-1]
        return c


def plotn(t):
    f = 0
    t_spis = [223, 233, 253, 273, 293, 313, 333, 353, 373, 393, 413, 433, 453, 473, 533]
    ro_spis = [864, 858, 842, 830, 819, 808, 795, 781, 766, 751, 736, 720, 703, 685, 638]
    #ro_spis_egor = [452.7, 440.6, 428.5, 403.2, 376.3, 346.8, 331, 314.3, 269.5, 224, 184.9, 155.7, 134.8, 119.5, 107.8, 98.5, 84.7, 74.7, 67.1, 61.1]
    m = t_spis[0]
    for j in t_spis:
        r = abs(t - j)
        if r <= m:
            m = r
            f = j
        # elif r > m:
        #   m = r
        #  f = j

    if t < f:
        b = t_spis.index(f)
        if b != 0:
            a = t_spis.index(f) - 1
        else:
            a = 0
        c = ro_spis[a] + (ro_spis[b] - ro_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    elif t > f and t <= t_spis[-1]:
        b = t_spis.index(f) + 1
        a = t_spis.index(f)
        c = ro_spis[a] + (ro_spis[b] - ro_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    else:
        if f >= ro_spis[0]:
            c = ro_spis[t_spis.index(f)]
        else:
            c = ro_spis[0]
        #c = ro_spis[t_spis.index(f)]
        return c


def din_vyaz(t):
    f = 0
    t_spis = [223, 233, 253, 273, 293, 313, 333, 353, 373, 393, 413, 433, 453, 473, 533]
    di_vyaz_spis = [120, 73, 35, 20, 15, 10, 8, 6, 5, 4.5, 3.9, 3.5, 3, 2.6, 2.0]
    di_vyaz_spis_egor = [194.43, 151.43, 122.89, 87.40, 60, 51.44, 45.74, 40.8, 31.16, 24.75, 21.05, 19.16, 18.29, 17.94, 17.9, 18.02, 18.56, 19.3, 20.14, 21.2]
    m = t_spis[0]
    for j in t_spis:
        r = abs(t - j)
        if r <= m:
            m = r
            f = j
        # elif r > m:
        #   m = r
        #  f = j

    if t < f:
        b = t_spis.index(f)
        if b != 0:
            a = t_spis.index(f) - 1
        else:
            a = 0
        c = di_vyaz_spis[a] + (di_vyaz_spis[b] - di_vyaz_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    elif t > f and t <= t_spis[-1]:
        b = t_spis.index(f) + 1
        a = t_spis.index(f)
        c = di_vyaz_spis[a] + (di_vyaz_spis[b] - di_vyaz_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    else:
        if f >= di_vyaz_spis[0]:
            c = di_vyaz_spis[t_spis.index(f)]
        else:
            c = di_vyaz_spis[0]
        #c = di_vyaz_spis[t_spis.index(f)]
        return c


def lambda_oxl(t):
    f = 0
    t_spis = [223, 233, 253, 273, 293, 313, 333, 353, 373, 393, 413, 433, 453, 473, 533]
    lambd_spis = [0.127, 0.125, 0.123, 0.120, 0.117, 0.114, 0.110, 0.108, 0.104, 0.102, 0.099, 0.096, 0.093, 0.090,
                  0.084]
    m = t_spis[0]
    for j in t_spis:
        r = abs(t - j)
        if r <= m:
            m = r
            f = j
        # elif r > m:
        #   m = r
        #  f = j

    if t < f:
        b = t_spis.index(f)
        if b != 0:
            a = t_spis.index(f) - 1
        else:
            a = 0
        c = lambd_spis[a] + (lambd_spis[b] - lambd_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    elif t > f and t <= t_spis[-1]:
        b = t_spis.index(f) + 1
        a = t_spis.index(f)
        c = lambd_spis[a] + (lambd_spis[b] - lambd_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    else:
        if f >= lambd_spis[0]:
            c = lambd_spis[t_spis.index(f)]
        else:
            c = lambd_spis[0]
        #c = lambd_spis[t_spis.index(f)]
        return c


def KaKAkakA(t):
    f = 0
    t_spis = [223, 233, 253, 273, 293, 313, 333, 353, 373, 393, 413, 433, 453, 473, 533]
    K_spis = [38, 40, 55, 70, 80, 90, 100, 110, 120, 130, 140, 150, 155, 160, 178]
    K_spis_egor = [318, 339, 354, 375, 387, 396, 399, 402, 407, 403, 390, 376, 367, 364, 366, 372, 389, 411, 436, 462]
    m = t_spis[0]
    for j in t_spis:
        r = abs(t - j)
        if r <= m:
            m = r
            f = j
        # elif r > m:
        #   m = r
        #  f = j

    if t < f:
        b = t_spis.index(f)
        if b != 0:
            a = t_spis.index(f) - 1
        else:
            a = 0
        c = K_spis[a] + (K_spis[b] - K_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    elif t > f and t <= t_spis[-1]:
        b = t_spis.index(f) + 1
        a = t_spis.index(f)
        c = K_spis[a] + (K_spis[b] - K_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    else:
        if f >= K_spis[0]:
            c = K_spis[t_spis.index(f)]
        else:
            c = K_spis[0]
        return c


def lambda_stt(t):
    f = 0
    t_spis = [373, 423, 473, 523, 573, 623, 673, 723, 773, 823, 873]
    lambd_spis = [240, 250, 255, 270, 283, 290, 297, 305, 310, 315, 318]
    m = t_spis[0]
    for j in t_spis:
        r = abs(t - j)
        if r <= m:
            m = r
            f = j
        elif r > m:
            m = r
            f = j

    if t < f:
        b = t_spis.index(f)
        if b != 0:
            a = t_spis.index(f) - 1
        else:
            a = 0
        c = lambd_spis[a] + (lambd_spis[b] - lambd_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    elif t > f and t <= t_spis[-1]:
        b = t_spis.index(f) + 1
        a = t_spis.index(f)
        c = lambd_spis[a] + (lambd_spis[b] - lambd_spis[a]) * (t - t_spis[a]) / (t_spis[b] - t_spis[a])
        return c
    else:
        c = lambd_spis[t_spis.index(f)]
        return c


D_kr_d = 0.091
F_kr_d = 0.006570322

x, D, D_, F, F_, delt_x, delt_x_s, delt_S, np, D05, t, tn, f, dg = [], [], [], [], [], [], \
                                                                   [], [], [], [], [], [], [], []
x = [0, 50, 103, 155, 208, 261, 314, 366, 419, 472, 525, 536, 548, 560, 572, 583, 595, 607, 618, 630, 642, 654, 665,
677, 689, 701, 712, 724, 736, 742, 747, 753, 759, 765, 771, 777, 783, 788, 794, 800, 806, 812, 818, 824, 830, 835,
841, 847, 853, 859, 866, 871, 876, 882, 888, 894, 900, 906, 912, 917, 923, 929, 935, 941, 947, 953, 958, 964, 970,
976, 982, 988, 994, 1005, 1017, 1029, 1041, 1052, 1064, 1076, 1087, 1099, 1111, 1134, 1158, 1181, 1205, 1228, 1252,
1275, 1298, 1322, 1345, 1369, 1392, 1416, 1439, 1463, 1486, 1510, 1533, 1556, 1580, 1603, 1627, 1650, 1674, 1697,
1721, 1744, 1767, 1791, 1814, 1838, 1861, 1885, 1908, 1932, 1955, 1978, 2002, 2025, 2049, 2072, 2096, 2119, 2143,
2166, 2190, 2213, 2236, 2260, 2283, 2307, 2330, 2354, 2377, 2401, 2424, 2447, 2471, 2494, 2518, 2541, 2565, 2588,
2612, 2635, 2659, 2682, 2705, 2729, 2752, 2776, 2799, 2823, 2846]

R_sech = [
283.05, 283.05, 283.05, 283.05, 283.05, 283.05, 283.05, 283.05, 283.05, 283.05, 283.05, 282.8, 282.07, 280.85,
279.13, 276.91, 274.16, 270.89, 267.05, 262.64, 257.62, 251.96, 245.6, 238.5, 230.59, 221.78, 211.95, 201.08,
192.29, 188.32, 184.6, 181.14, 177.9, 174.88, 172.08, 169.48, 167.07, 164.85, 162.82, 160.96, 159.28, 157.76,
156.41, 155.23, 154.2, 153.33, 152.62, 152.06, 151.65, 151.4, 151.29, 151.56, 152.59, 154.45, 157.25, 160.92,
164.64, 168.33, 171.99, 175.61, 179.17, 182.69, 186.15, 189.57, 192.96, 196.31, 199.62, 202.91, 206.18, 209.42,
212.64, 215.84, 219.03, 225.33, 231.55, 237.68, 243.72, 249.67, 255.54, 261.33, 267.04, 272.68, 278.25, 289.18,
299.86, 310.29, 320.48, 330.46, 340.22, 349.78, 359.15, 368.34, 377.35, 386.2, 394.88, 403.41, 411.79, 420.03,
428.13, 436.1, 443.94, 451.65, 459.25, 466.73, 474.1, 481.36, 488.51, 495.57, 502.52, 509.38, 516.14, 522.82, 529.4,
535.91, 542.32, 548.66, 554.91, 561.09, 567.2, 573.23, 579.19, 585.08, 590.9, 596.65, 602.34, 607.96, 613.52,
619.02, 624.46, 629.84, 635.17, 640.44, 645.65, 650.81, 655.91, 660.97, 665.97, 670.92, 675.83, 680.68, 685.49,
690.26, 694.97, 699.64, 704.26, 708.84, 713.38, 717.89, 722.36, 726.79, 731.18, 735.53, 739.82, 744.06, 748.23,
752.36, 756.47]

delt_x_s = [50, 52.742, 52.742, 52.742, 52.742, 52.742, 52.742, 52.742, 52.742, 52.742, 11.72, 11.75, 11.79, 11.85,
11.93, 12.04, 12.17, 12.33, 12.53, 12.75, 13.02, 13.34, 13.71, 14.14, 14.67, 15.3, 15.99, 14.66, 7.08, 6.94,
6.81, 6.69, 6.59, 6.5, 6.41, 6.34, 6.27, 6.2, 6.13, 6.06, 6.05, 6.02, 5.98, 5.95, 5.92, 5.91, 5.89, 5.87,
5.85, 6.84, 4.9, 5.95, 6.15, 6.5, 6.91, 6.94, 6.93, 6.91, 8.9, 6.86, 6.83, 6.81, 6.79, 6.77, 6.75, 6.74,
6.72, 6.71, 6.7, 6.9, 6.8, 6.7, 13.31, 13.27, 13.23, 13.19, 13.15, 13.11, 13.08, 13.04, 13.01, 12.98, 25.87,
25.77, 25.66, 25.57, 25.48, 25.4, 25.32, 25.25, 25.18, 25.12, 25.06, 25, 24.95, 24.9, 24.85, 24.81, 24.77,
24.72, 24.69, 24.65, 24.61, 24.58, 24.55, 24.52, 24.49, 24.46, 24.43, 24.41, 24.38, 24.36, 24.33, 24.31,
24.29, 24.27, 24.25, 24.23, 24.21, 24.19, 24.18, 24.16, 24.14, 24.11, 24.1, 24.09, 24.07, 24.06, 24.05,
24.03, 24.02, 24.01, 24, 23.99, 23.98, 23.97, 23.96, 23.95, 23.94, 23.93, 23.92, 23.91, 23.9, 23.89, 23.88,
23.88, 23.87, 23.86, 23.86, 23.85, 23.84, 23.83, 23.82, 23.81, 23.81, 23.8]

x = list(map(lambda x:x/1000, x))
delt_x_s = list(map(lambda x:x/1000, delt_x_s))
R_sech = list(map(lambda x:x/1000, R_sech))
D = list(map(lambda x:2*x, R_sech))
D_ = list(map(lambda x: x/D_kr_d, D))
F = list(map((lambda x: mt.pi*x**2), R_sech))
F_ = list(map(lambda x: x/F_kr_d, F))

for i in range(len(x)-1):
    delt_x.append(abs(x[i+1] - x[i]))

for i in range(len(delt_x_s)):
    delt_S.append(0.5 * mt.pi * (D[i] + D[i+1]) * delt_x_s[i])

delta_st = 0.001
delta_st_naruj = 0.003
delta_r = 0.001
h_p = 0.015
betta_rebra = 0*mt.pi/180

D_05h_kr = D_kr_d + ((2*delta_st)+h_p)
t_N_min = 0.0025
n_p_kr_ = mt.pi*D_05h_kr*mt.cos(betta_rebra)/t_N_min
n_p_kr_ = int(n_p_kr_)
bet_rebr_spis = []
while(n_p_kr_ / 2) % 1 != 0:
    n_p_kr_ -= 1

D05 = list(map(lambda x: (x) + ((2*delta_st)+h_p), D))
i = 0
n_p_i = n_p_kr_
while i != (len(D05)):
    if i <= 45:
        betta_rebra = 0*mt.pi/180
        t_i = mt.pi * D05[i] / n_p_i
        t_N_i = t_i * mt.cos(betta_rebra)
    else:
        betta_rebra = 0 * mt.pi / 180
        t_i = mt.pi*D05[i]/n_p_i
        t_N_i = t_i * mt.cos(betta_rebra)
    if t_N_i <= 0.0055:
        t.append(t_i)
        tn.append(t_N_i)
        np.append(n_p_i)
        bet_rebr_spis.append(betta_rebra)
        i+=1
        n_p_i = n_p_kr_
    else:
        n_p_i *=2
for i in range(len(tn)):
    f.append(tn[i] * h_p * np[i] * (1 - (delta_r / tn[i])))
    dg.append(2 * h_p * (tn[i] - delta_r) / (tn[i] - delta_r + h_p))

#for i in range(len(np)):
    #print( i, np[i], round(tn[i],4))

#print(np)



# Расчет тепловых потоков в камере
k_prist = 1.18
lombod = 0
lambd = []
d_ii = 0
step = 1 / (k_prist - 1)
perv = (((k_prist + 1) / 2) ** (step))
tret = ((k_prist - 1) / (k_prist + 1))
while len(lambd) < len(D_):
    dvoy = ((1 - (tret * (lombod ** 2))) ** step)
    ur = (D_[d_ii] ** (-2)) - (perv * lombod * dvoy)
    # print(len(lambd), d_ii, D_[d_ii]**(-2) , perv * lombod * dvoy, lombod)
    # if d_ii <= 2:
    #   lambd.append(0)
    #  d_ii += 1
    if ur <= 0.000001 and ur >= 0:
        lambd.append(lombod)
        #print(lombod)
        # print(lombod, ur, D_[d_ii]**(-2), perv * lombod * dvoy)
        # if d_ii >= 7.5:
        #   lombod = 1
        # else:
        d_ii += 1
    else:
        lombod += 0.0000005
A = 0.01352
T_st_g = 700
T_yadr = 3808.8
T_0g = 2008  # 1750
m_t = 616
m_st = m_t * 0.05
T_st_ = T_st_g / T_0g
alfa_ = 1.813 * (((2) / (k_prist + 1)) ** (0.85 / (k_prist - 1))) * ((2 * k_prist / (k_prist + 1)) ** 0.425)
R_0g = 338
c_p_0g = 2004
c_p_st = 2170
c_p_sr = 0.5 * (c_p_0g + c_p_st)
mu = 0.978 * (10 ** (-4))
S = (2.065 * c_p_sr * (T_0g - T_st_g) * (mu ** 0.15)) / (
        ((R_0g * T_0g) ** 0.425) * ((1 + T_st_) ** 0.595) * ((3 + T_st_) ** 0.15))
eps = 1
Pr = 0.75
p_k = 15 * (10 ** 6)

# расчет конвективных тепловых потоков
betta = []
Z_ = []
B = []
q_konv = []
q_luch = []
q_g = []
for i in range(len(lambd)):
    beti = lambd[i] * (((k_prist - 1) / (k_prist + 1)) ** 0.5)
    betta.append(beti)
    Z_it = 1.769 * (1 - (betta[i] ** 2) + (
            (betta[i] ** 2) * (1 - ((0.086 * (1 - (betta[i] ** 2))) / (1 - T_st_ - (0.1 * (betta[i] ** 2))))))) / (
                   1 - T_st_ - (0.1 * (betta[i] ** 2)))
    Z_.append(Z_it)
    bi = 0.4842 * alfa_ * A * (Z_[i] ** 0.075)
    B.append(bi)
for i in range(len(lambd)):
    q_koni = (B[i] * (1 - (betta[i] ** 2)) * eps * (p_k ** 0.85) * S) / (
            (D_[i] ** 1.82) * (D_kr_d ** 0.15) * (Pr ** 0.58))
    q_konv.append(q_koni)

# Расчет лучистых тепловых потоков
eps_st = 0.8
eps_st_ef = (eps_st + 1) / 2
c_0 = 5.67
l_c = 0.700
l_e = 0.6 * D[1]
p_H2O = 4.9875 * (10 ** 6)
p_CO2 = 2.7176 * (10 ** 6)
R_H2O = 8.31 / 0.018
R_CO2 = 8.31 / 0.044
ro_H2O = p_H2O / (R_H2O * T_yadr)
ro_CO2 = p_CO2 / (R_CO2 * T_yadr)
#print(ro_H2O, ro_CO2)
#print(p_CO2*l_e/1000000, p_H2O*l_e/1000000)
#print(ro_CO2*l_e, ro_H2O*l_e)
bet_H2O = 1.35
eps_0_H2O = 0.175
eps_H2O = bet_H2O * eps_0_H2O
eps_CO2 = 0.0794
eps_g = eps_H2O + eps_CO2 - (eps_H2O * eps_CO2)
# print(eps_g)
q_luch_Km = eps_st_ef * eps_g * c_0 * ((T_yadr / 100) ** 4)
#print(q_luch_Km)
fi_popr_na_pogl = 0.9
q_luch_ks = fi_popr_na_pogl * q_luch_Km
#print(q_luch_ks)

for i in range(len(D_)):
    if i == 0:
        q_luch.append(0.25 * q_luch_ks)
    elif D_[i] >= 1.2 and i < 8:
        q_luch.append(q_luch_ks)
    elif i < 8:
        q_luch.append(q_luch_ks * (1 - (12.5 * ((1.2 - D_[i]) ** 2))))
    elif i == 8:
        q_luch.append(q_luch_ks * 0.5)
    elif i > 8:
        q_luch.append(0.5 * q_luch_ks / (D_[i] ** 2))
for i in range(len(q_luch)):
    q_g.append(q_konv[i] + q_luch[i])
    #print(q_g[i])
# for i in range(len(lambd)):
# print(lambd[i], betta[i], Z_[i] ,B[i]*1000, q_konv[i]/1000000)
# print(S)
    #print(q_konv[i]/1000000, q_luch[i]/1000000, q_g[i]/1000000)

# print(delt_S)
# Расчет теплоотдачи в тракте охлаждения
K_m = 2.73
m_oxl = 0.7528*(m_t / (1 + K_m))
j = 0
T_oxl_real = []
T_oxl_i_ = 293
T_sr_i1 = T_oxl_i_
delta_T = []
c_p_sr_ = []
c_p_oxl = []
# print(delt_S[24-22], delt_S[23-22])
 #print(0.5 * (q_g[24-22] + q_g[23-22]) * 0.3 / (m_oxl * 3633))
#print(len(delt_S))
#print( delt_S[93], m_oxl, '--------------------------------')
#print(len(q_g), len(D_))
while j < (len(D_)-1):
    #print(j)
    c_p_oxl_0 = teplyom_gor(T_sr_i1)
    delta_t_i1 = 0.5 * (q_g[int(len(D_)) - 1 - j] + q_g[int(len(D_)) - 2 - j]) * delt_S[len(q_g) - 2 - j] / (m_oxl * c_p_oxl_0)
    T_sr_i1 = T_oxl_i_ + (0.5 * delta_t_i1)
    c_p_oxl_s1 = teplyom_gor(T_sr_i1)
    delta_t_i2 = 0.5 * (q_g[len(q_g) - 1 - j] + q_g[len(q_g) - 2 - j]) * delt_S[len(q_g) - 2 - j] / (m_oxl * c_p_oxl_s1)
    T_sr_i2 = T_oxl_i_ + (0.5 * delta_t_i2)
    c_p_oxl_s2 = teplyom_gor(T_sr_i2)
    delta_cp = abs(c_p_oxl_s2 - c_p_oxl_s1) / c_p_oxl_s1
    #print(T_sr_i1)
    #print(q_g[int(len(D_)) - 1 - j] ,'--', q_g[int(len(D_)) - 2 - j],'--', delt_S[len(q_g) - 2 - j],'--', m_oxl,'--', c_p_oxl_0)
    #print(c_p_oxl_s1,c_p_oxl_s2)
    if delta_cp <= 0.05 and delta_cp >= 0:
        delta_T.append(delta_t_i2)
        T_oxl_i_ += delta_t_i2
        T_oxl_real.append(T_oxl_i_)
        c_p_sr_.append(c_p_oxl_s2)
        #print(q_g[len(D_) - 1 - j], '------', q_g[len(D_) - 2 - j], '------', delt_S[len(D_) - 2 - j], '------', c_p_oxl_s2,m_oxl)
        #print(j)
        j += 1
    else:
        T_sr_i1 = T_sr_i2
    #print(j)


delta_T.reverse()
T_oxl_real.reverse()
T_oxl_real.append(293)
c_p_sr_.reverse()

# Расчнет коэффициента теплоотдачи
ro__u = []
K = []
alfa_oxl = []
lambd_oxl = []

for j in range(len(f)):
    c_p_oxl.append(teplyom_gor(T_oxl_real[j]))
for j in range(len(f)):
    ro__u.append(m_oxl / f[j])
for j in range(len(f)):
    K.append(KaKAkakA(T_oxl_real[j]))
for j in range(len(f)):
    lambd_oxl.append(lambda_oxl(T_oxl_real[j]))
for j in range(len(f)):
    alfa_oxl.append(0.023 * K[j] * (ro__u[j] ** 0.8) / (dg[j] ** 0.2))
# Расчет коэфициент оребрения
delt_p = 0.001
delt_st = 0.0001
dzet_p = 1
lammbd_oxl_ = []
din_vyaz_oxl = []
ro_oxl = []
u_oxl = []
E_oxl = []
kpd_oxl = []
T_st_g_real = []
#print(D)
for i in range(len(T_oxl_real)):
    Bi = 10 * alfa_oxl[i] * delt_p / lambda_oxl(T_oxl_real[i])
    psi = delt_p * ((2 * Bi) ** 0.5) / h_p
    # print(psi, Bi)
    E_psi = math.tanh(psi) / psi
    # print(E_psi)
    kpd_p = 1 + ((1 / math.cos(bet_rebr_spis[i])) * ((2 * h_p * E_psi * dzet_p / t[i]) - (delt_p / t[i])))
    din_vyaz_oxl.append(din_vyaz(T_oxl_real[i]))
    ro_oxl.append(plotn(T_oxl_real[i]))
    u_oxl.append(ro__u[i] / plotn(T_oxl_real[i]))
    E_oxl.append(E_psi)
    kpd_oxl.append(kpd_p)
# Определение температурного состояния стенки
lambda_st = 280
for i in range(len(T_oxl_real)):
    chisl_1 = T_0g / (T_0g - T_st_g)
    chisl_2 = T_oxl_real[i] / (((delt_st / lambda_st) + (1 / (alfa_oxl[i] * kpd_oxl[i]))) * q_g[i])
    chisl_3 = q_luch[i] / q_g[i]
    znam_1 = 1 / (T_0g - T_st_g)
    znam_2 = 1 / (((delt_st / lambda_st) + (1 / (alfa_oxl[i] * kpd_p))) * q_g[i])
    T_st_g_real_i = (chisl_1 + chisl_2 + chisl_3) / (znam_1 + znam_2)
    T_st_g_real.append(T_st_g_real_i)
    #print(chisl_1,'---', chisl_2,'---', chisl_3,'---', znam_1,'---', znam_2)
    #print(T_st_g_real_i)
#print(np)
plt.plot(x,q_g)
#plt.show()
# Расчет T_ст_г при наличии локальной завесы
# K_m_st = 0.537
# T_s = 523
# T_n = T_oxl_real[7]
# m_z = m_oxl * 0.01
# kpd_z = 0.75
# T_z_sr = (T_n + T_s) / 2
# c_z_sr = teplyom_gor(T_z_sr)
# alf_g = q_konv[7] / (T_0g - T_st_g)
# l_j = (kpd_z * m_z) / (3.14*D[7]) * ((c_z_sr * (T_s - T_n))/(alf_g * (T_0g - T_s)))
# K_m_st_ = K_m_st / (1 + ((1 + K_m_st)* m_z/m_st))
# S_Z =

# Расчет температуры стенки во втором приближении

# print('------------')
q__ = []
S_ = []
for i in range(len(T_oxl_real)):
    T_st_i = T_st_g_real[i] / T_0g
    S_i = (2.065 * c_p_sr * (T_0g - T_st_g_real[i]) * (mu ** 0.15)) / (
            ((R_0g * T_0g) ** 0.425) * ((1 + T_st_i) ** 0.595) * ((3 + T_st_) ** 0.15))
    q__i = q_g[i] * S_i / S
    q__.append(q__i)
    S_.append(S_i)
j = 0
T_st_g_real2 = []
for i in range(len(T_oxl_real)):
    chisl_1 = T_0g / (T_0g - T_oxl_real[i])
    chisl_2 = T_oxl_real[i] / (((delt_st / lambda_st) + (1 / (alfa_oxl[i] * kpd_p))) * q__[i])
    chisl_3 = q_luch[i] / q__[i]
    znam_1 = 1 / (T_0g - T_oxl_real[i])
    znam_2 = 1 / (((delt_st / lambda_st) + (1 / (alfa_oxl[i] * kpd_p))) * q__[i])
    T_st_g_real_i = (chisl_1 + chisl_2 + chisl_3) / (znam_1 + znam_2)
    T_st_g_real2.append(T_st_g_real_i)
    # print(T_st_g_real_i)

# Третье приближение
q___ = []
S__ = []
for i in range(len(T_oxl_real)):
    T_st_i = T_st_g_real[i] / T_0g
    S_i = (2.065 * c_p_sr * (T_0g - T_st_g_real2[i]) * (mu ** 0.15)) / (
            ((R_0g * T_0g) ** 0.425) * ((1 + T_st_i) ** 0.595) * ((3 + T_st_) ** 0.15))
    q__i = q_g[i] * S_i / S
    q___.append(q__i)
    S__.append(S_i)
j = 0
T_st_g_real3 = []
for i in range(len(T_oxl_real)):
    chisl_1 = T_0g / (T_0g - T_oxl_real[i])
    chisl_2 = T_oxl_real[i] / (((delt_st / lambda_st) + (1 / (alfa_oxl[i] * kpd_p))) * q___[i])
    chisl_3 = q_luch[i] / q___[i]
    znam_1 = 1 / (T_0g - T_oxl_real[i])
    znam_2 = 1 / (((delt_st / lambda_st) + (1 / (alfa_oxl[i] * kpd_p))) * q___[i])
    T_st_g_real_i = (chisl_1 + chisl_2 + chisl_3) / (znam_1 + znam_2)
    T_st_g_real3.append(T_st_g_real_i)

# Определение T_st_oxl
q__g = []
q___g = []
T_st_oxl = []
for i in range(len(q_g)):
    q__g.append(q__[i] + q_luch[i])
    q___g.append((q___[i] + q_luch[i]))
for i in range(len(T_oxl_real)):
    T_st_oxl_i = T_st_g_real3[i] - (delt_st * q___[i] / lambda_stt(T_st_g_real2[i]))
    T_st_oxl.append(T_st_oxl_i)
    print(T_st_oxl_i, '------------', T_st_g_real3[i], '--------', T_st_g_real[i])

# Расчет потерь давления охладителя в тракте охлаждения
sum_delt_p = 0
Re__ = []
delt__ = []
Re_gr = []
dzet__ = []
l__ = []
delt_p__ = []
for i in range(len(ro_oxl)-1):
    a_b = (tn[i] - delt_p) / h_p
    if a_b < 0.05:
        w = 1.5
    elif a_b > 0.05 and a_b < 0.1:
        w = 1.32
    elif a_b > 0.1 and a_b < 0.2:
        w = 1.25
    elif a_b > 0.2 and a_b < 0.3:
        w = 1.1
    elif a_b > 0.3 and a_b < 0.4:
        w = 1.03
    elif a_b > 0.4 and a_b < 0.5:
        w = 0.97
    elif a_b > 0.5 and a_b < 0.7:
        w = 0.91
    elif a_b > 0.7:
        w = 0.9
    Re = m_oxl / (3.14 * D[i] * din_vyaz(T_oxl_real[i]) * (10 ** (-4)))
    Re__.append(Re)
    ll = delt_x_s[i]
    delt_ = 0.005 / dg[i]
    if Re < 3500:
        dzet = 64 * w / Re
    elif Re > 3500 and delt_ < (560 / delt_):
        dzet = 1.42 * w / (math.log10(Re / delt_) ** 2)
    elif Re >= (560 / delt_):
        dzet = w / (4 * (math.log10(3.7 / delt_) ** 2))
    delta_p = dzet * ro_oxl[i] * ((ro__u[i] / ro_oxl[i]) ** 2) * ll / (2 * dg[i])
    sum_delt_p += delta_p
    delt__.append(0.005 / dg[i])
    Re_gr.append(560 / delt_)
    dzet__.append(dzet)
    l__.append(ll)
    delt_p__.append(delta_p)
#print(sum_delt_p / (14720000 + sum_delt_p))
#print(T_oxl_real[0] - T_oxl_real[-1])
#print(sum_delt_p)
tochki = []
for i in range(len(R_sech)):
    tochki.append(str(x[i]) + '\t' + str(R_sech[i]))
with open('kontur.txt', 'w') as toch:
    for i in tochki:
        toch.write(str(i) + '\n')
print(m_oxl)
print(sum_delt_p)
#for i in range(len(T_st_g_real)):
#    print(ro__u[i]/ro_oxl[i], '---')
for i in range(len(T_oxl_real)):
    print(T_oxl_real[i], ro__u[i]/ro_oxl[i])
print(h_p)



import pandas as pd
Geom_xarakt_SO = pd.DataFrame({'x':x, 'd':D, 'D_':D_, 'F':F, 'F_':F_, 'delt_x':delt_x, 'delt_X_S':delt_x_s, \
'delt_S':delt_S, 'np':np, 't':t, 'tn':tn, 'f':f, 'd_g':dg})
Geom_xarakt_SO.to_excel('./Geom_xarakt_SO.xlsx')
Rezult_gasch_ntpl_pot = pd.DataFrame({'x':x, 'kambd':lambd, 'bet':betta, 'Z_':Z_, 'B':B, 'qk':q_konv, 'ql':q_luch, 'q':q_g})
Rezult_gasch_ntpl_pot.to_excel('./Rezult_gasch_ntpl_pot.xlsx')

Rez_rasch_temp_oxl_i_stenk=pd.DataFrame({'T_oxl':T_oxl_real, 'Cp':c_p_oxl, 'lambd':lambd_oxl, 'ro':ro_oxl, 'K':K, 'u oxl':u_oxl, 'alf_oxl':alfa_oxl, 'E':E_oxl, 'kpd oxl':kpd_oxl, 'T_st_g': T_st_g_real})
Rez_rasch_temp_oxl_i_stenk.to_excel('./Rez_rasch_temp_oxl_i_stenk.xlsx')

Rez_rasch_temp_sost_ogn_st=pd.DataFrame({'x':x, 'alf_oxl':alfa_oxl, 'Q':q___g, 'T_oxl':T_oxl_real, 'T_st_g':T_st_g_real3, 'T_st_oxl':T_st_oxl})
Rez_rasch_temp_sost_ogn_st.to_excel('./Rez_rasch_temp_sost_ogn_st.xlsx')

Poteri=pd.DataFrame({'Re':Re__, 'delt_':delt__, 'Dzet':dzet__, 'deltp':delt_p__})
Poteri.to_excel('./Poteri.xlsx')