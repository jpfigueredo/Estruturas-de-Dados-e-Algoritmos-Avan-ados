class Processo:  
    def __init__(self, id, tempo_execucao, prioridade):  
        self.id = id  
        self.prioridade = prioridade  
        self.tempo_execucao = tempo_execucao  

    def __lt__(self, outro):  
        return self.prioridade < outro.prioridade  

class EscalonadorHeap:  
    def __init__(self):  
        self.heap = []  
        self.indices = {}  

    def adicionar_processo(self, processo):  
        self.heap.append(processo)  
        self.indices[processo.id] = len(self.heap) - 1  
        self._subir(len(self.heap) - 1)  

    def executar_proximo(self):  
        if not self.heap:  
            return None  
        processo_executado = self.heap[0]  
        del self.indices[processo_executado.id]  
        ultimo = self.heap.pop()  
        if self.heap:  
            self.heap[0] = ultimo  
            self.indices[ultimo.id] = 0  
            self._descer(0)  
        return processo_executado  

    def modificar_prioridade(self, id_processo, nova_prioridade):  
        if id_processo not in self.indices:  
            raise ValueError("Processo não encontrado")  
        indice = self.indices[id_processo]  
        processo = self.heap[indice]  
        prioridade_antiga = processo.prioridade  
        processo.prioridade = nova_prioridade  
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
    p1 = Processo(1, 5, 3)  
    p2 = Processo(2, 3, 1)  
    p3 = Processo(3, 2, 2)  

    escalonador = EscalonadorHeap()  
    escalonador.adicionar_processo(p1)  
    escalonador.adicionar_processo(p2)  
    escalonador.adicionar_processo(p3)  

    escalonador.modificar_prioridade(3, 0)  

    print("Ordem de execução:")  
    while len(escalonador.heap) > 0:  
        processo = escalonador.executar_proximo()  
        print(f"Processo {processo.id} (Prioridade: {processo.prioridade})")  

if __name__ == "__main__":  
    main()
