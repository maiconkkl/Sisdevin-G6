# Sisdevin G6 - Sistema de Declarações Vinícolas 
Esse repositorio foi criado com intuito de facilitar a comunicação com o Sisdevin – Sistema de Declarações Vinícolas e o 
sistemas G6 da digisat.

O que é o Sisdevin
-------------------
Tendo em vista as inúmeras vantagem como agilidade, segurança e rapidez, e propiciando
uma maior facilidade de integração Empresas/Fiscalização e uma maior e facilidade de envio de
dados para o Órgão Fiscalizador, desenvolveu-se o "sistemas de remessas" para o Sisdevin. Gerando o arquivo denominado "remessa" de acordo com as especificações adiante detalhadas, caberá à empresa destiná-lo ao Órgão Fiscalizador. O formato do arquivo de remessa utilizado
pelo sistema anteriormente utilizado (Sisdeclara) foi mantido para facilitar a migração entre os
sistemas. 

Como instalar
-----------------
* Ele foi desenvolvido para o python 3.8, não quer dizer que não funcione com futuras versões do python ou até mesmo que 
funcione com versões anteriores. Então esse fica sendo um dos primeiro requisitos.

* Depois de instalar o python fica sendo necessario criar um ambiente virtual para controle as bibliotecas utlizadas
dentro desse projeto. O mesmo pode ser criado usando o seguinte comando pelo CMD:


    python -m venv venv
    
> Lembrando que o python precisa esta nas variaveis ambientes do windows para que o comando acima seja reconhecido pelo CMD.

* Depois precisamos ativar o ambiente virtual que acabamos de criar usando o comando

    
    venv\Scripts\activate.bat
    
> É necessario que a pasta ativa do CMD seja a pasta que acabamos de criar o ambiente virtual, caso não seja use o 
> comando CD para se deslocar até a pasta correta


* Agora vamos instalar as bibliotecas utilizadas no projeto com o comando abaixo:


    pip install -r requeriments.txt
    
Quando todos os passos acima forem concluidos a instalação esta finalizada.
