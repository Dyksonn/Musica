import pygame
print()
t = 'SPOTIFY'
print('\033[32m{:^30} \033[m'.format(t))
print('\033[32m=-\033[m' * 16)
music = str(input('Deseja ouvir uma música? [S/N] \n')).lower()
print('\033[32m=-\033[m' * 16)
if music in 'sim s':
    while True:
        try:
            gen = int(input('''Que música deseja ouvir:
(1) - sertanejo
(2) - funk
(3) - Country
Opção: '''))
            print('\033[32m=-\033[m' * 22)
        except ValueError:
            print()
            print('\033[31mDigite apenas o número que indica \033[m')
            print()
            continue
        if gen == 2:
            try:
                funk = int(input('''Música funk:
(1) - Mc genry - Parado no bailão
(2) - Mc livinho - Parem de transar
Opção: '''))
                print('\033[32m=-\033[m' * 22)
            except ValueError:
                print()
                print('\033[31mDigite apenas o número que indica \033[m')
                print()
                continue
            if funk == 1:
                pygame.mixer.init()
                pygame.mixer.music.load('/home/dykson/Música/parado.mp3')
                pygame.mixer.music.play()
                print('\033[34mMc genry - Parado no bailão \033[m')
                print('Aproveite a música funk escolhida para você')
                pass
            elif funk == 2:
                pygame.mixer.init()
                pygame.mixer.music.load('/home/dykson/Música/transar.mp3')
                pygame.mixer.music.play()
                print('\033[34mMc livinho - Parem de transar \033[m')
                print('Aproveite a música funk escolhida para você')
                pass
        elif gen == 1:
            try:
                sert = int(input('''Música sertanejo:
(1) - Breno e Caio Cesar - Londres
(2) - Zé Neto e Cristiano - Grão de Arroz
Opção: '''))
                print('\033[32m=-\033[m' * 25)
            except ValueError:
                print()
                print('\033[31mDigite apenas o número que indica \033[m')
                print()
                continue
            if sert == 1:
                pygame.mixer.init()
                pygame.mixer.music.load('/home/dykson/Música/londres.mp3')
                pygame.mixer.music.play()
                print('\033[34mBreno e Caio Cesar - Londres \033[m')
                print('Aproveite a música sertanejo escolhida para você')
                pass
            elif sert == 2:
                pygame.mixer.init()
                pygame.mixer.music.load('/home/dykson/Música/arroz.mp3')
                pygame.mixer.music.play()
                print('\033[34mZé Neto e Cristiano - Grão de Arroz \033[m')
                print('Aproveite a música sertanejo escolhida para você')
                pass
        elif gen == 3:
            try:
                colt = int(input('''Música Country:
(1) - Brett Young - In Case You Didn know
(2) - Lil Nas X - Old Town Road
Opção: '''))
                print('\033[32m=-\033[m' * 22)
            except ValueError:
                print()
                print('\033[31mDigite apenas o número que indica \033[m')
                print()
                continue
            if colt == 1:
                pygame.mixer.init()
                pygame.mixer.music.load('/home/dykson/Música/know.mp3')
                pygame.mixer.music.play()
                print('\033[34mBrett Young - In Case You Didn know \033[m')
                print('Aproveite a música country escolhida para você')
            elif colt == 2:
                pygame.mixer.init()
                pygame.mixer.music.load('/home/dykson/Música/old.mp3')
                pygame.mixer.music.play()
                print('\033[34mLil Nas X - Old Town Road \033[m')
                print('Aproveite a música country escolhida para você')
        print()
        input('\033[32mAperte a tecla ENTER para ouvir outra música. \033[m')
        choice = str(input('Deseja ouvir outra música? [sim/não] \n')).lower()
        print()
        if choice in 'sim s':
            continue
        else:
            print()
            print('\033[31mOK \033[m')
            print('\033[31mVolte qualquer hora, Quando quiser ouvir uma música. \033[m')
            break
elif music in 'nao não n':
    print('\033[31mVolte qualquer hora, Quando quiser ouvir uma música. \033[m')