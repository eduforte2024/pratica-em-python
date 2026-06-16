# Autor: Majda Guillermo
# Fecha de creación: 08/08/2025
# Rock That Body Lyrics Player (Clean Text Version)

import sys
from time import sleep

def print_lyrics():
    # Lista de tuplas: (texto da linha, atraso por caractere)
    lines = [
        ("I wanna da-", 0.06),
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.07),
        ("I wanna rock your body", 0.08),
        ("I wanna go", 0.08),
        ("I wanna go for a ride", 0.068),
        ("Hop in the music and", 0.07),
        ("Rock your body", 0.08),
        ("Rock that body", 0.069),
        ("Come on, come on,", 0.035),
        ("Rock that body,", 0.05),
        ("(Rock your body)", 0.03),
        ("Rock that body", 0.049),
        ("Come on, come on,", 0.035),
        ("Rock that body", 0.08),
    ]
    
    # Tempo de espera após o término de cada linha
    delays = [0.2, 1, 0.2, 1, 0.2, 0.8, 0.2, 0.5, 0.18, 0.1, 0.15, 0.3, 0.3, 0.1, 5]
    
    print("-" * 40)
    print("      🎵 Reproduzindo: Rock That Body 🎵      ")
    print("-" * 40)
    print() # Linha em branco para separar o cabeçalho
    
    for i, (line, char_delay) in enumerate(lines):
        # Se for o coro de fundo, adiciona um recuo para os lados para destacar
        if line == "(Rock your body)":
            sys.stdout.write("   ")
            
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(char_delay)
            
        sys.stdout.write("\n")
        sys.stdout.flush()
        
        sleep(delays[i])
        
    print()
    print("-" * 40)

if __name__ == "__main__":
    try:
        print_lyrics()
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário. Até logo!")
        sys.exit(0)
