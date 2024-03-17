d = {
    1: {
        "name": "Siri",
        "plan": "Basic",
    },
    2: {"name": "surjo", "plan": "Premium"},
}


def upDict(nm, pln, d):
    d.update({len(d) + 1: {"name": nm, "plan": pln}})
    for i in d.values():
        if i["plan"] == "Basic":
            print(f"{i['name']} plan cost 9.99")
        elif i["plan"] == "Standard":
            print(f"{i['name']} standard plan cost 15.99")
        elif i["plan"] == "Premium":
            print(f"{i['name']} premium plan cost 19.99")


upDict("jishan", "Premium", d)
upDict("rafi", "Basic",d)
