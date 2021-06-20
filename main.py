'''
class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self._z = float("infinity")
        print(f"Я начал в {self.x}, {self.y}")
    def distance(self,x1,y1):
        self.y += y1
        self.x += x1
    def __call__(self, *args, **kwargs):
        return self.x,self.y
    def print(self):
        print(self.x, self.y)
    def __del__(self):
        print(f"Я закончил в {self.x}, {self.y}")

#main
my_point = Point(2,1)
my_point.print()
my_point.distance(1,2)
my_point.print()
Point.color = "GREEN"
print(f"color is {Point.color}")
print(my_point._z)
del my_point



# warcraft & dota
class Warcraft(object):
    def __init__(self):
        self.game_type = "strategy"
class Dota(Warcraft):
    def __init__(self, game_type):
        self.game_type = game_type
        print(self.game_type)
game1 = Warcraft()
game = Dota(game1.game_type)

###########

class Room(object):
    def __init__(self, assets):
        self.assets = assets
    def __str__(self):
        return self.assets
directors_room_1 = Room(['director'])
teachers_room_1 = Room(['director','teacher'])
students_room_1 = Room(['director','teacher','student'])
main_room_1 = Room(['director','teacher','student','parents'])
roomsss = ["directors_room_1", 'teachers_room_1', 'students_room_1', 'main_room_1']

class User(object):
    def __init__(self, assets, name, features):
        self.assets = assets
        self.features = features
        self.name = name

    def __str__(self):
        return str(str(self.name) + "\n" +str(self.features)+"\n")
p1 = User('student','Alex Miller', 'Enough Swag')
p2 = User('teacher', 'Shevchenko Makar', "director: wyd?; programmer: compiling my project; director: u programing on python dude...")
p3 = User('parent',"Alisa Snow", "Good Looking")
p4 = User('director', "Vitaliy Rubinov", "91")
p5 = User('teacher', 'Maria Easy', "html issa pl.")
p6 = User('student', "Nikita Chislov", 'Without Swag')

def enter_room(m,room, r):
    line = f"The {m.assets} {m.name} tries to enter {r.split('_')[0]} room with number {r.split('_')[2]}"
    if str(m) in room.assets:
        print(line)
        print("ACCESSED")
        print()
    else:
        print(line)
        print("NO ACCESS")
        print()

print(str(p1))
print(str(p2))
print(str(p3))
print(str(p4))
print(str(p5))
print(str(p6))
print()
print(*roomsss)

enter_room(p1, directors_room_1, "directors_room_1")
enter_room(p4, directors_room_1, "directors_room_1")
enter_room(p5, teachers_room_1, "teachers_room_1")
enter_room(p2, teachers_room_1, "teachers_room_1")
enter_room(p3, students_room_1, "students_room_1")
enter_room(p6, main_room_1, "main_room_1")
enter_room(p3, main_room_1, "main_room_1")
enter_room(p3, teachers_room_1, "teachers_room_1")
enter_room(p3, directors_room_1, "directors_room_1")
###############


class Person():
    def __init__(self, old, FIO):
        self.old = old
        self.FIO = FIO
    def __str__(self):
        return str(self.FIO) + " " + str(self.old)
class Driver(Person):
    def __init__(self, skill, old, FIO):
        super().__init__(old, FIO)
        self.skill = skill
class Engine():
    def __init__(self,power_of_engine,comp):
        self.power_of_engine = power_of_engine
        self.comp = comp




class MakeSomePoints():

    """Line is a str obj

    State constants and transmit it to the other funcs

    POINT it is a constant with str "."
    """
    def __init__(self, line):
        self.line = line
        self.POINT = '.'

    def add_point(self):
        return str(self.line)+self.POINT  # add point
                                          # to custom line


line1 = MakeSomePoints('Ok')  # state specimen with str line
print(line1.add_point())
'''


class TimeCheck():
    OUTPUT_FALSE = "-"
    OUTPUT_ERROR = "-"
    '''
    Checking is time correctly

    '''
    def __init__(self,time_):
        try:
            self.ENTERED_TIME_1 = int(time_.split(":")[0])
            self.ENTERED_TIME_2 = int(time_.split(":")[1])
            if self.ENTERED_TIME_1 >= 0 and self.ENTERED_TIME_1 <= 24 and 0 <= self.ENTERED_TIME_2 <= 59:
                self.time_ = time_
            else:
                self.time_ = TimeCheck.OUTPUT_FALSE
        except:
            self.time_ = TimeCheck.OUTPUT_ERROR


#a = TimeCheck("14:00")
#print(a.time_)

class FindTime():
    '''
    This class scanning line and searching "утр" or "am".
    When he search some type text he start searching some digit.

    returned data when string don't have time is "-".
    '''
    EXITED_TIME_CONST = "-"

    def __init__(self, line):
        self.line = line.split()

    def find_time(self):
        exited_time = FindTime.EXITED_TIME_CONST
        for word in self.line:
            if ":" in word:
                exited_time = TimeCheck(word).time_
                if exited_time not in [TimeCheck.OUTPUT_FALSE, TimeCheck.OUTPUT_ERROR]:
                    break


        if exited_time == FindTime.EXITED_TIME_CONST:
            for word_index in range(len(self.line)):
                if self.line[word_index].lower().find("утр") != -1 or self.line[word_index].lower().find("am") != -1:
                    #print(self.line[word_index].find("утр"))
                    try:
                        #print(self.line[word_index-1])
                        hours = int(self.line[word_index-1])
                        exited_time = TimeCheck(str(hours)+":00").time_

                    except:
                        try:
                            hours = int(self.line[word_index-2])
                            TimeCheck(str(hours) + ":00")
                            exited_time = TimeCheck(str(hours) + ":00").time_
                        except:
                            continue
        return exited_time


class FindDate():
    EXITED_TIME_CONST = ""

    def __init__(self, line):
        self.line = line.split()

    def find_date(self):
        exited_time = FindTime.EXITED_TIME_CONST
        '''
        for word in self.line:
            if ":" in word:
                exited_time = TimeCheck(word).time_
                if exited_time not in [TimeCheck.OUTPUT_FALSE, TimeCheck.OUTPUT_ERROR]:
                    break
        '''

        if exited_time == FindTime.EXITED_TIME_CONST:
            for word_index in range(len(self.line)):
                if self.line[word_index].lower().find("январ") != -1\
                        or self.line[word_index].lower().find("феврал") != -1 \
                        or self.line[word_index].lower().find("март") != -1 \
                        or self.line[word_index].lower().find("апрел") != -1 \
                        or self.line[word_index].lower().find("мае") != -1 \
                        or self.line[word_index].lower().find("мая") != -1 \
                        or self.line[word_index].lower().find("июн") != -1 \
                        or self.line[word_index].lower().find("июл") != -1 \
                        or self.line[word_index].lower().find("август") != -1 \
                        or self.line[word_index].lower().find("сентябр") != -1 \
                        or self.line[word_index].lower().find("октябр") != -1 \
                        or self.line[word_index].lower().find("ноябр") != -1 \
                        or self.line[word_index].lower().find("декабр") != -1:
                    #print(self.line[word_index].find("утр"))
                    try:
                        #print(self.line[word_index-1])
                        hours = int(self.line[word_index-1])
                        exited_time = str(hours) + self.line[word_index]

                    except:
                        try:
                            hours = int(self.line[word_index-3])
                            exited_time = str(hours) + self.line[word_index]
                        except:
                            continue
        return exited_time


inputed = input()
ooo = FindTime(inputed)
oo = ooo.find_time()

temp21 = FindDate(inputed)
temp22 = temp21.find_date()
print(oo)


