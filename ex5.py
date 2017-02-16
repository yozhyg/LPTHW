# -*- encoding: utf-8 -*-
my_name = 'Олег'
my_age = 35 # и это так
my_height = 176 #  см
my_weight = 77 # кг
my_eyes = 'Серые'
my_teeth = 'Белые'
my_hair = 'Русые'

print "Давайте поговорим о %s." % my_name
print "Его рост %s см." % my_height
print "Он весит %s кг." % my_weight
print "На самом деле это не очень много."
print "У него %s глаза и %s волосы." % (my_eyes, my_hair)
print "Его зубы обычно %s, зависит от кофе." % my_teeth

# Эта строка хитрая, попытайтесь написать ее правильно
print "Если я прибавлю %d, %d и %d то получу %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)