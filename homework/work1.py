from abc import ABC, abstractmethod

# 1 задание
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f"{self.name} готов к бою! "

# 2 задание
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP {self.mp}"
class WarriorHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
    def action(self):
        return f"Воин {self.name} рубит мячом! Уровень : {self.lvl}"

merlin = MageHero("Merlin", 60, 80, 100)
print(merlin.action())
conan = WarriorHero("Conan", 80, 90, 130)
print(conan.action())

# задание 3
class BankAccount:
    bank_name = "Simba"
    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password
    def login(self,password):
        if password == self.__password:
            return True
        else:
            return False
    @property
    def full_info(self):
        return f"{self.hero.name} | Баланс : {self._balance} SOM"
    @classmethod
    def get_bank_name(cls):
        return f"Банк: {cls.bank_name}"
    @staticmethod
    def bonus_for_level(lvl):
        return f"Бонус за {lvl} уровень : {lvl*10} SOM"
    def __str__(self):
        return f"{self.hero.name} | Баланс : {self._balance} SOM"
    def __add__(self, other):
        if type(self.hero) is type(other.hero):
            total_balance = self._balance + other._balance
            return f"Суммарный баланс: {total_balance} SOM"
        else:
            return "Ошибка: нельзя объединять счета разных типов героев!"
    def __eq__(self, other):
        return self.hero.name == other.hero.name and self.hero.lvl == other.hero.lvl
acc1 = BankAccount(merlin, 4000, "123wer")
acc2 = BankAccount(conan, 6000, "456asd")
print(acc1)
print(acc2)

# Абстрактный класс SmsService
class SmsService(ABC):
    @abstractmethod
    def send_otp(self,phone):
        pass

class KGSms(SmsService):
    def send_otp(self,phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"

class RUSms(SmsService):
    def send_otp(self,phone):
        return {"text": "Код: 1234", "phone": "{phone}"}

print(BankAccount.get_bank_name())
print(BankAccount.bonus_for_level(100))
sms = KGSms()
print(sms.send_otp("+996505123456"))







