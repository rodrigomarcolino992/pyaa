from tkinter import *
from tkinter import messagebox
import qrcode
import psycopg2

class Banco():
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="QRCode",
            user="postgres",
            password="pabd"
        )

        self.cursor = self.conn.cursor()
    
    def insertOne(self, id, url, path):
        self.cursor.execute("INSERT INTO tbcodes (id_code, url, qrcode_path) VALUES ({},'{}','{}')".format(id, url, path))
        self.conn.commit()

#172.31.200.1
#10.89.1.29

def gerar_qr_code():
    url = texto_resposta.get()

    if (len(url) == 0):
        messagebox.showinfo(
            title="Erro!",
            message="Inserir URL válida pls"
        )
    else:
        opcao = messagebox.askokcancel(
            title=url,
            message=f"O Endereço é: \n"
                f"Endereço: {url} \n"
                f"Salvar?"
        )

        if opcao:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            img_name = 'qrExport.png'
            img.save(img_name)
            banco.insertOne(2, url, 'qrCode,png')
            


banco = Banco()

janela = Tk()
janela.title ('Gerador de Codigo QRCode')

id = Label(janela, text = 'ID:')
id.grid(column=0, row=2, padx=10, pady=10)

id_resposta = Entry(width=45)
id_resposta.grid(column=1, row=2, columnspan=2)


texto = Label(janela, text = 'URL:')
texto.grid(column=0, row=2, padx=10, pady=10)

texto_resposta = Entry(width=45)
texto_resposta.grid(column=1, row=2, columnspan=2)

botao = Button(janela, text='Gerar QRCode', command=gerar_qr_code)
botao.grid(column=1, row=3, padx=10, pady=10)



janela.mainloop()