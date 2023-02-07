#Challenge taken from  www.101computing.net/guitar-chords-reader/
import time
import os

#A Python Dictionary matching chord names with "fret notation"
chords = {"C": "x32010", "A":"x02220", "G": "320033", "E": "022100", "D": "xx0232", "F": "x3321x", "Am": "x02210", "Dm": "xx0231", "Em": "022000"}

#A procedure to display where to position your fingers to play a given chord
def displayChord(chord):
  
  """
  Input: Chords in the dictionary
  
  Output: Fret notation
  """
  
  fretNotation = chords[chord]
  
  print("  " + chord) # Printing chord on top
  nut=""
  
  for string in fretNotation:
    #Checking if it is x
    if string=="x":
      nut=nut+"x"  # x means don't play this string
    else:
      nut = nut + "_"
  print(nut) #Guitar Nut, the line below chord name (i.e below Em)
  for fretNumber in range(1,5):
    fret=""
    
    #Looping to put the numbers frrom the directionary
    #In the right place
    for string in fretNotation:
      #If you have to play it, then it will appear as 0
      if string==str(fretNumber):
        fret=fret+"O"
        
      #else, just a line
      else:
        fret = fret + "|"
    print(fret)
    
    
    

#Main Program Starts Here
#song = "C,D,G,Em,C,D,G,Em"


#Let's read this song, one chord at a time
#songChords = song.split(",")
#for chord in songChords:
#  displayChord(chord)
#  time.sleep(2)
#  #Clear the screen
#  os.system("cls")
  
  
def AskPlayer():
  """
  
  Input1: Ask player to write the chords. It should be in str format
  i.e: C,D,G,Em,C,D,G,Em with a comma
  
  Input2 = Ask about song. Write the lyrics in the same order
  
  i.e:I, Love, You
  
  
  Input 2 needs to be the same length as input 1. So if there is 
  no song in that part, just let it empty
  
  I, Love, , You
  """
  
  
  #Asking for Music
  
  print("Write the chords in like the following format")
  print("\n")
  
  print("C,D,G,Em,C,D,G,Em")
  
  print("\n")

  print("Options: C, A, G, E, D, F, Am, Dm,Em")
  
  song= input("What Are the Chords?")

  Music = input("What is the lyrics for each chord? I.e: I, Love, You")
  
  songChords = song.split(",")
  Musica = Music.split(",") 

  #Printing the chords and lyrics
  for i in range(len(songChords)):
    #Calling chords
    displayChord(songChords[i])
    #Getting the lyric
    print(Musica[i])

    #Time between loops
    time.sleep(2)
    #Clear the screen
    os.system("cls")


#Calling  AskPlayer
AskPlayer()
  
  
  

