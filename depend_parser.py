#coding:utf-8

from pyhanlp import *

class HanlpParser():
    def __init__(self,
                 dict_path:str = None):
        if dict_path:
            self.load_dict(dict_path)



    def load_dict(self, path:str):
        '''
        load Dictionary
        :param path:
        :return:
        '''
        CustomDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
        with open(path, "r") as fin:
            lines = fin.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    CustomDictionary.add(line)

    def parser(self, sentence:str):
        parser_sentence = HanLP.parseDependency(sentence)
        print(parser_sentence)
        lis = []
        for word in parser_sentence.iterator():  # 通过dir()可以查看sentence的方法
            print(type(word))
            dic = {
                "LEMMA": word.LEMMA,
                "DEPREL": word.DEPREL,
                "POSTAG": word.POSTAG,
                "HEAD": word.HEAD.LEMMA
            }
            print(dic)

if __name__ == '__main__':
    sentence = "为加强健康医疗大数据服务管理"
    sentence = "在已有的基础性通用性大数据体系基础上组织制定健康医疗大数据标准体系规划"

    hanlp = HanlpParser()
    hanlp.parser(sentence)




    pass




