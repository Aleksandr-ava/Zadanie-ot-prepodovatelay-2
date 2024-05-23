from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Confirm
from rich.columns import Columns

console = Console()

list_items = []
amount = []


def add_cas():
    global list_items
    global amount
    items = input('Что хотите добавить в корзину? ')
    price = input('Уточните цену товара? ')
    print()
    print('Вы добавили свой товар!')
    print()
    list_items.append(items)
    amount.append(price)


def check_cart(items, price):
    global list_items
    global amount
    items_panel = Panel(
        Text('\n'.join([f'{item}' for item in items])),
        title='Твои продукты',
        width=34
    )

    amount_panel = Panel(
        Text('\n'.join([f'₽ {amount}' for amount in price])),
        title='Цена продуктов',
        width=34
    )

    dub_panel = Columns([items_panel, amount_panel])
    console.print(dub_panel)


def clear_cart():
    global list_items
    global amount
    list_items.clear()
    amount.clear()


def create_check(items, price):
    total_price = sum([int(i) for i in price])
    len_items = len(items)
    name_saller = 'Александр Белоусов'
    street_shop = 'Калининград Суворова 15'
    console.print(Panel(
        Text(
            f'''
        Большое спасибо за покупку!
           Будем ждать вас ещё!
        ___________________________
        Кол-во товаров:  {len_items}
        Общая стоимость: {total_price} ₽
        Покупатель:      {name_saller}

        Адрес магазина:  {street_shop}

                    ''',
        ),
        title='Чек', subtitle='Досвидание!',
        width=60
    ))


def run():
    console.print(Panel(Text(
        '''  
    Выбери одну из операций!
         '''),
        title='Касса', subtitle='Добро пожаловать!',
        width=34
    ))
    print()
    while True:
        console.print(Panel(Text(
            '''   
        1. Добавить товар
        2. Что в корзине
        3. Очистить корзину
        4. Создать чек
        5. Завершить работу
            '''),
            width=34
        ))
        print()
        oper = console.input('Что хочешь сделать? (1-5) ')
        if oper == '1':
            add_cas()
        elif oper == '2':
            check_cart(list_items, amount)
        elif oper == '3':
            clear_cart()
        elif oper == '4':
            create_check(list_items, amount)
        elif oper == '5':
            if Confirm.ask('Вы действительно хотите выйти? '):
                break
        else:
            console.print('Что-то не то! Выберите, что хотите сделать!')


run()
