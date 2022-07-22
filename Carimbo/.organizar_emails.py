from distutils import dist
import os
import shutil

def generalizador_pastas(func):
    def pasta_para_analise(*args, **kwargs):
        geral = []
        os.chdir(args[1])
        diretorios = os.listdir()
        for dirs in diretorios:
            local = os.path.join(args[1],dirs)
            os.chdir(local)
            arquivos = os.listdir()
            geral.append(func(nomes=arquivos, dir=local, dst=args[2]))
        return geral
    return pasta_para_analise


def generalizador_arquivos(func):
    def local_arquivo(*args,**kwargs):
        os.chdir(args[1])
        diretorios = os.listdir()
        for i in range(len(diretorios)):
            local = os.path.join(args[1],diretorios[i])
            arquivos = args[0][i]
            func(arquivos,dir_atual = local, dir_novo = args[2])
    return local_arquivo

@generalizador_pastas
def criar_pastas(nomes: list(str()), dir: str(), dst: str()):
    def nomes_arquivo(nomes_msg: list(str())) -> list():

        """
        Recebe uma lista de string poluido com os nomes de cada email 
        e retorna o nome da thread

        dir = diretorio q contem todos os arquivos

        dst = arquivo de destinação, para onde os arquivos irão ir

        """
        #dados
        temp = []
        #processamento dos nomes
        for nome in nomes_msg:
            aux = nome.split(' ')
            for i in ['RES','RE','Re','LIDA','Lida']:
                try:
                    while(True): #tenta remover RES e RE até dar erro
                        aux.remove(i)
                except:
                    pass
            temp.append([' '.join(aux[1:])[:-4].strip(),nome]) # o -4 é para não colocar o .msg no nome da pasta
        return temp
    
    def pastas(nomes_geral: list(), local_base: str()):
        """
        Recebe uma lista de nomes de pastas e um diretorio e criar 
        os diretorio com o nome das pastas
        """
        
        #recorte do array principal somente nos nomes de pastas
        nomes_pastas =[]
        for elemento in nomes_geral:
            nomes_pastas.append(elemento[0])
        #criação das pastas
        for nome in list(set(nomes_pastas)):
            local = os.path.join(local_base,nome)
            if os.path.exists(local_base):
                try:
                    os.makedirs(local)
                    #colocação das pastas enviar,receber e lida
                    for pastas_gerais in ['enviados','lidas','recebidos']:
                        os.makedirs(os.path.join(local,pastas_gerais))
                    
                    print(f'\033[92m diretorio {nome} criado com sucesso \033[92m')
                except:
                    print(f'\033[93m diretorio {nome} já existente \033[93m')
            else:
                print(f'\033[91m diretorio {nome} falhou \033[91m')

    nomes_pastas = nomes_arquivo(nomes)
    pastas(nomes_pastas,dst)

    return nomes_pastas

@generalizador_arquivos
def mover_arquivos(nomes_geral: list(str()), dir_atual: str(),dir_novo: str()):

    #dados 

    erro = 0
    sucesso = 0

    #--------------------------------

    fi = dir_atual.split('\\')[-1]

    #--------------------------------


    print('--------------------------------------------------------------------------')
    for elemento in nomes_geral:
        local = os.path.join(dir_novo,elemento[0])
        if os.path.exists(local):
            try:
                shutil.copyfile(src=os.path.join(dir_atual,elemento[1]), dst=os.path.join(local,fi,elemento[1]))
                print(f'\033[92m sucesso ao mover arquivo {elemento[1]} \033[92m')
                sucesso += 1
            except:
                print(f'\033[91m falha ao mover arquivo{elemento[1]} \033[91m')
                erro += 1
        else:
            print('diretorio invalido ou não existente')
            erro += 1
    print(f'a taxa de sucesso foi de {sucesso/(sucesso+erro)}')
    print(f'a taxa de erro foi de {erro/(sucesso+erro)}')

        
    
    


# local dos arquivos

diretorio = r'L:\ENVIAR\Breno\suzano'
os.chdir(diretorio)
arquivos = os.listdir()
dst = r'L:\ENVIAR\Breno\Suzano Organizado'

nomes_pastas = criar_pastas(arquivos,diretorio,dst)
mover_arquivos(nomes_pastas,diretorio,dst)











