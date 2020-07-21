class No:
    def __init__(self,chave,dado):
        self.dado = dado
        self.chave = chave
        self.esq = None
        self.dir= None

class ArvoreBinaria:
    def __init__(self):
        self.__raiz = None
        self.__tam = 0

    def __len__(self):
        return self.__tam

    def __str__(self):
        preordem = []
        strElem = ''
        self.__preOrdem(self.__raiz, preordem)
        for elem in preordem:
            strElem += repr(elem.chave) + ':' + repr(elem.dado) +'->'
        strElem = strElem[:-2]
        return strElem

    def __preOrdem(self, no, listaPreOrdem):
        if no:
            listaPreOrdem.append(no)
            self.__preOrdem(no.esq,listaPreOrdem)
            self.__preOrdem(no.dir,listaPreOrdem)

    def inserir(self,chave,dado):
        if self.__raiz is None:
            self.__raiz = No(chave,dado)
            self.__tam += 1
        else:
            buscar = self.__buscarNo(chave)
                    
            if chave < buscar.chave :
                buscar.esq = No(chave,dado)
                self.__tam += 1

            elif chave > buscar.chave:
                buscar.dir = No(chave,dado)
                self.__tam += 1
            
            else:
                buscar.dado = dado

    def buscar(self, chave):
        buscar = self.__buscarNo(chave)
        if chave == buscar.chave :
            return buscar.dado
        else:
            raise KeyError


    def __buscarNo(self,chave):
            buscar = self.__raiz
            continua = True

            while continua:
                if buscar.chave < chave:
                    if buscar.dir is None:
                        continua = False
                    else: 
                        buscar = buscar.dir

                elif buscar.chave > chave:
                    if buscar.esq is None:
                        continua = False
                    else: 
                        buscar = buscar.esq
                else:
                    continua= False
            return buscar 

arvore = ArvoreBinaria()
arvore.inserir(15, 'quinze')
arvore.inserir(10, 'dez')
arvore.inserir(17, 'dezessete')
arvore.inserir(5, 'cinco')

print(arvore)