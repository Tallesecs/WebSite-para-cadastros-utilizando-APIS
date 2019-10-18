Desafio SNET - Talles Eduardo
=================
_Neste sistema os usuários irão se cadastrar e dentro de suas especificidades, poderão cadastrar clientes(criar, atualizar, apagar, listar e ler). Existe a opção de preenchimento automatico de endereço usando a api viaCEP, trocar o cep padrão(sem hifen) para um outro cep(sem hifen) e clicar enter. Após o cadastro, clicar em VER para ver as informações do usuário e o MAPS utilizando a api do googleMaps)

## [](#considera%C3%A7%C3%B5es-iniciais)Considerações Iniciais

Essas instruções serão necessárias para configuração e execução do projeto em sua maquina local. Antes de tudo, visualize o arquivo abaixo sobre como você realizará a configuração do projeto para execução oficial.

### [](#pr%C3%A9-requisitos)Pré-requisitos

_REQUERIMENTOS BÁSICOS PARA UMA APLICAÇÃO._

```python
- Python==3.7
- Django==2.2.5
- Pytz==2019.2
- Sqlparse==0.3.0
- certifi==2019.9.11
- chardet==3.0.4
- idna==2.8
- requests==2.22.0
- urllib3==1.25.6
- python-decouple-3.1
- dj-database-url-0.5.0
- dj-static-0.0.6
- static3-0.7.0





```

### [](#instalando)Instalando

É necessário ter instalado em sua máquina o Python 3.7 ou superior que é disponibilizado no site oficial do Python ([https://www.python.org/downloads/](https://www.python.org/downloads/)). Antes de finalizar confira em suas Variações de Ambiente do Windows e verifique que o Python encontra-se configurado em sua "path". Posteriormente, tem-se necessário criar e configurar a sua própria máquina virtual de desenvolvimento para que as ferramentas de projeto não se instalem em suas respectivas máquinas permanentemente.

```
	Criar a virtual enviroment:
		--> python -m venv (nomeDaEnviroment)
	Ativar a enviroment criada:
		--> (nomeDaEnviroment)/Scripts/activate
	Instalar o requirements.txt:
	    --> pip install -r requirements.txt
	Atualizar as migrações do banco de dados:
	    --> python manage.py makemigrations
	Construir o banco de dados da aplicação:
	    --> python manage.py migrate
```

Caso haja algum erro, instalar manualmente o django e o requests para rodar o servidor:

```

	pip install django
	pip install requests

```

Para rodar o servidor:

```

	python manage.py runserver

```

## [](#constru%C3%ADdo-com)Construído com

- [Bootstrap v4.3.1](https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css) - Design do sistema

## [](#constru%C3%ADdo-com)Considerações finais

- Não tive tempo hábil para linkar com postgres porém sei conectar o banco
- Fiz todos os passos para deploy no heroku, mas encontrei alguns erros no fim e não tive tempo de terminar, deixei essa versão sem configurações para o heroku
- Não consegui implementar a api do Facebook
- Todos os outros requisitos foram concluídos!
- Agradeço a todos!!

  

## [](#autores)Autores

-   **Talles Eduardo** - _Desenvolvedor Back-End_ - [@Tallesecs](https://github.com/Tallesecs)

