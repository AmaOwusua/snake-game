import curses

#setup window
curses.initscr()
win = curses.newwin(20, 60, 0, 0)  #column, row (y,x, startpoint, startpoint)
win.keypad(1)                      #arrow keys to ctrl snake
curses.noecho()                    #no listening to other inputs
curses.curs_set(0)
win.border(0)
win.nodelay(1)


#game logic
score = 0

while True:
    event = win.getch()
print(f"Final score ={score}")









