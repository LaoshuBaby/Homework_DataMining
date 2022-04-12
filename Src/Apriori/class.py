class Itemset:
    # contain 3 parts:
    # 1. data: list of items
    # 2. sup: support of itemset
    # 3. count: number of transactions contain itemset
    def __init__(self, data, sup, count):
        self.data = data
        self.sup = sup
        self.count = count

    def __str__(self):
        return str(self.data) + ' ' + str(self.sup) + ' ' + str(self.count)