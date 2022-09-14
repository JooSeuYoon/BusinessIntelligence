import sys

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

   file = open(file_name, "r")
   #exception needed

   lines = file.readlines()

   for l in lines:
      setList.append(set(l.strip().split(" ")))
      for one in l.strip().split(" "):
         if one not in itemList:
            itemList.append(one)
   
   return setList, itemList


# make frequent itemsets
# 빈번항목집합을 만들어준다.
# return : frequentItemsets : list
def makeFrequentItemsets(setList : list, itemList : list, min_sup : int):
   
   nextsetList = []
   nextItemList = []

   for item in itemList :
      count = 0

      for set in setList :
         if (item - set) is False:
            count += 1
      
      if count > min_sup :
         nextItemList.append(item)
   
   if len(nextItemList) == 1:
      return nextItemList

   for i in range(len(nextItemList) - 1):
      for j in range(i, len(nextItemList)) : 
         newset = nextItemList[i] + nextItemList[j]
         if newset not in nextsetList:
            nextsetList.append(newset)
   



# main function
def main():
   file_name = ""
   min_sup = 0

   if len(sys.argv) != 3:
      print("Entering wrong arguments.\n"
      + "Show the result by using transaction1.txt file.\n"
      + "The minimum support count threshold set as 3.\n")
      file_name = "transactions1.txt"
      min_sup = 3
   else :
      file_name = sys.argv[1]
      min_sup = int(sys.argv[2])
      

   setList, itemList = readFileMakeT(file_name)

   




if __name__ == "__main__":
	main()
