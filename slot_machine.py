import random
import time
import os
import json
import atexit
import signal
import sys

class SlotMachine:
    def __init__(self):
        self.fruits = {
            "orange": "🍊",
            "lemon": "🍋",
            "cherry": "🍒",
            "grape": "🍇",
            "watermelon": "🍉",
            "mango": "🥭",
            "pineapple": "🍍",
            "peach": "🍑",
            "kiwi": "🥝",
            "blueberry": "🫐",
            "jackpot": "⭐"
        }
        self.chances = {
            "jackpot": 0.01,  # 1% chance of jackpot
            "big_win": 0.03,  # 3% chance of big win
            "small_win": 0.05,  # 5% chance of small win
            "zonk": 0.91  # 91% chance of zonk
        }

    def spin(self, bet, auto_spin=False):
        print("Spinning... 🔄")
        if not auto_spin:
            time.sleep(1)
        elif auto_spin:
            time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")

        outcome = random.random()
        slots = self._determine_slots(outcome)
        self._print_slots(slots, animate=True, auto_spin=auto_spin)

        return self._determine_payout(slots, bet)

    def _determine_slots(self, outcome):
        if outcome < self.chances["jackpot"]:  
            return ["jackpot", "jackpot", "jackpot"]
        elif outcome < self.chances["jackpot"] + self.chances["big_win"]:  
            return ["orange", "orange", "orange"]
        elif outcome < self.chances["jackpot"] + self.chances["big_win"] + self.chances["small_win"]:  
            fruit = random.choice([fruit for fruit in self.fruits.keys() if fruit not in ["jackpot", "orange"]])
            return [fruit, fruit, fruit]
        else:  
            return [random.choice([fruit for fruit in self.fruits.keys() if fruit != "jackpot"]),
                    random.choice([fruit for fruit in self.fruits.keys() if fruit != "jackpot"]),
                    random.choice([fruit for fruit in self.fruits.keys() if fruit != "jackpot"])]

    def _print_slots(self, slots, animate, auto_spin=False):
        if animate:
            print("---------------")
            print(f"| {self.fruits[slots[0]]} |   |   |")
            print("---------------")
            if auto_spin:
                time.sleep(0.2)
            else:
                time.sleep(0.5)
            os.system("cls" if os.name == "nt" else "clear")
            print("---------------")
            print(f"| {self.fruits[slots[0]]} | {self.fruits[slots[1]]} |   |")
            print("---------------")
            if auto_spin:
                time.sleep(0.2)
            else:
                time.sleep(0.5)
            os.system("cls" if os.name == "nt" else "clear")
            print("---------------")
            print(f"| {self.fruits[slots[0]]} | {self.fruits[slots[1]]} | {self.fruits[slots[2]]} |")
            print("---------------")
            if auto_spin:
                time.sleep(0.2)
            else:
                time.sleep(0.5)
        else:
            print("---------------")
            print(f"| {self.fruits[slots[0]]} | {self.fruits[slots[1]]} | {self.fruits[slots[2]]} |")
            print("---------------")
            time.sleep(0.5)

    def _determine_payout(self, slots, bet):
        if slots[0] == slots[1] == slots[2]:
            if slots[0] == "jackpot":
                print("⭐⭐ JACKPOT! ⭐⭐")
                return bet * 1000
            elif slots[0] == "orange":
                print("🎉 BIG WIN! 🎉")
                return bet * 200
            else:
                print("🎊 SMALL WIN! 🎊")
                return bet * 10
        else:
            print("😐 Better luck next time! 😐")
            return -bet

class Game:
    def __init__(self):
        self.save_file = "SaveData/balance.json"
        self.balance = self.load_balance()
        self.auto_spin = False
        self.bet = 0
        self.slot_machine = SlotMachine()
        atexit.register(self.save_balance)
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, sig, frame):
        self.save_balance()
        print("\n👋 Thanks for playing! 👋")
        sys.exit(0)

    def load_balance(self):
        try:
            with open(self.save_file, "r") as f:
                save_data = json.load(f)
                return save_data["balance"]
        except FileNotFoundError:
            return 100

    def save_balance(self):
        save_data = {"balance": self.balance}
        with open(self.save_file, "w") as f:
            json.dump(save_data, f)

    def play(self):
        while True:
            print(f"Balance: ${self.balance} 💸")
            if self.balance <= 0:
                print("😔 You've run out of money! 😔")
                print("Here's $10 to play again! 🎁")
                self.balance = 10
            if self.bet == 0:
                self.bet = int(input("Enter your bet for all spins: "))
                if self.bet > self.balance:
                    print("Insufficient balance!")
                    self.bet = 0
                    continue
            if not self.auto_spin:
                print("Press Enter to spin the slot machine\ntype 'auto' to enable auto spin\ntype 'exit' to quit")
                action = input("")
                if action.lower() == 'auto':
                    self.auto_spin = True
                    num_spins = int(input("Enter the number of auto spins: "))
                elif action.lower() == 'exit':
                    self.save_balance()
                    print("👋 Thanks for playing! 👋")
                    break
            if self.auto_spin:
                if num_spins > 0:
                    print(f"Auto spin {num_spins} 🔄")
                    num_spins -= 1
                    self.balance += self.slot_machine.spin(self.bet, auto_spin=True)
                    if self.balance <= 0:
                        self.save_balance()
                        print("😔 You've run out of money! 😔")
                        break
                else:
                    self.auto_spin = False
            else:
                self.balance += self.slot_machine.spin(self.bet)
                if self.balance <= 0:
                    self.save_balance()
                    print("😔 You've run out of money! 😔")
                    break

def main():
    print("Slot Machine Game 🎰")
    print("-----------------")
    while True:
        print("1. Play 🎲")
        print("2. Exit 👋")
        choice = input("Enter your choice: ")
        if choice == "1":
            game = Game()
            game.play()
        elif choice == "2":
            print("👋 Thanks for playing! 👋")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
