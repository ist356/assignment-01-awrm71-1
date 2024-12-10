'''
Write a python program to input integer values until a 0 is entered.
For each input integer if its odd, store in a dictionary under the key 'odd' 
and if its even, store in a dictionary under the key 'even'.

After a zero is entered, print the dictionary.

For example, if the input is:
2 3 5 4 6 0 

The output should be:
{'odd': [3, 5], 'even': [2, 4, 6]}
'''

def main():
    numbers = {'odd': [], 'even': []}  # Initialize the dictionary
    while True:
        try:
            value = int(input("Enter an integer (0 to stop): "))
            if value == 0:
                break
            if value % 2 == 0:
                numbers['even'].append(value)  # Append to 'even' key
            else:
                numbers['odd'].append(value)  # Append to 'odd' key
        except ValueError:
            print("Please enter a valid integer.")
    
    print(numbers)  # Print the dictionary

if __name__ == "__main__":
    main()