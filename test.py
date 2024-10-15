import unittest
from main import SuperHeroHeightFilter

class TestSuperHeroHeightFilter(unittest.TestCase):
    def setUp(self):
        self.filterManWithWork = SuperHeroHeightFilter("Male", True)
        self.filterManWithoutWork = SuperHeroHeightFilter("Male", False)
        self.filterFemaleWithWork = SuperHeroHeightFilter("Female", True)
        self.filterFemaleWithoutWork = SuperHeroHeightFilter("Female", False)
        self.filterInvalidGender = SuperHeroHeightFilter("Non-binary", True)

    def testTallestManHeroWithWork(self):
        hero = self.filterManWithWork.tallestHero()
        self.assertIsNotNone(hero)
        self.assertEqual(hero["appearance"]["gender"], "Male")
        self.assertNotEqual(hero["work"]["occupation"], "-")
    
    def testTallestManHeroWithoutWork(self):
        hero = self.filterManWithoutWork.tallestHero()
        self.assertIsNotNone(hero)
        self.assertEqual(hero["appearance"]["gender"], "Male")
        self.assertEqual(hero["work"]["occupation"], "-")

    def testTallestFemaleHeroWithWork(self):
        hero = self.filterFemaleWithWork.tallestHero()
        self.assertIsNotNone(hero)
        self.assertEqual(hero["appearance"]["gender"], "Female")
        self.assertNotEqual(hero["work"]["occupation"], "-")
    
    def testTallestFemaleHeroWithoutWork(self):
        hero = self.filterFemaleWithoutWork.tallestHero()
        self.assertIsNotNone(hero)
        self.assertEqual(hero["appearance"]["gender"], "Female")
        self.assertEqual(hero["work"]["occupation"], "-")

    def testInvalidGender(self):
        with self.assertRaises(ValueError):
            self.filterInvalidGender.tallestHero()

if __name__ == '__main__':
    unittest.main()
