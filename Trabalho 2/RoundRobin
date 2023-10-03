import matplotlib.pyplot as plt

processos = [("P1", 8), ("P2", 4), ("P3", 2), ("P4", 6)]

quantum_valores = [1, 2, 4]

resultados = {}

for quantum in quantum_valores:
    tempo_total = 0
    espera_total = 0
    retorno_total = 0
    vazao = 0
    fila = []
    tempo_atual = 0

    while processos:
        processo, burst_time = processos.pop(0)
        fila.append((processo, burst_time))

    while fila:
        processo, burst_time = fila.pop(0)
        if burst_time <= quantum:
            tempo_total += burst_time
            espera_total += tempo_total - burst_time
            retorno_total += tempo_total
        else:
            tempo_total += quantum
            burst_time -= quantum
            fila.append((processo, burst_time))

        vazao += 1

    resultados[quantum] = {
        "Tempo Médio de Espera": espera_total / len(quantum_valores), 
        "Tempo Médio de Retorno": retorno_total / len(quantum_valores),  
        "Vazão": vazao
    }

for quantum, metricas in resultados.items():
    print(f"Quantum {quantum}:")
    print(f"Tempo Médio de Espera: {metricas['Tempo Médio de Espera']:.2f}")
    print(f"Tempo Médio de Retorno: {metricas['Tempo Médio de Retorno']:.2f}")
    print(f"Vazão: {metricas['Vazão']}\n")


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(resultados.keys(), [metricas['Tempo Médio de Espera'] for metricas in resultados.values()])
plt.xlabel('Quantum')
plt.ylabel('Tempo Médio de Espera')
plt.title('Tempo Médio de Espera vs. Quantum')

plt.subplot(1, 2, 2)
plt.bar(resultados.keys(), [metricas['Tempo Médio de Retorno'] for metricas in resultados.values()])
plt.xlabel('Quantum')
plt.ylabel('Tempo Médio de Retorno')
plt.title('Tempo Médio de Retorno vs. Quantum')

plt.tight_layout()
plt.show()
