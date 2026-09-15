from address import Address
from mailing import Mailing

to_addr = Address("101000", "Москва", "Тверская", "1", "10")
from_addr = Address("190000", "Санкт-Петербург", "Невский", "10", "5")

my_mailing = Mailing(to_addr, from_addr, 250.50, "TRACK123456789")

print(f"Отправление {my_mailing.track} из "
      f"{my_mailing.from_address.index}, {my_mailing.from_address.city}, "
      f"{my_mailing.from_address.street}, {my_mailing.from_address.house} - {my_mailing.from_address.apartment} "
      f"в {my_mailing.to_address.index}, {my_mailing.to_address.city}, "
      f"{my_mailing.to_address.street}, {my_mailing.to_address.house} - {my_mailing.to_address.apartment}. "
      f"Стоимость {my_mailing.cost} рублей.")