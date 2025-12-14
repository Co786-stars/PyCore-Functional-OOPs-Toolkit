"""
Use to import multiple class in __main__ module : -

syntax : - import module only 
import class_name
import class_name

Syntax : - import class only

from module_name import classname
from module_name import classname1, classname2...etc

"""

# import Class30_Import : It use to import module basic 
# from Class30_Import import Device 
# from Class30_Import import Tec
from Class30_Import import Device , Tec

obj = Device()
x = obj.motorspeed()
print(x)

obj2 = Tec()
x = obj2.odometer_speed()
print(x)
