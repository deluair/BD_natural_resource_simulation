import os
import matplotlib.pyplot as plt

class NaturalResourceAnalysisEngine:
    """Analyze and visualize natural resource simulation results"""
    def __init__(self, simulation_results, config):
        """
        Initializes the AnalysisEngine.
        
        Args:
            simulation_results (dict): The results collected from the simulation run.
            config: Configuration object/dictionary.
        """
        self.results = simulation_results
        self.config = config
        self.metrics = None # To store calculated metrics
        self.summary = None # To store analysis summary
        self.output_dir = config.get("output_dir", "./outputs/")
        self.viz_dir = os.path.join(self.output_dir, 'visualizations')
        self.report_file = os.path.join(self.output_dir, 'report.html')
        
        # Ensure output directories exist
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(self.viz_dir, exist_ok=True)
            
        print("Initializing Natural Resource Analysis Engine...")

    def generate_resource_metrics(self):
        """
        Calculate key natural resource indicators and metrics from simulation results for Bangladesh.
        
        Returns:
            dict: A dictionary of calculated metrics.
        """
        print("Generating resource metrics...")
        metrics = {}
        
        # Placeholder logic: Iterate through self.results 
        # Example: Extract end-state value or calculate trend
        try:
            years = sorted(self.results.keys())
            start_year = years[0]
            end_year = years[-1]
            
            # Example: Calculate total change in urban area
            start_urban_change = self.results[start_year]['land']['urban_area_expansion']
            end_urban_change = self.results[end_year]['land']['urban_area_expansion']
            # This is simplistic as it uses the *change* value, not the total area
            metrics['total_simulated_urban_expansion'] = sum(self.results[y]['land']['urban_area_expansion'] for y in years)
            
            metrics['water_availability_trend_placeholder'] = -0.5 
            metrics['land_degradation_rate_placeholder'] = 0.2 
            metrics['forest_carbon_balance_placeholder'] = -5e6 
            metrics['biodiversity_index_change_placeholder'] = -3.0 
            metrics['energy_renewable_share_2035'] = self.results[end_year]['energy']['energy_mix_renewable_share_change_percent_points'] + 3 # Assuming start was 3%
            metrics['marine_stock_sustainability_score_placeholder'] = 45 
            metrics['climate_vulnerability_end_change'] = self.results[end_year]['climate']['overall_vulnerability_index_change'] # Example end value
            metrics['governance_effectiveness_score_placeholder'] = 62 
            metrics['community_empowerment_end_change'] = self.results[end_year]['community']['community_empowerment_index_change'] # Example end value
            metrics['resource_efficiency_improvement_placeholder'] = 15 
            metrics['conservation_coverage_effectiveness_placeholder'] = 58

        except Exception as e:
            print(f"Error calculating metrics: {e}. Using placeholder values.")
            metrics = {k: v for k, v in metrics.items() if 'placeholder' in k} # Keep only placeholders if error
            metrics['error'] = str(e)
            
        print(f"Generated metrics (examples): {metrics}")
        self.metrics = metrics # Store for reporting
        return metrics

    def analyze_sustainability_dynamics(self):
        """
        Assess resource system evolution under different scenarios (if applicable) 
        and overall sustainability trends.
        """
        print("Analyzing sustainability dynamics...")
        # Placeholder logic:
        analysis_summary = {
            "scenario_name": self.config.get("scenario", "Unknown"),
            "simulation_period": f"{self.config.get('start_year', '?')}-{self.config.get('end_year', '?')}",
            "overall_sustainability_trend": "Mixed, progress in some areas, decline in others (placeholder assessment)",
            "key_tradeoffs": ["Land Use (Agri vs Urban) Placeholder", "Water (Irrigation vs Environment) Placeholder"],
            "critical_risks": ["Coastal Vulnerability Placeholder", "Groundwater Depletion Placeholder"],
        }
        print(f"Sustainability analysis summary (example): {analysis_summary}")
        self.summary = analysis_summary # Store for reporting
        return analysis_summary

    def generate_visualizations(self):
        """
        Generate plots and potentially dashboards to visualize the results.
        """
        print(f"Generating visualizations in {self.viz_dir}...")
        
        try:
            years = sorted(self.results.keys())
            # Example: Plot simulated urban area expansion per year
            urban_expansion = [self.results[y]['land']['urban_area_expansion'] for y in years]
            
            plt.figure(figsize=(10, 5))
            plt.plot(years, urban_expansion, marker='o', linestyle='-')
            plt.title('Simulated Annual Urban Area Expansion')
            plt.xlabel('Year')
            plt.ylabel('Area Expansion (sq km/yr - Placeholder)')
            plt.grid(True)
            plot_filename = os.path.join(self.viz_dir, 'urban_expansion_trend.png')
            plt.savefig(plot_filename)
            plt.close() # Close the plot to free memory
            print(f"Generated plot: {plot_filename}")

            # Add more plots here for other key variables...
            # Example: Water - Groundwater Level Change
            gw_level_change = [self.results[y]['water']['groundwater_level_change'] for y in years]
            plt.figure(figsize=(10, 5))
            plt.plot(years, gw_level_change, marker='s', linestyle='--', color='blue')
            plt.title('Simulated Annual Groundwater Level Change')
            plt.xlabel('Year')
            plt.ylabel('Change (m - Placeholder)')
            plt.grid(True)
            plot_filename_gw = os.path.join(self.viz_dir, 'groundwater_level_change.png')
            plt.savefig(plot_filename_gw)
            plt.close()
            print(f"Generated plot: {plot_filename_gw}")
            
        except Exception as e:
            print(f"Error generating visualizations: {e}")

    def generate_html_report(self):
        """
        Generates a simple HTML report summarizing the simulation results.
        """
        print(f"Generating HTML report: {self.report_file}...")
        
        if not self.metrics:
            print("Metrics not calculated yet. Running metric generation first.")
            self.generate_resource_metrics()
            
        if not self.summary:
            print("Sustainability analysis not performed yet. Running analysis first.")
            self.analyze_sustainability_dynamics()
            
        # Basic HTML Structure
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulation Report: {self.config.get("simulation_name", "Bangladesh Natural Resources")}</title>
    <style>
        body {{ font-family: sans-serif; margin: 20px; }}
        h1, h2 {{ color: #333; }}
        table {{ width: 100%; border-collapse: collapse; margin-bottom: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .summary-section {{ background-color: #eef; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
        img {{ max-width: 100%; height: auto; border: 1px solid #ccc; margin-top: 10px; }}
    </style>
</head>
<body>
    <h1>Simulation Report</h1>
    <p><strong>Simulation Name:</strong> {self.config.get("simulation_name", "N/A")}</p>
    <p><strong>Scenario:</strong> {self.summary.get("scenario_name", "N/A")}</p>
    <p><strong>Period:</strong> {self.summary.get("simulation_period", "N/A")}</p>

    <div class="summary-section">
        <h2>Sustainability Summary</h2>
        <p><strong>Overall Trend:</strong> {self.summary.get("overall_sustainability_trend", "N/A")}</p>
        <p><strong>Key Trade-offs Identified:</strong> {', '.join(self.summary.get("key_tradeoffs", []))}</p>
        <p><strong>Critical Risks Identified:</strong> {', '.join(self.summary.get("critical_risks", []))}</p>
    </div>

    <h2>Key Metrics</h2>
    <table>
        <thead>
            <tr><th>Metric</th><th>Value</th></tr>
        </thead>
        <tbody>
"""
        # Populate metrics table
        if self.metrics:
            for key, value in self.metrics.items():
                # Simple formatting for readability
                display_value = f"{value:.2f}" if isinstance(value, (int, float)) else value
                html_content += f"            <tr><td>{key.replace('_', ' ').title()}</td><td>{display_value}</td></tr>\n"
        else:
            html_content += "            <tr><td colspan=\"2\">No metrics calculated.</td></tr>\n"
            
        html_content += """
        </tbody>
    </table>

    <h2>Visualizations</h2>
    <p>(Placeholder plots generated from simulation outputs)</p>
    <div>
        <h3>Urban Expansion Trend</h3>
        <img src="visualizations/urban_expansion_trend.png" alt="Urban Expansion Trend Plot">
    </div>
    <div>
        <h3>Groundwater Level Change</h3>
        <img src="visualizations/groundwater_level_change.png" alt="Groundwater Level Change Plot">
    </div>
    <!-- Add more img tags for other generated plots -->

</body>
</html>
"""
        
        try:
            with open(self.report_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"HTML report successfully generated: {self.report_file}")
        except Exception as e:
            print(f"Error writing HTML report: {e}")
            
    def run_analysis(self):
        """
        Run the full analysis pipeline.
        """
        print("\n--- Running Analysis Engine ---")
        self.generate_resource_metrics() # Calculate metrics
        self.analyze_sustainability_dynamics() # Perform summary analysis
        self.generate_visualizations() # Generate plots
        self.generate_html_report() # Generate HTML report using calculated metrics/summary
        print("--- Analysis Engine Finished ---\n")
        # Return the calculated metrics and summary for potential further use
        return {"metrics": self.metrics, "summary": self.summary}

# Example usage (if run directly, though typically used by the main script)
if __name__ == '__main__':
    # Create dummy results and config for testing
    dummy_results = {
        2025: {'land': {'urban_area_expansion': 18}, 'water': {'groundwater_level_change': -0.05}, 'energy': {'energy_mix_renewable_share_change_percent_points': 0.1}, 'climate': {'overall_vulnerability_index_change': 0.1}, 'community': {'community_empowerment_index_change': 0.05} },
        2026: {'land': {'urban_area_expansion': 20}, 'water': {'groundwater_level_change': -0.06}, 'energy': {'energy_mix_renewable_share_change_percent_points': 0.15}, 'climate': {'overall_vulnerability_index_change': 0.12}, 'community': {'community_empowerment_index_change': 0.06} },
        # ... more years and models ...
        2035: {'land': {'urban_area_expansion': 25}, 'water': {'groundwater_level_change': -0.1}, 'energy': {'energy_mix_renewable_share_change_percent_points': 0.8}, 'climate': {'overall_vulnerability_index_change': 0.3}, 'community': {'community_empowerment_index_change': 0.2} }
    }
    dummy_config = {
        "simulation_name": "Test Simulation",
        "start_year": 2025,
        "end_year": 2035,
        "scenario": "Test Scenario",
        "output_dir": "./outputs_test/"
    }
    
    analyzer = NaturalResourceAnalysisEngine(dummy_results, dummy_config)
    analysis_output = analyzer.run_analysis()
    print(f"\nFinal Analysis Output Dictionary:\n{analysis_output}") 