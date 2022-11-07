import yaml
import xmltodict

with open("shedule.xml", encoding="utf-8") as f:
    s = f.read()
d = xmltodict.parse(s)
with open("shedulLibrary.yaml", "w", encoding="utf-8") as out:
    yaml.dump(d, out, allow_unicode=True, sort_keys=False)


