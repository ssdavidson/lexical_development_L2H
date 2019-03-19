#Copyright 2019 Sam Davidson
#
#Script to calculate lexical density in COWS-L2H corpus of learner Spanish.
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import io, nltk, pickle
from collections import defaultdict
from matplotlib import pyplot

essay_famous = pickle.load(open("essays_famous_tagged_spr18.pickle", "rb"))
essay_vacation = pickle.load(open("essays_vacation_tagged_spr18.pickle", "rb"))
essay_list = essay_famous + essay_vacation

verbs = defaultdict()
nouns = defaultdict()
adverbs = defaultdict()
adjectives = defaultdict()
total_words = defaultdict()
count = defaultdict()

def get_ratio(essay):
  verb_list = list()
  noun_list = list()
  for word_tuple in essay:
    lemma = word_tuple[0]
    tag = word_tuple[2]
    if tag[0] == "V" and lemma not in verb_list:
      verb_list.append(lemma)
    elif tag[0] == "N" and lemma not in noun_list:
      noun_list.append(lemma)
  return len(noun_list)/len(verb_list)

lex_density_list = {1:[],2:[],3:[],21:[],22:[],23:[],24:[],31:[],32:[],33:[],0:[]}

for essay in essay_list:
  temp_lex = 0
  temp_tot = 0
  class_num = essay[0]
  if class_num not in count:
    count[class_num] = 0
  count[class_num] += 1
  word_tups = essay[1]
  for word_tup in word_tups:
    temp_tot += 1
    if class_num not in total_words:
      total_words[class_num] = 0
    total_words[class_num] += 1
    if word_tup[2][0] == "V":
      if class_num not in verbs:
        verbs[class_num] = 0
      verbs[class_num] += 1
      temp_lex += 1
    elif word_tup[2][0] == "N":
      if class_num not in nouns:
        nouns[class_num] = 0
      nouns[class_num] += 1
      temp_lex += 1
    elif word_tup[2][0] == "A":
      if class_num not in adjectives:
        adjectives[class_num] = 0
      adjectives[class_num] += 1
      temp_lex += 1
    elif word_tup[2][0] == "R":
      if class_num not in adverbs:
        adverbs[class_num] = 0
      adverbs[class_num] += 1
      temp_lex += 1
  lex_dens = temp_lex/temp_tot
  lex_density_list[class_num].append(lex_dens)


SPA1 = (verbs[1] + nouns[1] + adjectives[1] + adverbs[1])/total_words[1]
SPA2 = (verbs[2] + nouns[2] + adjectives[2] + adverbs[2])/total_words[2]
SPA3 = (verbs[3] + nouns[3] + adjectives[3] + adverbs[3])/total_words[3]
SPA21 = (verbs[21] + nouns[21] + adjectives[21] + adverbs[21])/total_words[21]
SPA22 = (verbs[22] + nouns[22] + adjectives[22] + adverbs[22])/total_words[22]
SPA23 = (verbs[23] + nouns[23] + adjectives[23] + adverbs[23])/total_words[23]
SPA24 = (verbs[24] + nouns[24] + adjectives[24] + adverbs[24])/total_words[24]
SPA31 = (verbs[31] + nouns[31] + adjectives[31] + adverbs[31])/total_words[31]
SPA32 = (verbs[32] + nouns[32] + adjectives[32] + adverbs[32])/total_words[32]
SPA33 = (verbs[33] + nouns[33] + adjectives[33] + adverbs[33])/total_words[33]

x = [SPA1, SPA2, SPA3, SPA21, SPA22, SPA23, SPA24]
y = ["SPA1", "SPA2", "SPA3", "SPA21", "SPA22", "SPA23", "SPA24"]
w = [SPA31, SPA32, SPA33]
z = ["SPA31", "SPA32", "SPA33"]

for a,b in zip(x,y):
    print(b + ": " + str(a))

for a,b in zip(w,z):
    print(b + ": " + str(a))

#a = [SPA1_famous, SPA2_famous, SPA3_famous, SPA21_famous, SPA22_famous, SPA23_famous]
#b = [SPA1_vacation, SPA2_vacation, SPA3_vacation, SPA21_vacation, SPA22_vacation, SPA23_vacation]
#c = [SPA31_famous, SPA32_famous, SPA33_famous]
#d = [SPA31_vacation, SPA32_vacation, SPA33_vacation]

pyplot.title("Lexical Density by Course")
pyplot.ylabel("Lexical Density")
pyplot.xlabel("Course Number")
#pyplot.plot(y, x, 'bo-') #this is a scatterplat, using green(g) triangles(^)
#pyplot.plot(z, w, 'r+-')
pyplot.plot(y, x, 'bo-') #this is a scatterplat, using green(g) triangles(^)
#pyplot.plot(y, b, 'r+-', label = "Vacation prompt")
#pyplot.plot(z, c, 'bo-')
pyplot.plot(z, w, 'r+-')
pyplot.legend()
pyplot.show() #display graph


max_len = max(len(lex_density_list[24]), len(lex_density_list[31]))
new_list = []
other_list = []
swap = False


if len(lex_density_list[24]) < max_len:
    for i in range(max_len - len(lex_density_list[24])):
        new_list = lex_density_list[24].copy()
        new_list.append("NA")
        other_list = lex_density_list[31].copy()

elif len(lex_density_list[31]) < max_len:
    for i in range(max_len - len(lex_density_list[31])):
        new_list = lex_density_list[31].copy()
        new_list.append("NA")
        other_list = lex_density_list[24].copy()
        swap = True

with open('lex_density_diff.csv', 'w') as csvfile:
  csvfile.write("SPA24,SPA31\n")
  if not(swap):
    for item1, item2 in zip(new_list, other_list):
      data = str(item1) + "," + str(item2) + '\n'
      csvfile.write(data)
  else:
    for item1, item2 in zip(other_list, new_list):
      data = str(item1) + "," + str(item2) + '\n'
      csvfile.write(data)
