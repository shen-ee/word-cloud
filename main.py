# coding:utf-8
import thulac	
input = "raw.txt"
output = "output.txt"

def read_text(filename):
    str = ""
    with open(filename,'r') as raw_text:
        for line in raw_text:
            # print(line)
            str+=line
    return str

thu1 = thulac.thulac(seg_only=True)  #默认模式
str = read_text(input)
text = thu1.cut(str, text=True)  #进行一句话分词

with open(output,'w') as output_txt:
    output_txt.write(text)

print(text)