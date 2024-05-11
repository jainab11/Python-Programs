import random

class CouponCollector:
    """  the generate_coupon_numbers(n) function is used to create a set containing n 
    unique coupon numbers, which represent the different types of coupons available in the problem. This 
    set is then used to simulate the process of collecting
    coupons until at least one of each type has been obtained."""
    @staticmethod
    def generate_coupon_numbers(n):
        return set(random.sample(range(1, n + 1), n))

    @staticmethod
    def collect_coupons(n):
        # store distinct value in set
        distinct_coupons = set()
        # how many attempts it take to grnrate n nomber of coupon
        total_attempts = 0
        while len(distinct_coupons) < n:
            random_number = random.randint(1, n)
            total_attempts += 1
            distinct_coupons.add(random_number)
        return total_attempts

def main():
    # taking valid input from user
    while True:
        try:
            num_coupons = int(input("Enter the number of coupons: "))
            if num_coupons <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    total_attempts = CouponCollector.collect_coupons(num_coupons)
    # print total attempts it take tp genrate random coupon
    print(f"Total attempts to collect all {num_coupons} coupons: {total_attempts}")

if __name__ == "__main__":
    main()
