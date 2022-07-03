w = int(input('Enter the wavelength of the light within visible range: '))
if w >= 380 and w < 450:
    print(f'The colour of the light of wavelength {w} is Violet')
elif w >= 450 and w < 495:
    print(f'The colour of the light of wavelength {w} is Blue')
elif w >= 495 and w < 570:
    print(f'The colour of the light of wavelength {w} is Green')
elif w >= 570 and w < 590:
    print(f'The colour of the light of wavelength {w} is Yellow')
elif w >= 590 and w < 620:
    print(f'The colour of the light of wavelength {w} is Orange')
elif w >= 620 and w <= 750:
    print(f'The colour of the light of wavelength {w} is Red')
else:
    print(
        f'The colour of the light of wavelength {w} is out of the visible spectrum')
