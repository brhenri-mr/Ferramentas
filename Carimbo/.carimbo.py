import os 
import shutil
import PySimpleGUI as sg

#programa que passa todas as versões que vc quer para outra pasta
#matricial =r"L:\OBRAS\Obras Andamento\1677_Brafer_Suzano Cerrado_Engenharia\Interno\Desenhos\03-ENFARDAMENTO\03 executivo" 
#destination = r"L:\OBRAS\Obras Andamento\1677_Brafer_Suzano Cerrado_Engenharia\Interno\Documentos\Verificações\executivo\00 enfardamento"

def login():
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Pasta do Arquivo'),sg.InputText()],
                [sg.Text('Pasta de Destino'), sg.InputText()],
                [sg.Text('Versão'), sg.InputText()],
                [sg.Button('Ok'), sg.Button('Cancel')] ]
    return sg.Window('login',layout, finalize = True)

#janela = login()
#window,event, values = sg.read_all_windows()
while True:
    janela = login()
    window,event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    elif janela == window and event =="Ok":
        try:
            matricial = values[0]
            destination = values[1]
            if len(values[2]) >= 2:
                if values[2][0] =="0":
                    versao = values[2][1]
                else:
                    versao = values[2]
            else:
                versao = values[2]
            os.chdir(matricial)

            documentos = os.listdir()

            for documento in documentos:
                #mudar de diretorio
                if os.path.isdir(documento):
                    os.chdir(documento)
                    local = os.getcwd()
                    for arquivo in os.listdir():
                        if (versao+".pdf") in arquivo or (versao+"A.pdf") in arquivo or (versao+").pdf") in arquivo:
                            try:
                                shutil.copyfile(src = os.path.join(local,arquivo), dst = os.path.join(destination,arquivo))
                                print(f"arquivo{arquivo} copiado com sucesso")
                                break
                            except:
                                print(f"tivemos erro no arquivo {arquivo}")
                    os.chdir(matricial)
        except:
            print("insira parametros")
            widown.close()




