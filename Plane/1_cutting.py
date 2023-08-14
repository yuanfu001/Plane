from utils import get_info, cut
import argparse
import os
import shutil

#先通过"cutting"方法将每条lane都切割出来
def cutting(xlsx_filename):
    result_dict = get_info(xlsx_filename)
    marker_lane=0
    for picture in result_dict.keys():
        # 创建目录
        if os.path.exists(picture):
            print(f"The directory {picture} already exists. Removing and creating a new one.")
            shutil.rmtree(picture)  
            os.makedirs(picture)    
        else:
            os.makedirs(picture)
        cut(result_dict, picture, marker_lane=0, center=0.05, move=0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="test arguments for Plane")
    parser.add_argument("--xlsx_filename", default="/Users/fy/Desktop/project/Plane/test/data/pic_info.xlsx", type=str, help="传入胶图信息的xlsx文件")
    parser.add_argument("--marker_lane", type=int, default=0, help="marker的泳道，默认为0")
    parser.add_argument("--center", type=float, default=0.05, help="去除边缘的比例")
    args = parser.parse_args()
    cutting(args.xlsx_filename)
