class Pacote:  
    def __init__(self, id_pacote, prioridade, tempo_transmissao):  
        self.id = id_pacote  
        self.prioridade = prioridade  
        self.tempo_transmissao = tempo_transmissao  

    def __lt__(self, outro):  
        return self.prioridade < outro.prioridade

class HeapRoteador:  
    def __init__(self):  
        self.heap = []  
        self.indices = {}

    def inserir_pacote(self, pacote):  
        self.heap.append(pacote)  
        self.indices[pacote.id] = len(self.heap) - 1  
        self._subir(len(self.heap) - 1)  

    def remover_pacote_prioritario(self):  
        if not self.heap:  
            return None  
        pacote_removido = self.heap[0]  
        del self.indices[pacote_removido.id]  
        ultimo = self.heap.pop()  
        if self.heap:  
            self.heap[0] = ultimo  
            self.indices[ultimo.id] = 0  
            self._descer(0)  
        return pacote_removido  

    def atualizar_prioridade(self, id_pacote, nova_prioridade):  
        if id_pacote not in self.indices:  
            raise ValueError("Pacote não encontrado")  
        indice = self.indices[id_pacote]  
        pacote = self.heap[indice]  
        prioridade_antiga = pacote.prioridade  
        pacote.prioridade = nova_prioridade  
        if nova_prioridade < prioridade_antiga:  
            self._subir(indice)  
        else:  
            self._descer(indice)  

    def _subir(self, indice):  
        while indice > 0:  
            pai = (indice - 1) // 2  
            if self.heap[indice] < self.heap[pai]:  
                self._trocar(indice, pai)  
                indice = pai  
            else:  
                break  

    def _descer(self, indice):  
        tamanho = len(self.heap)  
        while True:  
            esquerda = 2 * indice + 1  
            direita = 2 * indice + 2  
            menor = indice  
            if esquerda < tamanho and self.heap[esquerda] < self.heap[menor]:  
                menor = esquerda  
            if direita < tamanho and self.heap[direita] < self.heap[menor]:  
                menor = direita  
            if menor != indice:  
                self._trocar(indice, menor)  
                indice = menor  
            else:  
                break  

    def _trocar(self, i, j):  
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]  
        self.indices[self.heap[i].id] = i  
        self.indices[self.heap[j].id] = j  

def main():  
    p1 = Pacote(1, 3, 2.5)  
    p2 = Pacote(2, 1, 1.0)  
    p3 = Pacote(3, 2, 0.5)  

    roteador = HeapRoteador()  
    roteador.inserir_pacote(p1)  
    roteador.inserir_pacote(p2)  
    roteador.inserir_pacote(p3)  

    roteador.atualizar_prioridade(1, 0)  

    print("Ordem de transmissão:")  
    while roteador.heap:  
        pacote = roteador.remover_pacote_prioritario()  
        print(f"Pacote {pacote.id} (Prioridade: {pacote.prioridade})")  

if __name__ == "__main__":  
    main()  