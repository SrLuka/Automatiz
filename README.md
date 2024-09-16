# Automação de Cliques para Instalação de Modpack de 365 Mods no Skyrim VR

Este programa foi criado para automatizar os cliques durante o processo de instalação de um modpack com 365 mods para **Skyrim VR**. 
Utilizando a biblioteca `pyautogui`, o script busca uma imagem específica na tela e clica automaticamente nela, 
facilitando a interação repetitiva necessária durante o processo de instalação pelo Nexus, a qual exige uma assinatura pelo serviço de automatização.

## Como Funciona

O script realiza as seguintes ações:

1. Busca por uma imagem especificada (`cpt.png`) na tela. Está imagem refere-se ao botão slow download presente em todos os 375 modes desse conjunto
2. Tenta localizar a imagem com uma confiança de 80% (`confidence=0.8`).
3. Se a imagem for encontrada, o programa clicará automaticamente no centro dela.
4. Repete o processo até o número máximo de tentativas, que é configurado no script.

## Requisitos

- **Python 3.x**
- Biblioteca `pyautogui`

Como Usar:
1-Certifique-se de ter o Python instalado em sua máquina.
2-Instale a biblioteca pyautogui utilizando o comando acima.
3-Capture uma imagem de referência que será usada para localizar o botão ou área de clique desejada (neste exemplo, a imagem cpt.png).
4-Salve a imagem no mesmo diretório do script Python.
5-Execute o script.

Personalização:
*Imagem de Referência: A imagem usada para o clique automático deve ser trocada conforme necessário. Atualmente, o script utiliza cpt.png.
*Número de Tentativas: O número máximo de tentativas para localizar a imagem está configurado como 365, mas pode ser ajustado no parâmetro tentativas.
*Tempo de Espera: O tempo de espera entre tentativas é configurado com o comando sleep(3) e sleep(5), e pode ser ajustado para mais ou menos tempo dependendo da sua necessidade.
