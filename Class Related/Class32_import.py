# Importing an entire module 

"""
import Class30_Import
y  = Class30_Import.Toys("Car", 2000)
y.x(y.toy_name, y.toy_price)

obj = Class30_Import.Toys(str(input("Enter Toy name : - ")), int(input("Enter Toy Price : - ")))
print(obj.x(obj.toy_name, obj.toy_price))
"""

# Importing using alias
from Class31_import  import Tec as T
y = T()
y.odometer_speed()

#  importing module 

"""import Class31_import as module31"""




