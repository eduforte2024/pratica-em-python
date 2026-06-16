import os

def limpar_tela():
    """Limpa o terminal para manter o menu organizado."""
    os.system('cls' if os.name == 'nt' else 'clear')

def ler_nota(mensagem, nota_maxima):
    """Garante que o usuário digite apenas números entre 0 e a nota máxima estipulada."""
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= nota_maxima:
                return nota
            print(f"❌ Erro: A nota deve estar entre 0.0 e {nota_maxima}.0.")
        except ValueError:
            print("❌ Erro: Digite um número válido (ex: 7.5).")

def ler_inteiro(mensagem):
    """Garante a digitação de um número inteiro positivo."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor > 0:
                return valor
            print("❌ Erro: O valor deve ser maior que zero.")
        except ValueError:
            print("❌ Erro: Digite um número inteiro válido.")

# --- CADASTRO DE ALUNOS ---
alunos = []
limpar_tela()
print("=== SISTEMA DE CADASTRO ACADÊMICO ===")
qntdaluno = ler_inteiro("Quantos alunos serão cadastrados? ")

for i in range(qntdaluno):
    print(f"\n📝 Cadastro do Aluno {i+1}:")
    nome = input("Nome: ").strip().title()
    
    # Entrada de dados com as novas nomenclaturas e limites de pontos
    ativ1 = ler_nota("-> Nota Atividade 1 (Máx 10): ", 10)
    ativ2 = ler_nota("-> Nota Atividade 2 (Máx 10): ", 10)
    
    prova1 = ler_nota("-> Nota Prova 1 (Máx 100): ", 100)
    prova2 = ler_nota("-> Nota Prova 2 (Máx 100): ", 100)
    prova3 = ler_nota("-> Nota Prova 3 (Máx 100): ", 100)
    
    trabalho = ler_nota("-> Nota Trabalho (Máx 50): ", 50)
    
    # --- CONVERSÃO DE ESCALA (Tudo para base 10) ---
    # Atividades já estão na base 10.
    # Provas (0 a 100) dividimos por 10.
    p1_base10 = prova1 / 10
    p2_base10 = prova2 / 10
    p3_base10 = prova3 / 10
    # Trabalho (0 a 50) dividimos por 5.
    trab_base10 = trabalho / 5

    # --- CÁLCULO DAS MÉDIAS ---
    # Média Teórica (MT): Média das duas Atividades (Peso 0.4 para Ativ1 e 0.6 para Ativ2)
    MT = 0.4 * ativ1 + 0.6 * ativ2
    
    # Média Prática (MP): Média simples das 3 Provas + Nota do Trabalho convertido
    MP = (p1_base10 + p2_base10 + p3_base10 + trab_base10) / 4

    # Média Final (MF)
    if MT > 5.0 and MP > 5.0:
        MF = 0.3 * MP + 0.7 * MT
    else:
        MF = min(MT, MP)

    # Armazenando os dados no dicionário
    alunos.append({
        "nome": nome,
        "atividades": [ativ1, ativ2],
        "provas": [prova1, prova2, prova3],
        "trabalho": trabalho,
        "MT": MT,
        "MP": MP,
        "MF": MF
    })

# --- MENU PRINCIPAL INTERATIVO ---
while True:
    input("\nPressione [ENTER] para ir ao Menu...")
    limpar_tela()
    
    print("=" * 30)
    print("       MENU DE OPÇÕES")
    print("=" * 30)
    print(" [1] Boletim da Sala\n [2] Buscar por Nome\n [3] Maior Nota da Sala\n [4] Menor Nota da Sala\n [5] Estatísticas de Aprovados\n [6] Sair")
    print("=" * 30)
    
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print(f"\n{'Nome':<20}{'MT':<6}{'MP':<6}{'MF':<6}{'Situação'}")
        print("-" * 50)
        for aluno in alunos:
            situacao = "APROVADO" if aluno['MF'] >= 5.0 else "REPROVADO"
            print(f"{aluno['nome']:<20}{aluno['MT']:<6.1f}{aluno['MP']:<6.1f}{aluno['MF']:<6.1f}{situacao}")

    elif opcao == "2":
        nome_busca = input("\nDigite o nome para buscar: ").strip().lower()
        encontrado = False
        for aluno in alunos:
            if nome_busca in aluno['nome'].lower():
                print(f"\n📌 Aluno: {aluno['nome']}")
                print(f"   Atividades: Ativ 1 = {aluno['atividades'][0]} | Ativ 2 = {aluno['atividades'][1]} -> MT: {aluno['MT']:.1f}")
                print(f"   Provas: P1 = {aluno['provas'][0]} | P2 = {aluno['provas'][1]} | P3 = {aluno['provas'][2]}")
                print(f"   Trabalho: {aluno['trabalho']} -> MP (Provas + Trab): {aluno['MP']:.1f}")
                print(f"   💥 Média Final (MF): {aluno['MF']:.1f}")
                encontrado = True
        if not encontrado:
            print("❌ Aluno não encontrado!")

    elif opcao == "3":
        maior = max(alunos, key=lambda x: x['MF'])
        print(f"\n🏆 Maior Média Final: {maior['nome']} com Nota {maior['MF']:.1f}")

    elif opcao == "4":
        menor = min(alunos, key=lambda x: x['MF'])
        print(f"\n⚠️ Menor Média Final: {menor['nome']} com Nota {menor['MF']:.1f}")

    elif opcao == "5":
        aprovados = sum(1 for aluno in alunos if aluno['MF'] >= 5.0)
        percaprovados = (aprovados / len(alunos)) * 100
        print(f"\n📊 Estatísticas da Turma:")
        print(f"   Total de Alunos: {len(alunos)}")
        print(f"   Alunos Aprovados: {aprovados} ({percaprovados:.1f}%)")
        print(f"   Alunos Reprovados: {len(alunos) - aprovados}")

    elif opcao == "6":
        print("\n👋 Sistema encerrado com sucesso. Até logo!")
        break
    else:
        print("❌ Opção inválida! Escolha um número de 1 a 6.")
