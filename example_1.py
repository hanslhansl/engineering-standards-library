from din743 import *
from din3990 import *
import diniso21771
import din6885
import din6892
from din3962 import din3962_2


print("Getriebegeometrie")
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
print()

print("Verzahnung")
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
print()

werkstoff = din743_3.S500
K_A = 1.75
K_S = 2.5

print("Kerbe Lamellenkupplung")
lamellenkupplung = Calculator(fall = 2,
    werkstoff = werkstoff,
    kerbe = din743_2.Passfeder(din6885.PassfederHoheForm(30, 43, din6885.Passfeder.Form.A), 2),
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
print()

print("Passfeder Lamellenkupplung")
din6892.C.Calculator(lamellenkupplung.kerbe, K_A, lamellenkupplung.M_tm, lamellenkupplung.werkstoff.sigma_S_d_B)
print()

print("Kerbe Ritzel")
ritzel = Calculator(fall = 2,
    werkstoff = lamellenkupplung.werkstoff,
    kerbe = din743_2.Passfeder(din6885.PassfederHoheForm(50, 54, din6885.Passfeder.Form.A), 1),
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
print()

print("Passfeder Ritzel")
din6892.C.Calculator(ritzel.kerbe, K_A, ritzel.M_tm, ritzel.werkstoff.sigma_S_d_B)
print()

print("Kerbe Rad")
rad = Calculator(fall = 2,
    werkstoff = werkstoff,
    kerbe = din743_2.Passfeder(din6885.PassfederHoheForm(70, 48.3, din6885.Passfeder.Form.B), 2),
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
print()

print("Passfeder Rad")
din6892.C.Calculator(rad.kerbe, K_A, rad.M_tm, rad.werkstoff.sigma_S_d_B)
print()

print("Kerbe drehstarre Kupplung")
drehstarr = Calculator(fall = 2,
    werkstoff = rad.werkstoff,
    kerbe = din743_2.Passfeder(din6885.PassfederHoheForm(55, 86, din6885.Passfeder.Form.A), 2),
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
print()

print("Passfeder drehstarre Kupplung")
din6892.C.Calculator(drehstarr.kerbe, K_A, drehstarr.M_tm, drehstarr.werkstoff.sigma_S_d_B)
print()

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
print()

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
print()

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
print()

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
print()