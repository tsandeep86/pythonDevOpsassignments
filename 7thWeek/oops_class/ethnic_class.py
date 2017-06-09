class ethinicity:
    
    
    
    def __init__(self,nationality,color,avg_height,lang):
        
        self.nationality=nationality
        self.color=color
        self.avg_height=avg_height
        self.lang=lang
        
    
    def widely_spoken(self):
        
        if self.lang == 'english':
            print "widely spoken"
        else:
            print "Not widely spoken"
            
    
    def displayEthinicity(self):
        print "Nationality:", self.nationality , " Color:" , self.color , " avg_height:" , self.avg_height , " Language:" , self.lang
    