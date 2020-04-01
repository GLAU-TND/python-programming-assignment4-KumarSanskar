def function(nestedDict, Dic, currKey):
    for key in nestedDict.keys():
        if type(nestedDict[key]) == int:
            Dic[(currKey+"."+key).strip(".")] = nestedDict[key]
        else:
            Dic = function(nestedDict[key], Dic, (currKey+"."+key).strip('.'))

    return Dic

def func_dic(nestedDic):
    return function(nestedDic, dict(), "")

def main():
    nestDictionary = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }

    dicten = func_dic(nestDictionary)
    print(dicten)

if __name__ == "__main__":
    main()
