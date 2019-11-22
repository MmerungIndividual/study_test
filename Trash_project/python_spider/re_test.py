
import re
string = "<p>我是谁</p>"
pattern = re.compile(r"<.*?>")
str = re.sub(pattern,"",string)
print(str)