import random
def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    #assert(alist)
    return alist
    
"""
print a generate_list
"""

def printIt():
    print(generate_list())


def main():
    printIt()
    
"""
if this script flie is called, it will run main() directly
"""

if __name__=='__main__' :
    
    print("Test printIt() :")
    main()


