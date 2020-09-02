#Calculate the final score of the game using original Nintendo scoring system
########################################################
#The scoring formula is built on the idea that more difficult line clears should be awarded more points. For example, a single line clear is worth 40 points, clearing four lines at once (known as a Tetris) is worth 1200.

#A level multiplier is also used. The game starts at level 0. The level increases every ten lines you clear. For our task you can use this table:
#Level Points for 1 line Points for 2 lines	Points for 3 lines	Points for 4 lines
#0	40	            100                     300	                    1200
#1	80	            200	                    600	                    2400
#2	120	            300	                    900	                    3600
#3	160	            400	                    1200	            4800
#...
#7	320	            800	                    2400	            9600
#...	For level n you must determine the formula by yourself using given examples from the table.

def get_score(arr) -> int:
    total = 0 
    level = 0
    linCount = 0
    for num in arr:
        if(num == 1):
            total += (level + 1) * 40
            linCount += num;
        elif(num == 2):
            total += (level + 1) * 100
            linCount += num;
        elif(num == 3):
            total += (level + 1) * 300
            linCount += num;
        elif(num == 4):
            total += (level + 1) * 1200
            linCount += num;
        if (linCount >= 10): 
            level += 1
            linCount = linCount - 10
    return total

get_score([2, 0, 4, 2, 2, 3, 0, 0, 3, 3])
