import os
import cv2
import tqdm

class AverageMeter(object):
    """Computes and stores the average and current value"""

    def __init__(self):
        self.initialized = False
        self.val = None
        self.avg = None
        self.sum = None
        self.count = None
        self.max = float("-inf")   # 负无穷
        self.min = float("inf")  # 正无穷

    def initialize(self, val, weight):
        self.val = val
        self.avg = val
        self.sum = val * weight
        self.count = weight
        self.initialized = True


    def update(self, val, weight=1):
        if not self.initialized:
            self.initialize(val, weight)
        else:
            self.add(val, weight)
        if val > self.max:
            self.max = val
        if val < self.min:
            self.min = val

    def add(self, val, weight):
        self.val = val
        self.sum += val * weight
        self.count += weight
        self.avg = self.sum / self.count

    def value(self):
        return self.val

    def average(self):
        return self.avg
    
    def info(self):
        print(f"min:{self.min} max:{self.max} avg:{self.avg} count:{self.count} ")

path = "256_ObjectCategories"
pb = tqdm.tqdm(total=30607)
height = AverageMeter()
width = AverageMeter()
fsizes = AverageMeter()

for root,dirs,files in os.walk(path):
    for file in files:
        if file.endswith("DS_Store"):continue # 这文件烦死了，像个👻一样阴魂不散
        pb.update(1)
        img = cv2.imread(os.path.join(root,file))
        fsize = os.path.getsize(os.path.join(root,file)) / 1024
        h,w,c = img.shape
        height.update(h)
        width.update(w)
        fsizes.update(fsize)

width.info() # min:75 max:7913 avg:371.31202012611493 count:30607 
height.info() # min:75 max:7913 avg:325.90495638252685 count:30607 
fsizes.info() # min:1.1904296875 max:6390.7041015625 avg:36.99148826887028 count:30607 

