def choquetIntegral(Set, measure, measureType = 'fuzzy'):
    """
    Calcula a Integral de Choquet para um conjunto e uma medida fornecidos.

    Parâmetros:
    - Set (list): Um conjunto de valores numéricos (pode representar critérios ou atributos).
    - measure (list): Uma medida associada ao conjunto Set. Pode ser uma medida difusa ou de Möbius.
    - measureType (str): Tipo da medida fornecida. Pode ser 'fuzzy' (medida difusa padrão), 
                         'simetricFuzzy' (medida difusa simétrica) ou 'mobius' (medida de Möbius).

    Descrição:
    A função implementa o cálculo da Integral de Choquet, que é usada em tomadas de decisão multicritério
    para agregar valores considerando interações entre os elementos do conjunto. O cálculo depende do tipo
    de medida fornecida:

    1. Para medidas difusas ('fuzzy' ou 'simetricFuzzy'):
       - Ordena-se o conjunto Set e cria-se um vetor de coeficientes baseado nas diferenças entre os valores
         ordenados consecutivos.
       - Multiplica-se esse vetor de coeficientes pela medida difusa ordenada correspondente para obter a integral.

    2. Para medidas de Möbius ('mobius'):
       - Gera-se todos os subconjuntos possíveis do conjunto Set (representados em ordem binária).
       - Calcula-se os coeficientes como o mínimo dos valores do conjunto Set em cada subconjunto.
       - Converte-se a medida difusa para a forma de Möbius e calcula-se a integral como o produto interno
         entre os coeficientes e a medida de Möbius.

    Retorno:
    - float: O valor da Integral de Choquet calculado com base nos parâmetros fornecidos.

    Exceções:
    - ValueError: É lançada se o tipo de medida fornecido não for válido ('fuzzy', 'simetricFuzzy' ou 'mobius').

    Observação:
    - A função assume que as funções auxiliares `sortedFuzzyMeasure`, `fuzzy2Mobius` e outras estão definidas
      corretamente no escopo global.
    """
