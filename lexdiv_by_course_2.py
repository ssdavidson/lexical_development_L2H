import csv, io, nltk
from collections import defaultdict
from matplotlib import pyplot
import lexical_diversity as lexdiv
import string

essays = list()
essays_famous = list()
essays_vacation = list()

mltd_dict = defaultdict()

with io.open('CORPUS_050718.csv', encoding = 'utf-8') as wb:
  csvreader = csv.reader(wb)
  for row in csvreader:
    if (row[16] != '' and row[16] != "S18_Famous"):
      if (row[3] != ''):
        text = nltk.word_tokenize(row[16])
        if len(text) >= 50:
          essays.append((int(row[3][4:]), lexdiv.mtld(text)))
          essays_famous.append((int(row[3][4:]), lexdiv.mtld(text)))
    if (row[30] != '' and row[30] != "W18_Famous"):
      if (row[17] != ''):
        text = nltk.word_tokenize(row[30])
        if len(text) >= 50:
          essays.append((int(row[17][4:]), lexdiv.mtld(text)))
          essays_famous.append((int(row[17][4:]), lexdiv.mtld(text)))
    if (row[31] != '' and row[31] != "W18_Vacation"):
      if (row[17] != ''):
        text = nltk.word_tokenize(row[31])
        if len(text) >= 50:
          essays.append((int(row[17][4:]), lexdiv.mtld(text)))
          essays_vacation.append((int(row[17][4:]), lexdiv.mtld(text)))
    if (row[46] != '' and row[46] != "F17_Famous"):
      if (row[32] != ''):
        text = nltk.word_tokenize(row[46])
        if len(text) >= 50:
          essays.append((int(row[32][4:]), lexdiv.mtld(text)))
          essays_famous.append((int(row[32][4:]), lexdiv.mtld(text)))
    if (row[47] != '' and row[47] != "F17_Vacation"):
      if (row[32] != ''):
        text = nltk.word_tokenize(row[47])
        if len(text) >= 50:
          essays.append((int(row[32][4:]), lexdiv.mtld(text)))
          essays_vacation.append((int(row[32][4:]), lexdiv.mtld(text)))
    if (row[60] != '' and row[60] != "S17_Famous"):
      if (row[48] != ''):
        text = nltk.word_tokenize(row[60])
        if len(text) >= 50:
          essays.append((int(row[48][4:]), lexdiv.mtld(text)))
          essays_famous.append((int(row[48][4:]), lexdiv.mtld(text)))
    if (row[61] != '' and row[61] != "S17_Vacation"):
      if (row[48] != ''):
        text = nltk.word_tokenize(row[61])
        if len(text) >= 50:
          essays.append((int(row[48][4:]), lexdiv.mtld(text)))
          essays_vacation.append((int(row[48][4:]), lexdiv.mtld(text)))
    if (row[76] != '' and row[76] != "SU17_Famous"):
      if (row[62] != ''):
        text = nltk.word_tokenize(row[76])
        if len(text) >= 50:
          essays.append((int(row[62][4:]), lexdiv.mtld(text)))
          essays_famous.append((int(row[62][4:]), lexdiv.mtld(text)))
    if (row[77] != '' and row[77] != "SU17_Vacation"):
      if (row[62] != ''):
        text = nltk.word_tokenize(row[77])
        if len(text) >= 50:
          essays.append((int(row[62][4:]), lexdiv.mtld(text)))
          essays_vacation.append((int(row[62][4:]), lexdiv.mtld(text)))

totals = defaultdict()
list_by_course = defaultdict()
totals_famous = defaultdict()
totals_vacation = defaultdict()
class_count = defaultdict()
class_count_famous = defaultdict()
class_count_vacation = defaultdict()

for essay in essays:
  if(essay[0] not in totals):
    if essay[1] > 0:
      list_by_course[essay[0]] = []
      list_by_course[essay[0]].append(essay[1])
      totals[essay[0]] = essay[1]
  else:
    if essay[1] > 0:
      totals[essay[0]] += essay[1]
      list_by_course[essay[0]].append(essay[1])
  if (essay[0] not in class_count):
    if essay[1] > 0:
      class_count[essay[0]] = 1
  else:
    if essay[1] > 0:
      class_count[essay[0]] += 1

