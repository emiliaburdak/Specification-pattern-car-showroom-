from main import ElectricCar, GasCar, PetrolCar, Car, CarShowroom, ModelSpecification, MilageSpecification, \
    BrandSpecification, YearSpecification, AndSpecification

import unittest


class TestCarType(unittest.TestCase):

    def test_electric_car(self):
        car = ElectricCar()
        self.assertEqual(car.engine_type(), "this is electric car")

    def test_gas_car(self):
        car = GasCar()
        self.assertEqual(car.engine_type(), "this is gas car")

    def test_petrol_car(self):
        car = PetrolCar()
        self.assertEqual(car.engine_type(), "this is engine car")


class TestCar(unittest.TestCase):

    def test_how_does_the_car_looks_like(self):
        car = Car('BMW', 'Q5', 2023, 10, ElectricCar())
        self.assertEqual(str(car), "this is electric car brand: BMW, model: Q5, year: 2023, milage: 10")


class TestManagement(unittest.TestCase):
    def setUp(self):
        self.car_showroom = CarShowroom()
        self.car_1 = Car('Tesla', 'Model S', 2020, 10000, ElectricCar())
        self.car_2 = Car('Ford', 'F-150', 2018, 50000, GasCar())

    def test_add_car(self):
        initial_len = len(self.car_showroom.all_cars)
        self.car_showroom.add_car(self.car_1)
        final_len = len(self.car_showroom.all_cars)
        self.assertEqual(final_len, initial_len + 1)

    def test_if_showroom_shows_correct_cars(self):
        self.car_showroom.add_car(self.car_1)
        self.car_showroom.add_car(self.car_2)
        self.assertEqual(self.car_showroom.show_cars(), [self.car_1, self.car_2])

    def test_search_cars_by_specification(self):
        self.car_showroom.add_car(self.car_1)
        self.car_showroom.add_car(self.car_2)
        spec1 = ModelSpecification('S')
        spec2 = MilageSpecification(0, 50000)
        specs = spec1, spec2
        filtered_cars = self.car_showroom.search_cars_by(*specs)
        self.assertEqual(filtered_cars, [self.car_1])


class TestCarSpecification(unittest.TestCase):

    def setUp(self):
        self.car_showroom = CarShowroom()
        self.car_1 = Car('Tesla', 'Model S', 2020, 10000, ElectricCar())
        self.car_2 = Car('Ford', 'F-150', 2018, 50000, GasCar())
        self.car_showroom.add_car(self.car_1)
        self.car_showroom.add_car(self.car_2)

    def test_brand_specification(self):
        spec = BrandSpecification('Tesla')
        self.assertTrue(spec.is_satisfied_by(self.car_1))
        self.assertFalse(spec.is_satisfied_by(self.car_2))

    def test_model_specification(self):
        spec_part = ModelSpecification('S')
        spec = ModelSpecification('Model S')
        self.assertTrue(spec_part.is_satisfied_by(self.car_1))
        self.assertTrue(spec.is_satisfied_by(self.car_1))
        self.assertFalse(spec_part.is_satisfied_by(self.car_2))
        self.assertFalse(spec.is_satisfied_by(self.car_2))

    def test_year_specification(self):
        spec = YearSpecification(2019, 2023)
        self.assertTrue(spec.is_satisfied_by(self.car_1))
        self.assertFalse(spec.is_satisfied_by(self.car_2))

    def test_millage_specification(self):
        spec = MilageSpecification(0, 40000)
        self.assertTrue(spec.is_satisfied_by(self.car_1))
        self.assertFalse(spec.is_satisfied_by(self.car_2))

    def test_and_specification(self):
        spec1 = YearSpecification(2015, 2023)
        spec2 = BrandSpecification('Tesla')
        and_spec = AndSpecification(spec1, spec2)
        self.assertTrue(and_spec.is_satisfied_by(self.car_1))
        self.assertFalse(and_spec.is_satisfied_by(self.car_2))


if __name__ == "__main__":
    unittest.main()
