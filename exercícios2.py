meses = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
data_nasc = input ("Informe sua data de nascimento no formato DD-MM-AAAA: ")

indice = int (data_nasc[3:5]) - 1
mes = meses[indice]
print("Você nasceu no mês de",mes)

ano = int (data_nasc[6:10])
print("Você nasceu no ano de:",ano)