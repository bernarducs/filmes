import csv

# lendo um arquivo com 1 uma info por linha
with open('test.csv') as arquivo:
    leitor = csv.reader(arquivo)
    dados = [d[0] for d in leitor]

# salvando um arquivo com 1 uma info por linha
with open('test.csv', 'w') as arquivo:
    leitor = csv.writer(arquivo)
    for dado in dados:
        leitor.writerow([dado])
