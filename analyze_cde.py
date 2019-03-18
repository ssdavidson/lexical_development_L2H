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
