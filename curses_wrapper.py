try:
	import curses
except:	
	print("The builtin curses module is not supported on Windows.")
	print("However, you can install the windows-curses module in order to play on Windows.")
	while True:
		print("Would you like to install windows-curses? (Y/N)")
		choice = input(">> ")
		if choice:
			c = choice[0].lower()
			if c == "y":
				print("Beginning installation...")
				import subprocess
				code = subprocess.call(["pip", "install", "windows-curses"])
				if code:
					print("Failed to install windows-curses. Try manual `pip install windows-curses`")
					exit(code)
				break
			elif c == "n":
				exit()
			else:
				print("Please enter Y or N")
	import curses
	os.system("cls" if os.name == "nt" else "clear")


class WindowPlain:
    def __init__(self):
        pass
    def clear(self):
        pass
            
    def addstr(self,x,y,text):
        pass
            
    def getch(self):
        pass
        
    def getstr(self):
        pass
        
    def move(self, x, y):
        pass
        
    def refresh(self):
        pass

class CursesWrapper:
    def __init__(self, is_plain):
        self.is_plain = is_plain
        self.plain_window = WindowPlain

    def flushinp(self):
        if self.is_plain:
            pass
        else:
            curses.flushinp()

    def nocbreak(self):
        if self.is_plain:
            pass
        else:
            curses.nocbreak()
        
    def echo(self):
        if self.is_plain:
            pass
        else:
            curses.echo()
    
    def noecho(self):
        if self.is_plain:
            pass
        else:
            curses.noecho()
    
    def endwin(self):
        if self.is_plain:
            pass
        else:
            curses.endwin()
            
    def initscr(self):
        if self.is_plain:
            return self.plain_window
        else:
            return curses.initscr()
            
    def start_color(self):
        if self.is_plain:
            pass
        else:
            curses.start_color()
            
    def init_pair(self,pair_number, fg, bg):
        if self.is_plain:
            pass
        else:
            curses.init_pair(pair_number,fg,bg)
            
    def color_pair(self,pair_number):
        if self.is_plain:
            return 0
        else:
            return curses.color_pair(pair_number)
            