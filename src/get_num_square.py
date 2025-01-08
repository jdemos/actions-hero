import os

# get the input and convert it to int
num = os.environ.get("INPUT_NUM")

def get_num_square(num):
    return num ** 2

if __name__ == "__main__":
    try:
        num = int(num)
        print(f"The square of {num} is {get_num_square(num)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")