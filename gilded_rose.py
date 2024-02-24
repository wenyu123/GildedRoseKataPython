# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)



class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_single_item(item)

    def update_single_item(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            self.update_sulfuras(item)
        elif item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass(item)
        elif item.name.startswith("Conjured"):
            self.update_conjured(item)
        else:
            self.update_regular_item(item)

    def update_sulfuras(self, item):
        pass  # Sulfuras does not change

    def update_aged_brie(self, item):
        self.increase_quality(item)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.increase_quality(item)

    def update_backstage_pass(self, item):
        self.increase_quality(item)
        if item.sell_in < 11:
            self.increase_quality(item)
        if item.sell_in < 6:
            self.increase_quality(item)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            item.quality = 0

    def update_regular_item(self, item):
        self.decrease_quality(item)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.decrease_quality(item)

    def update_conjured(self, item):
        self.decrease_quality(item,2)
        self.decrease_sell_in(item)
        if item.sell_in < 0:
            self.decrease_quality(item, 2)

    def increase_quality(self, item, amount=1):
        item.quality = min(50, item.quality + amount)

    def decrease_quality(self, item, amount=1):
        item.quality = max(0, item.quality - amount)

    def decrease_sell_in(self, item):
        item.sell_in -= 1
