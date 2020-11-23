from datetime import timedelta, datetime
from dataclasses import dataclass
import os


a = timedelta.max
b = timedelta.max

if a == b:
    print("true")

@dataclass
class Test:
    first: datetime

text = "SVF2018-05-24_12:02:58.917"
print(text[14:].rstrip())
text1 = datetime.strptime(text[14:].rstrip(), "%H:%M:%S.%f")
print(text1)
text2 = Test(text1)
print(text2)

print(os.getcwd())
print(os.path.basename(__file__))
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
azaza = os.path.join(os.path.dirname(__file__), "data")
print(azaza)
