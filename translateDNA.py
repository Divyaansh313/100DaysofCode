"""
File: translate_dna.py
----------------
This program translates a strand of DNA to create its matching base pair.
A becomes T, T becomes A, G becomes C, and C becomes G.
"""

# The line below imports TextGrid for use here
from TextGrid import TextGrid

def translate_DNA(filename):
	"""
	This function takes a DNA TextGrid and converts each nucleotide to its
	matching base pair.

	Input:
		filename (string): name of TextGrid to be read in

	Returns:
		TextGrid of DNA with all its base pairs changed
	"""

	dna = TextGrid(filename)

	for y in range(dna.height):
		for x in range(dna.width):
			my_cell = dna.get_cell(x,y)
			val = my_cell.value
			if val == 'A':
				my_cell.value = 'T'
			elif val == 'T':
				my_cell.value = 'A'
			elif val == 'G':
				my_cell.value = 'C'
			else:
				my_cell.value = 'G'
	return dna


def main():
	"""
	This program tests your translate_DNA function by displaying
	the original DNA grid as well as the resulting DNA grid
	from your translate_DNA function.
	"""
	print('Original sequence:')
	original_dna = TextGrid('COVID19_firstsequence.txt')
	print(original_dna)
	print()
	print("Translated sequence:")
	translated_dna = translate_DNA('COVID19_firstsequence.txt')
	print(translated_dna)


if __name__ == '__main__':
	main()