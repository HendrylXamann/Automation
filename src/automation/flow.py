import pandas as pd
from views.interface import *
from config.settings import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

class Flow:
    def __init__(self, browser_url:str):
        self.data_atual, self.nome_arquivo_final, self.df = bd_excel('gerado', 'arquivoTal')
        self.drive = open_browser(browser_url)

    def run(self) -> None:
        janela_usuario = Interface()
        janela_usuario.litle_window()
        
        listafinal = []

        for index, row in self.df.iterrows():
            click_linha = WebDriverWait(self.drive, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="msisdn"]')))
            click_linha.send_keys(int(row["LINHA"]))
            click_consult = WebDriverWait(self.drive, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnSearch"]')))
            click_consult.click()
            
            try:
                elemnto_except = WebDriverWait(self.drive, 8).until(EC.presence_of_element_located((By.XPATH, '//*[@id="msg-info"]/p')))
                print("Linha não localizada")
                volta_consult = WebDriverWait(self.drive, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/center/table/tbody/tr[2]/td/div/ul/li[1]/a')))
                volta_consult.click() 
                time.sleep(1)
                continue

            except NoSuchElementException: 
                pass
                situa = WebDriverWait(self.drive, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frmConsulta"]/div/table/tbody/tr[1]/td[5]'))).text
                datasituacao = WebDriverWait(self.drive, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frmConsulta"]/div/table/tbody/tr[1]/td[6]'))).text
                tipo_product = WebDriverWait(self.drive, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frmConsulta"]/div/table/tbody/tr[1]/td[4]'))).text
                
                volta_consult = WebDriverWait(self.drive, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/center/table/tbody/tr[2]/td/div/ul/li[1]/a')))
                volta_consult.click()  
                time.sleep(2)

                resultadoss = {'Linha': row['LINHA'], 'Situacao': situa, 'Datasitua': datasituacao, 'TipoProduto': tipo_product}
                listafinal.append(resultadoss)
                df_listafinal = pd.DataFrame(listafinal, columns=['Linha', 'Situacao', 'Datasitua', 'TipoProduto'])
                df_listafinal.to_excel(self.nome_arquivo_final, index=False)

        print("Portanto alegra-te, Ó Iniciado, pois quanto maior a tua prova, maior o teu Triunfo.")
