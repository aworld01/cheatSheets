"""
Power = Watt (W)
Current = Ampare (I)
Power fector = PF (0.8)
W = Watt
I = Current (Ampare)
R = Resistence (ohm)
V = Volt
pf = 0.8
root(3) = 1.732


DC current
----------
W = I*V
V = 12V
I = 200A
2400W = 12*200

I = W/V
W = 2400W
V = 12V
200V = 2400/12


AC current (Single phase)
-------------------------
V = 220V
pf = 0.8
P = 1000W
I = P/(V*pf)

5.69 = 1000W/(220V*0.8)


AC current (Three phase)
------------------------
V = 415V
pf = 0.08
P = 1000W
I = P/(root(3)*V*pf)

1.74 = 1000/(1.732*415*0.8)



R = V / I
V = R * I





"""


V = int(input("Enter the voltage: "))
W = int(input("Enter the watt: "))

def electricity(v,w):
    pf = 0.8
    A = w/(v*pf)
    ohm = v/A
    ohm =  f"{ohm:.2f}"
    I = f"{A:.2f}"
    I = float(I)
    watt = w*pf
    print()

    print(f"PF: {pf}")
    print(f"Voltage: {v} V")
    print(f"Watt before PF: {w} W")
    print(f"Watt after PF: {watt} VA")
    print(f"Current: {I} A")
    print(f"Resistence: {ohm} Ohm")
    
    if I < 6:
    	print(f"Bracker size: 6A")
    elif I > 6 and I < 10:
    	print(f"Bracker size: 10A")
    elif I > 10 and I < 16:
    	print(f"Bracker size: 16A")
    elif I > 16 and I < 20:
    	print(f"Bracker size: 20A")
    elif I > 20 and I < 25:
    	print(f"Bracker size: 25A")
    elif I > 25 and I < 32:
    	print(f"Bracker size: 32A")
    elif I > 32 and I < 40:
    	print(f"Bracker size: 40A")
    elif I > 40 and I < 50:
    	print(f"Bracker size: 50A")
    elif I > 50 and I < 63:
    	print(f"Bracker size: 63A")
    
electricity(V,W)