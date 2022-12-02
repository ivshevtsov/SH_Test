import numpy as np

'''
A_set = {1,2,3,4,5,6}
B_set = {1,2,3,7,4,5,6}
A_set.add('hello')
print(A_set-B_set)
print(B_set-A_set)
print(B_set^A_set)
'''

def buf_calc(Id, Veff, uCox, Vin=1.22, R_PPF=800):
    Cox = 4e-3
    Lmin = 550e-9
    gm = 2*Id/Veff
    Rbuf = 1/gm
    W = 2*Id*Lmin/(uCox*Veff)
    Cgs = (2/3)*W*Lmin*Cox
    Loss = R_PPF/(R_PPF+Rbuf)
    Loss_dB = 20*np.log10(Loss)

    print(f'Transconductance {gm*1e3} mS')
    print(f'Width {W * 1e6} um')
    print(f'Buffer resistance {Rbuf} Ohm')
    print(f'Input capacitance {Cgs*1e15} fF')
    print(f'Loss dB {Loss_dB}')
    print(f'Loss {Loss}')
    print(f'Loss in voltages {Vin*Loss}')


buf_calc(Id=500e-6, Veff=0.2, uCox=55e-6)


print(1.22*0.6 * 0.60 * 0.60 )
print(2.20*0.8 * 0.65 * 0.65 )

one=25
n_sim = 280 + 250
multiple = one*n_sim/60
print(f'ppf calc {multiple} hours')
print(f'ppf calc {multiple/24} days')

#for mixer we must watch input impedance for matching
#and design proper buffer with correct input cap
#input buffers must be much higher





