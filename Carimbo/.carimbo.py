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
                [sg.Button('Ok'), sg.Button('Cancel')] ]
    return sg.Window('login',layout, finalize = True)

janela = login()
window,event, values = sg.read_all_windows()
while True:
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    elif janela == window and event =="Ok":
        matricial = values[0]
        destination = values[1]
        break

os.chdir(matricial)

documentos = os.listdir()

for documento in documentos:
    #mudar de diretorio
    if '.dwg' not in documento and '.bak' not in documento and '.pdf' not in documento:
        os.chdir(documento)
        local = os.getcwd()
        for arquivo in os.listdir():
            if "0.pdf" in arquivo :
                try:
                    shutil.copyfile(src = os.path.join(local,arquivo), dst = os.path.join(destination,arquivo))
                    print(f"arquivo{arquivo} copiado com sucesso")
                    break
                except:
                    print(f"tivemos erro no arquivo {arquivo}")
        os.chdir(matricial)












