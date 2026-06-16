import time
import sys
import random

# Cores para o terminal
VERDE = "\033[92m"
AMARELO = "\033[93m"
NEON = "\033[96m"
RESET = "\033[0m"

def efeito_digitacao(texto, velocidade=0.03):
    """Faz o texto aparecer como se estivesse sendo digitado ao vivo."""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def carregamento_animado():
    total_barras = 30
    efeito_digitacao(f"\n{AMARELO}[!] Iniciando protocolo de libertação...{RESET}\n")
    time.sleep(0.5)
    
    progresso = 0
    while progresso <= 100:
        # Calcula o preenchimento real baseado na porcentagem atual
        blocos = int((progresso * total_barras) / 100)
        barra = "█" * blocos + "░" * (total_barras - blocos)
        
        # Mostra a barra com cores
        print(f"\r{NEON}Carregando: [{barra}] {progresso}%{RESET}", end='', flush=True)
        
        # Faz o carregamento parecer mais realista (com pequenas pausas aleatórias)
        if progresso < 100:
            progresso += random.randint(1, 4)
            if progresso > 100: progresso = 100
            time.sleep(random.uniform(0.02, 0.15))
        else:
            break
    print("\n") # Quebra de linha final

# --- Execução do programa ---
nome = input("Digite seu nome: ").strip()

carregamento_animado()

efeito_digitacao(f"{VERDE}🚀 Parabéns, {nome}! O plano foi ativado para a vida. Vamos deixar de ser CLT!{RESET}")
