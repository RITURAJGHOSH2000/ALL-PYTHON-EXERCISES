P = float(input('Enter the pressure (in kPa): '))
PSI = P * 0.14503773773020923
PSI_format = "{:.2f}".format(PSI)
ML = P / 0.133322
ML_format = "{:.2f}".format(ML)
ATM = P / 101.325
ATM_format = "{:.2f}".format(ATM)
print(f'The pressure value of {P}kPa when converted to:\nPounds per square inch is {PSI_format}psi\nMillimeters of mercury is {ML_format}mmHg\nAtmosphere is {ATM_format}atm')
