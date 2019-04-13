from Line import Line

class Triangle:
  def __init__(self,pt1, pt2, pt3):
    self._m_pt1 = pt1
    self._m_pt2 = pt2
    self._m_pt3 = pt3

  @property
  def point1(self):
    return self._m_pt1
  @point1.setter
  def point1(self,value):
    self.point1 = value

  @property
  def point2(self):
    return self._m_pt2
  @point2.setter
  def point2(self,value):
    self.point2 = value

  @property
  def point3(self):
    return self._m_pt3
  @point3.setter
  def point3(self,value):
    self.point3 = value
