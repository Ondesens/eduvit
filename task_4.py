from datetime import  datetime
class Fish:
    def __init__(self, name: str, species: str,habitat: str,begin_spawning: str, finish_spawning : str ,fishing_method: str, weight: float) -> None:
        self.name = name
        self.species = species
        self.habitat = habitat
        self.weight = weight
        self.fishing_method = fishing_method
        self.begin_spawning=begin_spawning
        self.finish_spawning=finish_spawning
    def __str__(self):
        return f'Название:{self.name}, Вид: {self.species}, Среда обитания: {self.habitat}, Метод ловли: {self.fishing_method}, Вес: {self.weight} кг, Начало нереста: {self.begin_spawning}, Конец нереста: {self.finish_spawning}  )'

    def change_weight(self, weight: float) :
        self.weight = weight

    def change_fishing_method(self, fishing_method: str) -> None:
        self.fishing_method = fishing_method

    def is_fish_gigantic(self) :
        if self.weight<=0.3 :
            return "Небольшая рыба"
        elif 0.3<self.weight<1 :
            return "Средняя рыба"
        else :
            return "Гигантская рыба!"

    def spawning_time(self) :

        return  f'Продолжительность нереста: {datetime.strptime(self.finish_spawning,'%d.%m.%Y') - datetime.strptime(self.begin_spawning,'%d.%m.%Y')}'

fish1= Fish("Окунь","Хищная", "в пресной воде","14.2.2022","17.03.2022","спиннинг", 0.3)
print(fish1)
print(fish1.spawning_time())
print(fish1.is_fish_gigantic())
fish1.change_weight(1.53)
fish1.change_fishing_method("Поплавочная удочка ")
print(fish1)

