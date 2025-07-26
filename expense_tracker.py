"""
Personal Expense Tracker
A simple command-line application for tracking personal expenses by category.
"""

import json
from collections import defaultdict
try:
    from colorama import Fore, Style, init
    init()  # Initialize colorama
    COLORS_AVAILABLE = True
except ImportError:
    # Fallback if colorama is not installed
    COLORS_AVAILABLE = False
    class Fore:
        GREEN = RED = YELLOW = CYAN = ""
    class Style:
        RESET_ALL = ""

def add_expense(expenses, amount, category):
    """Add a new expense to the expenses list."""
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    """Display all expenses in a formatted table."""
    if not expenses:
        print(f"{Fore.YELLOW}No expenses recorded.{Style.RESET_ALL}")
        return
    
    # Create table header with proper formatting
    print(f"\n{Fore.CYAN}{'Amount':<10} | Category{Style.RESET_ALL}")
    print('-' * 25)
    for expense in expenses:
        print(f"${expense['amount']:<9.2f} | {expense['category']}")
    
def total_expenses(expenses):
    """Calculate and return the sum of all expenses."""
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    """Return expenses filtered by the specified category."""
    return filter(lambda expense: expense['category'] == category, expenses)

def category_totals(expenses):
    """Calculate total expenses by category."""
    totals = defaultdict(float)
    for exp in expenses:
        totals[exp['category']] += exp['amount']
    return totals

def save_expenses_to_file(expenses, filename='expenses.json'):
    """Save expenses list to JSON file for persistence."""
    try:
        with open(filename, 'w') as f:
            json.dump(expenses, f, indent=2)
    except IOError as e:
        print(f"{Fore.RED}Error saving to file: {e}{Style.RESET_ALL}")

def load_expenses_from_file(filename='expenses.json'):
    """Load expenses from JSON file, return empty list if file not found."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Return empty list if file doesn't exist or is corrupted
        return []

def main():
    """Main program loop with interactive menu."""
    # Load existing expenses from file
    expenses = load_expenses_from_file()
    
    # Show welcome message with loaded data info
    if expenses:
        print(f"{Fore.GREEN}Loaded {len(expenses)} existing expenses.{Style.RESET_ALL}")
    
    while True:
        # Display menu options with color
        print(f'\n{Fore.GREEN}=== Expense Tracker ==={Style.RESET_ALL}')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Show total expenses by category')
        print('6. Exit')
        
        # Show current stats if expenses exist
        if expenses:
            total = total_expenses(expenses)
            count = len(expenses)
            print(f'{Fore.CYAN}Current: {count} entries, Total: ${total:.2f}{Style.RESET_ALL}')
       
        choice = input('Enter your choice: ')

        # Handle adding new expense with validation
        if choice == '1':
            try:
                amount = float(input('Enter amount: '))
                category = input('Enter category: ').strip()
                if category:  # Ensure category is not empty
                    add_expense(expenses, amount, category)
                    # Save to file after adding expense
                    save_expenses_to_file(expenses)
                    print(f"{Fore.GREEN}Expense added and saved successfully!{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Category cannot be empty.{Style.RESET_ALL}")
            except ValueError:
                # Handle non-numeric input gracefully
                print(f"{Fore.RED}Invalid input. Please enter a numeric value.{Style.RESET_ALL}")

        # Display all expenses in formatted table
        elif choice == '2':
            print(f'\n{Fore.CYAN}All Expenses:{Style.RESET_ALL}')
            print_expenses(expenses)
    
        # Calculate and show total expenses
        elif choice == '3':
            total = total_expenses(expenses)
            print(f'\n{Fore.GREEN}Total Expenses: ${total:.2f}{Style.RESET_ALL}')
    
        # Filter and display expenses by category
        elif choice == '4':
            category = input('Enter category to filter: ').strip()
            print(f'\n{Fore.CYAN}Expenses for {category}:{Style.RESET_ALL}')
            # Convert filter iterator to list for proper display
            expenses_from_category = list(filter_expenses_by_category(expenses, category))
            print_expenses(expenses_from_category)
        
        # Show breakdown of totals by category
        elif choice == '5':
            print(f"\n{Fore.CYAN}Total by Category:{Style.RESET_ALL}")
            totals = category_totals(expenses)
            if totals:
                for category, total in totals.items():
                    print(f"{category}: ${total:.2f}")
            else:
                print(f"{Fore.YELLOW}No expenses recorded.{Style.RESET_ALL}")
    
        # Exit program and save data
        elif choice == '6':
            # Final save before exit
            save_expenses_to_file(expenses)
            print(f'{Fore.GREEN}Data saved. Exiting the program.{Style.RESET_ALL}')
            break
        
        # Handle invalid menu choices
        else:
            print(f"{Fore.RED}Invalid choice. Please select 1-6.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()