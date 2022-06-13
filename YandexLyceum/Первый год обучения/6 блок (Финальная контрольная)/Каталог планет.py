catalog = input()
list_is_catalog = []
while '&' in catalog:
    string = catalog.split(' & ')
    vl = string[2]
    planet = string[0]
    classp = string[-1]
    sattel = string[1]
    list_is_catalog.append((vl, planet, classp, sattel))
    catalog = input()
for tupl in sorted(list_is_catalog, key=lambda x: x[1], reverse=True):
    if tupl[0] == catalog:
        print(f"{tupl[1]} ({tupl[2]}), {tupl[3]};")
