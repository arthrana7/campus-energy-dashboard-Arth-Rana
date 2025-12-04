import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.ingest import load_energy_data
from src.aggregate import calculate_daily_totals, calculate_weekly_aggregates, building_wise_summary
from src.visualize import generate_dashboard
from src.summary import export_outputs

df = load_energy_data("data")

daily = calculate_daily_totals(df)
weekly = calculate_weekly_aggregates(df)
summary = building_wise_summary(df)

generate_dashboard(daily, weekly, summary)

export_outputs(df, daily, weekly, summary)

print("Pipeline completed successfully!")

