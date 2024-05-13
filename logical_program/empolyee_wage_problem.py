import random

class EmployeeWageCalculator:
    def __init__(self, wage=20, full_day=8):
        """
        Initializes the EmployeeWageCalculator object with default wage per hour and full day hours.

        Args:
            wage (int, optional): Wage per hour. Defaults to 20.
            full_day (int, optional): Hours in a full day. Defaults to 8.
        """
        self.wage = wage
        self.full_day = full_day
        
    def attendance(self):
        return random.randint(0, 1)
      
    def daily_wage(self):
        """
        Calculates the daily wage
        """
        return self.wage * self.full_day
    
    def monthly_wage(self, working_days):
        """
        Calculates the monthly wage.
        daily_eage * working_days
        Args:
            working_days : Number of working days in the month.
        Returns:
            int: Monthly wage.
            
        """
        return self.daily_wage() * working_days
    
    def calculate(self, total_hours, total_days):
        """
        Calculates the total wage until a condition of total working hours or days is reached.

        Args:
            total_hours : Total working hours condition.
            total_days: Total working days condition.

        Returns:
         Total employee wage till condition.
        """
        total_wage = hours_worked = days_worked = 0
        
        while hours_worked < total_hours and days_worked < total_days:
            if self.attendance() == 1:
                hours_worked += self.full_day
                days_worked += 1
                total_wage += self.daily_wage()
        return total_wage

def main():
    """
    Main function to demonstrate EmployeeWageCalculator functionality.
    """
    print("Welcome to Employee Wage Problem")
    print("START")
    
    calculator = EmployeeWageCalculator()
    
    daily_wage = calculator.daily_wage()
    print("UC 1: Daily Employee Wage:", daily_wage)
    
    working_days_per_month = 20
    monthly_wage = calculator.monthly_wage(working_days_per_month)
    print("UC 4: Monthly Employee Wage:", monthly_wage)

    total_hours_condition = 100
    total_days_condition = 20
    total_wage_condition = calculator.calculate(total_hours_condition, total_days_condition)
    print("UC 5: Total Employee Wage till Condition:", total_wage_condition)

if __name__ == "__main__":
    main()
