# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_vest_item_should_decrease_after_one_day(self):
        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6)]
        gr = GildedRose(items)
        
        gr.update_quality()

        expected_items = [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]
        self.assertEqual(str(items), str(expected_items))

    def test_aged_brie_increases_in_quality_over_time(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0), Item(brie, -1, 2)]
        gr = GildedRose(items)

        gr.update_quality()

        expected_items = [Item(brie, 1, 1), Item(brie, -2, 4)]  
        self.assertEqual(str(items), str(expected_items))

    def test_backstage_passes_increase_in_quality_as_sellin_approaches(self):
        pass_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(pass_name, 9, 20), Item(pass_name, 5, 45), Item(pass_name, 3, 45)]
        gr = GildedRose(items)

        gr.update_quality()

        expected_items = [Item(pass_name, 8, 22), Item(pass_name, 4, 48), Item(pass_name, 2, 48)]
        self.assertEqual(str(items), str(expected_items))

    def test_conjured_items_degrade_twice_as_fast(self):
        conjured = "Conjured Mana Cake"
        items = [Item(conjured, 3, 6), Item(conjured, -1, 6)]
        gr = GildedRose(items)

        gr.update_quality()

        expected_items = [Item(conjured, 2, 4), Item(conjured, -2, 2)]  
        self.assertEqual(str(items), str(expected_items))

if __name__ == '__main__':
    unittest.main()
