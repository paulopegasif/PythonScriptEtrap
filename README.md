#### (Colocar aqui todo o processo para o funcionamento do Script (instalação de pacotes, bibliotecas, configurações e afins))

# Script de automação no fluxo de trabalho da e-trap.

## Pré-Requisitos
(Colocar tudo o que necessita para o funcionamento do Script)

## Instalando Dependências

(Colocar aqui todo o processo de instalação dos componentes necessários para o funcionamento do Script no Raspberry) 




## Fluxo do Script
1. Pergunta ao usuário qual o ID da placa;
2. Chama a classe para fazer a captura da imagem (P - capturar | Q - sair);
3. Pergunta ao usuário qual o tipo de inseto (1 - Afídeo | 2 - Parasitóide);
4. Seta o nome correto para o arquivo (Data Atual + _ + Id da Placa + _ + Tipo do inseto + _ + Id da Imagem(contador) + .jpg)
5. Chama a função para fazer o Crop 
6. Realiza o upload dos arquivos em pastas no GoogleDrive
