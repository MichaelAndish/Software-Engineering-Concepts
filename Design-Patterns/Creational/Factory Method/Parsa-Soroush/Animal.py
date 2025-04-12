from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Dog: Woof woof!")


class Cat(Animal):
    def make_sound(self):
        print("Cat: Meow meow!")


class AnimalTrainer(ABC):

    @abstractmethod
    def make_animal(self) -> Animal:
        pass

    def teach_to_speak(self):
        animal = self.make_animal()
        animal.make_sound()


class DogTrainer(AnimalTrainer):
    def make_animal(self) -> Animal:
        return Dog()


class CatTrainer(AnimalTrainer):
    def make_animal(self) -> Animal:
        return Cat()


if __name__ == "__main__":
    print("Dog Trainer:")
    dog_trainer = DogTrainer()
    dog_trainer.teach_to_speak()

    print("\nCat Trainer:")
    cat_trainer = CatTrainer()
    cat_trainer.teach_to_speak()
