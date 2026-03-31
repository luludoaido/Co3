import pandas as pd
import time 
from algorithmn.GA_random_parents import genetic_algorithm
from algorithmn.monte_carlo import monte_carlo_optimization
from algorithmn.optimizer_SA import simulated_annealing
from base.objective_function import objective
from main_script import objects
from utils.shape_visualization_3D import visualize_objects
import matplotlib.pyplot as plt
from utils.converting import sort_coordinate
import os, sys



# to find the convergance --> maybe into their own algorithm. --> yes let's do that 5%


def test_algorithm(algorithm, epoch):
    """
    Test algorithm and save start time, end time, objects, and scores.
    Args:
        algorithm: Algorithm function to test.
    Return:
        DataFrame with score, objects, start_time, end_time
    """

    results_dict = {"score":[], "objects":[], "start_time":[], "end_time":[]}
    for _ in range(epoch):
        results_dict["start_time"].append(time.time())
        best_coordinates, best_score = algorithm
        results_dict["end_time"].append(time.time())
        results_dict["score"].append(best_score)
        results_dict["objects"].append(best_coordinates)
        
    return pd.DataFrame(results_dict)


epoch = 2

GA_result = test_algorithm(genetic_algorithm(),epoch)

GA_result["duration(s)"] = GA_result["end_time"] - GA_result["start_time"]

# Extract and save coordinates of GA results
for i in range(epoch):
    output_dir = "picture/GA"
    os.makedirs(output_dir, exist_ok=True)
    visualize_objects(GA_result["objects"][i], W=38.0, D=28.4, H=38.0)
    plt.savefig(f"{output_dir}/GA_{i}.png", dpi=300)  # dpi for quality
    plt.close()
    GA_coords = sort_coordinate(GA_result["objects"][i])
    GA_coords_df = pd.DataFrame({
        "Object_Name": GA_coords[3],
        "X": GA_coords[0],
        "Y": GA_coords[1],
        "Z": GA_coords[2],
        "Volume": GA_coords[4]
    })
    GA_coords_df.to_csv(f"{output_dir}/GA_coordinates.csv", index=False)
    print("GA Algorithm - Best Configuration Coordinates:")
    print(GA_coords_df.to_string(index=False))
    print(f"\nCoordinates saved to {output_dir}/GA_coordinates.csv")
     


monte_carlo_result = test_algorithm(monte_carlo_optimization(objects), epoch)

# Extract and save coordinates of Monte Carlo results
MC_coords = sort_coordinate(monte_carlo_result["objects"][0])
MC_coords_df = pd.DataFrame({
    "Object_Name": MC_coords[3],
    "X": MC_coords[0],
    "Y": MC_coords[1],
    "Z": MC_coords[2],
    "Volume": MC_coords[4]
})
output_dir_mc = "picture/Monte_Carlo"
os.makedirs(output_dir_mc, exist_ok=True)
MC_coords_df.to_csv(f"{output_dir_mc}/MC_coordinates.csv", index=False)
print("\nMonte Carlo Algorithm - Best Configuration Coordinates:")
print(MC_coords_df.to_string(index=False))

simulated_annealing_result = test_algorithm(simulated_annealing(objects,objective), epoch)

# Extract and save coordinates of Simulated Annealing results
SA_coords = sort_coordinate(simulated_annealing_result["objects"][0])
SA_coords_df = pd.DataFrame({
    "Object_Name": SA_coords[3],
    "X": SA_coords[0],
    "Y": SA_coords[1],
    "Z": SA_coords[2],
    "Volume": SA_coords[4]
})
output_dir_sa = "picture/Simulated_Annealing"
os.makedirs(output_dir_sa, exist_ok=True)
SA_coords_df.to_csv(f"{output_dir_sa}/SA_coordinates.csv", index=False)
print("\nSimulated Annealing Algorithm - Best Configuration Coordinates:")
print(SA_coords_df.to_string(index=False))