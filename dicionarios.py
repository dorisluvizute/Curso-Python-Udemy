# Dicionário também é um conjunto de valores
# Esses valores não são uma sequência ordenada, não posso acessar pelos índices
# São sempre formados por 2 valores
joao = {"nome": "joao", "sobrenome": "pereira", "profissão": "programador python", "filhos": ["pedro","maria"]}
print(type(joao))
print(joao["sobrenome"])
print(joao["filhos"])

# Posso descobrir a quantidade de indices
print(len(joao))

# Posso deletar indices com a chave del
del joao["filhos"]
print(joao)

# Posso trocar informações
joao["profissão"] = "aposentado"
print(joao)

# Posso confirmar dados com a chave in
print("sobrenome" in joao)
print("idade" in joao)

# A função get coloca condições de verificação no dicionário
print(joao.get('nome', 'Esta informação não consta no cadastro'))
print(joao.get('idade', 'Esta informação não consta no cadastro'))

joao['filhos'] = ['pedro','maria']
print(joao)

# Adicionar uma informação:
joao['filhos'].append('jorge')
print(joao)

# Limpar todas as informações do dicionario
joao.clear()
print(joao)