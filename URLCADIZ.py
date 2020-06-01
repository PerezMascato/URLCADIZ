#/usr/bin/python3
#Created by @perez_mascato
import os
import time
import pyshorteners
from time import sleep

os.system('clear')

def Main():
    print("\033[93m--------------------------------------------")
    print("                 URLCADIZ                   ")
    print("   Hide custom URL for social engineering   ")
    print("                           @perez_mascato   ")
    print("--------------------------------------------")
    print("\n[*1]  Google")
    print("[*2]  Youtube")
    print("[*3]  Spotify")
    print("[*4]  Instagram")
    print("[*5]  Facebook")
    print("[*6]  New York Times")
    print("[*7]  Personalized")
    print("\n[*99]  Exit")
    Selector()


def Selector():
    select = int(input("\nSelect a option: "))
    if select == 1:
        EnlaceGoogle()
    elif select == 2:
        EnlaceYoutube()
    elif select == 3:
        EnlaceSpotify()
    elif select == 4:
        EnlaceInstagram()
    elif select == 5:
        EnlaceFacebook()
    elif select == 6:
        EnlaceNewyorkTimes()
    elif select == 7:
        EnlacePersonalized()
    elif select == 99:
        os.system('clear')
        print("Goodbye...")
        sleep(1)
        os.system('clear')
        exit()
    else:
        os.system('clear')
        print("Not valid option...")
        sleep(1)
        os.system('clear')
        Main()


def EnlaceGoogle():
    os.system('clear')
    print("You have selected Google.")
    OriginalLink = str(input("\nOriginal URL: "))
    
    print("\nInput something that: new-user-in-twitter-this-is-a-perez-mascato-i-love")
    Postlink = str(input("\nPost LINK: "))
    os.system('clear')
    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    print(f"\nYour link is: https://www.google.com-{Postlink}@{Withouthttp}")
    Other()

def EnlaceYoutube():
    os.system('clear')
    print("You have selected Youtube.")
    OriginalLink = str(input("\nOriginal URL: "))
    
    print("\nInput something that: new-video-in-youtube-this-is-a-perez-mascato-i-love")
    Postlink = str(input("\nPost LINK: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\nYour link is: https://www.youtube.com-video-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceSpotify():
    os.system('clear')
    print("You have selected Spotify.")
    OriginalLink = str(input("\nOriginal URL: "))
    
    print("\nInput something that: new-song-in-spotify-this-is-a-perez-mascato-i-love")
    Postlink = str(input("\nPost LINK: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\nYour link is: https://www.spotify.com-video-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceInstagram():
    os.system('clear')
    print("You have selected Instagram.")
    OriginalLink = str(input("\nOriginal URL: "))
    
    print("\nInput something that: new-photo-in-instagram-this-is-a-perez-mascato-i-love")
    Postlink = str(input("\nPost LINK: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\nYour link is: https://www.instagram.com-photo-{Postlink}@{Withouthttp}")
    
    Other()

def EnlaceFacebook():
    os.system('clear')
    print("You have selected Facebook.")
    OriginalLink = str(input("\nOriginal URL: "))
    
    print("\nInput something that: new-post-in-facebook-this-is-a-perez-mascato-i-love")
    Postlink = str(input("\nPost LINK: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    
    print(f"\nYour link is: https://www.facebook.com-profile-{Postlink}@{Withouthttp}")
    os.system('clear')
    Other()

def EnlaceNewyorkTimes():
    os.system('clear')
    print("You have selected New York Times.")
    OriginalLink = str(input("\nOriginal URL: "))
    
    print("\nInput something that: new-post-in-new-york-times-this-is-a-perez-mascato-i-love")
    Postlink = str(input("\nPost LINK: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\033[95m\nYour link is: https://www.newyorktimes.com-{Postlink}@{Withouthttp}")
    
    Other()

def EnlacePersonalized():
    os.system('clear')
    print("You have selected Personalized.")
    Domain = str(input("Example.com/es... input domain: "))
    OriginalLink = str(input("\nOriginal URL: "))
    
    print("\nInput something that: new-post-in-new-york-times-this-is-a-perez-mascato-i-love")
    Postlink = str(input("\nPost LINK: "))

    Shortener = pyshorteners.Shortener()
    EndLink = Shortener.tinyurl.short(OriginalLink)
    Withouthttp = EndLink[7:]
    os.system('clear')
    print(f"\nYour link is: https://www.{Domain}-{Postlink}@{Withouthttp}")
    
    Other()

def Other():
    print("\033[93m\nDo you want to create another link?")
    print("Yes [*1] \nNo  [*2]")
    select=int(input("\nSelect a option: "))
    if select == 1:
        os.system('clear')
        Main()
    else:
        os.system('clear')
        exit()

#SYSCALL

Main()