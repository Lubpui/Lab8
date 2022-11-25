class hoare:
    def __init__(self,listVal):
        self.hoareList = listVal
        self.pivot = 0

    def calculate(self):

        i = 0
        j = len(self.hoareList) - 1

        while i != j:
            while self.hoareList[i] <= self.hoareList[self.pivot]:
                i += 1
            while self.hoareList[j] >= self.hoareList[self.pivot]:
                if j == self.pivot:
                    break
                j -= 1

            print(self.hoareList)
            self.hoareList[i],self.hoareList[j] = self.hoareList[j],self.hoareList[i]
            print(self.hoareList)

            if i > j:
                self.hoareList[i], self.hoareList[j] = self.hoareList[j], self.hoareList[i]
                print(self.hoareList)
                self.hoareList[self.pivot], self.hoareList[j] = self.hoareList[j], self.hoareList[self.pivot]
                i = 0
                j = len(self.hoareList) - 1

            print(self.hoareList)


listVal = [29,10,14,37,14,20,7,16,12]
print(listVal)
h = hoare(listVal)
h.calculate()