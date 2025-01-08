from din743 import *
from din3990 import *
import diniso21771
from din3962 import din3962_2


print("Verzahnung")
S_Hstatmin = 1.3
S_Hdyn_interval = (1.2, 1.5)
S_Fstatmin = 3.5
S_Fdyn_interval = (1.5, 2)
geometrie = diniso21771.GearGeometry(m_n = 4,
                    z = (19, 104),
                    x = (0.5, 0.15),
                    bezugsprofil = (din3990_11.Normalprofil1, din3990_11.Normalprofil1),
                    beta = 0,
                    k = 0,
                    b_d_1_verhältnis = 0.64)

werkstoff = din3990_5.Werkstoff(din3990_5.Werkstoff.Art.Einsatzstahl, 1500, 860, 220)
getriebe = din3990_11.Calculator(geometrie = geometrie, P = 55,
            n_1 = 980,
            verzahnungsqualität = (din3962_2.GearToothQuality.DIN6, din3962_2.GearToothQuality.DIN7),
            werkstoff = (werkstoff, werkstoff),
            K_A = 1.75,
            K_S = 2.5,
            R_z = (5, 5),

            anpassungsmaßnahmeUndFlankenlinienkorrektur = din3990_11.AnpassungsmaßnahmeUndFlankenlinienkorrektur.ohne,
            f_ma = 0,  # Annahme, siehe Fußnote 5
            s = 0,
            fertigungsverfahren = (din3990_11.Fertigungsverfahren.geläpptGeschliffenGeschabt, din3990_11.Fertigungsverfahren.geläpptGeschliffenGeschabt),

            S_Hstatmin=S_Hstatmin, S_Hdynmin=S_Hdyn_interval, S_Fstatmin=S_Fstatmin, S_Fdynmin=S_Fdyn_interval,

            _assert = True)

assert geometrie.b / geometrie.m_n <= 30 # Konstruktionsvorgaben Tabelle 4
assert getriebe.R_z100 < 4 # Konstruktionsvorgaben Seite 7


werkstoff = din743_3.S500
K_A = 1.75
K_S = 2.5

print("Passfeder Lamellenkupplung")
lamellenkupplung = Calculator(fall = 2,
    werkstoff = werkstoff,
    kerbe = din743_2.Passfeder(d = 30, i = 2),
    d_eff = 56,
    F_zdm = 0,
    F_zda = 0,
    F_zdmax = 0,
    M_bm = 0,
    M_ba = 0,
    M_bmax = 0,
    M_tm = 535.93,
    M_ta = 0,
    M_tmax = 535.93 * K_S,
    Rz = 16,
    K_V = 1,
    harte_randschicht = False)
l = lamellenkupplung.werkstoff.sigma_S_d_B * 0.9 * (7 - 4) * (35) * lamellenkupplung.kerbe.d / 2 * 2 * 0.75 / 1000
r = 535.93 * 1.75
print(f"{l} >= {r}")
print(l/r)
print()
assert l >= r

print("Passfeder Ritzel")
ritzel = Calculator(fall = 2,
    werkstoff = lamellenkupplung.werkstoff,
    kerbe = din743_2.Passfeder(d = 50, i = 1),
    d_eff = 56,
    F_zdm = 0,
    F_zda = 0,
    F_zdmax = 0,
    M_bm = 0,
    M_ba = 450.256 * K_A,
    M_bmax = 450.256 * K_S,
    M_tm = 535.93,
    M_ta = 0,
    M_tmax = 535.93 * K_S,
    Rz = 16,
    K_V = 1,
    harte_randschicht = False)
l = ritzel.werkstoff.sigma_S_d_B * 0.9 * (9 - 5.5) * (40) * ritzel.kerbe.d / 2 * 1 * 1 / 1000
r = 535.93 * 1.75
print(f"{l} >= {r}")
print(l/r)
print()
assert l >= r

