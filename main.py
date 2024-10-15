import requests

class SuperHeroHeightFilter:
    def __init__(self, gender: str, work: bool):
        self.__gender = gender
        self.__work = work
        self.__data = requests.get("https://akabab.github.io/superhero-api/api/all.json").json()

    def tallestHero(self):
        filteredHeroes = self.filterHeroes()
        tallest_hero = max(filteredHeroes, key=self.getHeight)
        return tallest_hero

    def filterHeroes(self):
        return [
            hero for hero in self.__data
            if hero["appearance"]["gender"] == self.__gender and
               self.workCondition(hero["work"]["occupation"])
        ]

    def workCondition(self, occupation):
        if self.__work:
            return occupation != '-'
        else:
            return occupation == '-'

    def getHeight(self, hero):
        height_str = hero["appearance"]["height"][1]
        try:
            if "cm" in height_str:
                return int(height_str.replace(" cm", ""))
            elif "meters" in height_str:
                return float(height_str.replace(" meters", "")) * 100
            else:
                return 0
        except ValueError:
            return 0
        
if  __name__ == "__main__":
    checker = SuperHeroHeightFilter("Male", False)
    print(checker.tallestHero())