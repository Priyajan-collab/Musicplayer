from pygame import mixer
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
from tkinter import Tk
#screen
main_screen=Tk()
#title
main_screen.title("music player")

current_volume= float(0.5)
#play song
song_title="choose a song"
def play_song():
    filename=filedialog.askopenfilename(initialdir="C:/")
    song_to_play=filename
    song_title=filename.split("/")
    song_title=song_title[-1]
    print(song_title)
    
    try:
        mixer.init()
        mixer.music.load(song_to_play)
        mixer.music.set_volume(current_volume)
        mixer.music.play()

    except exception as e:
        print(e)
def pause():
    mixer.music.pause()
#labels
Label(main_screen, text="music player",font=("ariel",15),fg="red"   ).grid(sticky="N" ,row=0,padx=120 )


#buttons
Button(main_screen, text="play",font=("ariel",12),fg="green",command=play_song).grid(sticky="N" ,row=5)
Button(main_screen, text="next",font=("ariel",12),fg="green"   ).grid(sticky="E" ,row=5)
Button(main_screen, text="previous",font=("ariel",12),fg="green"   ).grid(sticky="W" ,row=5)
Button(main_screen, text="pause",font=("ariel",12),fg="green",command=pause ).grid(sticky="N" ,row=6)






main_screen.mainloop()