import matplotlib.pyplot as plt
import numpy as np

#This program finds peaks in the amount of playable notes. Peaks are where the ideal RPM's for the fan harp is.
#They can be calculated from one peak by multiplying the RPM by 1.05946 (The same as the multiple between )
#Still not sure how to calculate the first peak without brute forcing it

####USER INPUT####
amountOfNotes=80 ## Starting from A0, the amount of semitones up you want to include in the chart


# Create array with all notes
notes = [27.5] # Holds all unrounded note frequencies
names = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#'] # Base note names
notesnames = ['A0'] # Holds all note names
octave = 0
for i in range(1,amountOfNotes):
    notes.append(notes[-1]*1.05946) #Equal temperament
    if(names[i%12]=='C'):octave+=1 #12 / octave
    notesnames.append(names[i%12]+str(octave))

#Maths
#rpm = 1000
#rps = 1
compatibility = [[],[]]
red=[0.35,0.96,1]
green=[0.80,0.66,1]
blue=[0.98,0.72,1]
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
            plt.plot([rpm],[notes[i]],marker='.',color=(red[i%3],green[i%3],blue[i%3]))

#for ln in finalNotes: # Display end notes
#    print(ln)

#xpoints = range(0,40)
#ypoints = hzOffsets
plt.xlabel('RPM')
plt.ylabel('Hz')
#ax = plt.axes()
#ax.set_facecolor('black')
plt.plot(compatibility[0],compatibility[1],marker='*',color='pink')
plt.yscale(value='log')
plt.show()


'''
A lot of code in here is probably unnecessary. This was just to generate the graph to get some visual representation of what works best.
The spreadsheet contains a lot more information on how to tune, but this generates some necessary numbers for the spreadsheet.
'''