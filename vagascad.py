import sys
 # importano o sys para poder usar o sys.exit() no else da verificação de idade
 # poderia usar apenas o exit(), mas quero explorar o máximo que puder.

vagas = ["Mecânico", "Eletricista", "Técnico de Informática", "Programador(a)"]

# Uma pequena lista para exibir as vagas

vagas.append("Engenheiro(a)")
vagas.append("Entregador(a)")
vagas.append("Técnico(a) em enfermagem")
# adicionei novas vagas com o parâmetro append

idade = int(input("Sua idade:"))
print("\n")

if idade >= 18:
    print("Liberado para cadastro!")

else:
    print("Acesso negado. Volte quando tiver 18!") 
    sys.exit()
    # AQUI TAMBÉM CABERIA UM exit()
    # Aqui um if-else (condicional) para verificas a condição de maioridade

print("\n")    


nome = str (input("Digite seu nome:"))
print("\n")



nome_social = input("Possui Nome Social? (Responda: Sim/Não):").strip().capitalize()
     # Usei .strip() e . capitalize() aqui, assim se o usuário digitar "sim", "Sim", "SIM" etc
     # o código roda normalmente
print("\n")

if nome_social == "Sim":
    
    nomex = str(input("Digite seu nome Social:"))
    print("\n")
    print(f"Seja Bem Vindo(a): {nomex}")
    print(idade, "Anos de idade")

elif nome_social == "Não":
    print("Seja Bem vindo(a):" +nome)
    print(idade, "Anos de idade")
print("\n")

# A forma de acessar as variáveis nomex e nome estão diferentes, mas foi proposital, apenas para treinar




print("\n")

print("VAGAS DISPONÍVEIS:")

print("\n")

# Um print com msg de boas vindas e 2 quebras de linhas, para organização.

for x in (vagas):
    print(x)

# Inseri esse pequeno FOR, para mostrar a lista na vertical, dando mais cara de sistema. 


