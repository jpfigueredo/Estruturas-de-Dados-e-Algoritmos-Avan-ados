class TrieNode:  
    def __init__(self):  
        self.children = {}  
        self.is_end_of_word = False  

class Trie:  
    def __init__(self):  
        self.root = TrieNode()  

    def insert(self, palavra):  
        no_atual = self.root  
        for caractere in palavra:  
            if caractere not in no_atual.children:  
                no_atual.children[caractere] = TrieNode()  
            no_atual = no_atual.children[caractere]  
        no_atual.is_end_of_word = True  
        return True  

    def search(self, palavra):  
        no_atual = self.root  
        for caractere in palavra:  
            if caractere not in no_atual.children:  
                return False  
            no_atual = no_atual.children[caractere]  
        return no_atual.is_end_of_word  

    def autocomplete(self, prefixo):  
        sugestoes = []  
        no_atual = self.root  
        for caractere in prefixo:  
            if caractere not in no_atual.children:  
                return sugestoes  
            no_atual = no_atual.children[caractere]  
        self._dfs(no_atual, prefixo, sugestoes)  
        return sugestoes  

    def _dfs(self, no, prefixo_atual, sugestoes):  
        if no.is_end_of_word:  
            sugestoes.append(prefixo_atual)  
        for caractere, filho in no.children.items():  
            self._dfs(filho, prefixo_atual + caractere, sugestoes)  

    def autocorrect(self, palavra, distancia_max=1):  
        variacoes = self._gerar_variacoes(palavra)  
        sugestoes = []  
        for variacao in variacoes:  
            if self.search(variacao):  
                sugestoes.append(variacao)  
        return sugestoes  

    def _gerar_variacoes(self, palavra):  
        letras = 'abcdefghijklmnopqrstuvwxyz'  
        variacoes = set()  
        for i in range(len(palavra) + 1):  
            # Inserção  
            for letra in letras:  
                variacoes.add(palavra[:i] + letra + palavra[i:])  
            if i < len(palavra):  
                variacoes.add(palavra[:i] + palavra[i+1:])  
                for letra in letras:  
                    variacoes.add(palavra[:i] + letra + palavra[i+1:])  
        for i in range(len(palavra) - 1):  
            chars = list(palavra)  
            chars[i], chars[i+1] = chars[i+1], chars[i]  
            variacoes.add(''.join(chars))  
        return variacoes  

def main():  
    trie = Trie()  
    livros = ["harrypotter", "hobbit", "heroi", "harry", "habito"]  
    for livro in livros:  
        trie.insert(livro)  

    prefixo = "har"  
    print(f"Sugestões para '{prefixo}': {trie.autocomplete(prefixo)}")

    entrada_errada = "harrt"  
    print(f"Correção para '{entrada_errada}': {trie.autocorrect(entrada_errada)}")

if __name__ == "__main__":  
    main()  
