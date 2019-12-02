import yaml


def read_yaml(filename):
    with open("./data/" + filename, "r", encoding="utf-8") as f:
        arr = []
        for data in yaml.load(f).values():
            arr.append(tuple(data.values()))
        return arr


if __name__ == '__main__':
    print(read_yaml("test01.yaml"))
    print("--" * 50)
    """需求：[[]] [(),()]"""
    # arr = []
    # for data in read_yaml("mp_login.yaml").values():
    #     arr.append(tuple(data.values()))
    # print(ar)r
