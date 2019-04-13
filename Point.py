class Point:
  def __init__(self, x = 0.0, y = 0.0):
    self._m_x = x;
    self._m_y = y;

  @property
  def x(self):
    "I am the 'x' property."  
    return self._m_x

  @x.setter
  def x(self, value):
    self._m_x = value

  @property
  def y(self):
    "I am the 'y' property."  
    return self._m_y

  @y.setter
  def y(self, value):
    self._m_y = value

  def Print(self):
    print (self.x, self.y)
