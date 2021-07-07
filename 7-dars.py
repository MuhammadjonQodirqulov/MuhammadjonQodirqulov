# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 23:42:49 2021

@author: Muhammadjon
"""

#7-dars


ismlar = ['Muhammadali','Diyorbek','Salohiddin']
print(f'Salom {ismlar[0]} bugun choyxonaga borasanmi?')
print(f'{ismlar[2]} ishlaring yaxshimi?')
print(f'Ko`rinmeysan {ismlar[1]}')

sonlar = [4,-9,3.145,10]

print(sonlar[-1] + sonlar[2])
print(sonlar[-2] * sonlar[-3])
      
del sonlar[2]
sonlar.append(5)
print(sonlar)

t_shaxslar = ['Amir Temur', 'Imom Buxoriy', 'At-Termiziy']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Jeff Bezos']
print(f'Men tarixiy shaxslardan {t_shaxslar.pop(1)} bilan zamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan suhbat qurishni istayman')

friends = []

friends.append('Suhrob')
friends.append('Zarif')
friends.append('Shaxriyor')
friends.append('Samandar')
print(friends)

friends.remove('Zarif')
friends.remove('Suhrob')
print(friends)
               
friends.insert(0,'Zohid')
friends.append('Hayot')
friends.insert(3,'Hayit')
print(friends)

mehmonlar = []

mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))

print("\nKelgan mehmonlar: ", mehmonlar)