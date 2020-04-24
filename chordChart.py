notes = ['Db', 'D ', 'Eb', 'E ', 'F ', 'Gb', 'G ', 'Ab', 'A ', 'Bb', 'B ', 'C ']
intervals = [' 1', 'b2', ' 2', 'b3', ' 3', ' 4', 'b5', ' 5', 'b6', ' 6', 'b7', ' 7']

ukulele = ['G ', 'C ', 'E ', 'A ']
mandolin = ['G ', 'D ', 'A ', 'E ']
violin = mandolin
piano = notes+notes+notes+notes+notes+notes+notes+notes
guitar = ['E ', 'A ', 'D ', 'G ', 'B ', 'E ']
openG = ['D ', 'G ', 'D ', 'G ', 'B ', 'D ']
bass = ['E ', 'A ', 'D ', 'G ']
doubleBass = bass+bass
default = guitar

major = [0,4,7]
minor = [0,3,7]
dominantSeven = [0,4,7,10]
minorSeven = [0,3,7,10]
majorSeven = [0,4,7,11]
minorMajorSeven = [0,3,7,11]
dominantSevenSharpNine = [0,3,4,7,10]
hendrix = dominantSevenSharpNine
majorSix = [0,4,7,9]
minorSevenFlatFive = [0,3,6,10]
minorSix = [0,3,7,9]
susTwo = [0,2,7]
susFour = [0,5,7]

def createChart(chord, tuning = default):
    string = [intervals[i] if i in chord else '--' for i in range(12)]
    print('    ', end=' ')
    for n in notes[::-1]:
        print(n, end=' ')
    print()
    for n in tuning[::-1]:
        print(n, end=' ')
        for i in range(12):
            print(string[(i+notes.index(n)+1)%12], end='|')
        for i in range(12):
            print(string[(i+notes.index(n)+1)%12], end='|')
        print()

if __name__ == "__main__":
    print('Major:')
    createChart(major)
