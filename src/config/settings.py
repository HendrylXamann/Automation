import datetime
import pandas as pd
from typing import Tuple
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def open_browser(url:str) -> webdriver:
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.execute_cdp_cmd("Network.setUserAgentOverride", {
        "userAgent": user_agent})
    browser.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    browser.get(url)

    return browser

def bd_excel(file_result:str, file_xlsx:str) -> Tuple[str, str, pd.DataFrame]:
    data_atual = datetime.datetime.now().strftime("%Y%m%d") 
    nome_arquivo_final = f"{file_result}.xlsx" 
    nome_do_arquivo = file_xlsx
    df = pd.read_excel(nome_do_arquivo)
    return data_atual, nome_arquivo_final, df
