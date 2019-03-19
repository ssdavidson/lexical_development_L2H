
    
#Copyright 2019 Sam Davidson
#
#Script to calculate lexical density, type-token ratio, and MTLD values for sample of Corpus del Espanol.
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import io
import lexical_diversity as lexdiv
from statistics import mean
import string

infile = io.open("wordLemPoS.txt",  encoding='latin-1')

essay_types = []
essay_toks = []

essay_lexical = []
essay_ttr = []
essay_mtld = []

temp_types = []
temp_essay = ""
temp_types_tot = 0
temp_toks = 0
temp_lex = 0

for line in infile:
  split = line.split('\t')
  if "@@" not in split[2][:2]:

    word = split[2]
    lemma = split[3]
    tag = split[4]

    if "@" not in word and word not in string.punctuation:
      temp_essay += (word + ' ')
      temp_toks += 1
    if lemma not in temp_types and lemma not in string.punctuation:
      temp_types.append(lemma)
      temp_types_tot += 1
    if 'o' in tag[0] or 'n' in tag[0] or 'v' in tag[0] or 'j' in tag[0] or 'r' in tag[0]:
      temp_lex += 1

  if "@@" in split[2][:2]:
    if temp_toks != 0:
    #  print(temp_essay)
      ttr = len(temp_types)/temp_toks
      essay_ttr.append(ttr)

      lex_density = temp_lex/temp_toks
      essay_lexical.append(lex_density)

      if len(temp_essay.split()) >= 50:
        lex_diversity = lexdiv.mtld(temp_essay.split())
        essay_mtld.append(lex_diversity)
      else:
        essay_mtld.append(0)

      temp_types = []
      temp_essay = ""
      temp_types_tot = 0
      temp_toks = 0
      temp_lex = 0

print(mean(essay_lexical))
print(mean(essay_mtld))
print(mean(essay_ttr))

csv_out = io.open("cde_lexdensity.csv", mode="w")
csv_out.write("CDE\n")
for essay in essay_lexical:
  csv_out.write(str(essay) + '\n')
