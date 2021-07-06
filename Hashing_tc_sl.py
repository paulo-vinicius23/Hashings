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
        print(posi)
        while True:
            if self.est[posi] == 1:
                self.tab[posi] = num
                self.est[posi] = 0
                return
            posi += 1
            if posi == self.larg:
                posi = 0
    def busca(self, num):
        for i in range(self.larg):
            prc = ((num % self.larg) + i) % self.larg
            if num == self.tab[prc]:
                print(f'numero: {num}\nposicao: {prc}\nlocomocao: {i}')
                return
        print('numero nao encontrado')
        return
    def remocao(self, num):
        for i in range(self.larg):
            prc = ((num % self.larg) + i) % self.larg
            if num == self.tab[prc]:
                self.tab[prc] = None
                self.est[prc] = 1
                return
        print('numero nao encontrado')
        return
    def mostrar(self):
        print('--------------------')
        print('| numero | posicao |')
        print('--------------------')
        for i in range(self.larg):
            print(f'| {self.tab[i]} | {i} |')
            print('--------------------')
        return

a = hash(7)
x = input().split()
for i in x:
    a.inserir(int(i))
print(a.tab)
print(a.est)
a.mostrar()