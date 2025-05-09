import numpy as np

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

    n = len(Set)

	if measureType == 'fuzzy' or measureType == 'simetricFuzzy':
		#cria o vetor de coeficientes que é multiplicado pelo vetor medida difusa para determinar a integral de Choquet
		Set0 = [0] + sorted(Set)
		xi0 = np.array(Set0)
		coefsCI = np.zeros(2**n)
		pos=0
		ant=1
		for j in range(1,n+1):
			pos += math.comb(n,j-1)
			ant = math.comb(n,j-1)
			coefsCI[2**n-pos+ant-1] = xi0[j]-xi0[j-1]
		return coefsCI@np.array(sortedFuzzyMeasure(Set, measure))

	elif measureType == 'mobius':
		# Gera todos os subconjuntos em ordem binária (0 a 2^n-1)
		subsets = []
		for i in range(2**n):
			bits = bin(i)[2:].zfill(n)
			subset = [j for j, bit in enumerate(reversed(bits)) if bit == '1']
			subsets.append(subset)
		
		# Calcula os coeficientes como o mínimo do conjunto em cada subconjunto
		coefs_mobius = np.zeros(2**n)
		for idx, subset in enumerate(subsets):
			if not subset:  # Subconjunto vazio
				coefs_mobius[idx] = 0.0
			else:
				coefs_mobius[idx] = min(Set[j] for j in subset)
		
		# Calcula a integral como o produto interno entre coeficientes e medida de Möbius
		return coefs_mobius @ np.array(fuzzy2Mobius(measure))  # Converte a medida difusa para a forma de Möbius antes de calcular o produto interno

	else:
		raise ValueError("Tipo de medida inválido. Use 'fuzzy', 'simetricFuzzy' ou 'mobius'.")
