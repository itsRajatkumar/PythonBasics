from pygame import mixer

mixer.init()
mixer.music.load("00 Jai Ganesh Deva.mp3")
mixer.music.set_volume(15)
mixer.music.play()

while(1):
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    choice1 = input("Enter your choice ")


    if choice1 == 'p':
        mixer.music.pause()

    elif choice1 == 'r':
        mixer.music.unpause()

    elif choice1 == 'e':
        mixer.music.stop()
        break  