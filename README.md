# Chord-Chart
A chart for finding chords on the guitar or other string instruments. 

Here is an example of the chart for major chords on the guitar:
```
     C  B  Bb A  Ab G  Gb F  E  Eb D  Db 
E   3|--|--| 5|--|--|--|--| 1|--|--|--| 3|--|--| 5|--|--|--|--| 1|--|--|--|
B  --| 1|--|--|--| 3|--|--| 5|--|--|--|--| 1|--|--|--| 3|--|--| 5|--|--|--|
G   5|--|--|--|--| 1|--|--|--| 3|--|--| 5|--|--|--|--| 1|--|--|--| 3|--|--|
D  --|--| 3|--|--| 5|--|--|--|--| 1|--|--|--| 3|--|--| 5|--|--|--|--| 1|--|
A  --|--|--| 1|--|--|--| 3|--|--| 5|--|--|--|--| 1|--|--|--| 3|--|--| 5|--|
E   3|--|--| 5|--|--|--|--| 1|--|--|--| 3|--|--| 5|--|--|--|--| 1|--|--|--|
```
Say you want to find a G major chord. First you find G in the top row. The vertical line below G represents the nut, each vertical line to the right represents a fret, and each line to the left can be ignored. Then each 1 represents where to put your finger to play the root of the chord, each 3 represents the major third, and each 5 represents the perfect fifth. In this case each 1 is a G, each 3 is a B, and each 5 is a D. This makes it quick to find all the possible ways to play a G major on the guitar, and you can see what inversions are possible. See if you can find some familiar chord shapes in this chart.

The `createChart` function will automatically generate such a chart for any chord as described as a list of intervals in semitones, e.g. a major seventh chord is `[0, 4, 7, 11]`. You can also specify a different tuning, so this generalizes easily to any string instrument. Several chords and tunings are preprogrammed in.

I invented this when I was learning guitar and it helped me a lot. It helped in the early stages when I was learning basic chords, and was still helpful in the later stages when I was learning jazz. Hopefully this can help you understand your instrument better too.
