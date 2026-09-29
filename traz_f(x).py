from sympy import symbols, Rational, simplify, Symbol

def encontrar_polinomio(pontos):
    x = Symbol('x')
    n = len(pontos)
    polinomio = 0
    
    # Interpolação de Lagrange
    for i in range(n):
        xi, yi = pontos[i]
        xi, yi = Rational(xi), Rational(yi)
        
        termo = 1
        for j in range(n):
            if i != j:
                xj = Rational(pontos[j][0])
                termo *= (x - xj) / (xi - xj)
                
        polinomio += yi * termo
        
    return simplify(polinomio)

def ler_pontos():
    # 1. Pergunta primeiro o número exato de pontos
    while True:
        try:
            qtd = int(input("Digite o número de pontos que deseja inserir: "))
            if qtd >= 2:
                break
            print("Você precisa de pelo menos 2 pontos para gerar um polinômio!\n")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.\n")

    pontos = []
    print(f"\nAgora digite os {qtd} pontos no formato x,y:\n")
    
    # 2. Loop para coletar a quantidade exata definida pelo usuário
    for i in range(1, qtd + 1):
        while True:
            entrada = input(f"Ponto {i} de {qtd}: ").strip()
            try:
                partes = entrada.split(',')
                if len(partes) != 2:
                    raise ValueError
                    
                x_val = float(partes[0].strip())
                y_val = float(partes[1].strip())
                
                # Validação: o valor de x não pode se repetir na interpolação
                if any(p[0] == x_val for p in pontos):
                    print("Erro: O valor de 'x' já foi digitado anteriormente! Digite um 'x' diferente.\n")
                    continue
                
                # Preserva números inteiros sem o .0
                x_val = int(x_val) if x_val.is_integer() else x_val
                y_val = int(y_val) if y_val.is_integer() else y_val
                
                pontos.append((x_val, y_val))
                break
            except ValueError:
                print("Formato inválido! Use o formato: x,y (exemplo: 3,5)\n")

    return pontos

if __name__ == "__main__":
    pontos = ler_pontos()
    resultado = encontrar_polinomio(pontos)
    
    print("\n----------------------------------------")
    print(f"Pontos informados: {pontos}")
    print(f"f(x) = {resultado}")
    print("----------------------------------------")