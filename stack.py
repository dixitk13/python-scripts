class MinStack:
    #stack1 = []
    def __init__(self):
        self.stack2 = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack2.append(x)

    # @return nothing
    def pop(self):
        self.stack2.pop()

    # @return an integer
    def top(self):
        self.stack2.pop()

    # @return an integer
    def getMin(self):
        return self.stack2.sort().reverse().pop()

    def __iter__(self):
        return iter(self.stack2)

if __name__ == '__main__':
    s = MinStack()
    print("->",isinstance(s,MinStack))
    #print(s.push(1))
    # s.push(1)
    # print(s)
    # print(s.pop())
    # print(s)
    # test = []
    # test.append(1)
    # print(test.pop())
    test = ["test1","test2","tset3","test4"]
    print(test)
    test.extend(["test5","test6"])
    print(test)
    test.insert(3, 66)
    test.insert(3, 'fs"d"sa""d')
    print(test)
    supportingactors = ["support1","support2"]
    cast1  = ["cast1,cast2",supportingactors]

    mov = ["movie1",cast1]
    print(mov)
    print('fullitem',cast1)

    def fun1(item,inv):
        #inv = 0
        for items in item:
            if isinstance(items,list):
                inv+=1
                fun1(items,inv)
            else:
                #print('"{:>", inv, "}"'.format(items))
                """blank"""
                print(items)
                #        print("{:>5}\tQ0\t{:>5}\t{:>5}\t{:>20}\t{:>10}".format(query_id, x[0], rank, x[1], system_name))





    print("===")
    fun1(mov,0)



else:
    print("exit no main")#s.stack1
