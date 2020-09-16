# Instalação do repositório e dependências

Primeiramente baixe o repositorio

`git clone git@github.com:RandersonM/extensive_number_api.git`

Instale as dependências com

`pip install -r requirements.txt`

E execute o arquivo app.py para iniciar o server

## Consumindo o server

- Após iniciar o server com o host do `app.py`(foi setado o nome de localhost)

- Basta realizar um curl com o host e a porta(foi setada a porta 3000)

Exemplo

`curl localhost:3000/-5435`
 

E o retorno será o objeto

`{ "extenso": "menos cinco mil e quatrocentos e trinta e cinco" }
`

### OBS

- O programa só trabalha com numeros inteiros, numeros com virgulas não são arrendados em inteiros