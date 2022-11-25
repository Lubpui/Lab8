class lomuto:
    def __init__(self,listVal):
        self.lomutoList = listVal
        self.pivot = len(listVal)-1

    def calculate(self):
        l = len(self.lomutoList)
        if self.pivot < 0:
            return 0

        if self.lomutoList[0] >= self.lomutoList[self.pivot]:
            self.lomutoList[0],self.lomutoList[self.pivot] = self.lomutoList[self.pivot],self.lomutoList[0]

        print(self.lomutoList[self.pivot])
        print(self.lomutoList)

        for i in range(self.pivot):
            if self.lomutoList[self.pivot] <= self.lomutoList[i]:
                self.lomutoList[i], self.lomutoList[i+1] = self.lomutoList[i+1], self.lomutoList[i]
        self.pivot -= 1
        print(self.lomutoList)
        lomuto.calculate(self)

listVal = [29,10,14,37,14,20,7,16,12]
l = lomuto(listVal)
l.calculate()