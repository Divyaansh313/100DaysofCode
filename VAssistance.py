import pyttsx3 as pyt
import os

pyt.speak("Welcome, What would you like to do?")

while True:
	print()
	print("Enter the program which you desire to run: ",end="")
	user_input= input()
	
	if(("run" in user_input) or ("open" in user_input) or ("execute" in user_input)) and (("chrome" in user_input) or ("google" in user_input) or ("web browser" in user_input)):
  		print("Opening Chrome")
  		os.system("chrome")

	elif(("run" in user_input) or ("open" in user_input) or ("execute" in user_input)) and (("song app" in user_input) or ("media player" in user_input) or ("song application" in user_input)):
  		print("Opening media player")
  		os.system("wmplayer")

	elif(("run" in user_input) or ("open" in user_input) or ("execute" in user_input)) and (("notepad" in user_input) or ("editor" in user_input) or ("write text" in user_input)):
  		print("Opening notepad")
  		os.system("notepad")

	elif(("run" in user_input) or ("open" in user_input) or ("execute" in user_input)) and (("Microsoft edge" in user_input) or ("edge" in user_input) or ("edge browser" in user_input)):
  		print("Opening Edge browser")
  		os.system("msedge")

	elif(("run" in user_input) or ("open" in user_input) or ("execute" in user_input)) and (("firefox" in user_input) or ("Firefox" in user_input)):
  		print("Opening Firefox")
  		os.system("firefox")
	
	elif(("run" in user_input) or ("open" in user_input) or ("execute" in user_input)) and (("Discord" in user_input) or ("discord" in user_input)):
  		print("Opening Discord")
  		os.system("Discord")
	
	elif(("run" in user_input) or ("open" in user_input) or ("play" in user_input)) and (("spotify" in user_input) or ("Spotify" in user_input) or ("songs" in user_input)):
  		print("Opening Spotify")
  		os.system("spotify")

	elif(("run" in user_input) or ("open" in user_input) or ("execute" in user_input)) and (("vscode" in user_input) or ("VSCode" in user_input) or ("ide" in user_input) or ("IDE" in user_input) or ("Code editor" in user_input)):
  		print("Opening VS Code")
  		os.system("Code")

	elif(("run" in user_input) or ("open" in user_input) or ("execute" in user_input)) and (("Excel" in user_input) or ("excel" in user_input) or ("sheets" in user_input) or ("microsoft excel" in user_input) or ("Microsoft Excel" in user_input)):
  		print("Opening Microsoft Excel")
  		os.system("EXCEL")

	elif(("run" in user_input) or ("open" in user_input) or ("execute" in user_input)) and (("Word" in user_input) or ("word" in user_input) or ("Microsoft Word" in user_input) or ("microsoft word" in user_input)):
  		print("Opening Microsoft Word")
  		os.system("WINWORD")

	elif(("run" in user_input) or ("open" in user_input) or ("execute" in user_input)) and (("Powerpoint" in user_input) or ("powerpoint" in user_input) or ("PowerPoint" in user_input) or ("microsoft powerpoint" in user_input) or ("Microsoft Powerpoint" in user_input) or ("ppt" in user_input) or("PPT" in user_input)):
  		print("Opening Microsoft Powerpoint")
  		os.system("POWERPNT")

	elif(("exit" in user_input) or ("close" in user_input) or ("close program" in user_input) or ("exit program" in user_input) or ("Exit" in user_input) or ("Close" in user_input)):
  		print("Exiting the program")
  		pyt.speak("Visit Again!")
  		break

	else:
  		print("Operation not supported")
  		pyt.speak("Enter a valid operation")




