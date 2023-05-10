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


# ---- Demo suite ----

def do_basic_demo() -> None:
	"""Creates a single QR Code, then prints it to the console."""
	text = input('Enter the URL to make into a QR code : ')
	errcorlvl = QrCode.Ecc.LOW  # Error correction level
	
	# Make and print the QR Code symbol
	qr = QrCode.encode_text(text, errcorlvl)
	# print_qr(qr)
	print(to_svg_str(qr, 4))


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

	myqr= f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {qr.get_size()+border*2} {qr.get_size()+border*2}" stroke="none">
	<rect width="100%" height="100%" fill="#FFFFFF"/>
	<path d="{" ".join(parts)}" fill="#000000"/>
</svg>
"""
	qrsvgname = input('Enter the file name including extension .svg : ')
	# with open( 'myqr.svg', 'w') as q:
	with open(qrsvgname, 'w') as q:
		q.write(myqr)

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