"""
Author:Jingting
"""
import collections
class coins:
    def __init__(self):
        # dime 10 -> 100; quater 25 -> 100; nickel 5 -> 100 penny 1 -> 100
        self.coins = {1:'penny',5:'nickel',10:'dime',25:'quater'}

    def arrage_coins(self,res):
        """
        give the coins as less as best
        :param res: 
        :return: 
        """
        total_res = res * 100.00
        dp = [float('inf')] * int(total_res + 1)
        dp[0] = 0
        memo = collections.defaultdict(list) # coins combination
        res_coin_name = []
        for i in range(1,len(dp)):
            for c in self.coins.keys():
                if dp[i-c]+1 < dp[i]:
                    dp[i] = dp[i-c] + 1
                    if memo[i-c]:
                        memo[i] = [c]+memo[i-c]
                    else:
                        memo[i] = [c]

        for each_coin_value in memo[total_res]:
            res_coin_name.append(self.coins[each_coin_value])
        return res_coin_name


class product:
    def __init__(self,name,price,qut):
        self.name = name
        self.price = price
        self.quantity = qut

class coke(product,object):
    def __init__(self,name,price,qut):
        super(coke,self).__init__(name,price,qut)

class snack(product,object):
    def __init__(self,name,price,qut):
        super(snack,self).__init__(name,price,qut)


class vendorMachine:
    def __init__(self):

        self.products = {1:product("coke", 1.5, 20),2:product('chocolate', 2, 30)}
        self.coin_count = {'dime':100,'penny':1000,'nickel':100,'quater':100}

    def make_payment(self,bill):
        """
        machine take the money return True trigger the item choose function
        calculate the change machine need to send back call give it back
        :return: boolean
        """

        if self.checkMoney(bill):
            return True
        else:
            self.refund()

    def choose(self,id):
        """
        choose the item if exisit update the product via pro class
        :param item:
        :return: boolean
        """
        if self.checkProductavailable(id):
            self.products[id].quantity -= 1
            return True
        else:
            print("no item!")
            return False

    def display_items(self):
        """
        display all items in the machine including the price
        :return:void
        """
        for k,v in self.products.items():
            print ("No.{} item {} price is {} has {}".format(k,v.name,v.price,v.quantity))


    def checkMoney(self,bill):
        if bill <= 10:

            if bill < min([v.price for k,v in self.products.items()]):

                print("not enough money")
                return False
            else:
                return True
        else:
            return False


    def checkProductavailable(self,id):
        if self.products[id].quantity > 0:
            return True
        else:
            return False

    def takeItem(self):
        """
        sensor does
        :return:
        """
        print("processing")
        pass
    def calculate_change(self,bill,id):
        """
        calclate the residue money the machine will send back
        :param bill:
        :param id:
        :return: float
        """

        return bill - self.products[id].price

    def giveBackchange(self,bill,item):
        """
        sensor give residue to customer
        :return: void
        """
        res = self.calculate_change(bill,item)
        if res == 0:
            print("no need to return")
        else:
            coin = coins()
            print(coin.arrage_coins(res))
            print("processing")
            return coin.arrage_coins(res)

    def calculate_coin_count(self,coin_back):
        """
        calculate the coins left
        :param coin_back: 
        :return: 
        """
        for each_coin in coin_back:
            self.coin_count[each_coin] -= 1

    def errorcheck(self):

        pass

    def refund(self):
        """
        press button and force to exit
        :return: 
        """
        print("processing")
import sys
import datetime
def main():


    v  = vendorMachine()

    while True:
        print("This is Vendor Machine system!")
        # if v.errorcheck():
        #     break

        while True:
            print("please insert your card or cash! only 1,5 or 10")
            bill = input()
            ans = v.make_payment(bill)
            if not ans:
                print("your bill will be returned")
                v.refund()
                break
            else:

                v.display_items()
                print("Enter item number:")
                id = input()
                while True:

                    if v.choose(id):
                        break
                coins_back = v.giveBackchange(bill,id)
                v.calculate_coin_count(coins_back)
                print (v.coin_count)




if __name__ == '__main__':
    main()



