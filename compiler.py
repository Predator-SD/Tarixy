class compiler(object):
  def __init__(self):
    self.debug()
    self.name={}
    self.val={}
    self.type={}
    self.range={}
    self.atclass=''
  def debug(self):
    print(self.analysis("class new (){"))
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
  def gettype(self,str):
    range=str[:3]
    raw=(self.de(str)).replace("char","1").replace("int","2").replace("double","3").replace("method","4")
    type=raw[4]
    if type=="1":
      type="char"
    elif type=="2":
      type="int"
    elif type=="3":
      type="double"
    elif type=="4":
      type="method"
    else:
      type="error"
    mat=[range,type]
    return mat
  def scan(self,line,key):
    time=0
    res=[]
    for i in line:
      time=time+1
      if i == key:
        res.append(time)
    return res
  def analysis(self,line):
    if line[:6]=="class ":
      p2=line.replace(' ','$')
      m1=self.scan(p2,'$')
      r1=p2[m1[0]:m1[1]-1]
      self.atclass=r1
      print("Met new class:")
      print(self.atclass)
    if line[:4]=="met " or line[:4]=="var ":
      line=line[4:]
test=compiler()
