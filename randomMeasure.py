import numpy as np

def randomMatrix(m, n, a, b, decisionMatrixType, method, seed=None, numDigits=6):

	if seed is not None:
		np.random.seed(seed)
	
	# Verifica se o intervalo [a, b] é válido
	if a >= b:
		raise ValueError("O intervalo [a, b] deve satisfazer a < b.")
	
	# Função auxiliar para truncar valores no intervalo [a, b]
	def truncate(values, a, b):
		return np.clip(values, a, b)
	
	# Geração da matriz com base na distribuição e método escolhidos
	if decisionMatrixType == 'uniform':
		matrix = np.round(np.random.uniform(low=a, high=b, size=(m, n)), numDigits)
	
	elif decisionMatrixType == 'normal':
		if method == 'truncated':
			matrix = []
			while len(matrix) < m * n:
				sample = np.random.normal(loc=(a + b) / 2, scale=(b - a) / 6)
				if a <= sample <= b:
					matrix.append(sample)
			matrix = np.array(matrix[:m * n]).reshape((m, n))
		elif method == 'normalized':
			matrix = np.random.normal(loc=(a + b) / 2, scale=(b - a) / 6, size=(m, n))
			matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))  # Normaliza para [0, 1]
			matrix = a + matrix * (b - a)  # Escala para [a, b]
		else:
			raise ValueError("Método inválido. Escolha 'normalized' ou 'truncated'.")
		matrix = np.round(matrix, numDigits)
	
	elif decisionMatrixType == 'exponential':
		if method == 'truncated':
			matrix = []
			while len(matrix) < m * n:
				sample = np.random.exponential(scale=1.0)
				if a <= sample <= b:
					matrix.append(sample)
			matrix = np.array(matrix[:m * n]).reshape((m, n))
		elif method == 'normalized':
			matrix = np.random.exponential(scale=1.0, size=(m, n))
			matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))  # Normaliza para [0, 1]
			matrix = a + matrix * (b - a)  # Escala para [a, b]
		else:
			raise ValueError("Método inválido. Escolha 'normalized' ou 'truncated'.")
		matrix = np.round(matrix, numDigits)
	
	elif decisionMatrixType == 'beta':
		if method == 'truncated':
			matrix = np.random.beta(a=2, b=2, size=(m, n))  # Beta centrado em torno de 0.5
			matrix = truncate(matrix, a, b)
		elif method == 'normalized':
			matrix = np.random.beta(a=2, b=2, size=(m, n))  # Beta centrado em torno de 0.5
			matrix = a + matrix * (b - a)  # Escala para [a, b]
		else:
			raise ValueError("Método inválido. Escolha 'normalized' ou 'truncated'.")
		matrix = np.round(matrix, numDigits)
	
	elif decisionMatrixType == 'lognormal':
		if method == 'truncated':
			matrix = []
			while len(matrix) < m * n:
				sample = np.random.lognormal(mean=0, sigma=0.5)
				if a <= sample <= b:
					matrix.append(sample)
			matrix = np.array(matrix[:m * n]).reshape((m, n))
		elif method == 'normalized':
			matrix = np.random.lognormal(mean=0, sigma=0.5, size=(m, n))
			matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))  # Normaliza para [0, 1]
			matrix = a + matrix * (b - a)  # Escala para [a, b]
		else:
			raise ValueError("Método inválido. Escolha 'normalized' ou 'truncated'.")
		matrix = np.round(matrix, numDigits)
	
	elif decisionMatrixType == 'triangular':
		matrix = np.random.triangular(left=a, mode=(a + b) / 2, right=b, size=(m, n))
		matrix = np.round(matrix, numDigits)
	
	elif decisionMatrixType == 'weibull':
		if method == 'truncated':
			matrix = []
			while len(matrix) < m * n:
				sample = np.random.weibull(a=1.5)
				if a <= sample <= b:
					matrix.append(sample)
			matrix = np.array(matrix[:m * n]).reshape((m, n))
		elif method == 'normalized':
			matrix = np.random.weibull(a=1.5, size=(m, n))
			matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))  # Normaliza para [0, 1]
			matrix = a + matrix * (b - a)  # Escala para [a, b]
		else:
			raise ValueError("Método inválido. Escolha 'normalized' ou 'truncated'.")
		matrix = np.round(matrix, numDigits)
	
	else:
		raise ValueError("Distribuição inválida. Escolha 'uniform', 'normal', 'exponential', 'beta', 'lognormal', 'triangular'  ou 'weibull'.")
	
	return matrix.tolist()

# Exemplo de teste
randomMatrix(m=5, n=3, a=0, b=1, decisionMatrixType='uniform', method='normalized', seed=None, numDigits=6)
