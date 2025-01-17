import pandas as pd
from datetime import time

class Scenario():
    def __init__(self, name: str, year: int, total_consumption: int, charging_hours: list):
        self.name = name
        self.year = year
        self.total_consumption = total_consumption
        self.charging_hours = charging_hours

        self.daily_usage = self.total_consumption/365
        self.hourly_charge = self.daily_usage/len(self.charging_hours)

def calculate_total_cost(scenario:Scenario, df):
    df = df[df['timestamp']>f'{scenario.year}-01-01']
    df = df[df['timestamp']<f'{scenario.year+1}-01-01']

    df = df[df['timestamp'].dt.time>=time(min(scenario.charging_hours))]
    df = df[df['timestamp'].dt.time<=time(max(scenario.charging_hours))]

    df["cost2"] = df['cost'].mul(scenario.hourly_charge).to_frame('cost2')

    return df["cost2"].sum()/100

def print_results(scenario:Scenario, cost, lang="English"):
    if lang=="Finnish":
        print(f"Skenaario: {scenario.name}")
        print(f"Vaadittu laturin latauskyky: {scenario.hourly_charge:.2f} kwh/h:")
        print(f"Lataustunteja päivässä: {len(scenario.charging_hours)} h")
        print(f"Päivittäinen kulutus: {scenario.daily_usage} kwh")
        print()
        print(f"Lasketut kokonaiskustannukset vuodelle: {cost:.2f} €")
        print()
    else:
        print(f"Scenario: {scenario.name}")
        print(f"Required charger capability: {scenario.hourly_charge:.2f} kwh/h:")
        print(f"Total yearly cost: {cost:.2f} €")
        print()
    

