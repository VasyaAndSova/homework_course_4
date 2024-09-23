class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def add_product(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
        return product_str

    @add_product.setter
    def add_product(self, task):
        self.__products.append(task)
        Category.product_count += 1

    @property
    def products_in_list(self):
        return self.__products