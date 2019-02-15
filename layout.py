# this goes to my one and only ...

import os
import platform as pf
from time import sleep
from merry import letters
from termcolor import colored
try:
	import pafy
except ImportError:
	os.system( "pip install youtube-dl" )
	os.system( "pip install pafy" )
try:
	import vlc
except ImportError:
	system( "pip install python-vlc" )
import sys

layout = """\
           000              000
        001111100        001111100
       0011222221100  0011222221100
       0011223332211001122333221100
       0011223343322112233433221100
        00112233443322334433221100
         001122334454454433221100
          0011223344554433221100
            001122334433221100
              00112233221100
                0011221100
                  001100
                    00\
"""

def clear():
	if pf.system() == "Linux":
		return os.system( "clear" )
	else:
		return os.system( "cls" )

song = sys.argv[1]
if "youtube" in song:
	p = pafy.new( song )
	song = p.m4astreams[0].url
player = vlc.MediaPlayer( song )
bpm = 60.00 / int( sys.argv[2] )
colors = [ "red", "green", "blue", "yellow", "white" ]

tword = sys.argv[3:]
loutput = []

for word in tword:
	tloutput = "\n"
	for words in word.split( "@" ):
		l = 0
		for le in words: 
			if le.isalpha(): 
				l += 17 
			else: 
				l += 5
		tab = int( ( 190 - l ) / 2 )
		for n in range( 9 ):
			tloutput += " " * tab
			for w in words:				
				if w != " ":
					tloutput += letters[ w ].split( "\n" )[ n ] + " "
				else:
					tloutput += " " * 5
			tloutput += "\n"
	loutput.append( tloutput )

try:
	while True:	
		player.play()
		for loutputx in loutput:
			for n in range( 6 ):
				clear()
				output = "\n" * 8
				z = 5 - n
				for x in layout.split( "\n" ):
					output += " " * 72
					for y in x:
						if y == " ":
							output += " "
						else:
							if int( y ) >= z:
								output += "*"
							else:
								output += " "
					output += "\n"
				print( colored( output, colors[0], None, [ "bold" ] ) + colored( loutputx, colors[z - 1], None, [ "bold" ] ) )
				sleep( bpm )
except KeyboardInterrupt:
	print( "I LOVE YOU" )		
