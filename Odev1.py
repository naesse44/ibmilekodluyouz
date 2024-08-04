#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math


noktalar = [(2, 3), (5, 4), (1, 1), (6, 1)]


def euclideanDistance(noktalar1, noktalar2):
    return math.sqrt((noktalar2[0] - noktalar1[0])**2 + (noktalar2[1] - noktalar1[1])**2)


uzaklık = []


for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        dist = euclideanDistance(noktalar[i], noktalar[j])
        uzaklık.append(dist)


min_uzaklık = min(uzaklık)
print(min_uzaklık)


# In[ ]:




