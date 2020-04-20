import csv

def write2file(linha):
    with open('BGF.csv', 'a', newline='') as saida:
        escrever = csv.writer(saida, delimiter=';')
        escrever.writerow(linha)
    saida.close()
    

# Abertura do arquivo
file2work = open(r'\Users\rcardoso\Documents\Python Scripts\GarantiaFabril_02052018.csv', 'r')
file2work_reader = csv.reader(file2work , delimiter=';')
file2work_data = list(file2work_reader)


tamanho = len(file2work_data)
i = 0

while i < tamanho:
    if (file2work_data[i][4] == ''):
        linha = file2work_data[i]
        write2file(linha)
    i += 1

