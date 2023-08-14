


# if __name__ == "__main__":
#     for picture in result_dict.keys():
#         marker=os.path.join(picture, 'marker.png')
#         num_parts = result_dict[f'{picture}']["lane_num"]
#         for i in range(num_parts):
#             if i == marker_lane:
#                 continue
#             else:
#                 protein = os.path.join(picture, f'lane{i}.jpg')
#                 xulab_id = result_dict[picture][f'lane{i}']
#                 output_path = os.path.join(picture, f'{picture}_{xulab_id}.png')
#                 concatenate(img1=marker, img2=protein, title=xulab_id, output_path = output_path)
#                 #将超链接写入原表中
#                 add_hyperlinker(xlsx_filename=xlsx_filename, picture=picture, target_text=xulab_id, local_file_path=output_path)