import sys
import itertools

## Input
## D, a database of transactions (txt file)
## min_sup, the minimum support count threshold (최소지지도)

## Output
## L, frequent itemsets in D

# read transcations txt file and make it as set list, make it to item list
# 트랜잭션 텍스트 파일을 읽고 그것을 조합들의 리스트로 만듭니다. 또 아이템의 리스트를 추출해냅니다.
# return : setList: list , itemList: list
def readFileMakeT(file_name: str) : 

   setList = []
   itemList = []

   try:
      file = open(file_name, "r")
   except:
      print("File I/O Error occure. Please try again.")
   

   lines = file.readlines()

   for l in lines:
      setList.append(set(l.strip().split(" ")))
      for one in l.strip().split(" "):
         if set(one) not in itemList:
            itemList.append(set([one]))
   
   return setList, itemList


# pruning process execution
# pruning 작업을 진행합니다. 후보 집합의 하위집합이 이전 빈번항목집합에 없는 경우 false를 리턴, 모두 있는 경우 true를 리턴
# return : if new candidate's subsets are not in ex-sets, true, else false
def pruning(newSet : set, itemList : list):
   newSets = list(itertools.combinations(newSet, len(newSet) - 1))

   for e in newSets:
      if (len(e) == len(newSet) - 1):
         if set(e) not in itemList:
            return False

   return True


# make frequent itemsets
# 빈번항목집합을 만들어준다.
# return : frequentItemsets : list
def makeFrequentItemsets(setList : list, itemList : list, min_sup : int):

   nextsetList = []
   nextItemList = []
   maxitemList = []
   maxnum = 0

   for item in itemList :
      count = 0

      for set in setList :
         if not (item - set):
            count += 1

      if count >= min_sup :
         nextItemList.append(item)

      if maxnum < count:
         maxnum = count
         maxitemList = []
         if item not in maxitemList:
            maxitemList.append(item)
      elif maxnum == count:
         if item not in maxitemList:
            maxitemList.append(item)
         

   for i in range(len(nextItemList) - 1):
      for j in range(i, len(nextItemList)) : 
         newset = nextItemList[i] | nextItemList[j]

         if newset not in nextsetList and (len(newset) == len(nextItemList[0]) + 1) and (pruning(newset, nextItemList)):
            nextsetList.append(newset)
   
   if len(nextsetList) == 1:
      return nextsetList
   elif len(nextsetList) == 0:
      return maxitemList

   return makeFrequentItemsets(setList, nextsetList, min_sup)


# count frequency of sets in data transaction file
# 집합의 빈도수를 계산한다.
# return : count : integer
def countFrequence(setList, oneset):
   count = 0

   for set in setList:
      if not (oneset - set):
         count +=1

   return count

# main function
def main():
   file_name = ""
   min_sup = 0

   if len(sys.argv) != 3:
      print("Entering wrong arguments.\n"
      + "Show the result by using transaction1.txt file.\n"
      + "The minimum support count threshold set as 3.\n")
      file_name = "ARM/transactions2.txt"
      min_sup = 3
   else :
      file_name = sys.argv[1]
      min_sup = int(sys.argv[2])
      

   setList, itemList = readFileMakeT(file_name)

   resultSet = makeFrequentItemsets(setList, itemList, min_sup)

   for i in range(len(resultSet)):
      print(resultSet[i], end=" : ") 
      c = countFrequence(setList, resultSet[i])
      print(c, end=" times, ")
      print(str(int(c/len(setList)*100)) + "% frequent")



if __name__ == "__main__":
	main()
