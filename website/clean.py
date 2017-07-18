#coding=utf-8
import os
import os
dir=os.getcwd()
jpg=["jpg","jpeg","png","bmp"]
for root,dirs,files in os.walk(dir):
    for file in files:
        for i in jpg:
            if file.split(".")[-1]==i:
                target_filename=root+"/"+file
                print target_filename
                file=root.split("/")[3]+"/"+file
                url="web.file.myqcloud.com/files/v1/1251518466/tecplaces/pic/"+file
                header={
                    "Host": "< Region >.file.myqcloud.com",
                    "Content - Type": "multipart / form - data",
                    "Authorization": "< multi_effect_signature >"
                }
                data={}
                data['op']="upload"
                data['filecontent']=