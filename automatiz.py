# Este programa visa automatizar clickes em um processo de instalação de um modpack com 365 mods para Skyrim Vr!
from time import sleep
import pyautogui

# Número de tentativas
tentativas = 365

# Loop para buscar a imagem
for i in range(tentativas):
    sleep(3)  # Aguardar 5 segundos entre as tentativas
    
    # Entender os resultados!
    try:
        # Localizar todas as ocorrências da imagem na tela
        img = pyautogui.locateOnScreen('cpt.png', confidence=0.8)

        if img:
            # Clicar na imagem localizada
            pyautogui.click(img.left + img.width / 2, img.top + img.height / 2)
            print(f'Imagem encontrada e clicada na tentativa {i + 1}')
        else:
            print('Imagem não encontrada')

        sleep(5)  # Esperar 5 segundos antes de tentar novamente

    except Exception as e:
        print(f'Erro ao tentar localizar ou clicar na imagem: {e}')
