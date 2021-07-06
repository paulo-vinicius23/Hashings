class node:
    def __init__(self,dado):
        self.dado = dado
        self.proximo = None
class encade:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    def printLista(self): 
        temp = self.cabeca 
        while (temp): 
            print (temp.dado, "", end = '') 
            temp = temp.proximo
        print("")
    def add_final(self,dado):   
        no  = node(dado)
        if self.cabeca is None:
            self.cabeca = no
            self.tamanho+=1
            return   
        temp = self.cabeca
        while temp.proximo:
            temp = temp.proximo
        self.tamanho+=1
        temp.proximo = no
    def remover_de_elemento(self,dado):
        if self.cabeca is None:
            print("A lista nao tem elementos para deletar")
            return
        if self.cabeca.proximo is None:
            if self.cabeca.dado == dado:
                self.cabeca = None
            else:
                print("Item nao encontrado")
            return
        if self.cabeca.dado == dado:
            self.cabeca = self.cabeca.proximo
            self.cabeca.anterior = None
            self.tamanho-=1
            return
        n = self.cabeca
        while n.proximo is not  None:
            if n.dado == dado:
                break
            n = n.proximo
        if n.proximo is not None:
            n.anterior.proximo = n.proximo
            n.proximo.anterior = n.anterior
            self.tamanho -=1
        else:
            if n.dado == dado:
                n.anterior.proximo = None
                self.tamanho-=1
            else:
                print("Elemento nao encontrado")    
class tabela_hash:
    def __init__(self,tam):
        self.tam = tam
        self.casas = [None] * self.tam
        self.aux = [0] * self.tam
    def inserir(self,chave):
        if self.estado_tabela == True:
            print("Tabela cheia")
            return
        calc_hash = chave % self.tam
        if self.casas[calc_hash] == None:
            self.casas[calc_hash] = chave
        else:
            print("Ocorreu uma colisao \n Usando encadeamento separado")
            if self.aux[calc_hash] == 0: 
                aux = self.casas[calc_hash]
                self.casas[calc_hash] = encade()
                self.casas[calc_hash].add_final(aux)
                self.casas[calc_hash].add_final(chave)
                self.aux[calc_hash]=1
            elif self.aux[calc_hash] == 1:
                self.casas[calc_hash].add_final(chave)

    def estado_tabela(self):
        if None not in self.casas:
            return True
        return False

a = tabela_hash(7)
x = input().split()
for i in x:
    a.inserir(int(i))
print(a.casas)