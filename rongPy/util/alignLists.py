# -*- coding: utf-8 -*- 
#字体选择幼圆

punc = "！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."

def alignLst(lists):
    r_lists = []    
    max_lens = [lenWithCH(str(max(c, key = lambda x : lenWithCH(str(x))))) for c in zip(*lists)]
    
    #print(max_lens)
    
    for row in lists:
    #    r_lists.append('|'.join('{0:{width}}'.format(x, width = y) for x, y in zip(row, max_lens)))
        str_temp = ''
        for x, y in zip(row, max_lens):
            num = numOfCH(x)
            str_temp = str_temp + '|' + '{0:{width}}'.format(x, width = y - num)
        r_lists.append(str_temp)
        
    #for line in r_lists:
    #    print(line)
       
    return r_lists

def numOfCH(str_temp):
    i = 0
    for ch in str_temp:
        if u'\u4e00' <= ch <= u'\u9fff' or ch in punc:
            i += 1
    return i

def lenWithCH(str_temp):
    i = len(str_temp) + numOfCH(str_temp)
    return i

'''   
l1 = ["中文","level","value"]
l2 = ["Some long name", "这是一串很长的中文", "a value"]
l3 = ["An even longer name", "another level", "another value"]

lsts = []

lsts.append(l1)
lsts.append(l2)
lsts.append(l3)

print(numOfCH("中文"))
print(lenWithCH("test中文"))

for line in alignLst(lsts):
    print(line)
'''
