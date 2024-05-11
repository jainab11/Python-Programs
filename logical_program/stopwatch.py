import time
def stopwaatch():
    start_time = time.time()
    input("press enter to stop watch : ")
    end_time = time.time()
    elaspsed_time = end_time - start_time
    print("Elasped time {:.2f} seconds".format(elaspsed_time))
def main():
    input("press enter to start stopwaatch : ")
    stopwaatch()
if __name__ == "__main__":
    main()