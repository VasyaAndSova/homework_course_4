from src.product import Product


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

    def __str__(self):
        return f"{self.name}, количество продуктов: {sum(product.quantity for product in self.__products)} шт."

    def add_product(self, category):
        if isinstance(category, Product):
            self.__products.append(category)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_in_list(self):
        return self.__products

    def middle_price(self):
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products))
        except ZeroDivisionError:
            return 0
