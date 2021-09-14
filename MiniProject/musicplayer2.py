from pygame import mixer

mixer.init()

while(1):
    print("1. KGF_Monster")
    print("2. Nagin_Dance")
    print("3. Gang_Lekar_Aane_Wale_Hote_Hai_Gangster")
    print("4. Bade_ache_lagte_ho")
    print("5. Dheere_Dheere-Se_Meri_Zindagi")
    print("\nPress The Song Number You Want To Play")
    print("\nPress 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")

    choice1 = input("Enter your choice ")

    if choice1 == 'p':
        mixer.music.pause()

    elif choice1 == 'r':
        mixer.music.unpause()

    elif choice1 == '1':
        mixer.music.load("D:\RAJAT\pythonTraining\MiniProject\KGF_Monster.mp3")
        mixer.music.set_volume(15)
        mixer.music.play()

    elif choice1 == '2':
        mixer.music.load("D:\\RAJAT\\pythonTraining\\MiniProject\\Nagin_Dance.mp3")
        mixer.music.set_volume(15)
        mixer.music.play()

    elif choice1 == '3':
        mixer.music.load("D:\RAJAT\pythonTraining\MiniProject\Gang_Lekar_Aane_Wale_Hote_Hai_Gangster.mp3")
        mixer.music.set_volume(15)
        mixer.music.play()

    elif choice1 == '4':
        mixer.music.load("D:\RAJAT\pythonTraining\MiniProject\Bade_ache_lagte_ho.mp3")
        mixer.music.set_volume(15)
        mixer.music.play()

    elif choice1 == '5':
        mixer.music.load("D:\RAJAT\pythonTraining\MiniProject\Dheere_Dheere-Se_Meri_Zindagi.mp3")
        mixer.music.set_volume(15)
        mixer.music.play() 

    elif choice1 == 'e':
        mixer.music.stop()
        break