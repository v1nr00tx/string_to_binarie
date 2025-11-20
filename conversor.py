def conversor_binario_texto():
    """
    Solicita uma frase ao usuário e exibe o valor decimal (ASCII/UTF-8)
    e o valor binário de cada caractere na frase.
    """
    print("--- Conversor de Texto para Binário ---")
    
    # 1. Solicita a entrada
    texto = input("Digite a frase ou palavra que você deseja converter: ")
    
    print("\nProcessando a string: '{}'".format(texto))
    print("-" * 30)

    # Dicionário para armazenar os resultados
    resultados = []
    
    # 2. Itera sobre cada caractere
    for caractere in texto:
        # Pega o valor decimal (ASCII/UTF-8)
        # A função 'ord()' faz o trabalho de buscar o valor na tabela de codificação
        valor_decimal = ord(caractere)
        
        # Converte o decimal para binário
        # 'bin()' retorna uma string binária com prefixo '0b' (ex: '0b1000001')
        # '[2:].zfill(8)' remove o '0b' e garante que a string tenha 8 bits (um byte)
        valor_binario = bin(valor_decimal)[2:].zfill(8)
        
        resultados.append({
            "caractere": caractere,
            "decimal": valor_decimal,
            "binario": valor_binario
        })

    # 3. Exibe os resultados na tabela
    print("\n{:^10} {:^10} {:^10}".format("Caractere", "Decimal", "Binário (8 bits)"))
    print("=" * 30)
    for resultado in resultados:
        print("{:^10} {:^10} {:^10}".format(
            resultado["caractere"], 
            resultado["decimal"], 
            resultado["binario"]
        ))
    
    print("-" * 30)
    
    # 4. Oferece a explicação
    opcao = input("\nDeseja ver a explicação de como o computador chegou nesses valores? (S/N): ").strip().upper()
    if opcao == 'S':
        explicacao()

def explicacao():
    """
    Exibe a explicação detalhada do processo de codificação/conversão.
    """
    print("\n## ✨ Explicação: Como o Computador Converte Texto")
    print("---")
    print("O processo de transformar uma letra em binário segue 3 etapas principais:")
    
    # 1. Codificação (ASCII/UTF-8)
    print("\n### 1. Codificação (Tabela)")
    print("* O computador não entende letras. Ele usa uma **Tabela de Codificação** (como ASCII ou UTF-8) para atribuir um **número decimal** exclusivo a cada caractere.")
    print("* Exemplo: A letra 'A' (maiúscula) tem o número decimal 65 (no padrão ASCII).")
    print("* **No nosso código, a função `ord()` faz essa consulta na tabela.**")
    
    # 2. Conversão (Decimal para Binário)
    print("\n### 2. Conversão de Base")
    print("* O número decimal (ex: 65) é então convertido para o sistema **binário (base 2)**, que usa apenas 0s e 1s.")
    print("* Isso é feito através de **divisões sucessivas por 2**.")
    print("* Exemplo: 65 em decimal se torna **1000001** em binário (base 2).")
    print("* **No nosso código, a função `bin()` realiza essa conversão.**")
    
    # 3. Formatação (Byte)
    print("\n### 3. Armazenamento em Byte (8 bits)")
    print("* Para padronização, a maioria dos caracteres é armazenada em **1 Byte**, que é uma sequência de **8 bits**.")
    print("* Se a sequência binária tiver menos de 8 bits (como 1000001, que tem 7 bits), adicionamos um **0 à esquerda** para completar o Byte.")
    print(r"* Exemplo: $1000001 \rightarrow \mathbf{01000001}$.")
    print("* **No nosso código, a função `.zfill(8)` garante que tenhamos 8 dígitos.**")
    
    print("\n**Conclusão:** É assim que a letra 'A' se torna o Byte '01000001' no computador!")

# Executa o programa
conversor_binario_texto()
