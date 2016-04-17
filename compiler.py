class compiler(object):
  def __init__(self):
    print(self.load('test.ty'))
  def de(self,str):
    p1=str.replace(' ','7')
    time=0
    for i in p1:
      time=time+1
      if i!='7':
        res=p1[time-1:]
        return res
  def load(self,file):
    raw=open(file)
    try:
      txt=raw.read()
    finally:
      raw.close()
    return txt.split('\n')
test=compiler()
