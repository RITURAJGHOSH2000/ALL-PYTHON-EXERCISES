m = float(input('Enter the earthquake magnitude from the Richter Scale: '))
if m < 2.0:
    print(
        f'A magnitude of {m} earthquake in the Richter Scale is considered as Micro')
elif m >= 2.0 and m < 3.0:
    print(
        f'A magnitude of {m} earthquake in the Richter Scale is considered as Very Minor')
elif m >= 3.0 and m < 4.0:
    print(
        f'A magnitude of {m} earthquake in the Richter Scale is considered as Minor')
elif m >= 4.0 and m < 5.0:
    print(
        f'A magnitude of {m} earthquake in the Richter Scale is considered as Light')
elif m >= 5.0 and m < 6.0:
    print(
        f'A magnitude of {m} earthquake in the Richter Scale is considered as Moderate')
elif m >= 6.0 and m < 7.0:
    print(
        f'A magnitude of {m} earthquake in the Richter Scale is considered as Strong')
elif m >= 7.0 and m < 8.0:
    print(
        f'A magnitude of {m} earthquake in the Richter Scale is considered as Major')
elif m >= 8.0 and m < 10.0:
    print(
        f'A magnitude of {m} earthquake in the Richter Scale is considered as Great')
elif m >= 10.0:
    print(
        f'A magnitude of {m} earthquake in the Richter Scale is considered as Metric')
