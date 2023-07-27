# Webscraping1
Automação de Webscraping para Demandas Internas de uma empresa <br>
Este projeto foi desenvolvido para atender a uma demanda interna da empresa em que trabalho. Com essa aplicação, conseguimos economizar de 2 a 3 horas de trabalho de um dos nossos colaboradores. A automação coleta 3 informações do cliente e as consolida em um arquivo Excel, repetindo esse processo N vezes.

Funcionalidades:<br>
•	A aplicação abre o site da empresa e aguarda 40 segundos para permitir que o funcionário faça o login. <br>
•	Em seguida, realiza consultas no sistema com base em números obtidos de uma base de dados interna.<br>
•	A aplicação coleta 3 informações relacionadas a cada número consultado e as salva em uma linha de um arquivo Excel.<br>
•	Esse processo é repetido 100 vezes, conforme a quantidade estipulada.<br>

Estrutura do Código <br>
O código está organizado da seguinte forma: <br>
1.	Importação de bibliotecas e módulos no início do script.
2.	Definição de variáveis para gerar a data atual no formato necessário para a planilha resultante.
3.	Configuração para abrir o site da empresa.
4.	Implementação de uma função para a contagem regressiva.
5.	Leitura de um arquivo com os números a serem consultados e criação de uma lista.
6.	Utilização de laços de repetição para realizar o processo de automação em loop.
obs: Dentro do laço tem um try except que localiza linhas que não foram encontradas no sistema. 

Vídeo da aplicação funcionando: <br>
Youtube: https://youtu.be/qpeJCwrS6WA <br>
Linkedin: https://www.linkedin.com/posts/hendryl-roberto-44885a1b3_selenium-python-automaaexaetocomercial-activity-7084581640433188864-jELh?utm_source=share&utm_medium=member_desktop
