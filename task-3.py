# write a python program to check whether a given year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


    # Python program to validate leap year logic with meaningful variable names and comments
    # Function to check if a given year is a leap year using meaningful variable names

    def is_leap_year(calendar_year):
        """
        Determines if the provided year is a leap year.

        Parameters:
        calendar_year (int): The year to be checked

        Returns:
        bool: True if leap year, False otherwise
        """
        # A leap year is divisible by 4
        if calendar_year % 4 == 0:
            # Except for years that are divisible by 100,
            # unless they are also divisible by 400
            if calendar_year % 100 == 0:
                return calendar_year % 400 == 0
            else:
                return True
        else:
            return False