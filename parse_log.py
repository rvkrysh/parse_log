#!/usr/bin/python

key_word = ("start_gui", "synth")

def parse_log (args = "vivado.log"):
    
    try:
        with open(args, 'r') as f:
            for line in f:
                if line.strip():
                    if line.split()[0] == key_word[0]:
                        print ("blah")
	
    except FileNotFoundError:
        print ("File not found")

if __name__ == '__main__':
    parse_log()
	
