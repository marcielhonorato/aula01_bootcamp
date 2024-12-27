CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome

nome_usuario = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário Converte a entrada para um número de ponto flutuante

salario_usuario = float(input("Digite o valor do salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido Converte a entrada para um número de ponto flutuante

bonus_usuario = float(input("Digite o valor do bônus: "))

# 4) Calcule o valor do bônus final

valor_do_bonus = CONSTANTE_BONUS + (salario_usuario * bonus_usuario)

# 5) Imprima cálculo do KPI para o usuário

print(f"O usuario {nome_usuario}, recebeu um bônus de R$ {valor_do_bonus}")

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"O usuario {nome_usuario}, com um salário de R$ {salario_usuario}, recebeu um bônus de R$ {CONSTANTE_BONUS}, total de: R${valor_do_bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
    # Utilizar numeros por engano no nome, para a nossa regra não serve
    # Colocar ',' em variavel do tipo float, quebrará o programa
    # O programa aceita valores negativos, para a nossa regra não serve
    