#### (Colocar aqui todo o processo para o funcionamento do Script (instalação de pacotes, bibliotecas, configurações e afins))

# Script de automação no fluxo de trabalho da e-trap.

## Pré-Requisitos
(Colocar tudo o que necessita para o funcionamento do Script)

  - Instalação do Anaconda
  - Criação de ambiente virtual Anaconda com o Python 3.9
  - Incremento do SWAP e memória da GPU
  - Instalação do OpenCV


-------------------------------------------

- Python 3
- OpenCV 4.5.5
- Anaconda



## Instalando Dependências
(Colocar aqui todo o processo de instalação dos componentes necessários para o funcionamento do Script no Raspberry)

#### Python 3.9 ou superior
  Para realizar a instalação do Python no Raspberry, deve-se digitar no terminal:

<code> $ sudo apt-get install python3 </code> 

<code> $ sudo apt-get install python3-pip </code> 

#### Anaconda

Primeiramente deve fazer o download no site do Anaconda.
https://www.anaconda.com/products/distribution#download-section

Exemplo: “64-Bit (AWS Graviton2 / ARM64) Installer (534 MB)”

Feito isso, verifique se você tem permissão para executar o arquivo instalador, com o comando:

<code> chmod +x ~/Downloads/Anaconda3-xxxxx-Linux-armhf.sh </code>

Após concluir o download, abra o terminal e ache o arquivo baixado utilizando o comando: 

<code> cd ~/Downloads </code>

Execute o arquivo: 

<code> ./Anaconda3-xxxxx-Linux-armhf.sh </code>

substituindo os “x” pela versão que foi baixada;

Depois de concluir a instalação, feche e abra o terminal novamente para que as alterações tenham efeito.

Para iniciar o Anaconda Navigator, use o seguinte comando no terminal: 
<code> anaconda-navigator </code>




#### OpenCV
  



  
  
  



## Fluxo do Script
1. Pergunta ao usuário qual o ID da placa;
2. Chama a classe para fazer a captura da imagem (P - capturar | Q - sair);
3. Pergunta ao usuário qual o tipo de inseto (1 - Afídeo | 2 - Parasitóide);
4. Seta o nome correto para o arquivo (Data Atual + Id da Placa + Tipo do inseto + Id da Imagem(contador) + .jpg)
5. Chama a função para fazer o Crop 
6. Realiza o upload dos arquivos em pastas no GoogleDrive
  
# Funcionamento
  





