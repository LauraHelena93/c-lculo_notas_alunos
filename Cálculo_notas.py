# Introdução à Programação - Cálculo de Notas
import os
import time
os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela para melhor visualização

# Programa para calcular a média de notas de um aluno
print("="*70)
print("Bem-vindo ao sistema unificado para cálculo de notas!".center(70))# Título centralizado
print("="*70)
print()
print("Aguarde um momento enquanto preparamos o ambiente...".center(70))# Mensagem centralizada
time.sleep(2)  # Simula um atraso de 2 segundos para criar uma experiência mais realista
print("Pronto! Vamos começar!".center(70))# Mensagem centralizada
print()

# Solicitar dados dos alunos
def cadastro_aluno():
    nome = input("Digite o nome do aluno: ")   

    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1} do aluno(a) {nome}: "))
        notas.append(nota)  
    
    return {"nome": nome, "notas": notas} 

# Função para calcular a média e verificar aprovação
def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media    

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"   
    
alunos = {}
num_alunos = int(input("Quantos alunos deseja cadastrar? "))# Solicita o número de alunos a serem cadastrados
print()  # Espaço para melhor visualização
for i in range(num_alunos):# Loop para cadastrar cada aluno
    aluno = cadastro_aluno()
    alunos[aluno["nome"]] = aluno["notas"]    
    print("\n" + "-"*50 + "\n") 

# Exibir resultados
print()# Espaço para melhor visualização
print("="*70)
print("Relatório de Notas dos Alunos".center(70))# Título centralizado
print("="*70)
print() 


for nome, notas in alunos.items():
    media = calcular_media(notas)
    situacao = verificar_aprovacao(media)

    print(f"Aluno: {nome}")  
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("-"*50) 

# Fim do programa