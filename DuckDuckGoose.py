import random
import time

choices = ('duck', 'goose')
players = ['Marko', 'Ana', 'Maritza', 'Lily', 'Natalia', 'Ruby', 'Ruben']

def setup_round(players, new_picker=None):
    
    picker = ""
    if new_picker: # <-- CHANGED
        picker = new_picker
    else:
        picker = random.choice(players) # This only runs on the first game
        
    sitters = []

    for p in players:
        if p != picker:
            sitters.append(p)

    print("\n" + "="*30)
    print(f"NEW ROUND: The picker is: {picker}")
    # print(f"The sitters are: {sitters}") # Optional: can be noisy
    return picker, sitters 
    

def simulate_chase(picker, goose):
    winner = random.choice([picker, goose])

    if winner == goose:
        print("The goose made it to the empty spot! The picker is 'it' again.")
    else:
        print("The picker tagged the goose! The goose is now 'it'.")

def play_game():

    next_picker = None # <-- NEW: No picker has been chosen yet
    
    while True: # <-- NEW: The main game loop
    
        # --- Step 1: Setup the round ---
        # Pass in 'next_picker' so setup_round knows who is 'it'
        picker, sitters = setup_round(players, next_picker) # <-- CHANGED
        
        # --- Step 2: Assign Duck/Goose ---
        # These are *inside* the loop to reset every round
        assignments = {} 
        random_index = random.randrange(len(sitters)) 
        
        goose_name = "" # <-- Moved this up
        
        for p in range(len(sitters)):
            name = sitters[p]
            
            if p == random_index:
                assignments[name] = 'goose!'
                goose_name = name # <-- We can find the goose right here!
            else:
                assignments[name] = 'duck'
                
        # --- Step 3: Simulate the Taps (Optional idea from before) ---
        print("The picker starts tapping...")
        for sitter_name in sitters:
            time.sleep(0.5) # Pause for drama
            status = assignments[sitter_name]
            print(f"{picker} taps {sitter_name}... {status.upper()}")
            if status == 'goose!':
                break # Stop tapping once the goose is found
        
        # --- Step 4: Start the Chase! ---
        print(f"\nThe chase is on between {picker} (picker) and {goose_name} (goose)!")
        
        # We call simulate_chase and *save* the result
        # This name will be fed back into setup_round at the
        # top of the loop on the next iteration.
        next_picker = simulate_chase(picker, goose_name) # <-- CHANGED
        
        # --- Step 5: Ask to play again ---
        choice = input("Play another round? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break # <-- NEW: Exits the 'while True' loop


if __name__ == '__main__':      
    play_game()
