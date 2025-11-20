# 💻 Conversor de Texto para Binário

## 🌟 O que é este Repositório?

Este repositório contém um **script Python** simples e interativo, projetado para desmistificar a base da computação: a conversão de caracteres de texto em seu formato fundamental, o **código binário (0s e 1s)**.

O programa funciona como uma ferramenta educacional prática, permitindo ao usuário inserir qualquer palavra ou frase e visualizar, passo a passo, como ela é interpretada pelo computador.

## 🎯 Intuito e Propósito Educacional

O principal objetivo deste projeto é ser um recurso de aprendizado, atuando em três frentes:

1.  **Desmistificar o Binário:** Mostrar de forma clara que letras, números e símbolos são, na verdade, apenas sequências padronizadas de 0s e 1s no nível da máquina.
2.  **Entender a Codificação (ASCII/UTF-8):** Ilustrar o conceito de **tabelas de codificação**, como o valor decimal de um caractere (obtido via `ord()`) é o elo entre o texto que lemos e o binário que a máquina processa.
3.  **Praticar Python:** Oferecer um exemplo prático de manipulação de *strings* e formatação de saída em Python, utilizando funções essenciais como `ord()`, `bin()` e `zfill()`.

## ⚙️ Funcionalidades

O script `conversor.py` realiza as seguintes ações:

* **Entrada de Texto:** Solicita ao usuário que digite uma frase.
* **Conversão Caractere a Caractere:** Processa cada letra individualmente.
* **Exibição em Tabela:** Apresenta os resultados de forma organizada, mostrando:
    * O **Caractere** digitado.
    * O **Valor Decimal** correspondente (segundo a tabela de codificação).
    * O **Valor Binário** de 8 bits (1 Byte) formatado.
* **Explicação Teórica:** Oferece uma opção de exibir uma explicação detalhada sobre as três etapas de conversão (Codificação, Conversão de Base e Formatação em Byte).

## 🚀 Como Executar o Programa

### Pré-requisitos

Você só precisa ter o **Python 3** instalado em seu sistema operacional.

### Passos

1.  **Clone o Repositório** (ou baixe o arquivo `conversor.py`).
2.  **Abra o Terminal** ou Prompt de Comando na pasta onde o arquivo está salvo.
3.  **Execute o script** com o seguinte comando:

    ```bash
    python conversor.py
    ```

4.  Siga as instruções na tela e digite a frase que deseja converter.

## 📝 Base Teórica da Conversão

A mágica da conversão ocorre em três etapas que o script simula:

1.  **Busca na Tabela (Codificação):**
    * O Python usa a função `ord('A')` para encontrar o número decimal 65 (baseado na tabela de codificação UTF-8/ASCII).
2.  **Conversão de Base:**
    * O número decimal (65) é convertido para sua representação binária (Base 2), resultando em `1000001`.
3.  **Formatação (Byte):**
    * Para padronizar o armazenamento (1 Byte = 8 bits), um `0` é adicionado à esquerda: `01000001`.

**Dica:** Tente converter letras maiúsculas e minúsculas! Você verá que 'A' (65) e 'a' (97) têm binários completamente diferentes.
