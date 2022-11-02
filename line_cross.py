import cv2
from shapely.geometry import LineString
class LineCross():
    def __init__(self,coords,region,section):
        self.crossed_ids = []
        self.coords=coords
        self.region = region
        self.section_name = section
        self.sequence_lines = [(coords[i],coords[i+1])
                                for i in range(len(coords)-1)]
    
    def update(self,object_id,centroidarr):
        if object_id not in self.crossed_ids and \
            self.crosses(centroidarr):
            self.crossed_ids.append(object_id)
    def draw(self,img):
        for line in self.sequence_lines:
            img = cv2.line(img,line[0],line[1],(0,255,0), thickness=1)
        img = cv2.putText(img, self.section_name +' : ' +str(len(self.crossed_ids)), self.region, cv2.FONT_HERSHEY_SIMPLEX, 
                         1/2, (255, 0, 0), 1, cv2.LINE_AA)
        return img


    def crosses(self,sequence):
        if len(sequence)<2:return False
        linestring = LineString(sequence)
        line_barier = LineString(self.coords)
        intersection_point = linestring.intersection(line_barier)
        return 'POINT' in str(intersection_point)
