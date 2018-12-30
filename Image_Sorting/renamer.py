import os
folder = r"C:\Users\chris\Pictures\1.PNG"
file = os.path.join(folder, "img1.png")
m_time = os.path.getmtime(file)
print(m_time)
