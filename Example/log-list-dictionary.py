#เก็บแล้วแสดงแบบ list
box = []
box.append('Pen')
box.append('Pencil')
box.append('Rubber')
print(box)
['Pen', 'Pencil', 'Rubber']
print(box[0])
print(len(box))

#เก็บแบบ dictionary
brand = {'pen':['lamy','pental'],'pencil':['horse','staedtler'],'rubber':['pental','hi-polyper']}
print(brand)
print(brand.keys())
print(brand.values())

#
for b in box:
    print(b)

for br in brand.keys():
    print(br)
    
for br in brand.values():
    print(br)

for br in brand.items():
    print(br)