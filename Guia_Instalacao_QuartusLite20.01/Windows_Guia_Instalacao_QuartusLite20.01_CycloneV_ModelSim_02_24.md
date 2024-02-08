Windows 10/11
==========

Por: Marco Antonio Soares de Mello Alves (Laboratório de Arquitetura de
Computadores)

Dúvidas:

> **Email: marcoasma@insper.edu.br**

> **Teams: marco.alves@al.insper.edu.br**

Quartus 20.1 e ModelSim 20.1
============================

Instalando
----------

1.  Faça o download dos arquivos a seguir (salve na mesma pasta, todos
    os arquivos):
    
    **IMPORTANTE !!** : Faça o download dos 3 arquivos, todos em uma única pasta antes de instalar. 

-   Quartus Lite 20.01:
    https://download.altera.com/akdlm/software/acdsinst/20.1std/711/ib_installers/QuartusLiteSetup-20.1.0.711-windows.exe

-   ModelSim:
    https://download.altera.com/akdlm/software/acdsinst/20.1std/711/ib_installers/ModelSimSetup-20.1.0.711-windows.exe

-   Cyclone V (Chip usado no curso) :
    https://download.altera.com/akdlm/software/acdsinst/20.1std/711/ib_installers/cyclonev-20.1.0.711.qdz


2.  Execute o arquivo **QuartusLiteSetup-20.1.0.711-windows.exe** e
    clique **Next** até a instalação iniciar:

<p align="center">
  <img src="imgs/installQuartus.png">
</p>


3.  Após a instalação, finalize-a com as seguintes opções:

<p align="center">
  <img src="imgs/finish.png">
</p>


4.  A instalação do USB Blaster deverá iniciar em seguida:

<p align="center">
  <img src="imgs/UBSblaster.png">
</p>

**OBS:** Mesmo se der erro, siga para o passo de Atualização do driver USB Blaster


Atualizando o USB Blaster
-------------------------

Mesmo instalando o driver é necessário atualiza-lo.

1.  Faça o download da pasta que contém o driver:

    https://drive.google.com/drive/folders/1Fwxb5FHSR3s5fs2rNVUVys8bli5j52PV?usp=sharing


2.  Pressione Windows + R no teclado e insira o comando **devmgmt.msc**:

<p align="center">
  <img src="imgs/devmgmt.png">
</p>


3.  O gerenciador de dispositivo deverá abrir:

<p align="center">
  <img src="imgs/gerenciadorDISP.png">
</p>


4.  Conecte a placa e o driver USB-Blaster será reconhecido da seguinte
    maneira:

<p align="center">
  <img src="imgs/blasterNreconhecido.png">
</p>


5.  O símbolo de atenção em amarelo indica que o driver está
    desatualizado, selecione a opção **Atualizar driver** clicando com o
    botão direito do mouse em cima do USB-Blaster, a janela a baixo
    deverá abrir:

<p align="center">
  <img src="imgs/atualizarBlaster.png">
</p>


6.  Selecione a opção **Procurar software de driver no computador** e
    defina o caminho da pasta do driver que foi baixado no passo **1.** (**Exemplo:** "C:\Users\ArqComp\Downloads\driver_USB-Blater_DE0-CV"),
    selecione incluir subpastas e clique em avançar:

<p align="center">
  <img src="imgs/incluirSub.png">
</p>


7.  Aguarde a instalação do drive e o USB-Blaster agora deverá aparecer
    como **Altera USB-Blaster**, conforme a imagem abaixo:

<p align="center">
  <img src="imgs/AlteraUSB.png">
</p>


Validando
=========

1.  Execute o Quartus (**Quartus (Quartus Prime 20.1) Lite Edition**),
    esse ícone deverá estar na sua área de trabalho:

<p align="center">
  <img src="imgs/IconeQuartus.png">
</p>


2.  Selecione a segunda opção **Run the Quartus Prime Software**

<p align="center">
  <img src="imgs/Run.png">
</p>

3.  Por fim, o programa deverá abrir:

<p align="center">
  <img src="imgs/quartusAberto.png">
</p>
