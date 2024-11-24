import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            r1 = Runner('3loychik', speed=-993)
            for i in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError or TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_run(self):
        try:
            r1 = Runner('Xzkilza')
            for i in range(10):
                r1.run()
            self.assertEqual(r1.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except ValueError or TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        try:
            r1 = Runner('specteral')
            r2 = Runner('Фуад')
            for i in range(10):
                r1.walk()
                r2.run()
            self.assertNotEqual(r1.distance, r2.distance)
            logging.info('"test_challendge" выполнен успешно')
        except ValueError or TypeError:
            logging.warning("Неверный тип данных для объекта Runner")


logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log',
                    encoding="UTF-8",
                    format='%(asctime)s | %(filename)s | %(message)s')
