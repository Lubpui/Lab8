class merge:
    def __init__(self,):
        self.mergeList = []

    def calculate(self,listVal):

        def cal(mid):
            listLeft = listVal[:mid]
            listRight = listVal[mid:]

            listRight.sort()
            listLeft.sort()

            i = 0
            j = 0

            while True:
                if len(listLeft) < i and len(listRight) < j:
                    break
                elif len(listLeft) == i and len(listRight) > j:
                    self.mergeList.append(listRight[j])
                    j += 1
                    break
                elif len(listLeft) > i and len(listRight) == j:
                    self.mergeList.append(listLeft[i])
                    i += 1
                    break

                if listLeft[i] > listRight[j]:
                    self.mergeList.append(listRight[j])
                    j += 1
                else:
                    self.mergeList.append(listLeft[i])
                    i += 1
            print(self.mergeList)

        rangeList = len(listVal)

        if rangeList % 2 == 1:
            mid = int(rangeList / 2) + 1
            cal(mid)
        else:
            mid = int(rangeList / 2)
            cal(mid)

listVal = [29,10,14,37,14,20,7,16,12]
m = merge()
m.calculate(listVal)