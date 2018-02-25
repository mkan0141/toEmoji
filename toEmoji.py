from gensim.models import word2vec
import MeCab
import numpy as np
import json
import time

File = open('emoji.json', 'r')
emoji_data = json.load(File)
print('load model file')
model = word2vec.Word2Vec.load("./wiki.model")
print('completed')

def calc_similarity_number(word):
    ret = 0
    max_simil = 0
    for i in range(107):
        for j in range(2):
            tmp = model.wv.similarity(word, emoji_data[str(i)]['mean'][str(j)])
            if max_simil < tmp:
                max_simil = tmp
                ret = i
    return emoji_data[str(ret)]['emoji']

i

"""
形態素解析をして名詞、形容詞、
副詞の3つを抽出する    
"""
def create(doc):
    tagger = MeCab.Tagger('-Ochasen')
    tagger.parse('')
    result = tagger.parseToNode(doc)

    word_class = []
    while result:
        word = result.surface
        clazz = result.feature.split(',')[0]
        """print(word + " " + clazz)"""
        if clazz != 'BOS/EOS' and (clazz == '名詞' or clazz == '形容詞' or clazz == "動詞"):
            word_class.append((word, clazz))
        result = result.next
        
    return word_class


def main():
    while True:
        text = input()
        if text == "END":
            break
        words = create(text)
        emoji = ""
        for word in words:
            emoji += (calc_similarity_number(word[0])) + "  "
    
        print(emoji)

if __name__ == '__main__':
    main()


