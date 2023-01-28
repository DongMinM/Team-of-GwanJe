

class Datahub:

    def __init__ (self):
        """
        Communication Status Parameter
        """
        self.iscommunication_start = 0


        """
        Rocket Status Parameter
        """
        self.timespace = []
        self.rolls = []
        self.pitchs = []
        self.yaws = []
        self.rollSpeeds = []
        self.pitchSpeeds = []
        self.yawSpeeds = []
        self.Xaccels = []
        self.Yaccels = []
        self.Zaccels = []
        self.latitudes = []
        self.longitudes = []
        self.altitude = []
     
    def communication_start(self):
        self.iscommunication_start=1
        
    def communication_stop(self):
        self.iscommunication_start=0
        
        
        
    def update(self,datas):
        """Update Datas received from rocket"""
        
        self.timespace.append([datas[0],datas[1],datas[2],datas[3]])
        self.rolls.append(datas[4])
        self.pitchs.append(datas[5])
        self.yaws.append(datas[6])
        self.rollSpeeds.append(datas[7])
        self.pitchSpeeds.append(datas[8])
        self.yawSpeeds.append(datas[9])
        self.Xaccels.append(datas[10])
        self.Yaccels.append(datas[11])
        self.Zaccels.append(datas[12])
        self.latitudes.append(datas[13])
        self.longitudes.append(datas[14])
        self.altitude.append(datas[15])

        print(self.timespace)