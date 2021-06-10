'''
Given the integer N - the number of minutes that is passed since midnight
- how many hours and minutes are displayed on the 12h digital clock.
The program should print two numbers:the numbers of hours between 0 and 23 and the number of minutes between 0 and 59
'''
N = int(input('the numbers of minutes that is passed since midnight:'))
H = N//60
M = N%60
print(f'the number of hours {H} displayed on the digital clock')
print (f'the number of minutes {M} displayed on the digital clock')
print (f'the time displayed on clock is {H}:{M}')