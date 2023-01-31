import threading

from datasaver.datasaver import DataSaver
from receiver.receiver   import Receiver
from mainWindow.mainWindow import MainWindow
from datahub import Datahub

class Thread_Receiver(threading.Thread):
    def __init__(self,datahub):
        super().__init__()
        self.datahub = datahub

    def run(self):
        receiver = Receiver(self.datahub)
        receiver.start()


class Thread_DataSaver(threading.Thread):
    def __init__(self, datahub):
        super().__init__()
        self.datahub = datahub
        

    def run(self):
        datasaver = DataSaver(self.datahub)
        datasaver.start()


class Master:
  
    def __init__(self):
        
        self.datahub = Datahub()

        self.mainWindow = MainWindow(self.datahub)

        self.datasaver = Thread_DataSaver(self.datahub)

        self.receiver = Thread_Receiver(self.datahub)


        # self.datasaver.daemon = True
        self.receiver.daemon = True
        
        
    def run(self, isDatasaver, isReceiver):

        if isReceiver: self.receiver.start()
        if isDatasaver: self.datasaver.start()

        self.mainWindow.start() 
        self.mainWindow.setEventLoop()

if __name__ == "__main__":
    master = Master()

    master.run(isDatasaver=1,
               isReceiver=1
               )
