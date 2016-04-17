class compiler(object):
  def __init__(self):
    print(self.gettype("   var double 233"))
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
    return type
test=compiler()
