# simulation.py

from .models.water_resource import WaterResourceModel
from .models.land_resource import LandResourceModel
from .models.forest_resource import ForestResourceModel
from .models.biodiversity import BiodiversityModel
from .models.mineral_resource import MineralResourceModel
from .models.energy_resource import EnergyResourceModel
from .models.marine_resource import MarineResourceModel
from .models.climate_resilience import ClimateResilienceModel
from .models.resource_governance import ResourceGovernanceModel
from .models.community_resource import CommunityResourceModel
from .models.sustainable_use import SustainableUseModel
from .models.conservation import ConservationModel

# Potential future: from .data.handler import NaturalResourceDataHandler

class BangladeshNaturalResourceSimulation:
    """Main simulation environment integrating all components"""
    def __init__(self, config):
        """
        Initialize simulation with configuration parameters.
        
        Args:
            config: Configuration object/dictionary containing simulation parameters.
        """
        print("--- Initializing Simulation Environment --- W")
        self.config = config
        # Potential future: self.data_handler = NaturalResourceDataHandler(config)
        # Potential future: self.data_handler.load_historical_data()
        
        # Initialize all component models
        self.water_resources = WaterResourceModel(config)
        self.land_resources = LandResourceModel(config)
        self.forest_resources = ForestResourceModel(config)
        self.biodiversity = BiodiversityModel(config)
        self.mineral_resources = MineralResourceModel(config)
        self.energy_resources = EnergyResourceModel(config)
        self.marine_resources = MarineResourceModel(config)
        self.climate_resilience = ClimateResilienceModel(config)
        self.resource_governance = ResourceGovernanceModel(config)
        self.community_resource = CommunityResourceModel(config)
        self.sustainable_use = SustainableUseModel(config)
        self.conservation = ConservationModel(config)
        print("--- Simulation Environment Initialized --- \n")
        
    def run_simulation(self, start_year=2025, end_year=2035, scenarios=None):
        """
        Execute the simulation over the specified time period.
        
        Args:
            start_year (int): The starting year of the simulation.
            end_year (int): The ending year of the simulation (inclusive).
            scenarios (list, optional): List of scenario configurations to run. 
                                     Currently placeholder, runs one baseline.
                                     
        Returns:
            dict: A dictionary containing the simulation results, structured by year.
        """
        print(f"--- Starting Simulation Run: {start_year}-{end_year} ---")
        num_years = end_year - start_year + 1
        simulation_results = {}
        current_state = {} # Stores the latest state from all models

        # --- Initial State Setup (Optional) ---
        # Could populate current_state with initial values from models if needed
        # e.g., current_state['water'] = self.water_resources.get_initial_state()
        print("Setting up initial state (placeholders)...")

        # --- Simulation Loop ---
        for i in range(num_years):
            year = start_year + i
            print(f"\n--- Simulating Year {year} ---")
            year_results = {}
            
            # Define the order of model execution (can be adjusted based on dependencies)
            # E.g., Climate impacts affect water, which affects land, etc.
            # Passing 'current_state' allows models to potentially react to others' outputs
            # from the same year, though current stubs are simple.
            
            climate_state = self.climate_resilience.simulate_resilience_dynamics(year, current_state)
            current_state['climate'] = climate_state
            year_results['climate'] = climate_state

            water_state = self.water_resources.simulate_step(year, current_state)
            current_state['water'] = water_state
            year_results['water'] = water_state
            
            land_state = self.land_resources.simulate_land_dynamics(year, current_state)
            current_state['land'] = land_state
            year_results['land'] = land_state
            
            forest_state = self.forest_resources.simulate_forest_dynamics(year, current_state)
            current_state['forest'] = forest_state
            year_results['forest'] = forest_state
            
            biodiversity_state = self.biodiversity.simulate_biodiversity_dynamics(year, current_state)
            current_state['biodiversity'] = biodiversity_state
            year_results['biodiversity'] = biodiversity_state
            
            marine_state = self.marine_resources.simulate_marine_dynamics(year, current_state)
            current_state['marine'] = marine_state
            year_results['marine'] = marine_state
            
            mineral_state = self.mineral_resources.simulate_mineral_dynamics(year, current_state)
            current_state['mineral'] = mineral_state
            year_results['mineral'] = mineral_state
            
            energy_state = self.energy_resources.simulate_energy_dynamics(year, current_state)
            current_state['energy'] = energy_state
            year_results['energy'] = energy_state
            
            community_state = self.community_resource.simulate_community_dynamics(year, current_state)
            current_state['community'] = community_state
            year_results['community'] = community_state
            
            governance_state = self.resource_governance.simulate_governance_dynamics(year, current_state)
            current_state['governance'] = governance_state
            year_results['governance'] = governance_state
            
            sustainability_state = self.sustainable_use.simulate_sustainability_dynamics(year, current_state)
            current_state['sustainable_use'] = sustainability_state
            year_results['sustainable_use'] = sustainability_state
            
            conservation_state = self.conservation.simulate_conservation_dynamics(year, current_state)
            current_state['conservation'] = conservation_state
            year_results['conservation'] = conservation_state
            
            simulation_results[year] = year_results
            print(f"--- Finished Simulating Year {year} ---")

        print(f"\n--- Simulation Run Finished ({start_year}-{end_year}) ---")
        return simulation_results 