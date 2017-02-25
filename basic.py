# python 3

def run():
    print("hello")


ch_str = "Python 数据分析"


def test_encoding():
    print(ch_str)
    print(type(ch_str))
    b_str = ch_str.encode('utf-8')
    print(b_str)
    print(b_str.decode('utf-8'))


def test_format():
    print("{} {}".format("Hello", "world"))
    print("{0} {1} {0}".format("Hello", "world"))
    print("{name}, {year}".format(name="zhenglai", year=2017))


def test_dict():
    d = {"name": "zhenglai", "year": 2014}
    print(d)
    print(type(d.keys()))
    print(d.keys())
    print(type(d.values()))
    print(d.values() )
    for k, v in d.items():
        print("{} => {}".format(k, v))

if __name__ == "__main__":
    test_dict()
