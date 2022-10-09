def change_obj(the_obj: dict, obj_key, new_obj) -> dict:
    """
    Change the key in a dictionary.
    :param the_obj: the dictionary
    :param obj_key: key that we want to change
    :param new_obj: new name for that key
    :return: the dictionary with the new key
    """
    try:
        newkey = the_obj.get(f"{obj_key}").copy()
        for el in newkey.keys():
            del the_obj[f"{obj_key}"][el]
        del the_obj[f"{obj_key}"]
        the_obj[f"{new_obj}"] = newkey
    except AttributeError:
        try:
            newkey = the_obj.get(f"{obj_key}")
            del the_obj[f"{obj_key}"]
            the_obj[f"{new_obj}"] = newkey
        except KeyError:
            newkey = the_obj.get(obj_key)
            del the_obj[obj_key]
            the_obj[new_obj] = newkey
    return the_obj


if __name__ == "__main__":
    b = {
        "one": 1,
        "two": 2,
        "three": {
            "a": "A",
            "b": "B",
            "c": {
                "d": "D",
                "e": [{
                    "1": 1,
                    "2": 2
                }]
            }
        }
    }
    print(b)
    print(change_obj(b,'three', '4444'))

    n = {
        1: 11,
        "2": "2",
        3: 3
    }
    print(n)
    print(change_obj(n,1,"4444"))
