d = {'a':['apple','apricot'],'b':'banana','c':{'d':'dog','e':'eggs','f':{'g':('guns','asd'), 'h':{'i':'test'}}}}

def getValue(d,a):
    for x,y in d.items():
        if type(d[x]) is dict:
            getValue(d[x],a)
        else:
            if type(y) is list:
                for i in y:
                    a.append(i)
            elif type(y) is tuple:
                for i in y:
                    a.append(i)
            else:
                a.append(y)
    return a

def getThis(d,key):
    a,b =[],[]
    for x,y in d.items():
        if x == key:
            if type(d[x]) is dict:
                return getValue(d[x],a)
            elif type(y) is tuple:
                for i in y:
                    b.append(i)
                return b
            else:
                return y
        if type(d[x]) is dict:
            return getThis(d[x],key)

def get(d, key):
    temp = getThis(d, key)
    if type(temp) is list:
        print(*temp)
    else:
        print(temp)

get(d,'f')
