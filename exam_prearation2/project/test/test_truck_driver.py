from project.truck_driver import TruckDriver

from unittest import TestCase

# from exam_preparation.project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def set_Up(self) -> None:
        self.driver = TruckDriver('Test', 1)

    def test_init(self):
        assert self.driver.name == 'Test'
        assert self.driver.money_per_mile == 1
        assert self.driver.available_cargos == {}
        assert not self.driver.available_cargos
        assert self.driver.earned_money == 0
        assert self.driver.miles == 0

    def test_set_earned_money_cannot_be_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.set_earned_money = -3

        assert ex.exception.args[0] == "Test went bankrupt."

    def test_set_earned_money(self):
        assert self.driver.earned_money == 0
        self.driver.set_earned_money = 4

        assert self.driver.earned_money == 5

    def test_add_existing_cargo_offer(self):
        self.driver.add_cargo_offer('place1', 12)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('place1', 13)
        assert ex.exception.args[0] == "Cargo offer is already added."

    def test_add_offer(self):
        result = self.driver.add_cargo_offer('place1', 12)
        assert result == f"Cargo for 12 to place1" \
                         f" was added as an offer."

    def test_drive_best_cargo_offer_no_offers_raises(self):
        assert not self.driver.available_cargos

        res = self.driver.drive_best_cargo_offer()
        assert res == "There are no offers available."

    def test_drive_best_cargo_offer(self):
        self.driver.add_cargo_offer('place1', 100)
        self.driver.add_cargo_offer('place2', 200)
        self.driver.add_cargo_offer('place3', 50)

        assert self.driver.earned_money == 0
        assert self.driver.miles == 0

        res = self.driver.drive_best_cargo_offer()
        assert res == f"Test is driving 200 to place2."

        assert self.driver.earned_money == 200
        assert self.driver.miles == 200

    def test_eat(self):
        self.driver.earned_money = 50

        self.driver.eat(250)

        assert self.driver.earned_money == 30

    def test_sleep(self):
        self.driver.earned_money = 50

        self.driver.sleep(1000)

        assert self.driver.earned_money == 5

    def test_pump_gas(self):
        self.driver.earned_money = 600

        self.driver.pump_gas(1500)

        assert self.driver.earned_money == 100

    def test_repair_truck(self):
        self.driver.earned_money = 7600

        self.driver.repair_truck(10000)

        assert self.driver.earned_money == 100

    def test_represent(self):
        res = str(self.driver)
        res_repr = repr(self.driver)

        assert res == res_repr
        assert res == 'Test has 0 miles behind his back.'

    def test_check_for_activities(self):
        self.driver.earned_money = 11760

        res = self.driver.check_for_activities(10000)
        assert res is None

        assert self.driver.earned_money == 10

    def test_drive_best_offer_with_activities_money_ends(self):
        self.driver.earned_money = 11760 - 10011

        needed_money_for_the_cargo = 11750
        km_to_drive = 1000
        money_to_earn = self.driver.money_per_mile * km_to_drive

        self.driver.add_cargo_offer('place1', 10000)
        with self.assertRaises(ValueError) as ex:
            self.driver.drive_best_cargo_offer()

        assert ex.exception.args[0] == 'Test want bankrupt.'


