import utilities as u
import bloomfilter as b

words = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque id fermentum felis. Nullam consectetur bibendum pellentesque. Aliquam erat volutpat. Duis porta ante et sapien vehicula, in accumsan elit molestie. Nullam non tincidunt elit. Morbi suscipit dolor id bibendum sodales. Nunc ornare lectus ut ante hendrerit lobortis. Suspendisse sed sem et nisi rutrum consectetur. Pellentesque convallis dui vel elit semper, ut eleifend mi luctus. Aliquam suscipit sapien tortor, convallis aliquam tellus efficitur ut. Ut a volutpat enim. Praesent sed dui sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas mattis molestie ligula quis sodales. Cras.')
#words = words + words + words + words + words + words + words + words + words + words + words + words + words + words + words + words
#for i in range (0, 5):
#    words = words + words

words2 = ('Lorema ipsuma dolora sita ameta, consectetura adipiscing elit. Pellentesque id fermentum felis. Nullam consectetur bibendum pellentesque. Aliquam erat volutpat. Duis porta ante et sapien vehicula, in accumsan elit molestie. Nullam non tincidunt elit. Morbi suscipit dolor id bibendum sodales. Nunc ornare lectus ut ante hendrerit lobortis. Suspendisse sed sem et nisi rutrum consectetur. Pellentesque convallis dui vel elit semper, ut eleifend mi luctus. Aliquam suscipit sapien tortor, convallis aliquam tellus efficitur ut. Ut a volutpat enim. Praesent sed dui sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Maecenas mattis molestie ligula quis sodales. Cras.')


words3 = """
Saudara-saudara sekalian!

Saya telah minta saudara-saudara hadir disini untuk menyaksikan satu peristiwa maha-penting dalam sejarah kita.

Berpuluh-puluh tahun kita bangsa Indonesia telah berjoang, untuk kemerdekaan tanah air kita bahkan telah beratus-ratus tahun!

Gelombang aksi kita untuk mencapai kemerdekaan kita itu ada naiknya dan ada turunnya, tetapi jiwa kita tetap menuju ke arah cita-cita.

Juga di dalam jaman Jepang, usaha kita untuk mencapai kemerdekaan nasional tidak berhenti-hentinya.

Di dalam jaman Jepang ini, tampaknya saja kita menyandarkan diri kepada mereka, tetapi pada hakekatnya, tetap kita menyusun tenaga sendiri, tetapi kita percaya kepada kekuatan sendiri.

Sekarang tibalah saatnya kita benar-benar mengambil sikap nasib bangsa dan nasib tanah air kita di dalam tangan kita sendiri. Hanya bangsa yang berani mengambil nasib dalam tangan sendiri akan dapat berdiri dengan kuatnya.

Maka kami, tadi malah telah mengadakan musyawarat dengan pemuka-pemuka rakyat Indonesia dari seluruh Indonesia. Permusyawaratan itu seia sekata berpendapat bahwa sekaranglah datang saatnya untuk menyatakan kemerdekaan kita.

Saudara-saudara!

Dengan ini kami menyatakan kebulatan tekad itu. Dengarkanlah proklamasi kami:

Proklamasi

Kami bangsa Indonesia dengan ini menyatakan kemerdekaan Indonesia.
Hal-hal yang mengenai pemindahan kekuasaan dan lain-lain, diselenggarakan dengan cara saksama dan dalam tempo yang sesingkat-singkatnya.

Jakarta, 17 Agustus 1945
Atas Nama Bangsa Indonesia

Soekarno-Hatta

Demikianlah saudara-saudara!

Kita sekarang telah merdeka!

Tidak ada satu ikatan lagi yang mengikat tanah air kita dan bangsa kita!

Mulai saat ini kita menyusun Negara kita! Negara Merdeka, Negara Republik Indonesia – merdeka kekal dan abadi. Insyaallah, Tuhan memberkati kemerdekaan kita itu!

"""


#alist = u.getwords(words)
#blist = u.getwords(words2)

alist = u.getwords(words3)
blist = u.getwords(words3)

print (alist)
print (str(len(alist)))
bfValue = b.createstringbloomfilter(alist)
print (bfValue)
tested = b.teststringbloomfilter(bfValue, blist)
print (str(tested) + "%")