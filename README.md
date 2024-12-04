## Avaliação da UC03
### Curso de Programador de Sistemas
### SENAC Castanhal - João Gluck Paül

#### Intruções:

1- Clone o repositóroi para sua máquina executando o comando abaixo no terminal: 
```git
git clone https://github.com/TheParousia/SISTEMA-C.git
```

> Obs.: O repositório será salvo no diretório onde você executar o comando, recomenda-se salvar no Desktop, para isso, pressione o botão direioto do mouse na área de trabalho e clique na opção "abrir no terminal"

2- Feche o terminal abaerto anteriomente e abra a pasta baixada no Visual Studio Code

3- Inicie o terminal do Visual Studio Code e crie o ambiente virtual:

```powershell
python -m venv venv 
```

4- Em seguida, ative o ambiente virtual com o seguinte comando, o comando pode ser escrito de maneira ágil usando a tecla TAB, para isso escreva somente a inicial da pasta e pressione TAB:
```powershell
.\venv\Scripts\activate
```

5- Instale os pacote qu estçao listados no arquivo <i>requirements.txt</i> executando o comando abaixo:
```powershell
pip install -r requirements.txt
```

### Comando úteis para o desenvolvimento
Para cria um novo app dentro do projeto você deve executar o seguinte comando:
```powershell
python .\manage.py startapp <nome_do_app>
```

Onde o <nome_do_app> é o nome do app que será criado

Para executar o servidor e vizualiar como o projeto estar funcionando execute o seguinte comando:
```powershell
python .\manage.py runserver
```