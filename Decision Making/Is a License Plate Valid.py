lpl = input('Enter the first 3 letters present in the license plate: ')
lpd = input('Enter the last 3 or 4 digits present in the license plate: ')
if len(lpl) == 3 and len(lpd) == 3:
    print(
        f'The license plate number is {lpl.upper() + lpd} which is of older style and is VALID')
elif len(lpl) == 3 and len(lpd) == 4:
    print(
        f'The license plate number is {lpd + lpl.upper()} which is of newer style and is VALID')
else:
    print(f'The license plate number is NOT VALID')
