# -*- coding=utf-8 -*-
from flask import Flask
from flask import render_template,abort

import json
import os

app=Flask(__name__)
path = '/home/shiyanlou/files'
files = os.listdir(path)

@app.route('/')
def index():
    '''
    显示文章名称的列表
    页面中需要显示 ｀/home/shiyanlou/files/｀目录下所有的json文件
    中的｀title｀信息列表
    '''
    titles=[]
    for file in files:
        with open(path+'/'+file,'r') as f:
            json_info = json.load(f)
            titles.append(json_info['title'])
    return render_template('index.html',title_mod=titles)


@app.route('/files/<filename>')
def file(filename):
    '''
    读取并显示 filename.json中的文章内容
    例如 filename='helloshiyanlou'的时候显示helloshiyanlou.json
    中的内容
    如果filename不存在，则显示包含字符串｀shiyanlu 404｀ 404页面错误
    '''
    filename_j = filename+'.json'
    file_locate = path+'/'+filename+'.json'
    if filename_j not in files:
        abort(404)
    else:
        with open(file_locate,'r') as f:
            file_info_dic = json.load(f)
#        file_info_list = []
#        for k,v in file_info_dic.items():
#            file_info_list.append((k,v))
    return render_template('file.html',file_info_mod=file_info_dic)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404


if __name__=="__main__":
    app.run()

