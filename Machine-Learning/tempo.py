segundos = int(input())

minutos, segundos = int(segundos/60), segundos%60
horas, minutos = int(minutos/60), minutos%60

while segundos>60:
    segundos-=60
    minutos+=1

while minutos>60:
    minutos-=60
    horas+=1

print("{}:{}:{}".format(horas,minutos,segundos))