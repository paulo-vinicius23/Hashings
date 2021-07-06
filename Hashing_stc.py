class hash:
    def __init__(self, larg):
        self.larg = larg
        self.tab = [None]*larg
        self.est = [1]*larg
    def inserir(self, num):
        if None not in self.tab:
            print('Hash Cheio!')
            return
        posi = num % self.larg
        if self.est[posi] == 1:
                self.tab[posi] = num
                self.est[posi] = 0
        return
    def busca(self, num):
        prc = num % self.larg
        if num == self.tab[prc]:
            print(f'numero: {num}\nposicao: {prc}')
            return
        print('numero nao encontrado')
        return
    def remocao(self, num):
        prc = num % self.larg
        if num == self.tab[prc]:
            self.tab[prc] = None
            self.est[prc] = 1
            return
        print('numero nao encontrado')
        return