

def abrir_arquivos(root):

    '''
    Modifica arquivos cad para UMA pasta (não foi generalizado
    visto a complexidade sem sentido, não custa ficar abrindo 
    poucos diretorios e aplicando)
    
    '''
    import os
    import time
    import click
    import keyboard as kb

    def star_arquivo(root,arquivo):
        '''
        root = é o diretorio mãe
        pasta = é o diretorio filho no qual está o arquivo/file
        arquivo = é um file dentro de um diretorio
        
        '''
        os.startfile(os.path.join(root,arquivo))
        print(f'arquivo {arquivo} foi aberto')
        time.sleep(0.5)
        mudar_layer()
        time.sleep(0.1)
        kb.send('ctrl+s')

    #dados
    #inicialização
    os.chdir(root)
    items = os.listdir()

    for arquivo in items:
        if os.path.isdir(arquivo):
            pass
        else:
            if '.dwg' in arquivo or '.DWG' in arquivo:
                star_arquivo(root,arquivo)
                    
def dell_bak(root):
    import os
    os.chdir(root)
    items = os.listdir()
    for arquivos in items:
        if os.path.isdir(arquivos):
            pass
        else:
            if '.bak' in arquivos:
                os.remove(os.path.join(root,arquivos))

def mudar_layer():
    from pyzwcad import ZwCAD
    acad = ZwCAD()
    layers_nums = acad.ActiveDocument.Layers.count 
    for i in range(layers_nums):
        temp = acad.ActiveDocument.Layers.item(i).Name
        if temp == '0':
            pass
        else:
            if "EME-" in temp:
                pass
            else:
                acad.ActiveDocument.Layers.item(i).Name = "EME-" + temp



root = r'L:\BIBLIOTECA\BLOCOS AUTO CAD'
#abrir_arquivos(root)
#dell_bak(root)

mudar_layer()


