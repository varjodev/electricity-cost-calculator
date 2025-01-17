import pandas as pd

from electricity_cost_calculator import Scenario
from electricity_cost_calculator import calculate_total_cost
from electricity_cost_calculator import print_results

if __name__=="__main__":
    # Read hourly pörssisähkö data (columns: timestamp, cost)
    df = pd.read_csv("data.csv", parse_dates=[0])

    # Define scenarios
    year = 2024
    yearly_consumption = 20000
    scenarios = []
    
    scenarios.append(Scenario("constant", year, yearly_consumption, list(range(0,24))))
    scenarios.append(Scenario("night", year, yearly_consumption, list(range(0,8))))
    scenarios.append(Scenario("day", year, yearly_consumption, list(range(10,18))))

    # Calculate and print the result for each scenario
    print()
    costs = []
    for scenario in scenarios:
        cost = calculate_total_cost(scenario, df)
        costs.append(cost)
        print_results(scenario, cost)
        

    