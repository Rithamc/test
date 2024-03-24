"""
3.3PP Functions: Calculation of Stopping distance for a car
"""

__author__ = "Ritham Chhetri"

def distance(initial_velocity: float, reaction_time: float) -> float:
    """
    Calculate the stopping distance based on initial velocity and reaction time.
    """
    FRICTION = 0.7  # Coefficient of friction for the road surface
    GRAVITY = 9.81  # Acceleration due to gravity in m/s^2
    
    # Calculate stopping distance using the formula
    stopping_distance = (initial_velocity * reaction_time) + ((initial_velocity ** 2) / (2 * FRICTION * GRAVITY))
    return stopping_distance

def main():
    
    print("Stopping Distance \n")

    # Stopping Distance 1
    initial_velocity_1 = 27.8  # Initial velocity for stopping distance 1 in m/s
    time_1 = 1.5  # Reaction time in seconds
    
    # Calculate stopping distance 1 and print the result
    stopping_distance_1 = distance(initial_velocity_1, time_1)
    print(f"Stopping Distance 1: {stopping_distance_1:.2f} meters")

    # Stopping Distance 2
    initial_velocity_2 = 13.9  # Initial velocity for stopping distance 2 in m/s
    time_2 = 1.5  # Reaction time in seconds
    
    # Calculate stopping distance 2 and print the result
    stopping_distance_2 = distance(initial_velocity_2, time_2)
    print(f"Stopping Distance 2: {stopping_distance_2:.2f} meters\n")
    
    # User input for initial velocity and time to calculate stopping distance
    initial_velocity = float(input("Enter initial velocity (m/s): "))
    reaction_time = float(input("Enter reaction time (s): "))
    
    # Calculate stopping distance based on user input and print the result
    stopping_distance = distance(initial_velocity, reaction_time)
    print(f'Stopping Distance: {stopping_distance:.2f} meters')

    
if __name__ == "__main__":
    main()
