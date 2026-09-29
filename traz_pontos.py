from sympy import sympify, Symbol, lambdify

def calcular_pontos_livre():
    x = Symbol('x')
    
    print("=== Calculadora Interativa de f(x) ===")
    print("Dica: Use '*' para multiplicação e '**' para potência (ex: 2*x + 1 ou x**2 - 4/3*x)\n")
    
    # 1. Digita a função apenas uma vez
    while True:
        funcao_str = input("Digite a função f(x): ").strip()
        try:
            f_expr = sympify(funcao_str)
            # Converte a expressão SymPy em uma função numérica rápida
            f = lambdify(x, f_expr, 'math')
            break
        except Exception:
            print("Expressão inválida! Digite novamente usando a sintaxe correta do Python (ex: 3*x**2 - 5*x + 2).\n")

    print(f"\nFunção definida: f(x) = {f_expr}")
    print("--------------------------------------------------")
    print("Digite qualquer valor para 'x' para obter f(x).")
    print("Digite 'fim' ou pressione ENTER sem digitar nada para sair.")
    print("--------------------------------------------------\n")

    pontos_gerados = []
    
    # 2. Loop interativo e infinito para calcular x -> f(x)
    while True:
        entrada = input("Digite o valor de x: ").strip()
        
        if entrada.lower() == 'fim' or entrada == '':
            break
            
        try:
            # Suporta frações como entrada (ex: 1/2 ou -3/4)
            val_x = float(sympify(entrada))
            val_y = float(f(val_x))
            
            # Formatação para exibir inteiros sem o .0 (ex: 2.0 vira 2)
            val_x_print = int(val_x) if val_x.is_integer() else round(val_x, 4)
            val_y_print = int(val_y) if val_y.is_integer() else round(val_y, 4)
            
            ponto = (val_x_print, val_y_print)
            pontos_gerados.append(ponto)
            
            print(f"  -> Ponto: ({val_x_print}, {val_y_print})\n")
            
        except ValueError:
            print("Valor inválido! Digite um número para x (ex: 3, -1.5, 1/2).\n")
        except ZeroDivisionError:
            print("Erro: Divisão por zero para este valor de x!\n")

    # 3. Resumo dos pontos consultados durante a sessão
    if pontos_gerados:
        print("\n========================================")
        print("Resumo de todos os pontos gerados:")
        for px, py in pontos_gerados:
            print(f"  x = {px}  =>  f({px}) = {py}")
            
        print("\nLista formatada para copiar:")
        print(pontos_gerados)
        print("========================================")

if __name__ == "__main__":
    calcular_pontos_livre()