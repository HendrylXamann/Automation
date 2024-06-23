import time
from tkinter import Tk, Label

class Interface:
    
    @staticmethod
    def contagem_regressiva(tempo_total:int, janela:str) -> None:
        """Realiza uma contagem regressiva em uma janela tkinter.
        Args:
            tempo_total (int): O tempo total em segundos da contagem regressiva.
            janela (Label): A janela tkinter onde a contagem será exibida.
        """
        for segundos_restantes in range(tempo_total, 0, -1):
            minutos = segundos_restantes // 60
            segundos = segundos_restantes % 60
            tempo_restante = f"{minutos:02d}:{segundos:02d}"
            janela['text'] = tempo_restante
            janela.update()
            time.sleep(1)
        janela['text'] = "THE TIME IS OVER"

    @classmethod
    def litle_window(self) -> None:
        """Cria uma pequena janela tkinter com uma contagem regressiva."""
        root = Tk()
        root.title("Contagem Regressiva")
        root.geometry("200x100")
        label_contagem = Label(root, text="", font=("Arial", 20)) 
        label_contagem.pack(pady=20) 
        self.contagem_regressiva(30, label_contagem)
        root.destroy()
