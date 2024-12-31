import jieba
from matplotlib import pylab as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from utils.qureyhive import query_hive
#
# #词云图
# def get_img(targetImageSrc, resImagSrc):
#     data = query_hive('select title from jobData', [], 'select')
#     text = ''
#     for i in data:
#         if i[0] != '':
#             tarArr = i
#             for j in tarArr:
#                 text += j
#     data_cut = jieba.cut(text, cut_all=False)
#     string = ' '.join(data_cut)
#
#     #词云图
#     img = Image.open(targetImageSrc)
#     img_arr = np.array(img)
#     wc = WordCloud(
#         font_path='STHUPO.TTF',
#         mask = img_arr,
#         background_color='white',
#     )
#     wc.generate_from_text(string)
#
#     #图片生成
#     fig = plt.figure(1)
#     plt.imshow(wc)
#     plt.axis('off')
#     plt.savefig(resImagSrc, dpi=800, bbox_inches='tight', pad_inches=-0.1)
# print(111)
# get_img('static/static/images/cloudImg/love.png', 'static/static/images/titleCloud')



def get_img_work_tag(targetImageSrc, resImagSrc):
    data = query_hive('select workTag from jobData', [], 'select')
    text = ''
    for i in data:
        if i[0] != '':
            tarArr = i
            for j in tarArr:
                try:
                    text += j
                except:
                    continue
    data_cut = jieba.cut(text, cut_all=False)
    string = ' '.join(data_cut)

    #词云图
    img = Image.open(targetImageSrc)
    img_arr = np.array(img)
    wc = WordCloud(
        font_path='STHUPO.TTF',
        mask = img_arr,
        background_color='white',
    )
    wc.generate_from_text(string)

    #图片生成
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig(resImagSrc, dpi=800, bbox_inches='tight', pad_inches=-0.1)
print(111)
get_img_work_tag('static/static/images/cloudImg/tree.png', 'static/static/images/tagCloud')