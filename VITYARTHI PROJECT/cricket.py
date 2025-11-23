import random
import time


MATCH_OVERS = 5
TEAMS = ["Royal Challengers", "Super Kings"]


OUTCOMES = [0, 1, 2, 3, 4, 6, 'W']
WEIGHTS  = [25, 25, 15, 5, 10, 10, 10]


COMMENTARY = {
    0: ["Defended well.", "Straight to the fielder.", "No run."],
    1: ["Single taken.", "Push to mid-on for one.", "Just a quick single."],
    2: ["Good running between the wickets.", "Two runs added.", "In the gap for two."],
    3: ["Great fielding stops the boundary, they get 3.", "Three runs."],
    4: ["Smashed through the covers! FOUR.", "Beautiful timing! Boundary.", "One bounce and over the rope."],
    6: ["That is HUGE! Six runs.", "Into the stands! MAXIMUM.", "Clean strike over long-on."],
    'W': ["Clean Bowled!", "Caught at the boundary! He is out.", "Edged and taken! WICKET."]
}

def get_commentary(outcome):
    """Returns a random phrase based on what happened on the ball."""
    if outcome in COMMENTARY:
        return random.choice(COMMENTARY[outcome])
    return ""

def simulate_innings(batting_team, bowling_team, target=None):
    print(f"\n>>> {batting_team} steps out to bat.")
    if target:
        print(f">>> Target to win: {target} runs.")
    print("-" * 50)

    score = 0
    wickets = 0
    balls_bowled = 0
    
    for over_num in range(1, MATCH_OVERS + 1):
        print(f"\n[Over {over_num} Starts]")
        
        for ball_num in range(1, 7):
            time.sleep(0.5)  
            
           
            outcome = random.choices(OUTCOMES, weights=WEIGHTS, k=1)[0]
            balls_bowled += 1
            
           
            print(f"{over_num-1}.{ball_num} | ", end="")
            
            if outcome == 'W':
                wickets += 1
                print(f"OUT! {get_commentary('W')}")
            else:
                score += outcome
                
                if outcome >= 4:
                    print(f"{outcome} runs... {get_commentary(outcome)}")
                else:
                    print(f"{outcome} run(s).")

            
            if wickets == 10:
                print(f"\n>>> {batting_team} is All Out!")
                return score, wickets
            
            if target and score > target:
                return score, wickets

        
        print(f"   End of Over {over_num}: {batting_team} is {score}/{wickets}")
    
    return score, wickets

def perform_toss():
    print("... Flipping the coin ...")
    time.sleep(1)
    winner = random.choice(TEAMS)
    
    
    choice = random.choice(["Bat", "Bowl"])
    print(f"Match Update: {winner} won the toss and elected to {choice} first.")
    
    if choice == "Bat":
        return winner, (TEAMS[1] if winner == TEAMS[0] else TEAMS[0])
    else:
        return (TEAMS[1] if winner == TEAMS[0] else TEAMS[0]), winner

def main():
    print("=" * 50)
    print(f" CRICKET MATCH: {TEAMS[0]} vs {TEAMS[1]}")
    print("=" * 50)

    
    batting_first, bowling_first = perform_toss()

    
    score1, wickets1 = simulate_innings(batting_first, bowling_first)
    print(f"\n>>> Innings Break. {batting_first} finished with {score1}/{wickets1}.")
    
    target = score1 + 1
    print(f">>> {bowling_first} needs {target} runs to win from {MATCH_OVERS} overs.")
    time.sleep(2)

    
    score2, wickets2 = simulate_innings(bowling_first, batting_first, target=score1)

    
    print("\n" + "=" * 50)
    print("MATCH RESULT")
    print("=" * 50)
    print(f"{batting_first}: {score1}/{wickets1}")
    print(f"{bowling_first}: {score2}/{wickets2}")
    print("-" * 50)

    if score2 > score1:
        print(f"WINNER: {bowling_first} won by {10 - wickets2} wickets!")
    elif score1 > score2:
        print(f"WINNER: {batting_first} won by {score1 - score2} runs!")
    else:
        print("It's a TIE!")
    print("=" * 50)

if __name__ == "__main__":

    main()
