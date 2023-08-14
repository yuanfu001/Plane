import sys

sys.path.append("/Users/fy/Desktop/project/Plane")

print(sys.path)


import Plane
import os

project_path = os.path.dirname(os.path.realpath(Plane.__file__))
print(project_path)