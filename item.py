import csv

class Item:
	pay_rate = 0.8
	all = []
	def __init__(self, name: str, price: float, quantity = 0) -> None:
		assert price >= 0, f"Price {price} is invalid"
		assert quantity >= 0, f"Quantity {quantity} is invalid"

		self.__name = name
		self.__price = price
		self.quantity = quantity

		Item.all.append(self)

	def __repr__(self) -> str:
		return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity} )"
	
	def calculate_total_price(self):
		return self.__price * self.quantity

	def apply_discount(self):
		self.__price = self.__price * self.pay_rate

	def apply_increment(self, increment_value):
		self.__price = self.__price + self.__price * increment_value

	@property
	def name(self) -> None:
		return self.__name

	@property
	def price(self):
		return self.__price

	@name.setter
	def name(self, value):
		if len(value) > 10:
			error = f"The name {value} is too long"
			raise Exception(error)
		else:
			self.__name = value
	
	@price.setter
	def price(self, value):
		if value < 0:
			error = f"Invalid price {value}"
			raise Exception(error)
		else:
			self.__price = value

	@classmethod
	def instatiate_from_csv(cls):
		with open('items.csv', 'r') as f:
			reader = csv.DictReader(f)
			items = list(reader)
		
		for item in items:
			Item(name=item.get('name'), price=float(item.get('price')), quantity=int(item.get('quantity')))
	
	@staticmethod
	def is_integer(num):
		if isinstance(num, float):
			return num.is_integer()
		elif isinstance(num, int):
			return True
		else:
			return False

	def __connect(self):
		pass

	def __prepare_body(self):
		return f"""
		Hello there!

		We have {self.name} {self.quantity} times.
		"""

	def __send(self):
		pass

	def __send_email(self) -> None:
		self.__connect()
		self.__prepare_body()
		self.__send()