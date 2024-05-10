import random
def flip_coin(num_flip):
    if num_flip <= 0:
        print("Number should be greter that zero :")
        return
    head_count = 0
    tail_count = 0
    for _ in range(num_flip):
        if random.random()>0.5:
            head_count += 1
        else:
            tail_count +=1
    percentage_head = (head_count/num_flip)*100
    percentage_tail = (tail_count/num_flip)*100
    
    print(f" percentage of head is {percentage_head}")
    print(f" percentage of tail is {percentage_tail}")
number = int(input("Enter a number of time you want to flip a coin : " ))
flip_coin(number)