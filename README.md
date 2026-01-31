# Net Salary Calculator

This is a simple Python program that calculates a person's **net salary**
based on their **gross salary** and the **number of children** they have.

## How it works
- The program applies a tax rate based on the gross salary
- The tax rate is reduced depending on the number of children
- The final net salary is printed to the console

## Tax rules
- If gross < 1000 → 10% tax
- If gross < 2000 → 12% tax
- If gross < 4000 → 14% tax
- If gross ≥ 4000 → 18% tax
- Child tax reduction:
  - If gross < 2000 → 1% per child
  - If gross ≥ 2000 → 0.5% per child
