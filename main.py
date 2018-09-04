import getpass
import os
import sys
import time
import csv
from playsound import playsound

def main():
	invalid_text = "Error, invalid text"
	with open('ids.csv', 'rt') as csvfile:
		idList = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in idList:
			print(row)
	while True:
 		try:
 			print("Ready!")
 			enter_id_text = "Enter your student ID: "
 			input = getpass.getpass(enter_id_text)
 			parsed_input = str(parse_input(input, invalid_text))
 			if parsed_input == 'None':
 				print("Failed")
 				print(parsed_input)
 				playsound('/Users/michael/Code/SoDA_Swiper_Basic/error.wav')
 				time.sleep(0.5)
 				continue		
 			else:
 				print("Success")
 				print(parsed_input)
 				playsound('/Users/michael/Code/SoDA_Swiper_Basic/accept.wav')
 				time.sleep(0.5)
 		except KeyboardInterrupt:
 			sys.exit()
			
def parse_input(input, invalid_text):
 	if input[:7] == ';601744' and len(input) > 16:
 		return input[7:17]
 	elif input[:10] == '%E?;601744' and len(input) > 19:
 		return input[10:20]
 	else:
 		return None
		
if __name__ == '__main__':
	main()