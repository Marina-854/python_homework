from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79001112233"),
    Smartphone("Samsung", "Galaxy S24", "+79004445566"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79007778899"),
    Smartphone("Google", "Pixel 8", "+79001234567"),
    Smartphone("OnePlus", "12", "+79009876543")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")