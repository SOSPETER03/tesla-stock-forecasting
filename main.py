"""
Main entry point for the Tesla stock forecasting pipeline.
"""

from src.preprocessing import portfolio_project

def main():
    print("🚀 Starting Tesla Stock Forecasting Pipeline...")
    # Call your preprocessing or model pipeline here
    portfolio_project.run_pipeline()

if __name__ == "__main__":
    main()
