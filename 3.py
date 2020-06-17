import string
import operator


with open('text.txt', mode = 'rt', encoding = 'utf-8') as f:
    text = f.read()
print('Длинна исходного текста = ', len(text))
punctuation = string.punctuation

punctuation = punctuation.replace('-','')
print('Список символов пунктуации ', punctuation)
#добавим отсутствующие в преобразованый список
list_punk = list(punctuation)
list_punk.append('»')
list_punk.append('«')
list_punk.append('—')

for i in list_punk:
    text = text.replace(i,'')
print('Длинна текста без знаков пунктуации = ', len(text))

#2) сформировать list со словами (split);
list_words = text.split()
print(list_words)

#3) привести все слова к нижнему регистру (map)
list_words = list(map(lambda x: x.lower(),list_words))
print(list_words)
#3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
# нужно множество
words = set(list_words)
words_dic = {}
for i in words:
    words_dic.update({i:list_words.count(i)})
print(words_dic)

#№4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
small_sort = sorted(words_dic.items(), key=operator.itemgetter(1), reverse = True)
print(small_sort[:5])

#5) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
norm_list_word2 = [morph.parse(i)[0].normal_form for i in list_words]
words = set(norm_list_word2)
words_dic2 = {}
for i in words:
    words_dic2.update({i:norm_list_word2.count(i)})
small_sort2 = sorted(words_dic2.items(), key=operator.itemgetter(1), reverse = True)
print(small_sort2[:5])
