import subprocess
from ast import literal_eval
#result = subprocess.run(['fortune','off\atheism'], stdout=subprocess.PIPE)
result = subprocess.check_output(['fortune','off/atheism'])
#result.stdout
r = result.decode("utf-8")
#r.replace("\n","")
#print(literal_eval("%s" % result))
print(r)
#print(literal_eval("%s" % r))
