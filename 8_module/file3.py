# import random

# import math


# a=9
# ans=math.sqrt(a)
# print(ans)

# #numpy and pandas
# import numpy as np
# import pandas as pd


#what is pip
#pip freeze
#downlad pip install package_name
#downgrade a package
#pip3 install pandas==2.1.0
#pip3 install -U pandas
#pip3 uninstall pandas




import sys
import time
import random 
import os

r=random.randint(10,100)
print(r)
time.sleep(1)
print(os.getcwd())

if r>50:
    sys.exit()
else:
    print('below 50')
print('last line')