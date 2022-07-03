s1 = float(input('Enter the length of 1st side: '))
s2 = float(input('Enter the length of 2nd side: '))
s3 = float(input('Enter the length of 3rd side: '))
if s1 == s2 == s3:
    print('The triangle is equilateral in nature')
elif s1 == s2 or s1 == s3 or s2 == s3:
    print('The triangle is isosceles in nature')
elif s1 != s2 or s2 != s3 or s1 != s3:
    print('The triangle is scalene in nature')
