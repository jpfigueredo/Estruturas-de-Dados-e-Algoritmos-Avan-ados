from MinHeap import MinHeap

class Tarefa:
    def __init__(self, descricao, prioridade):
        self.descricao = descricao
        self.prioridade = prioridade

    def __lt__(self, outro):
        return self.prioridade < outro.prioridade

    def __repr__(self):
        return f"Tarefa('{self.descricao}', {self.prioridade})"

class AgendadorTarefas:
    def __init__(self):
        self.min_heap = MinHeap()

    def adicionar_tarefa(self, descricao, prioridade):
        tarefa = Tarefa(descricao, prioridade)
        self.min_heap.insert(tarefa)

    def executar_proxima_tarefa(self):
        proxima_tarefa = self.min_heap.extract_min()
        if proxima_tarefa:
            print(f"Executando: {proxima_tarefa.descricao} (Prioridade: {proxima_tarefa.prioridade})")
        else:
            print("Nenhuma tarefa para executar.")

    def mostrar_tarefas(self):
        print("Tarefas na fila:")
        for tarefa in self.min_heap.heap:
            print(tarefa)

# Exemplo de uso
agendador = AgendadorTarefas()

# Adicionando tarefas
agendador.adicionar_tarefa("Enviar e-mail", 3)
agendador.adicionar_tarefa("Fazer backup", 1)
agendador.adicionar_tarefa("Atualizar servidor", 2)
agendador.adicionar_tarefa("Reunião com equipe", 4)

# Exibindo tarefas na fila
agendador.mostrar_tarefas()

# Executando tarefas em ordem de prioridade
agendador.executar_proxima_tarefa()
agendador.executar_proxima_tarefa()
agendador.executar_proxima_tarefa()
agendador.executar_proxima_tarefa()
agendador.executar_proxima_tarefa()  # Tentando executar sem tarefas