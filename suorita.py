import pandas as pd

from electricity_cost_calculator import Scenario
from electricity_cost_calculator import calculate_total_cost
from electricity_cost_calculator import print_results

df = pd.read_csv("data.csv", parse_dates=[0])

print()
print("Tervetuloa pörssisähkön hintalaskuriin. (perustuu https://porssisahko.net/tilastot dataan)")
year = int(input("Syötä tarkasteluvuosi (2021-2025 väliltä) --> "))
yearly_consumption = int(input("Syötä vuoden kulutus (kwh) --> "))
charging_start_end_s = input("Syötä päivittäinen latausväli (aloitustunti-lopetustunti) --> ")
charging_start_end = [int(x) for x in charging_start_end_s.strip().split("-")]

charging_hours = list(range(charging_start_end[0], charging_start_end[1]))

s = Scenario("", year, yearly_consumption, charging_hours)

cost = calculate_total_cost(s, df)
print()
print_results(s, cost, lang="Finnish")

print("kiitos heihei!\n")