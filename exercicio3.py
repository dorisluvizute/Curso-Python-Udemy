cores = {
    'vermelho': 'red',
    'azul': 'blue',
    'verde': 'green',
    'amarelo': 'yellow',
    'branco': 'white',
    'preto': 'black'
}

cor = input('Digite uma cor para tradução: ').lower()

tradução = cores.get(cor, 'Esta cor não existe no dicionario.')

print(tradução)

# Função lower() transforma tudo oq o usuário escreve em letras minúsculas