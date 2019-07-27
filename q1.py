'''TO FIND THE SIMPLE INTEREST'''

PRINCIPLE = int(input("Principle?"))
TIME = float(input("Time?"))
RATE_OF_INTEREST = int(input("Rate of interest?"))
SIMPLE_INTEREST = PRINCIPLE*TIME*(RATE_OF_INTEREST/100)
print(f"Simple Interest:{SIMPLE_INTEREST}")