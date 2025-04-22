# config.py

# Basic configuration settings for the simulation

SIMULATION_CONFIG = {
    "simulation_name": "Bangladesh Natural Resources 2025-2035 Baseline",
    "start_year": 2025,
    "end_year": 2035,
    "time_step": 1, # Years
    "scenario": "Baseline",
    
    # Placeholder for data paths (if loading real data)
    "data_paths": {
        "water_data": "./data/input/water/",
        "land_data": "./data/input/land/",
        "forest_data": "./data/input/forest/",
        # ... etc
    },
    
    # Placeholder for specific model parameters (can be nested)
    "model_params": {
        "water": {
            "transboundary_flow_multiplier": 1.0, # Example parameter
            "irrigation_efficiency_target": 40 # Example target
        },
        "climate": {
            "rcp_scenario": "RCP4.5" # Example climate scenario choice
        },
        "policy": {
            "renewable_energy_subsidy_level": 0.1 # Example policy lever
        }
        # ... other model-specific parameters
    },
    
    # Output directory
    "output_dir": "./outputs/"
}

# You could also define configurations for different scenarios
SCENARIO_HIGH_CLIMATE_IMPACT = SIMULATION_CONFIG.copy()
SCENARIO_HIGH_CLIMATE_IMPACT["scenario"] = "High Climate Impact"
SCENARIO_HIGH_CLIMATE_IMPACT["model_params"]["climate"]["rcp_scenario"] = "RCP8.5"
SCENARIO_HIGH_CLIMATE_IMPACT["model_params"]["water"]["transboundary_flow_multiplier"] = 0.85

SCENARIO_GREEN_POLICY = SIMULATION_CONFIG.copy()
SCENARIO_GREEN_POLICY["scenario"] = "Green Policy Push"
SCENARIO_GREEN_POLICY["model_params"]["policy"]["renewable_energy_subsidy_level"] = 0.25
SCENARIO_GREEN_POLICY["model_params"]["water"]["irrigation_efficiency_target"] = 50

# Select the configuration to use
ACTIVE_CONFIG = SIMULATION_CONFIG 
# ACTIVE_CONFIG = SCENARIO_HIGH_CLIMATE_IMPACT
# ACTIVE_CONFIG = SCENARIO_GREEN_POLICY 