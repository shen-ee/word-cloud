# coding:utf-8
import thulac	
# 
# 

def read_txt(input_filename):
    str = ""
    with open(input_filename,'r') as raw_text:
        for line in raw_text:
            # print(line)
            str+=line
    return str

def tokenize(input_filename):
    thu1 = thulac.thulac(seg_only=True)  #默认模式
    str = read_txt(input_filename)
    text = thu1.cut(str, text=True)  #进行一句话分词

    # print(text)
    return text


if __name__ == "__main__":
    input = "raw.txt"
    output = "output.txt"
    text = tokenize(input)
    with open(output,'w') as output_txt:
        output_txt.write(text)
    print(text)