for essay in essays_famous:
  if(essay[0] not in totals_famous):
    if essay[1] > 0:
      totals_famous[essay[0]] = essay[1]
  else:
    if essay[1] > 0:
      totals_famous[essay[0]] += essay[1]
  if (essay[0] not in class_count_famous):
    if essay[1] > 0:
      class_count_famous[essay[0]] = 1
  else:
    if essay[1] > 0:
      class_count_famous[essay[0]] += 1

for essay in essays_vacation:
  if(essay[0] not in totals_vacation):
    if essay[1] > 0:
      totals_vacation[essay[0]] = essay[1]
  else:
    if essay[1] > 0:
      totals_vacation[essay[0]] += essay[1]
  if (essay[0] not in class_count_vacation):
    if essay[1] > 0:
      class_count_vacation[essay[0]] = 1
  else:
    if essay[1] > 0:
      class_count_vacation[essay[0]] += 1

SPA1 = totals[1]/class_count[1]
SPA2 = totals[2]/class_count[2]
SPA3 = totals[3]/class_count[3]
SPA21 = totals[21]/class_count[21]
SPA22 = totals[22]/class_count[22]
SPA23 = totals[23]/class_count[23]
SPA24 = totals[24]/class_count[24]
SPA31 = totals[31]/class_count[31]
SPA32 = totals[32]/class_count[32]
SPA33 = totals[33]/class_count[33]

SPA1_famous = totals_famous[1]/class_count_famous[1]
SPA2_famous = totals_famous[2]/class_count_famous[2]
SPA3_famous = totals_famous[3]/class_count_famous[3]
SPA21_famous = totals_famous[21]/class_count_famous[21]
SPA22_famous = totals_famous[22]/class_count_famous[22]
SPA23_famous = totals_famous[23]/class_count_famous[23]
SPA24_famous = totals_famous[24]/class_count_famous[24]
SPA31_famous = totals_famous[31]/class_count_famous[31]
SPA32_famous = totals_famous[32]/class_count_famous[32]
SPA33_famous = totals_famous[33]/class_count_famous[33]

SPA1_vacation = totals_vacation[1]/class_count_vacation[1]
SPA2_vacation = totals_vacation[2]/class_count_vacation[2]
SPA3_vacation = totals_vacation[3]/class_count_vacation[3]
SPA21_vacation = totals_vacation[21]/class_count_vacation[21]
SPA22_vacation = totals_vacation[22]/class_count_vacation[22]
SPA23_vacation = totals_vacation[23]/class_count_vacation[23]
SPA24_vacation = totals_vacation[24]/class_count_vacation[24]
SPA31_vacation = totals_vacation[31]/class_count_vacation[31]
SPA32_vacation = totals_vacation[32]/class_count_vacation[32]
SPA33_vacation = totals_vacation[33]/class_count_vacation[33]

print("SPA1 Avg lexdiv: " + str(SPA1))
print("SPA2 Avg lexdiv: " + str(SPA2))
print("SPA3 Avg lexdiv: " + str(SPA3))
print("SPA21 Avg lexdiv: " + str(SPA21))
print("SPA22 Avg lexdiv: " + str(SPA22))
print("SPA23 Avg lexdiv: " + str(SPA23))
print("SPA24 Avg lexdiv: " + str(SPA24))
print("SPA31 Avg lexdiv: " + str(SPA31))
print("SPA32 Avg lexdiv: " + str(SPA32))
print("SPA33 Avg lexdiv: " + str(SPA33))

print()

