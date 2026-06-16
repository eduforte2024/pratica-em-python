import random
import time
import os

SIMBOLOS = ["🍒", "🍋", "🍉", "⭐", "🔔", "💎", "7️⃣"]

saldo = 100
vitorias = 0

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def girar():
    return [
        random.choice(SIMBOLOS),
        random.choice(SIMBOLOS),
        random.choice(SIMBOLOS)
    ]

def animacao():
    print("\n🎰 Girando...\n")

    for _ in range(12):
        r = girar()
        print(f"\r{r[0]} | {r[1]} | {r[2]}", end="")
        time.sleep(0.15)

    print()
    return girar()

while True:
    limpar()

    print("=" * 35)
    print("      🎰 CAÇA-NÍQUEL PYTHON 🎰")
    print("=" * 35)
    print(f"💰 Saldo: {saldo} moedas")
    print(f"🏆 Vitórias: {vitorias}")
    print("=" * 35)

    if saldo <= 0:
        print("\n😢 Você ficou sem moedas!")
        break

    try:
        aposta = int(input("\nQuanto deseja apostar? "))

        if aposta <= 0:
            print("A aposta deve ser maior que zero.")
            time.sleep(2)
            continue

        if aposta > saldo:
            print("💸 Saldo insuficiente!")
            time.sleep(2)
            continue

    except ValueError:
        print("Digite um número válido!")
        time.sleep(2)
        continue

    saldo -= aposta

    resultado = animacao()

    r1, r2, r3 = resultado

    print("\n✨ Resultado Final ✨")
    print(f"{r1} | {r2} | {r3}\n")

    if r1 == r2 == r3:
        premio = aposta * 5
        saldo += premio
        vitorias += 1

        print(f"🎉 JACKPOT! Você ganhou {premio} moedas!")

    elif r1 == r2 or r2 == r3 or r1 == r3:
        premio = aposta * 2
        saldo += premio
        vitorias += 1

        print(f"🥳 Dois símbolos iguais!")
        print(f"Você ganhou {premio} moedas!")

    else:
        print("😔 Não foi dessa vez.")

    jogar_novamente = input(
        "\nPressione ENTER para continuar ou digite S para sair: "
    ).lower()

    if jogar_novamente == "s":
        break

print("\n🎮 Obrigado por jogar!")
print(f"🏆 Total de vitórias: {vitorias}")
print(f"💰 Saldo final: {saldo}")
