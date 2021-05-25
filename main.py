import json


def clean_ori():
    f = open('state_city_ori.json')
    data = json.load(f)

    for state in data:
        del state["id"]
        del state["lat"]
        del state["long"]
        del state["isIn"]
        for city in state["cities"]:
            del city["id"]
            del city["lat"]
            del city["long"]
            del city["isIn"]

    f.close()

    with open('state_city_v1.json', 'w') as f:
        json.dump(data, f, indent=2)


def clean_v1():
    f = open('state_city_v1.json')
    data = json.load(f)

    data = clean_empty(data)

    # for state in data:
    #     for city in state["cities"]:
    #         if (city["name"] == None):
    #             del city

    f.close()

    with open('state_city_v2.json', 'w') as f:
        json.dump(data, f, indent=2)


def clean_v2():
    f = open('state_city_v2.json')
    data = json.load(f)

    for state in data:
        for city in state["cities"]:
            city["name"] = city["name"].title()

    f.close()

    with open('state_city_v3.json', 'w') as f:
        json.dump(data, f, indent=2)


def clean_v3():
    f = open('state_city_v3.json')
    data = json.load(f)

    data.sort(key = lambda x:x['name'])

    for state in data:
        state["cities"].sort(key = lambda x:x['name'])

    f.close()

    with open('state_city_final.json', 'w') as f:
        json.dump(data, f, indent=2)


def clean_empty(d):
    if isinstance(d, dict):
        return {
            k: v
            for k, v in ((k, clean_empty(v)) for k, v in d.items())
            if v
        }
    if isinstance(d, list):
        return [v for v in map(clean_empty, d) if v]
    return d


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # clean_ori()
    clean_v3()
