import matplotlib.pyplot as plt
import numpy as np

####USER INPUT####
amountOfNotes=80 ## Starting from A0, the amount of semitones up you want to include in the chart


# Create array with all notes
notes = [27.5] # Holds all unrounded note frequencies
names = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#'] # Base note names
notesnames = ['A0'] # Holds all note names
octave = 0
for i in range(1,amountOfNotes):
    notes.append(notes[-1]*1.05946)
    if(names[i%12]=='C'):octave+=1
    notesnames.append(names[i%12]+str(octave))

#Maths
#rpm = 1000
#rps = 1
compatibility = [[],[]]
for rpm in range(1,1500):
    rps = rpm/60
    compatibility[0].append(rpm)
    compatibility[1].append(1)
    #print(compatibility)
    holes = []
    for tone in notes: # Round number of holes
        holes.append(round(tone/rps,0))

    notesRound = []
    for hole in holes: # Round frequencies to hole numbers
        notesRound.append(hole*rps)

    #finalNotes = []
    hzOffsets = []
    allowedDissonance=0.5
    for i in range(0,len(notes)):
        hzOffset = round(abs(notes[i]-notesRound[i]),3) # Get the difference between the frequency that would be made and the frequency of the note
        hzOffsets.append(hzOffset)
        if(hzOffset<allowedDissonance):
            #finalNotes.append('Frequency: '+str(round(notes[i],2))+' | Note: '+notesnames[i]+' | Dissonance: '+str(hzOffset)+' | Holes: '+str(holes[i]))
            compatibility[1][rpm-1]+=1
            plt.plot([rpm],[notes[i]],marker='.')

#for ln in finalNotes: # Display end notes
#    print(ln)

#xpoints = range(0,40)
#ypoints = hzOffsets

plt.plot(compatibility[0],compatibility[1],marker='*')
plt.yscale(value='log')
plt.show()