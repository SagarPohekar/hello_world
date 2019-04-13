from Point import Point

class Line:
  def __init__(self, start, end):
    self._m_start_point = start;
    self._m_end_point = end;

  @property
  def start_point(self):
    return self._m_start_point
  
  @start_point.setter
  def start_point(self,value):
    self._m_start_point.x = value.x;
    self._m_start_point.y = value.y

  @property
  def end_point(self):
    return self._m_end_point;

  @end_point.setter
  def end_point(self, value):
    self._m_end_point.x = value.x
    self._m_end_point.y = value.y

  def Print(self):
    print("Start Point",self.start_point.Print());
    print("End Point",self.end_point.Print());