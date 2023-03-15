#### (Colocar aqui todo o processo para o funcionamento do Script (instalação de pacotes, bibliotecas, configurações e afins))

# Script de automação no fluxo de trabalho da e-trap.

## Pré-Requisitos
(Colocar tudo o que necessita para o funcionamento do Script)

  - Instalação do Anaconda
  - Criação de ambiente virtual Conda com o Python 3.9
  - Incremento do SWAP e memória da GPU
  - Instalação do OpenCV


-------------------------------------------

- Python 3
- OpenCV 4.5.5
- MambaForge



## Instalando Dependências
(Colocar aqui todo o processo de instalação dos componentes necessários para o funcionamento do Script no Raspberry)

### Python 3.9 ou superior
  Para realizar a instalação do Python no Raspberry, deve-se digitar no terminal:

<code> $ sudo apt-get install python3 </code> 

<code> $ sudo apt-get install python3-pip </code> 

---

### MambaForge

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


---

### OpenCV
  
#### Checagem da versão do Sistema Operacional
Antes da instalação do OpenCV no Raspberry pi 4, há alguns passos a serem seguidos. Primeiramente, deve-se checar a versão do Raspberry, inserindo o seguinte
comando no terminal:

<code> $ uname -a </code>

Após fazer isso, deve-se verificar a versão do compilador de C++, por meio do comando:

<code> $ gcc -v </code>

Em ambas as verificações deve ser encontrado o "aarch64-linux-gnu version". Caso isso não ocorra, e o usuário possua um sistema operacional de 64 bits, deve-se 
reinstalar todo o SO, em sua versão mais recente.

#### Checagem da memória swap
Em seguida, deve ser checado o tamanho da memória swap, também conhecida como virtual ou ainda área de troca. Essa deve ser grande o suficiente para suportar o que
for necessitado.

#### Checagem da EEPROM (memória volátil para armazenamento de pequenas quantidades de dados)
A última checagem necessária para a configuração do Raspberry pi 4 é da versão do software da EEPROM. Nesse caso, isso não tem relação com o OpenCV, mas com a
dissipação do calor. Para esse ganho de performance e dissipação correta do calor, portanto, necessita-se verificar o estado da EEPROM, se necessita ser
atualizada, ou não:

<code> $ sudo rpi-eeprom-update </code>

Nesse caso, o terminal exibirá se está na versão mais recente, ou não. Caso apareça a mensagem "BOOTLOADER: up-to-date", está correta a versão. Contudo, se 
aparecer "BOOTLOADER: update required", necessita de atualização, a qual pode ser executada por meio do comando:

<code> $ sudo rpi-eeprom-update-a </code>

<code> $ sudo reboot </code>

#### Memória GPU (Unidade de Processamento Gráfico)
Como o chip de memória RAM é utilizado tanto pela CPU quando pela GPU, deve-se checar e modificar a quantidade da memória GPU para pelo menos 128 MB.
Para acessar e modificá-la, vá no canto superior esquerdo da tela, na "raspberry", selecione "Preferences", e então Raspberry Pi Configuration. Por fim,
vá na seção de "Performance" e modifique a memória GPU para no mínimo 128 MB. 

#### Script de Instalação
Dando fim às checagens necessárias, o script da instalação é simples. Primeiramente, cheque a memória disponível: são necessários no mínimo um total de 6.5 GB.

<code> $ free -m </code>

Para verificar a quantidade de memória disponível, basta somar a memória total com a memória swap. O resultado deve ser de no mínimo 6.5 GB. Se a memória for 
menor do que a necessária, deve-se expandi-la: 

// Verificar como expandir a memória !!!

<code> $ wget https://github.com/Qengineering/Install-OpenCV-Raspberry-Pi-64-bits/raw/main/OpenCV-4-5-5.sh </code>

<code> $ sudo chmod 755 ./OpenCV-4-5-5.sh </code>

<code> $ ./OpenCV-4-5-5.sh </code>

#### Finalização e limpeza
Após a instalação completa do OpenCV, pode ser necessária a limpeza do dphys-swap. Ela deve ser feita por meio do terminal do Raspberry Pi 4 da seguinte maneira:

<code> $ sudo dphys-swapfile swapoff </code>

<code> $ sudo dphys-swapfile uninstall </code>

Para verificar se tudo ocorreu como o esperado, digite o seguinte comando no terminal:

<code> $ free -h </code>

Verifique se na linha "Swap" indica 0B, pois isso indica que o arquivo de troca foi removido com sucesso.
Assim sendo, após ter seguido os passos supracitados corretamente, o OpenCV terá sido instalado com sucesso em seu Raspberry Pi 4.


  
  
  

---

## Fluxo do Script
1. Pergunta ao usuário qual o ID da placa;
2. Chama a classe para fazer a captura da imagem (P - capturar | Q - sair);
3. Pergunta ao usuário qual o tipo de inseto (1 - Afídeo | 2 - Parasitóide);
4. Seta o nome correto para o arquivo (Data Atual + Id da Placa + Tipo do inseto + Id da Imagem(contador) + .jpg)
5. Chama a função para fazer o Crop 
6. Realiza o upload dos arquivos em pastas no GoogleDrive
  
  
---
# Funcionamento
  
Após a instalação do mamba forge: 
irá aparecer no terminal [base] pi@raspberrypi: "......"
Criar ambiente virtual com a versão necessária do python para a utilização da câmera


<code>conda create --name venv_script_etrap_python3.10 python=3.10</code>
<code>conda activate venv_script_etrap_python3.10</code>
<code>pip install picamera</code>





