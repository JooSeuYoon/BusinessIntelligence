from bs4 import BeautifulSoup
import os
from konlpy.tag import Okt
import operator

JVM_PATH = '/Library/Java/JavaVirtualMachines/zulu-19.jdk/Contents/Home/bin/java'
okt = Okt(JVM_PATH)


def getReview():
   with open(os.path.dirname(os.path.abspath(__file__)) + "/TheGreatGatsby_review.html") as fp:
      soup = BeautifulSoup(fp, 'html.parser')

   review_list = soup.find_all('div',{"class":"css-1g78l7j"})


   review_text = open("review_text.txt", "w")

   for one in review_list:
      review_text.write(one.getText())

def splitWord():
   review = open(os.path.dirname(os.path.abspath(__file__)) + "/review_text.txt", "r")
   stopwords = open(os.path.dirname(os.path.abspath(__file__)) + "/stopwords.txt", "r").readline().split(" ")
   result = open(os.path.dirname(os.path.abspath(__file__)) + "/result.txt", "w")

   words = {}

   for line in review.readlines():   
      for user_word in okt.nouns(line):
         if (user_word not in stopwords) and user_word != "":
            if user_word in words:
               words[user_word] += 1
            else:
               words[user_word] = 1

   words = dict(sorted(words.items(), key=lambda item: item[1]))

   for one_word in words:
      result.write(one_word + " : " + str(words[one_word]) + "\n")

   result.close()

splitWord()