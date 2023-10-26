# %% LineItem
class LineItem:
    def __init__(self, sku: str, price: float, amount: int):
        self.sku = sku
        self.price = price
        self.amount = amount

    @property  # Computed property.
    def value(self):
        return self.price * self.amount

    @property  # Getter.
    def sku(self):
        return self._sku
    
    @sku.setter  # Setter.
    def sku(self, value):
        value = value.strip()
        if not value:
            raise ValueError(f'empty sku: {value!r}')
        self._sku = value


# %% Test
li = LineItem('esp32', 1.34, 10)
print(li.value)

# %% Invalid SKU
li.sku = ' '