print("SPA1_famous lexdiv: " + str(SPA1_famous))
print("SPA2_famous lexdiv: " + str(SPA2_famous))
print("SPA3_famous Avg lexdiv: " + str(SPA3_famous))
print("SPA21_famous Avg lexdiv: " + str(SPA21_famous))
print("SPA22_famous Avg lexdiv: " + str(SPA22_famous))
print("SPA23_famous Avg lexdiv: " + str(SPA23_famous))
print("SPA24_famous Avg lexdiv: " + str(SPA24_famous))
print("SPA31_famous Avg lexdiv: " + str(SPA31_famous))
print("SPA32_famous Avg lexdiv: " + str(SPA32_famous))
print("SPA33_famous Avg lexdiv: " + str(SPA33_famous))

print()

print("SPA1_vacation Avg lexdiv: " + str(SPA1_vacation))
print("SPA2_vacation Avg lexdiv: " + str(SPA2_vacation))
print("SPA3_vacation Avg lexdiv: " + str(SPA3_vacation))
print("SPA21_vacation Avg lexdiv: " + str(SPA21_vacation))
print("SPA22_vacation Avg lexdiv: " + str(SPA22_vacation))
print("SPA23_vacation Avg lexdiv: " + str(SPA23_vacation))
print("SPA24_vacation Avg lexdiv: " + str(SPA24_vacation))
print("SPA31_vacation Avg lexdiv: " + str(SPA31_vacation))
print("SPA32_vacation Avg lexdiv: " + str(SPA32_vacation))
print("SPA33_vacation Avg lexdiv: " + str(SPA33_vacation))

x = list()
y = list()

# for essay in essays:
#   x.append(essay[0])
#   y.append(essay[1])

x = [SPA1, SPA2, SPA3, SPA21, SPA22, SPA23,SPA24]
y = ["SPA1", "SPA2", "SPA3", "SPA21", "SPA22", "SPA23","SPA24"]
w = [SPA31, SPA32, SPA33]
z = ["SPA31", "SPA32", "SPA33"]

a = [SPA1_famous, SPA2_famous, SPA3_famous, SPA21_famous, SPA22_famous, SPA23_famous, SPA24_famous]
b = [SPA1_vacation, SPA2_vacation, SPA3_vacation, SPA21_vacation, SPA22_vacation, SPA23_vacation, SPA24_vacation]
c = [SPA31_famous, SPA32_famous, SPA33_famous]
d = [SPA31_vacation, SPA32_vacation, SPA33_vacation]

#pyplot.title("Lexical Diversity by Prompt")
pyplot.title("Lexical Diversity")
pyplot.ylabel("MTLD Score")
pyplot.xlabel("Course Number")
pyplot.plot(y, x, 'bo-', label = "L2 students") #this is a scatterplat, using green(g) triangles(^)
pyplot.plot(z, w, 'r+-', label = "Heritage students")
# pyplot.plot(y, a, 'go-', label = "Famous prompt") #this is a scatterplat, using green(g) triangles(^)
# pyplot.plot(y, b, 'm+-', label = "Vacation prompt")
# pyplot.plot(z, c, 'go-')
# pyplot.plot(z, d, 'm+-')
pyplot.legend()
pyplot.show() #display graph


max_len = max(len(list_by_course[24]), len(list_by_course[31]))
new_list = []
other_list = []
swap = False

if len(list_by_course[24]) < max_len:
    for i in range(max_len - len(list_by_course[24])):
        new_list = list_by_course[24].copy()
        new_list.append("NA")
        other_list = list_by_course[31].copy()

elif len(list_by_course[31]) < max_len:
    for i in range(max_len - len(list_by_course[31])):
        new_list = list_by_course[31].copy()
        new_list.append("NA")
        other_list = list_by_course[24].copy()
        swap = True

with open('lex_div_diff.csv', 'w') as csvfile:
  csvfile.write("SPA24,SPA31\n")
  if not(swap):
    for item1, item2 in zip(new_list, other_list):
      data = str(item1) + "," + str(item2) + '\n'
      csvfile.write(data)
  else:
    for item1, item2 in zip(other_list, new_list):
      data = str(item1) + "," + str(item2) + '\n'
      csvfile.write(data)
