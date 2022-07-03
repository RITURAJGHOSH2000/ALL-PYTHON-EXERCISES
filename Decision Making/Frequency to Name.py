f = float(input('Enter the frequency of the radiation: '))
if f >= (3 * (10 ** 3)) and f < (3 * (10 ** 9)):
    print(f'The name of the radiation of frequency {f} is Radio Wave')
elif f >= (3 * (10 ** 9)) and f < (3 * (10 ** 12)):
    print(f'The name of the radiation of frequency {f} is Microwave')
elif f >= (3 * (10 ** 12)) and f < (4.3 * (10 ** 14)):
    print(f'The name of the radiation of frequency {f} is Infrared Light')
elif f >= (4.3 * (10 ** 14)) and f < (7.5 * (10 ** 14)):
    print(f'The name of the radiation of frequency {f} is Visible Light')
elif f >= (7.5 * (10 ** 14)) and f < (3 * (10 ** 17)):
    print(f'The name of the radiation of frequency {f} is Ultraviolet Light')
elif f >= (3 * (10 ** 17)) and f < (3 * (10 ** 19)):
    print(f'The name of the radiation of frequency {f} is X-Ray')
elif f >= (3 * (10 ** 19)):
    print(f'The name of the radiation of frequency {f} is Gamma Ray')
else:
    print(f'The name of the radiation of frequency {f} is not known')
