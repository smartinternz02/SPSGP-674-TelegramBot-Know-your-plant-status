import random

def tehu(input_text):
     um = str(input_text).lower()
     if um in ("temparature","temp"):
        n=random.randint(26,49)
        print("temperature in degrees is %n")
        return n
     if um in ("humidity","hum"):
        n=random.randint(30,60)
        print("humidity in percentage is %n")
        return n

     if um in ("motoron"):
        return "motor is puton"
     if um in ("motoroff"):
        return "motor is putoff"

     return "i dont understand you."