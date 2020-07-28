# Começar a rastrear código que está só na máquina
git init

# Como associar minha máquina a uma repositório no github
git remote add origin https://github.com/dorisluvizute/teste.git

# Clonar código de repositório já existente 
git clone https://github.com/dorisluvizute/Curso-Python-Udemy.git

# Incluir qualquer alteração feita no rastreio da máquina
git add .

# Confirmar a alteração no código
git commit -m"alteracao"

# Jogar nova versão no repositório
git push

# Atualizar código na máquina com alterações no repo
git pull
