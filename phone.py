from item import Item

class Phone(Item):
	all = []
	def __init__(self, name, price, quantity, broken_phones=0) -> None:
		super().__init__(
			name, price, quantity
		)
		assert broken_phones >= 0, f"Broken phones {broken_phones} is invalid"

		self.broken_phones = broken_phones

		Phone.all.append(self)
