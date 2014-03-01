#Commands
#By Tyler Spadgenske

import datetime

class What(object):
    def __init__(self, cmd, DEBUG=False):
        self.DEBUG = DEBUG
        if DEBUG: print 'Running Command...'
        self.cmd = cmd
        self.cmd.pop(0)
        #Run math() if math problem
        if cmd[0] == 'is':
            self.cmd.pop(0)
            self.math()
        #Run time() if time question
        if cmd[0] == 'time' or cmd[0] == 'day':
            self.time()

    def get_month(self, num, num2):
        if num2 == '1':
            self.day = 'January'
        if num2 == '2':
            self.day = 'February'
        if num2 == '3':
            self.day = 'March'
        if num2 == '4':
            self.day = 'April'
        if num2 == '5':
            self.day = 'May'
        if num2 == '6':
            self.day = 'June'
        if num2 == '7':
            self.day = 'July'
        if num2 == '8':
            self.day = 'August'
        if num2 == '9':
            self.day = 'September'
        if num == '1' and num2 == '0':
            self.day = 'October'
        if num == '1' and num2 == '1':
            self.day = 'November'
        if num == '1' and num2 == '2':
            self.day = 'December'
        return self.day
        
    def math(self):
        if self.DEBUG: print 'EQUATION:', self.cmd

        #Check for valid command again
        if len(self.cmd) == 3 or len(self.cmd) == 4:
            pass
        else:
            for i in range(0, 2):
                self.cmd.append(None)
            if self.DEBUG: print 'Invalid Command'

        #Solve problem
        self.answer = None
        try:
            if self.cmd[1] == 'plus':
                self.answer = int(self.cmd[0]) + int(self.cmd[2])
            elif self.cmd[1] == 'minus':
                self.answer = int(self.cmd[0]) - int(self.cmd[2])
            elif self.cmd[1] == 'times':
                self.answer = int(self.cmd[0]) * int(self.cmd[2])
            elif self.cmd[1] == 'divided':
                self.answer = int(self.cmd[0]) / int(self.cmd[3])
        except:
            if self.DEBUG: print 'Not, math, looking elsewhere...'

        if self.DEBUG: print 'ANSWER = ', str(self.answer)

    def time(self):
        #Get current time
        self.raw_time = str(datetime.datetime.now()).split()
        #Say time if selected command
        if self.cmd[0].lower() == 'time':
            time = str(self.raw_time[1])
            if self.DEBUG: print 'It is ' + time[0] + time[1] + time[2] + time[3] + time[4] + ' AM.'
        #Say day if selected command
        if self.cmd[0].lower() == 'day':
            time = str(self.raw_time[0])
            month = self.get_month(time[5], time[6])
            
            if self.DEBUG: print 'Today is ' + month + ' ' + time[-2] + time[-1] + ', ' + time[0] + time[1] + time[2] + time[3] 
            
                
    
