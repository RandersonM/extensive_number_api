# Instalação do repositório e dependências via Docker

Primeiramente baixe o repositório

`git clone git@github.com:RandersonM/extensive_number_api.git`

Suponho que você já tenha o docker instalado em sua máquina, e após
baixar o repositório, usando a linha de comando navegue até o projeto clonado
e vamos então buildar a imagem do nosso docker:

`docker image build -t <your_tag_name> .`

Após buildar a imagem docker em sua máquina verá uma mensagem parecida com essa
`Successfully tagged <your_tag_name>:latest`

Agora vamos rodar o docker com a imagem que buildamos
`docker run -p <port>:3000 -d <your_tag_name>`

Lembrando que no app.py está setado a porta 3000, então quando formos rodar o docker apontamos para a porta que desejamos e a que foi exposta pelo docker e setada no aplicativo(3000).

Feito isso basta abrir o navegador e digitar `http://0.0.0.0/<port>/` para ver o docker rodando a aplicação.

# Instalação do repositório e dependências via python

Primeiramente baixe o repositório

`git clone git@github.com:RandersonM/extensive_number_api.git`

Instale as dependências com

`pip install -r requirements.txt`

Execute o arquivo app.py para iniciar o server

## Consumindo o server

- Após iniciar o server com o host do `app.py`(0.0.0.0)

- Basta realizar um curl com o host e a porta(3000)

Exemplo

`curl 0.0.0.0:3000/-5435`

E o retorno será o objeto

`{ "extenso": "menos cinco mil e quatrocentos e trinta e cinco" }`

### OBS

- O programa só trabalha com números inteiros, números com vírgulas não são arrendados em inteiros