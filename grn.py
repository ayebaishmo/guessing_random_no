import random

# guess the number
class ran_no:
    def __init__(self, first):
        self.first = first
    
    def r1_10(self):
        self.first = random.randint(1, 5)
        return self.first
    
    def __repr__(self):
        return str(self.first)
    
    def your_inp(self, k):
        self.k =k
        if self.first == self.k:
            return f"{self.k} and the right number {self.first} You guessed right"
        else:
            return f"{self.k} and the right number {self.first} You didn't get it right"
    
if __name__ == '__main__':
    ran_no1 = ran_no(1)
    print(ran_no1.r1_10())
    print(ran_no1.your_inp(5))
