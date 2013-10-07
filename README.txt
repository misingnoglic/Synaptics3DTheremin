Our group (RPIDeis) used the Synaptics Forcepad to create a theremin type instrument. With one finger it detects the x, y, and z coordinates. The x coordinate determines the note value, the y coordinate controls the volume, and the z coordinate changes the octave.

The notes that can be played are mapped to the major pentatonic scale to make improvisation over chords easier.

The Synaptics Forcepad API only worked in C++, so we had to figure out a way to transmit the files to Python, which used the music libraries.

If we had extra time, the notes will be read into an arduino through the use of an array. The single color LEDs would show what note is being played, and the multicolor LED would show the octave.

In addition, the note being played and the octave will be displayed on screen through Visual Python, a 3D graphics module for Python, though it is mostly buggy due to the quick responses of the Forcepad.

