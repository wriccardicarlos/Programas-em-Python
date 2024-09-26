import json

json_string = '{"nome":"Carlos","idade":21}'
objeto_python = json.loads(json_string)

print (objeto_python, type(objeto_python))

objeto_python = {"nome":'Carlos',"idade":21}
json_string = json.dumps(objeto_python)

print (json_string, type(json_string))

with open('texto_teste.txt','w') as arquivo:
    arquivo.write(json_string)

with open('texto_teste.json','r') as arquivo:
    objeto_json = json.load(arquivo)

print (objeto_json['nome'])
