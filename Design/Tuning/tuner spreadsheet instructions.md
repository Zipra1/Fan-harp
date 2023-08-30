
# Before you even use the spreadsheet,
You *probably* don't need to use this spreadsheet.
The ideal number of holes in a fan harp are:
2, 3, 4, 5, 6, 8, 9, 10, 12

The spreadsheet is mostly useful for:
- If you want more notes on the disk
- Changing tightness of tuning

# Column descriptions
Note HZ: Just a list of all notes in Hz

#Holes : The number of holes for a given RPM that will give the exact note frequency

Note name: Name of the note

Round #H: Rounds #Holes, because you can't have a fractional amount of holes.

Round Hz: The rounded number of holes converted back into a frequency, this is the note that will actually play when playing the fan harp.

Hz difference: This is the difference between the real note frequency and what will be played. The lower this number, the more in tune the note is. Aim for the lowest.

Column G: If this note is within acceptable dissonance, it will display a 1. This means this note will work.

% Working notes: Useless information, this was here to help me recognize a pattern.

RPS: Rotations per second

Dissonance: Allowable dissonance per note (Row 2 is a variable)

Peak RPMs: Written here from `tuner.py`, it is roughly where the most available notes are.
`Peak RPms can be calculated from roughly the number 826. If you know the significance of this number, PLEASE LET ME KNOW!`

1st diff: Useless information, this was here to help me recognize a pattern.

Peak RPMs F: From the number 826, multiply the previous number by 1.05946. x1.05946 is the same increase between each notes frequency.

Peak # Holes: The ideal number of holes, written down.

# Variables
While you probably don't need to change anything since Peak # Holes is all you really need to know, you can change:

RPM: You can change this to see what notes will be playable at what RPM. Useful if you're trying to make variable speeds on your fan harp.

Dissonance (only Row 2): The allowable dissonance for A0, increases as it goes up since changes in frequency are less noticable the higher the frequency.
I would reccomend keeping this at 0.2Hz, but you *could* change it if you wanted to. The higher this is, the less accurate the tuning will be.

