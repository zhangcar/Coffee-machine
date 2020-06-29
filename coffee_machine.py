class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    beans = 120
    disposable_cups = 9

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, '
              'back - to main menu:')
        choice = (input())
        if choice == '1':
            if self.water - 250 > 0 and self.beans - 16 > 0 and self.disposable_cups - 1 > 0:
                print('I have enough resources, making you a coffee!')
                self.water = self.water - 250
                self.beans = self.beans - 16
                self.money = self.money + 4
                self.disposable_cups = self.disposable_cups - 1
            else:
                print('Sorry, not enough water!')

        elif choice == '2':
            if self.water - 350 > 0 and self.beans - 20 > 0 and self.disposable_cups - 1 > 0 and self.milk - 75 > 0:
                print('I have enough resources, making you a coffee!')
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.beans = self.beans - 20
                self.money = self.money + 7
                self.disposable_cups = self.disposable_cups - 1
            else:
                print('Sorry, not enough water!')

        elif choice == '3':
            if self.water - 200 > 0 and self.beans - 12 > 0 and self.disposable_cups - 1 > 0 and self.milk - 100 > 0:
                print('I have enough resources, making you a coffee!')
                self.water = self.water - 200
                self.milk = self.milk - 100
                self.beans = self.beans - 12
                self.money = self.money + 6
                self.disposable_cups = self.disposable_cups - 1
            else:
                print('Sorry, not enough water!')

        elif choice == 'back':
            return None

    def fill(self):
        print('Write how many ml of water do you want to add:')
        add_water = int(input())
        self.water = self.water + add_water
        print('Write how many ml of milk do you want to add:')
        add_milk = int(input())
        self.milk = self.milk + add_milk
        print('Write how many grams of coffee beans do you want to add:')
        add_beans = int(input())
        self.beans = self.beans + add_beans
        print('Write how many disposable cups of coffee do you want to add:')
        add_cups = int(input())
        self.disposable_cups = self.disposable_cups + add_cups

    def take(self):
        print('I gave you ${}'.format(self.money))
        self.money = self.money - self.money

    def input_(self):
        self.choice = input()
        return self.choice

    def current_state(self):
        print('''The coffee machine has:\
        \n{} of water\
        \n{} of milk\
        \n{} of coffee beans\
        \n{} of disposable cups\
        \n{} of money'''.format(self.water, self.milk, self.beans, self.disposable_cups, self.money))


example = CoffeeMachine()

while True:
    print('Write action (buy, fill, take, remaining, exit):')
    choice = example.input_()
    if choice == 'buy':
        example.buy()
    elif choice == 'fill':
        example.fill()
    elif choice == 'take':
        example.take()
    elif choice == 'remaining':
        example.current_state()
    elif choice == 'exit':
        break