print("Passfeder Rad")
rad = Calculator(fall = 2,
    werkstoff = werkstoff,
    kerbe = din743_2.Passfeder(d = 70, i = 2),
    d_eff = 78,
    F_zdm = 0,
    F_zda = 0,
    F_zdmax = 0,
    M_bm = 0,
    M_ba = 313.678 * K_A, 
    M_bmax = 313.678 * K_S,
    M_tm = 2933.511,
    M_ta = 0, 
    M_tmax = 2933.511 * K_S,
    Rz = 16,
    K_V = 1,
    harte_randschicht = False)
l = rad.werkstoff.sigma_S_d_B * 0.9 * (12 - 7.5) * (48.3) * rad.kerbe.d / 2 * 2 * 0.75 / 1000
r = 2933.511 * 1.75
print(f"{l} >= {r}")
print(l/r)
print()
assert l >= r

print("Passfeder drehstarre Kupplung")
drehstarr = Calculator(fall = 2,
    werkstoff = rad.werkstoff,
    kerbe = din743_2.Passfeder(d = 55, i = 2),
    d_eff = 78,
    F_zdm = 0, 
    F_zda = 0, 
    F_zdmax = 0,
    M_bm = 0,
    M_ba = 0, 
    M_bmax = 0,
    M_tm = 2933.511,
    M_ta = 0, 
    M_tmax = 2933.511 * K_S,
    Rz = 16,
    K_V = 1,
    harte_randschicht = False)
l = drehstarr.werkstoff.sigma_S_d_B * 0.9 * (10 - 6) * 70 * drehstarr.kerbe.d / 2 * 2 * 0.75 / 1000
r = 2933.511 * 1.75
print(f"{l} >= {r}")
print(l/r)
print()
assert l >= r

print("Absatz 1")
absatz1 = Calculator(fall = 2,
    werkstoff = werkstoff,
    kerbe = din743_2.Absatz(d = 60, r = 1, t = 5),
    d_eff = 78,
    F_zdm = 0, 
    F_zda = 0,
    F_zdmax = 0,
    M_bm = 0,
    M_ba = 135.977 * K_A,
    M_bmax = 135.977 * K_S,
    M_tm = 2933.511,
    M_ta = 0,
    M_tmax = 2933.511 * K_S,
    Rz = 16,
    K_V = 1,
    harte_randschicht = False)

print("Absatz 2")
absatz2 = Calculator(fall = 2,
    werkstoff = werkstoff,
    kerbe = din743_2.Absatz(d = 70, r = 1, t = 4),
    d_eff = 78,
    F_zdm = 0,
    F_zda = 0,
    F_zdmax = 0,
    M_bm = 0,
    M_ba = 131.175 * K_A,
    M_bmax = 131.175 * K_S,
    M_tm = 2933.511,
    M_ta = 0, 
    M_tmax = 2933.511 * K_S,
    Rz = 16,
    K_V = 1,
    harte_randschicht = False)

print("Absatz 3")
absatz3 = Calculator(fall = 2,
    werkstoff = werkstoff,
    kerbe = din743_2.Absatz(d = 60, r = 1, t = 9),
    d_eff = 78,
    F_zdm = 0,
    F_zda = 0,
    F_zdmax = 0,
    M_bm = 0,
    M_ba = 6.003 * K_A,
    M_bmax = 6.003 * K_S,
    M_tm = 2933.511,
    M_ta = 0,
    M_tmax = 2933.511 * K_S,
    Rz = 16,
    K_V = 1,
    harte_randschicht = False)

print("Freistrich 1")
freistrich1 = Calculator(fall = 2,
    werkstoff = werkstoff,
    kerbe = din743_2.Freistrich(d = 55.4, r = 1, t = 2.3),
    d_eff = 78,
    F_zdm = 0,
    F_zda = 0,
    F_zdmax = 0,
    M_bm = 0,
    M_ba = 0,
    M_bmax = 0,
    M_tm = 2933.511,
    M_ta = 0, 
    M_tmax = 2933.511 * K_S,
    Rz = 16,
    K_V = 1,
    harte_randschicht = False)