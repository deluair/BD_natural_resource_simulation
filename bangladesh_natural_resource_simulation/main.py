# main.py

import time
import json
import os

from bangladesh_natural_resource_simulation.simulation import BangladeshNaturalResourceSimulation
from bangladesh_natural_resource_simulation.analysis.engine import NaturalResourceAnalysisEngine
from bangladesh_natural_resource_simulation.config import ACTIVE_CONFIG # Import the chosen config

def main():
    """Main function to run the simulation and analysis."""
    
    start_time = time.time()
    print(f"Starting Simulation run with config: {ACTIVE_CONFIG['simulation_name']}")
    print(f"Scenario: {ACTIVE_CONFIG['scenario']}")
    print(f"Period: {ACTIVE_CONFIG['start_year']}-{ACTIVE_CONFIG['end_year']}")
    
    # 1. Initialize Simulation
    simulation = BangladeshNaturalResourceSimulation(config=ACTIVE_CONFIG)
    
    # 2. Run Simulation
    results = simulation.run_simulation(
        start_year=ACTIVE_CONFIG['start_year'],
        end_year=ACTIVE_CONFIG['end_year']
        # scenarios parameter could be used here if implemented
    )
    
    # --- Optional: Save raw results --- 
    output_dir = ACTIVE_CONFIG.get("output_dir", "./outputs/")
    os.makedirs(output_dir, exist_ok=True)
    results_filename = os.path.join(output_dir, f"simulation_results_{ACTIVE_CONFIG['scenario']}.json")
    try:
        with open(results_filename, 'w') as f:
            # Use default=str to handle potential non-serializable types if models become complex
            json.dump(results, f, indent=4, default=str) 
        print(f"Raw simulation results saved to: {results_filename}")
    except Exception as e:
        print(f"Error saving raw results: {e}")
        
    # 3. Initialize and Run Analysis Engine
    analysis_engine = NaturalResourceAnalysisEngine(simulation_results=results, config=ACTIVE_CONFIG)
    analysis_output = analysis_engine.run_analysis()
    
    end_time = time.time()
    print(f"\nTotal execution time: {end_time - start_time:.2f} seconds")
    print("Simulation and Analysis complete. Check the output directory for results.")
    print(f"Report generated at: {analysis_engine.report_file}")

if __name__ == "__main__":
    main() 