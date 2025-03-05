{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 NewBaskervilleStd-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11905\paperh16837\margl1133\margr1133\margb1133\margt1133
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \up0 \nosupersub \ulnone import matplotlib.pyplot as plt\
import random\
\
def simulate_wrecked_village(villagers, loan_per_villager, interest_rate, years):\
    total_money = villagers * loan_per_villager\
    villager_list = [loan_per_villager for _ in range(villagers)]\
    yearly_summary = []\
\
    for year in range(1, years + 1):\
        # Step 1: Previous year's debts accumulate interest\
        villager_list = [debt * (1 + interest_rate) for debt in villager_list]\
\
        # Step 2: Calculate total debt before repayment\
        total_debt_before_repayment = sum(villager_list)\
\
        # Step 3: Randomize repayment order\
        random.shuffle(villager_list)\
\
        # Step 4: Villagers attempt repayment\
        available_money = total_money\
        winners = 0\
        for i in range(villagers):\
            if available_money >= villager_list[i]:\
                available_money -= villager_list[i]\
                villager_list[i] = 0\
                winners += 1\
            else:\
                villager_list[i] -= available_money\
                available_money = 0\
\
        losers = villagers - winners\
        unpaid_debt = sum(villager_list)\
\
        # Record summary explicitly\
        yearly_summary.append(\{\
            'year': year,\
            'total_debt_before_repayment': total_debt_before_repayment,\
            'unpaid_debt_carried_over': unpaid_debt,\
            'winners': winners,\
            'losers': losers\
        \})\
\
        # Step 5: Villagers borrow again next year (without immediate interest)\
        villager_list = [debt + loan_per_villager for debt in villager_list]\
\
    return yearly_summary\
\
\
def plot_results(summary, villagers, loan_per_villager):\
    years_list = [entry['year'] for entry in summary]\
    total_debt_before = [entry['total_debt_before_repayment'] for entry in summary]\
    unpaid_debt_carried_over = [entry['total_debt_before_repayment'] - villagers * loan_per_villager for entry in summary]\
    percentage_unpaid = [(unpaid / (villagers * loan_per_villager)) * 100 for unpaid in unpaid_debt_carried_over]\
    winners_list = [entry['winners'] for entry in summary]\
    losers_list = [entry['losers'] for entry in summary]\
\
    # Debt Accumulation Plot\
    plt.figure(figsize=(12, 6))\
    plt.plot(years_list, total_debt_before, 'ro-', label='Debt before repayment')\
    plt.plot(years_list, unpaid_debt_carried_over, 'bo-', label='Unpaid Debt Carried Over')\
    plt.title('Randomized Debt Simulation: Debt Accumulation')\
    plt.xlabel('Year')\
    plt.ylabel('Debt (dinars)')\
    plt.grid(True)\
    plt.legend()\
    plt.tight_layout()\
    plt.show()\
\
    # Percentage Unpaid Debt Plot\
    plt.figure(figsize=(10, 6))\
    plt.plot(years_list, percentage_unpaid, 'mo-', label='% Unpaid Debt to Principal')\
    plt.title('Percentage of Unpaid Debt Relative to Principal (500 dinars)')\
    plt.xlabel('Year')\
    plt.ylabel('Unpaid Debt (%)')\
    plt.grid(True)\
    plt.legend()\
    plt.tight_layout()\
    plt.show()\
\
    # Winners vs Losers Plot\
    plt.figure(figsize=(10, 6))\
    plt.plot(years_list, winners_list, 'go-', label='Winners (Fully Repaid)')\
    plt.plot(years_list, losers_list, 'ro-', label='Losers (Not Fully Repaid)')\
    plt.title('Number of Winners and Losers Each Year')\
    plt.xlabel('Year')\
    plt.ylabel('Number of Villagers')\
    plt.grid(True)\
    plt.legend()\
    plt.tight_layout()\
    plt.show()\
\
\
def print_summary(summary, villagers, loan_per_villager, years):\
    total_initial_principal = villagers * loan_per_villager\
    last_year_total_debt = summary[-1]['total_debt_before_repayment']\
    last_year_winners = summary[-1]['winners']\
    last_year_losers = summary[-1]['losers']\
\
    print("\\n--- Simulation Summary ---")\
    print(f"Number of villagers: \{villagers\}")\
    print(f"Loan per villager: \{loan_per_villager\} dinars")\
    print(f"Number of years simulated: \{years\}")\
    print(f"Total initial loan principal: \{total_initial_principal\} dinars")\
    print(f"Last period's total debt: \{last_year_total_debt:.2f\} dinars")\
    print(f"Last period's number of winners: \{last_year_winners\}")\
    print(f"Last period's number of losers: \{last_year_losers\}")\
\
def main():\
    # Simulation parameters clearly defined\
    villagers = 5\
    loan_per_villager = 100\
    interest_rate = 0.04\
    years = 4\
\
    # Run simulation\
    summary = simulate_wrecked_village(villagers, loan_per_villager, interest_rate, years)\
\
    # Plot results explicitly\
    plot_results(summary, villagers, loan_per_villager)\
\
    # Print clear summary\
    print_summary(summary, villagers, loan_per_villager, years)\
\
if __name__ == "__main__":\
    main()\
\
}