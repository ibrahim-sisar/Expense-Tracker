

# Expense-Tracker 💰
https://roadmap.sh/projects/expense-tracker

## Description
expense tracker is to manage your finances. The program allow users to add, delete, and view their expenses. The program also provide a summary of the expenses.

---

## Features
- Users can add an expense with a description and amount.
- Users can update or delete an expense.
- Users can view all expenses.
- Users can view a summary of all expenses.
- Users can view a summary of expenses for a specific month (of current year).

---

## Prerequisites
Before you begin, make sure you have the following installed:
- python3.8+
- json lib

---

## Installation
Follow these steps to set up the project locally:

  1. Clone the repository:
     ```bash
     git clone https://github.com/username/Expense-Tracker.git
     ```
  2. Navigate to the project directory:
    ```bash
    cd Expense-Tracker
    ```
  3. Run code:
     ```bash
     python main.py
     ```
## Usage
  ```bash
$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10

$ expense-tracker summary
# Total expenses: $30

$ expense-tracker delete --id 2
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20

$ expense-tracker summary --month 8
# Total expenses for August: $20
  ```
  

## Technologies Used
  - python
  - json
  - datetime

## Contributing
  #### Contributions are welcome! Please follow these steps:
   1. Fork the repository.
   2. Create a new branch:
      ```bash
        git checkout -b feature-name
      ```
   3. Commit your changes:
      ```bash
      git commit -m "Add your message here"
      ```
   4. Push to the branch:
      ```bash
      git push origin feature-name
      ```
   5. Open a pull request.

## License
   This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

  
  
