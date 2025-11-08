import random
import time

choices = ('duck', 'goose')
players = ['Marko', 'Ana', 'Maritza', 'Lily', 'Natalia', 'Ruby', 'Ruben']

def setup_round(players, new_picker=None):
    
    picker = ""
    if new_picker:
        picker = new_picker
    else:
        picker = random.choice(players) # This only runs on the first game
        
    sitters = []

    for p in players:
        if p != picker:
            sitters.append(p)

    print("\n" + "="*30)
    print(f"NEW ROUND: The picker is: {picker}")
    
    return picker, sitters 
    

def simulate_chase(picker, goose):
    winner = random.choice([picker, goose])

    if winner == goose:
        print("The goose made it to the empty spot! The picker is 'it' again.")
    else:
        print("The picker tagged the goose! The goose is now 'it'.")

def play_game():

    next_picker = None 
    
    while True: 
    
        # --- Setup the round ---
        picker, sitters = setup_round(players, next_picker) 
        
        # --- Assign Duck/Goose ---
        assignments = {} 
        random_index = random.randrange(len(sitters)) 
        
        goose_name = "" 
        
        for p in range(len(sitters)):
            name = sitters[p]
            
            if p == random_index:
                assignments[name] = 'goose!'
                goose_name = name 
            else:
                assignments[name] = 'duck'
                
        
        print("The picker starts tapping...")
        for sitter_name in sitters:
            time.sleep(0.5) 
            status = assignments[sitter_name]
            print(f"{picker} taps {sitter_name}... {status.upper()}")
            if status == 'goose!':
                break 
        
       
        print(f"\nThe chase is on between {picker} (picker) and {goose_name} (goose)!")
        
        
        # This name will be fed back into setup_round at the
        # top of the loop on the next iteration.
        next_picker = simulate_chase(picker, goose_name) # <-- CHANGED
        
        
        choice = input("Play another round? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break


if __name__ == '__main__':      
    play_game()
