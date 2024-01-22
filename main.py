from abc import ABC, abstractmethod


class CarType(ABC):
    @abstractmethod
    def engine_type(self):
        pass


class Management(ABC):
    @abstractmethod
    def add_car(self, car):
        pass

    @abstractmethod
    def show_cars(self):
        pass

    @abstractmethod
    def search_cars_by(self, searched_property):
        pass


class ElectricCar(CarType):
    def engine_type(self):
        return f"this is electric car"


class GasCar(CarType):
    def engine_type(self):
        return f"this is gas car"


class PetrolCar(CarType):
    def engine_type(self):
        return f"this is engine car"


class Car:
    def __init__(self, brand, model, year, milage, car_type: CarType):
        self.car_type = car_type
        self.milage = milage
        self.year = year
        self.model = model
        self.brand = brand

    def __str__(self):
        return f"{self.car_type.engine_type()} brand: {self.brand}, model: {self.model}, year: {self.year}, milage: {self.milage}"


class CarSpecification(ABC):
    @abstractmethod
    def is_satisfied_by(self, car):
        pass

    def and_specification(self, spec):
        return AndSpecification(self, spec)


class BrandSpecification(CarSpecification):
    def __init__(self, brand):
        self.brand = brand

    def is_satisfied_by(self, car):
        return self.brand == car.brand


class ModelSpecification(CarSpecification):
    def __init__(self, model):
        self.model = model

    def is_satisfied_by(self, car):
        return self.model in car.model


class YearSpecification(CarSpecification):
    def __init__(self, year_beg, year_end):
        self.year_end = year_end
        self.year_beg = year_beg

    def is_satisfied_by(self, car):
        return self.year_beg <= car.year <= self.year_end


class MilageSpecification(CarSpecification):
    def __init__(self, milage_beg, milage_end):
        self.milage_end = milage_end
        self.milage_beg = milage_beg

    def is_satisfied_by(self, car):
        return self.milage_beg <= car.milage <= self.milage_end


class AndSpecification(CarSpecification):
    def __init__(self, *specs):
        self.specs = specs

    def is_satisfied_by(self, car):
        return all(spec.is_satisfied_by(car) for spec in self.specs)


class CarShowroom(Management):

    def __init__(self):
        self.all_cars = []

    def add_car(self, car):
        self.all_cars.append(car)

    def show_cars(self):
        return self.all_cars

    def search_cars_by(self, *specs):
        filtered_cars = [car for car in self.all_cars if all(spec.is_satisfied_by(car) for spec in specs)]
        return filtered_cars



electric = ElectricCar()
gas = GasCar()
petrol = PetrolCar()

car1 = Car("BMW", "X5", 2022, 100, electric)
car2 = Car("Audi", "A4", 2017, 120, gas)
car3 = Car("BMW", "X3", 2015, 90, gas)
car4 = Car("BMW", "X2", 2015, 156, petrol)
car5 = Car("Audi", "A1", 1960, 220, electric)
car6 = Car("BMW", "X3", 2015, 90, electric)

showroom = CarShowroom()
showroom.add_car(car1)
showroom.add_car(car2)
showroom.add_car(car3)
showroom.add_car(car4)
showroom.add_car(car5)
showroom.add_car(car6)

brand_spec = BrandSpecification("BMW")
model_spec = ModelSpecification("X")
year_spec = YearSpecification(2005, 2024)
milage_spec = MilageSpecification(80, 150)

brand_model_year_milage_specification = brand_spec.and_specification(model_spec).and_specification(
    year_spec).and_specification(milage_spec)

brand_year_specification = brand_spec.and_specification(year_spec)

filtered_cars1 = showroom.search_cars_by(brand_year_specification)

filtered_cars = showroom.search_cars_by(brand_model_year_milage_specification)

for car in filtered_cars:
    print(car)