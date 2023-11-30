# Importando os módulos necessários
import random
import matplotlib.pyplot as plt

# Definindo a função para o algoritmo de substituição de páginas FIFO
def fifo(page_references, num_frames):
    frames = []  # Inicializando a lista de frames
    page_faults = 0  # Inicializando a contagem de page faults
    # Iterando sobre cada referência de página
    for reference in page_references:
        # Se a referência não estiver nos frames, temos um page fault
        if reference not in frames:
            # Se ainda houver espaço nos frames, adicionamos a referência
            if len(frames) < num_frames:
                frames.append(reference)
            else:
                # Se não houver espaço, removemos o frame mais antigo (FIFO) e adicionamos a nova referência
                frames.pop(0)
                frames.append(reference)
            # Incrementamos a contagem de page faults
            page_faults += 1
    # Retornamos o total de page faults
    return page_faults

# Definindo a função para o algoritmo de substituição de páginas Aging
def aging(page_references, num_frames):
    frames = [0] * num_frames  # Inicializando a lista de frames
    page_faults = 0  # Inicializando a contagem de page faults
    # Iterando sobre cada referência de página
    for reference in page_references:
        # Se a referência não estiver nos frames, temos um page fault
        if reference not in frames:
            # Se houver um frame vazio, substituímos ele pela referência
            if 0 in frames:
                empty_index = frames.index(0)
                frames[empty_index] = reference
            else:
                # Se não houver frame vazio, substituímos o frame com a menor idade
                min_age_index = frames.index(min(frames))
                frames[min_age_index] = reference
            # Incrementamos a contagem de page faults
            page_faults += 1
        # Para cada frame, atualizamos a idade
        for i in range(num_frames):
            frames[i] >>= 1  # Deslocamos a idade para a direita (dividimos por 2)
            # Se a referência atual for igual ao frame, setamos o bit mais significativo da idade para 1
            if reference == frames[i]:
                frames[i] |= 0x80000000
    # Retornamos o total de page faults
    return page_faults

# Função para gerar uma lista de referências de página aleatórias
def generate_page_references(num_references, num_pages):
    # Retornamos uma lista de números aleatórios entre 1 e num_pages
    return [random.randint(1, num_pages) for _ in range(num_references)]

# Função principal que executa o programa
def main():
    num_references = 1000  # Número de referências de página
    num_pages = 50  # Número de páginas
    frame_range = range(1, 11)  # Intervalo de frames para testar

    fifo_faults = []  # Lista para armazenar o número de page faults do algoritmo FIFO
    aging_faults = []  # Lista para armazenar o número de page faults do algoritmo Aging

    # Para cada número de frames no intervalo
    for num_frames in frame_range:
        # Geramos uma lista de referências de página
        page_references = generate_page_references(num_references, num_pages)
        # Executamos o algoritmo FIFO e adicionamos o número de page faults à lista correspondente
        fifo_faults.append(fifo(page_references, num_frames))
        # Executamos o algoritmo Aging e adicionamos o número de page faults à lista correspondente
        aging_faults.append(aging(page_references, num_frames))

    # Plotamos o número de page faults para o algoritmo FIFO
    plt.plot(frame_range, fifo_faults, label='FIFO')
    # Plotamos o número de page faults para o algoritmo Aging
    plt.plot(frame_range, aging_faults, label='Aging')
    # Definimos o rótulo do eixo x
    plt.xlabel('Número de Molduras de Página')
    # Definimos o rótulo do eixo y
    plt.ylabel('Faltas de Página por 1000 Referências')
    # Adicionamos uma legenda ao gráfico
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
