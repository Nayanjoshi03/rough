import os 
from config.config import DATA_DIR

os.makedirs(DATA_DIR,exist_ok=True)
raw_dir=os.path.join(DATA_DIR,'raw1')
os.makedirs(raw_dir,exist_ok=True)

with open(os.path.join(raw_dir,'data1.txt'),'w') as f:
    f.write("this is raw1 data 1")

with open(os.path.join(raw_dir,'data2.txt'),'w') as f:
    f.write("this is raw1 data 2")

raw_dir2=os.path.join(DATA_DIR,'raw2')
os.makedirs(raw_dir2,exist_ok=True)
with open(os.path.join(raw_dir2,'data1.txt'),'w') as f:
    f.write("this is raw2  data 1")

with open(os.path.join(raw_dir2,'data2.txt'),'w') as f:
    f.write("this is raw2 data 2")
    

