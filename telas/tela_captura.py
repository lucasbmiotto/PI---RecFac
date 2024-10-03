from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, messagebox
from tkinter import filedialog  # Para abrir o explorador de arquivos
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\vicre\Documents\GitHub\PI-RecFac\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# IMPORTANTE! TUDO ESTÁ NESSA FUNÇÃO, PARA QUE A TELA LOGIN POSSA CHAMAR ESSA TELA
def abrir_tela_captura():
    window = Tk()
    window.geometry("1195x797")
    window.configure(bg="#FFFFFF")
    window.title("SAD-RF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=797,
        width=1195,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1195.0,
        129.0,
        fill="#272727",
        outline=""
    )

    # Imagem da logo na parte de cima da tela
    image_logo_captura = PhotoImage(file=relative_to_assets("logo_captura.png"))
    canvas.create_image(
        86.0,
        72.0,
        image=image_logo_captura
    )

    # Quadrado preto da parte de baixo
    canvas.create_rectangle(
        0.0,
        743.0,
        1195.0,
        797.0,
        fill="#272727",
        outline=""
    )

    canvas.create_text(
        432.0,
        761.0,
        anchor="nw",
        text="© 2024 - Todos os direitos reservados a SAD-RF",
        fill="#FFFFFF",
        font=("Inter Bold", 14 * -1)
    )

    # Função para exportar os dados para CSV
    def exportar_dados_csv():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Salvar arquivo como",
            initialfile="dados_reconhecimento.csv"  # Nome sugerido para o arquivo
        )

        if file_path:
            dados_reconhecimento_facial = {
                'ID': [1, 2, 3],
                'Nome': ['Pessoa 1', 'Pessoa 2', 'Pessoa 3'],
                'Data_Hora': ['2024-10-01 14:23:00', '2024-10-01 15:05:00', '2024-10-01 15:12:00'],
                'Confiança': [98.5, 97.3, 99.1]
            }

            exportar_para_csv(dados_reconhecimento_facial, file_path)

            messagebox.showinfo(
                "Exportação Bem-sucedida",
                f"O arquivo foi exportado com sucesso para: {file_path}"
            )

            abrir_agora = messagebox.askyesno(
                "Abrir Arquivo",
                "Deseja abrir o arquivo no Excel agora?"
            )

            if abrir_agora:
                os.startfile(file_path)

    # Função para exportar os dados para o Power BI
    def exportar_dados_para_powerbi():
        # Abre o explorador de arquivos para o usuário escolher o local e o nome do arquivo
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Salvar arquivo como",
            initialfile="dados_powerbi.csv"  # Nome sugerido para o arquivo Power BI
        )

        if file_path:
            # Aqui você pode usar os dados de reconhecimento facial
            dados_reconhecimento_facial = {
                'ID': [1, 2, 3],
                'Nome': ['Pessoa 1', 'Pessoa 2', 'Pessoa 3'],
                'Data_Hora': ['2024-10-01 14:23:00', '2024-10-01 15:05:00', '2024-10-01 15:12:00'],
                'Confiança': [98.5, 97.3, 99.1]
            }

            # Exporta para o arquivo CSV
            exportar_para_csv(dados_reconhecimento_facial, file_path)

            # Mensagem de confirmação
            messagebox.showinfo(
                "Exportação para Power BI",
                f"O arquivo foi exportado com sucesso para: {file_path}"
            )

            # Pergunta se o usuário deseja abrir o Power BI
            abrir_powerbi = messagebox.askyesno(
                "Abrir no Power BI",
                "Deseja abrir o Power BI agora e importar o arquivo?"
            )

            # Não é possível abrir diretamente o Power BI, mas pode abrir o arquivo CSV
            if abrir_powerbi:
                # O usuário terá que abrir o Power BI manualmente e importar o arquivo CSV
                os.startfile(file_path)

    # Botão para exportar para CSV
    button_botao_csv = PhotoImage(file=relative_to_assets("botao_csv.png"))
    button_1 = Button(
        image=button_botao_csv,
        borderwidth=0,
        highlightthickness=0,
        command=exportar_dados_csv,
        relief="flat"
    )
    button_1.place(
        x=152.0,
        y=262.0,
        width=298.0,
        height=49.0
    )

    # Botão para exportar para Power BI
    button_botao_pb = PhotoImage(file=relative_to_assets("botao_pb.png"))
    button_2 = Button(
        image=button_botao_pb,
        borderwidth=0,
        highlightthickness=0,
        command=exportar_dados_para_powerbi,  # Chama a função de exportação para Power BI
        relief="flat"
    )
    button_2.place(
        x=746.0,
        y=262.0,
        width=298.0,
        height=49.0
    )

    # Botão de Captura de dados (mantido sem mudanças)
    button_botao_captura = PhotoImage(file=relative_to_assets("botao_captura.png"))
    button_3 = Button(
        image=button_botao_captura,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=450.0,
        y=461.0,
        width=296.0,
        height=85.0
    )

    window.resizable(False, False)
    window.mainloop()
