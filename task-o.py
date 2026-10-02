ruble=int(input())
kopeyka=int(input())
pirog=int(input())
kopeyka=pirog*kopeyka
ruble=(pirog*ruble)+(kopeyka // 100)
kopeyka = kopeyka % 100
print(ruble,kopeyka)