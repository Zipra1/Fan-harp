
# Create array with all notes
notes = [27.5]
names = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
notesnames = ['A0']
for i in range(1,40):
    notes.append(notes[-1]*1.05946)
    notesnames.append(names[i%12])

#print(notes)

#Maths
rps = 4

holes = []
for tone in notes: # Round number of holes
    holes.append(round(tone/rps,0))

notesRound = []
for hole in holes: # Round frequencies to hole numbers
    notesRound.append(hole*rps)

hzOffset = []
for i in range(0,len(notes)):
    hzOffset.append(round(abs(notes[i]-notesRound[i]),3))

print(hzOffset)