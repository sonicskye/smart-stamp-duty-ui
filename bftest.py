import utilities as u
import bloomfilter as b

words = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque id fermentum felis. Nullam consectetur bibendum pellentesque. Aliquam erat volutpat. Duis porta ante et sapien vehicula, in accumsan elit molestie. Nullam non tincidunt elit. Morbi suscipit dolor id bibendum sodales. Nunc ornare lectus ut ante hendrerit lobortis. Suspendisse sed sem et nisi rutrum consectetur. Pellentesque convallis dui vel elit semper, ut eleifend mi luctus. Aliquam suscipit sapien tortor, convallis aliquam tellus efficitur ut. Ut a volutpat enim. Praesent sed dui sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas mattis molestie ligula quis sodales. Cras.')
#words = words + words + words + words + words + words + words + words + words + words + words + words + words + words + words + words
#for i in range (0, 5):
#    words = words + words

words2 = ('Lorema ipsuma dolora sita ameta, consectetura adipiscing elit. Pellentesque id fermentum felis. Nullam consectetur bibendum pellentesque. Aliquam erat volutpat. Duis porta ante et sapien vehicula, in accumsan elit molestie. Nullam non tincidunt elit. Morbi suscipit dolor id bibendum sodales. Nunc ornare lectus ut ante hendrerit lobortis. Suspendisse sed sem et nisi rutrum consectetur. Pellentesque convallis dui vel elit semper, ut eleifend mi luctus. Aliquam suscipit sapien tortor, convallis aliquam tellus efficitur ut. Ut a volutpat enim. Praesent sed dui sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas mattis molestie ligula quis sodales. Cras.')


alist = u.getwords(words)
blist = u.getwords(words2)

print (alist)
print (str(len(alist)))
bfValue = b.createstringbloomfilter(alist)
print (bfValue)
tested = b.teststringbloomfilter(bfValue, blist)
print (tested)