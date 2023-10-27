import matplotlib.pyplot as plt

# Defina o número de processos que deseja (substitua N pelo número desejado)
N = 16

# Crie uma lista de processos com tempos de execução diferentes
processos = [("P1", 8), ("P2", 4), ("P3", 2), ("P4", 6)]

# Adicione mais processos de forma dinâmica, se necessário
for i in range(4, N):
    processos.append(("P" + str(i + 1), i + 3))

# Defina uma lista de valores de quantum para teste
quantum_valores = [0.5 + i * 0.1 for i in range(N*2)]


resultados = {"Tempo Médio de Espera": [], "Tempo Médio de Retorno": [], "Vazão": [], "Tempo de Conclusão": {}}

for quantum in quantum_valores:
    tempo_total = 0
    espera_total = 0
    retorno_total = 0
    vazao = 0
    fila = []
    tempo_atual = 0
    tempo_conclusao = {}  # Para rastrear o tempo de conclusão de cada processo


    # Inicialize uma lista para rastrear o tempo restante de cada processo
    tempo_restante = [burst_time for _, burst_time in processos]

    while any(tempo_restante):
        for i in range(N):
            processo, burst_time = processos[i]
            if tempo_restante[i] > 0:
                # O processo ainda não foi concluído
                if tempo_restante[i] <= quantum:
                    # O processo será concluído neste quantum
                    tempo_total += tempo_atual + tempo_restante[i]
                    espera_total += tempo_total - tempo_atual - burst_time
                    retorno_total += tempo_total - tempo_atual
                    tempo_atual += tempo_restante[i]  # Atualiza o tempo atual                
                    vazao += 1
                    tempo_conclusao[processo] = tempo_total
                    tempo_restante[i] = 0
                else:
                    # O processo ainda tem tempo restante
                    tempo_total += tempo_atual + quantum
                    tempo_restante[i] -= quantum
                    tempo_atual += quantum  # Atualiza o tempo atual
                fila.append(i)
               # tempo_atual += 1  # Adiciona 1 unidade de tempo para a mudança de contexto
            else:
                # O processo já foi concluído
                fila.append(-1)  # Marca um slot vazio na fila

    resultados["Tempo Médio de Espera"].append(espera_total / N)
    resultados["Tempo Médio de Retorno"].append(retorno_total / N)
    resultados["Vazão"].append(vazao)
    resultados["Tempo de Conclusão"] = tempo_conclusao    
    

# Imprime o tempo de conclusão de cada processo
print("Tempo de Conclusão de cada Processo:")
for processo, tempo in resultados["Tempo de Conclusão"].items():
    print(f"{processo}: {tempo:.2f}")

print(f"{'Quantum':<10}{'Tempo Médio de Espera':<25}{'Tempo Médio de Retorno':<25}{'Vazão':<10}")
for i in range(len(quantum_valores)):
    print(f"{quantum_valores[i]:<10.2f}{resultados['Tempo Médio de Espera'][i]:<25.2f}{resultados['Tempo Médio de Retorno'][i]:<25.2f}{resultados['Vazão'][i]:<10}")        
   
# Crie gráficos separados para as métricas
plt.figure(figsize=(10, 5))
plt.plot(quantum_valores, resultados["Tempo Médio de Espera"], marker='o')
plt.xlabel('Quantum')
plt.ylabel('Tempo Médio de Espera')
plt.title('Tempo Médio de Espera vs. Quantum')

plt.figure(figsize=(10, 5))
plt.plot(quantum_valores, resultados["Tempo Médio de Retorno"], marker='o')
plt.xlabel('Quantum')
plt.ylabel('Tempo Médio de Retorno')
plt.title('Tempo Médio de Retorno vs. Quantum')

# Gráfico para o tempo de conclusão de cada processo
plt.figure(figsize=(10, 5))
plt.xlabel('Processo')
plt.ylabel('Tempo')
plt.bar(resultados["Tempo de Conclusão"].keys(), resultados["Tempo de Conclusão"].values())
plt.title('Tempo de Conclusão de cada Processo')


plt.tight_layout()
plt.show()
