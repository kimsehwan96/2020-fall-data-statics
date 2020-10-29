
#재미삼아 만들어보는 통계 라이브러리 ~~!! 시험기건은 즐거웡 ㅎㅎ.
def mean(data):
    convert_value = None
    sum = 0
    for v in data:
        if (type(v) == int) or (type(v) == float):
            pass
        else:
            if type(v) == str:
                try:
                    convert_value = int(v)
                except ValueError:
                    try:
                        convert_value = float(v)
                    except Exception as e:
                        print("error occured", e)
            else:
                raise TypeError
        if convert_value:
            sum += convert_value
        else:        
            sum += v
    result = sum / len(data)
    return result
    #흠...try except을 분기처리에 쓰는건 좋지 않다구 하는뎅...
    #str을 정수 혹은 실수로 바꿀지 어떻게 판단하면 좋을까 ?_?

if __name__=="__main__":
    a = ['60.3', 30.2, 3253.3, 3, 2, 1]
    b = ['1', '5', '7', '9', '123']

    print(mean(a))
    print(mean(b))