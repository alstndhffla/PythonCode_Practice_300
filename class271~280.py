import random

# 271
"""
은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다.
Account 클래스를 생성한 후 생성자를 구현해보세요.
생성자에서는 예금주와 초기 잔액만 입력 받습니다.
은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성

3. 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장

4. Account 클래스에 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능

5. Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다

6. Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력

7. 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경

8. Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장

9. 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력

10. 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 
입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가
"""


class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)   # randint 0 부터 999 사이에 난수 생성.
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)   # 길이가 3인 문자열. 왼쪽부터 남은 부분을 0 으로 채움
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count = Account.account_count + 1

    # 정적 메소드 @classmethod 와 @staticmethod -> 인스턴스를 만들지 않아도 class의 메서드로 바로 실행할 수 있다.
    # 단, @classmethod 는 cls 라는 인자가 추가되어야 한다.
    # cls는 '클래스'를 가리킨다. 이것으로 클래스의 어떤 속성에도 접근할 수 있다. ex. cls.account_count
    @classmethod
    def get_account_num(cls):
        print(cls.account_count)    # 의미 -> Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count = self.deposit_count + 1
            if self.deposit_count % 5 == 0:
                self.balance = self.balance * 1.01

    def withdraw(self, amount):
        if amount < self.balance:
            self.withdraw_log.append(amount)
            self.balance = self.balance - amount

    # 6. Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력
    """
    은행이름: SC은행
    예금주: 파이썬
    계좌번호: 111-11-111111
    잔고: 10,000원
    """
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", format(self.balance, ","))    # format(값, ",") - 3자리마다 , 추가

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)


# 1
kim = Account("김민수", 100)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_number)
print(Account.account_count)


print("------------------")
# 2
lee = Account("이민수", 300)
print(Account.account_count)


print("------------------")
# 3
kim.get_account_num()


print("------------------")
# 5
k = Account("kim", 100)
k.deposit(100)
k.withdraw(90)
print(k.balance)


print("------------------")
# 6
p = Account("파이썬", 10000)
p.display_info()


print("------------------")
# 7
p = Account("파이썬", 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)


print("------------------")
# 8
data = []
k = Account("KIM", 10000000)
l = Account("LEE", 10000)
p = Account("PARK", 10000)

data.append(k)
data.append(l)
data.append(p)

print(data)

print("------------------")
# 9
data = []
k = Account("KIM", 10000000)
l = Account("LEE", 10000)
p = Account("PARK", 10000)
data.append(k)
data.append(l)
data.append(p)

for c in data:
    if c.balance >= 1000000:
        c.display_info()


print("------------------")
# 9
k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()