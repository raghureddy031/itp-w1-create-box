"""This is the entry point of the program."""

def create_box(height, width, character):
	i = 0
	j = 0
	ch = ''
	if width >= 1 and height >= 1:
		for i in range(i, height):
			for j in range(0, width):
				ch = ch + character
			else:
				ch = ch + '\n'
		return ch
	else:
		return 'Enter correct details'
		
def create_box_empty(height, width, character):
	i = 0
	j = 0
	ch = ''
	if width >= 3 and height >= 3:
		for i in range(i, height):
			for j in range(0, width):
				if i == 0 or i == height-1:
					ch = ch + character
				else:
					if j > 0 and j < (width-1):
						ch = ch + ' '
					else:
						ch = ch + character
			else:
				ch = ch + '\n'
		return ch
	else:
		return 'Enter correct details'