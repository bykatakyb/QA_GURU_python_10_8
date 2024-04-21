"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(300)
        assert not product.check_quantity(2000)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(50)
        assert product.quantity == 950

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1111)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_product_adding(self, product, cart):
        # проверка добавления товара в корзину (10 товаров)
        cart.add_product(product, 10)
        assert product in cart.products
        assert cart.products[product] == 10

    def test_product_removing(self, product, cart):
        # проверка удаления конкретного кол-ва конкретного товара из корзины
        cart.add_product(product, 10)
        cart.remove_product(product, 10)
        assert product not in cart.products

    def test_cart_clearing(self, product, cart):
        # проверка функции очистки корзины
        cart.add_product(product, 10)
        cart.clear()
        assert cart.products == {}

    def test_total_amount_counting(self, product, cart):
        # проверка расчета суммарной стоимости товаров в корзине
        cart.add_product(product, 15)
        assert cart.get_total_price() == 1500

    def test_quantity_in_stock_decreasing(self, product, cart):
        # проверка корректности списания остатков товара
        cart.add_product(product, 20)
        cart.buy()
        assert product.quantity == 980

    def test_try_to_buy_more_than_we_have_in_stock(self, product, cart):
        # проверка запрета покупки при превышении доспуного остатка товара
        cart.add_product(Product("item", 300, "just item", 5), 10)
        with pytest.raises(ValueError):
            cart.buy()
