Documentação para rodar o porjeto Chat Bot:

1 - Clone o repositório para o seu PC.

2 - Abra o projeto em um editor de codigo e abra o terminal na pasta do projeto.

3 - rode o comando "pyhton -m venv venv". -> Esse comando permite criar um ambiente virtal para que possa baixar e instalar as bibliotecas usadas no projeto sem afetar outros projetos.

4 - rode o comando "venv\Scripts\activate" para ativar o venv criado acima.

5 - com o venv ativo, no mesmo terminal, rode o comando "pip install nltk", para instalar o NLTK.

6 - com o venv ativo, no mesmo terminal, rode o comando "python -m nltk.downloader all".

7 - Após a instalação do NLTK, rode o comando "pip install flask".

8 - Após completar estes passos, ainda no terminal dentro do venv, rode o comando python .\app.py
