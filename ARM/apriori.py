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

   lines = file.readlines()

   for l in lines:
      setList.append(set(l.strip().split(" ")))
      for one in l.strip().split(" "):
         if one not in itemList:
            itemList.append(one)
   
   return setList, itemList



# main function
def main():
   file_name = ""

   if len(sys.argv) != 2:
      print("Entering no transaction file or too many transaction files.\n"
      + "Show the result by using transaction1.txt file.")
      file_name = "transactions1.txt"
   else :
      file_name = sys.argv[1]

   setList, itemList = readFileMakeT(file_name)






if __name__ == "__main__":
	main()
