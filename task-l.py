n = int(input())

h = n // 3600
m = (n % 3600) // 60
s = n % 60

print(h, ':', m + (m < 10) * 0, ':', s + (s < 10) * 0, sep='')