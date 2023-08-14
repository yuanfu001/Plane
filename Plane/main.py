from utils import get_info, cut, marker,concatenate,add_hyperlinker
import argparse
import os
import shutil

#先通过"cutting"方法将每条lane都切割出来

# os.chdir("./data")
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
    parser.add_argument("--marker_lane", type=int, default=0, help="marker的泳道 默认为0")
    parser.add_argument("--center", type=float, default=0.05, help="去除边缘的比例")
    args = parser.parse_args()
    cutting(args.xlsx_filename)

    #调试参数
    marker_list = [10, 15, 20, 25, 35, 40, 50, 70, 100, 150, 250]
    marker_thresh={
        "0412浓缩后":178,
        "0629浓缩后":185,
        "20230505_E":170,
        "20230523_E":165,
        "20230526_E":200,
        "20230531_E":183,
        "20230605_E":190,
        "20230607_E":135,
        "20230628_E":199
    }
    marker(marker_thresh, marker_list)

    for picture in result_dict.keys():
        marker=os.path.join(picture, 'marker.png')
        num_parts = result_dict[f'{picture}']["lane_num"]
        for i in range(num_parts):
            if i == marker_lane:
                continue
            else:
                protein = os.path.join(picture, f'lane{i}.jpg')
                xulab_id = result_dict[picture][f'lane{i}']
                output_path = os.path.join(picture, f'{picture}_{xulab_id}.png')
                concatenate(img1=marker, img2=protein, title=xulab_id, output_path = output_path)
                #将超链接写入原表中
                add_hyperlinker(xlsx_filename=xlsx_filename, picture=picture, target_text=xulab_id, local_file_path=output_path)