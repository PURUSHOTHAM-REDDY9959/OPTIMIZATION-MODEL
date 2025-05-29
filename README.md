# OPTIMIZATION-MODEL:

**COMPANY**  : CODTECH IT SOLUTIONS

**NAME**     : POLASANI PURUSHOTHAM REDDY

**INTERN ID**: CT08DN1100

**DOMAIN**   : DATA SCIENCE

**DURATION** : 8 WEEEKS

**MENTOR**   : NEELA SANTOSH



# DESCRIPTION:

# 🧠 Product Mix Optimization using Linear Programming and Python (PuLP)

This project demonstrates how to solve a real-world business problem using **Linear Programming (LP)** with the **PuLP** optimization library in Python. The problem modeled here is a classic **Product Mix Optimization** scenario often encountered in operations management.This project also  demonstrates how to apply Linear Programming (LP) techniques to solve a classic product mix optimization problem using Python. It focuses on helping a manufacturer determine the optimal quantity of products to produce in order to maximize profit while respecting resource constraints (e.g., machine hours).

In this scenario, the company manufactures two products — Product A and Product B — using two machines with limited weekly availability. Each product has a specific profit value and requires different amounts of time on each machine. The goal is to decide how many units of each product to produce so that the company earns the highest possible profit, without exceeding the available machine time
This project illustrates how mathematical optimization can be used in business decision-making. Whether in manufacturing, logistics, supply chain, or finance, linear programming is a powerful tool for making data-driven decisions under constraints.

It also provides a practical example of how Python can be used not just for data analysis, but for prescriptive analytics — guiding optimal action based on models.



## 📌 Problem Overview

A manufacturing factory produces two products — **Product A** and **Product B**. Each of these products requires processing time on two different machines:

- **Machine 1** has a limited number of hours available per week (100 hours).
- **Machine 2** also has a constraint on usage (80 hours).

Each product contributes a different profit and consumes machine time differently.

| Product     | Profit per Unit | Machine 1 Time (hrs) | Machine 2 Time (hrs) |
|-------------|-----------------|----------------------|----------------------|
| Product A   | $20             | 2                    | 1                    |
| Product B   | $30             | 1                    | 2                    |

### Objective

Maximize total profit by determining how many units of each product to produce, without exceeding machine time constraints.

## 🔧 Solution Approach

The problem is modeled using **Linear Programming (LP)**. The core steps in solving it include:

1. **Defining decision variables**: Let `x` be the units of Product A, and `y` be the units of Product B.
2. **Objective function**: Maximize `20x + 30y`.
3. **Constraints**:
   - `2x + y ≤ 100` (Machine 1 capacity)
   - `x + 2y ≤ 80` (Machine 2 capacity)
   - `x, y ≥ 0` (Non-negativity)

We implement this using the **PuLP** library in Python, which provides a clean and readable interface for defining LP problems and invoking solvers.


## 🧪 Technologies Used

- **Python 3**
- **PuLP** (for linear programming)
- **Matplotlib** (for visualization)
- **Jupyter Notebook / VS Code** (for development environment)
✅ Models a real-world business optimization problem using LP

✅ Solves the problem using the PuLP optimization library

✅ Visualizes the solution using Matplotlib

✅ Can be extended to more complex scenarios involving more products, constraints, or objectives




# OUTPUT :

![Image](https://github.com/user-attachments/assets/d3fb0789-3bff-4ef7-9a25-7c793606d47d)

