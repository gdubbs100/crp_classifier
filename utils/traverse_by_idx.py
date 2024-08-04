def traverse_by_idx(list_to_do):
    output = []
    for i in list_to_do:
        tmp = list_to_do[i]
        while tmp != list_to_do[tmp]:
            tmp = list_to_do[tmp]
        output.append(tmp)
    return output

if __name__=="__main__":
    x = [0,1,0,1,2,3,3,0,5,5,5, 9]
    output = []
    expected = [0,1,0,1,0,1,1,0, 1,1,1, 1]

    for i in x:
        print(i)
        tmp = x[i]
        print('tmp:',tmp)
        while tmp != x[tmp]:
            tmp = x[tmp]
            print('TMP:', tmp)
        output.append(tmp)
    
    print(x)
    print(output)
    print(expected)
