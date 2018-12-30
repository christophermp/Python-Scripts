import os
from datetime import datetime
folder = r"C:\Users\chris\Pictures"
file = os.path.join(folder, "1.png")
m_time = os.path.getmtime(file)
real_time = datetime.fromtimestamp(m_time)
print(real_time)
print(m_time)
f_time = datetime.strftime(real_time, "%y%m%d_%H%M%S")
print(f_time)
