# 
# QR Code generator demo (Python)
# 
# Run this command-line program with no arguments. The program computes a bunch of demonstration
# QR Codes and prints them to the console. Also, the SVG code for one QR Code is printed as a sample.
# 
# Copyright (c) Project Nayuki. (MIT License)
# https://www.nayuki.io/page/qr-code-generator-library
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# - The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
# - The Software is provided "as is", without warranty of any kind, express or
#   implied, including but not limited to the warranties of merchantability,
#   fitness for a particular purpose and noninfringement. In no event shall the
#   authors or copyright holders be liable for any claim, damages or other
#   liability, whether in an action of contract, tort or otherwise, arising from,
#   out of or in connection with the Software or the use or other dealings in the
#   Software.
# 

from typing import List
from qrcodegen import QrCode, QrSegment


def main() -> None:
	"""The main application program."""
	do_basic_demo()
	# do_variety_demo()
	# do_segment_demo()
	# do_mask_demo()



# ---- Demo suite ----

def do_basic_demo() -> None:
	"""Creates a single QR Code, then prints it to the console."""
	# text = "https://tinyurl.com/2qesbgd6"      # User-supplied Unicode text
	text = input('Enter the URL to make into a QR code : ')
	# qrsvgname = input('Enter the file name including extension .svg : ')
	errcorlvl = QrCode.Ecc.LOW  # Error correction level
	
	# Make and print the QR Code symbol
	qr = QrCode.encode_text(text, errcorlvl)
	print_qr(qr)
	print(to_svg_str(qr, 4))


def do_variety_demo() -> None:
	"""Creates a variety of QR Codes that exercise different features of the library, and prints each one to the console."""
	
	# Numeric mode encoding (3.33 bits per digit)
	qr = QrCode.encode_text("314159265358979323846264338327950288419716939937510", QrCode.Ecc.MEDIUM)
	print_qr(qr)
	
	# Alphanumeric mode encoding (5.5 bits per character)
	qr = QrCode.encode_text("DOLLAR-AMOUNT:$39.87 PERCENTAGE:100.00% OPERATIONS:+-*/", QrCode.Ecc.HIGH)
	print_qr(qr)
	
	# Unicode text as UTF-8
	qr = QrCode.encode_text("\u3053\u3093\u306B\u3061\u0077\u0061\u3001\u4E16\u754C\uFF01\u0020\u03B1\u03B2\u03B3\u03B4", QrCode.Ecc.QUARTILE)
	print_qr(qr)
	
	# Moderately large QR Code using longer text (from Lewis Carroll's Alice in Wonderland)
	qr = QrCode.encode_text(
		"Alice was beginning to get very tired of sitting by her sister on the bank, "
		"and of having nothing to do: once or twice she had peeped into the book her sister was reading, "
		"but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice "
		"'without pictures or conversations?' So she was considering in her own mind (as well as she could, "
		"for the hot day made her feel very sleepy and stupid), whether the pleasure of making a "
		"daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly "
		"a White Rabbit with pink eyes ran close by her.", QrCode.Ecc.HIGH)
	print_qr(qr)


# ---- Utilities ----

def to_svg_str(qr: QrCode, border: int) -> str:
	"""Returns a string of SVG code for an image depicting the given QR Code, with the given number
	of border modules. The string always uses Unix newlines (\n), regardless of the platform."""
	if border < 0:
		raise ValueError("Border must be non-negative")
	parts: List[str] = []
	for y in range(qr.get_size()):
		for x in range(qr.get_size()):
			if qr.get_module(x, y):
				parts.append(f"M{x+border},{y+border}h1v1h-1z")
# 	return f"""<?xml version="1.0" encoding="UTF-8"?>
# <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
# <svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {qr.get_size()+border*2} {qr.get_size()+border*2}" stroke="none">
# 	<rect width="100%" height="100%" fill="#FFFFFF"/>
# 	<path d="{" ".join(parts)}" fill="#000000"/>
# </svg>
# """

	myqr= f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {qr.get_size()+border*2} {qr.get_size()+border*2}" stroke="none">
	<rect width="100%" height="100%" fill="#FFFFFF"/>
	<path d="{" ".join(parts)}" fill="#000000"/>
</svg>
"""
	with open( 'myqr.svg', 'w') as q:
		q.write(myqr)

# 	with open('myqr.svg', 'w') as q:
# 		q.write("""<?xml version="1.0" encoding="UTF-8"?>
# <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
# <svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {qr.get_size()+border*2} {qr.get_size()+border*2}" stroke="none">
# 	<rect width="100%" height="100%" fill="#FFFFFF"/>
# 	<path d="{" ".join(parts)}" fill="#000000"/>
# </svg>
# """)

def print_qr(qrcode: QrCode) -> None:
	"""Prints the given QrCode object to the console."""
	border = 4
	for y in range(-border, qrcode.get_size() + border):
		for x in range(-border, qrcode.get_size() + border):
			print("\u2588 "[1 if qrcode.get_module(x,y) else 0] * 2, end="")
		print()
	print()


# Run the main program
if __name__ == "__main__":
	main()