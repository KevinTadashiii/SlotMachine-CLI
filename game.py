class Game:
    # ... (other methods)

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
            # ... (other code)
