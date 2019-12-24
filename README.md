# caltech 256数据集介绍

[下载地址](http://www.vision.caltech.edu/Image_Datasets/Caltech256/)

## 基本介绍
caltech 256下载解压后你会发现共有257个文件夹，其实只要前256个文件夹是有效目标，最后一个文件夹里的图片不算特定目标，相当于背景图片，不属于任何一类。先看下下面的图片，对这个数据集有个整体的感受。

![image.png](https://cdn.nlark.com/yuque/0/2019/png/655017/1577178832911-2f255243-367c-4d82-b3ba-02077d9e8e9c.png#align=left&display=inline&height=836&name=image.png&originHeight=1672&originWidth=1576&size=2095952&status=done&style=none&width=788)

## 详情：
通过以下代码，先看下图像大小、分辨率大小。
```python
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

```

30607张图片，宽的平均值为371，高的平均值是326，图像大小平均值为37Kb。
可以看出，图像质量其实挺一般的，不过公开数据集一般都这样。

不过里面最大的图像居然有6Mb多，宽和高的最大值都7900多了。用linux命令查看一下超过4Mb的图像有多少

```shell
yang@yangdeMacBook-Pro ~/P/p/d/256_ObjectCategories> find . -size +4M 
./073.fireworks/073_0054.jpg
./009.bear/009_0045.jpg
./043.coin/043_0042.jpg
```

4Mb以上的图像只有3张，看来这个大图只是特例，043_0042.jpg就是那个最大的了。其实1Mb以上的也就只有37张，也就是千分之一。

## 数据集分割

按照7:1:2的大致比例分割数据集，分别用于训练、验证和测试。分别为train.lst、val.lst、test.lst。





