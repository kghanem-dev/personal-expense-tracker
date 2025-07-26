# Personal Expense Tracker

A beginner-friendly Python CLI app to track your personal expenses by category. Easily add, list, filter, and summarize expenses. All with persistent data storage using JSON.

## Features

- Add and categorize new expenses
- List all expenses in a clean table format
- View total spending or by category
- Filter expenses by category
- Persistent storage (saved to `expenses.json`)
- Clean command-line interface with optional color
- Graceful fallback if `colorama` is not installed

## Demo

```bash
=== Expense Tracker ===
1. Add an expense
2. List all expenses
3. Show total expenses
4. Filter expenses by category
5. Show total expenses by category
6. Exit
Current: 3 entries, Total: $45.67
Enter your choice: 
```

## Requirements

- Python 3.7+
- (Optional) colorama for colored output

```bash
pip install colorama
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/kghanem-dev/personal-expense-tracker.git
cd personal-expense-tracker
```

2. Run the app:

```bash
python expense_tracker.py
```

3. Your expenses are saved automatically in `expenses.json`.

## Usage Examples

### Adding an Expense
```
Enter your choice: 1
Enter amount: 25.50
Enter category: groceries
Expense added and saved successfully!
```

### Viewing All Expenses
```
Amount     | Category
-------------------------
$25.50     | groceries
$12.99     | entertainment
$7.18      | transportation
```

### Category Totals
```
Total by Category:
groceries: $25.50
entertainment: $12.99
transportation: $7.18
```

## File Structure

```
personal-expense-tracker/
├── expense_tracker.py    # Main application
├── expenses.json        # Data storage (created automatically)
└── README.md           # This file
```

## Contributing

This is a beginner project for learning Python fundamentals. Feel free to fork and experiment with additional features like:

- Date tracking for expenses
- Budget limits and warnings
- Data visualization
- Export to CSV
- Multiple currency support

## License

This project is open source and available under the [MIT License](LICENSE). 
