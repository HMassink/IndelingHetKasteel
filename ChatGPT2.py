import random

# Create a list of players
players = ["speler" + str(i) for i in range(1, 21)]

# Add a random ELO rating to each player
players_with_elo = [{"name": player, "elo": random.randint(1300, 2100)} for player in players]

# Add a presence status for each player for each round
for player in players_with_elo:
    player["aanwezigheid"] = [True]*9  # Assuming all players are present for all rounds

# List of players who are not present in round 1
absent_players_round1 = ['speler2', 'speler8', 'speler9', 'speler10', 'speler11']

# Update the presence status for the absent players in round 1
for player in players_with_elo:
    if player['name'] in absent_players_round1:
        player['aanwezigheid'][0] = False  # Index 0 corresponds to round 1

# Filter out the players who are not present in round 1
present_players_round1 = [player for player in players_with_elo if player["aanwezigheid"][0]]

# Print the present players for round 1
print("Aanwezige spelers voor ronde 1:")
for player in present_players_round1:
    print(player["name"])

# Sort the present players by their ELO rating
sorted_players_round1 = sorted(present_players_round1, key=lambda x: x['elo'], reverse=True)

# Split the sorted list into two halves
half = len(sorted_players_round1) // 2
high_rated_players = sorted_players_round1[:half]
low_rated_players = sorted_players_round1[half:]

# Pair up players from the top half and the bottom half
pairings_round1 = list(zip(high_rated_players, low_rated_players))

# Print the pairings for round 1
print("\nIndeling voor ronde 1:")
for pairing in pairings_round1:
    print(f"{pairing[0]['name']} vs {pairing[1]['name']}")

# Possible outcomes
outcomes = [(1, 0), (0, 1), (0.5, 0.5)]

# Add a random outcome to each pairing
for pairing in pairings_round1:
    outcome = random.choice(outcomes)
    pairing[0]['score'] = outcome[0]
    pairing[1]['score'] = outcome[1]

# Add the round 1 results to the players_with_elo list
for player in players_with_elo:
    player["ronde1"] = None  # Initialize the round 1 result as None for all players
    for pairing in pairings_round1:
        # If the player is in this pairing, update their round 1 result
        if player["name"] == pairing[0]["name"]:
            player["ronde1"] = {"tegenstander": pairing[1]["name"], "score": pairing[0]["score"]}
        elif player["name"] == pairing[1]["name"]:
            player["ronde1"] = {"tegenstander": pairing[0]["name"], "score": pairing[1]["score"]}
    if player["ronde1"] is None:  # If the player was not present, assign a score of 0
        player["ronde1"] = {"tegenstander": None, "score": 0}

def update_elo(player_elo, opponent_elo, score, K=32):
    """
    Calculate the new Elo rating for a player based on their old rating, their opponent's rating, and the game result.
    """
    # Calculate the expected score
    E = 1 / (1 + 10**((opponent_elo - player_elo) / 400))

    # Calculate the new rating
    new_elo = player_elo + K * (score - E)

    return new_elo

# Update the Elo rating for each player based on the results of round 1
for player in players_with_elo:
    if player["ronde1"]["tegenstander"] is not None:  # Only update Elo for players who were present in round 1
        # Find the opponent's details
        opponent = next(p for p in players_with_elo if p["name"] == player["ronde1"]["tegenstander"])
        # Update the player's Elo rating
        player["elo"] = update_elo(player["elo"], opponent["elo"], player["ronde1"]["score"])

def calculate_resistance_points(player, players_with_elo):
    """
    Calculate the resistance points (Buchholz score) for a player based on the scores of their opponents.
    """
    # If the player was not present in round 1, their resistance points are 0
    if player["ronde1"]["tegenstander"] is None:
        return 0

    # Find the opponent's details
    opponent = next(p for p in players_with_elo if p["name"] == player["ronde1"]["tegenstander"])

    # The resistance points are the score of the opponent
    # If the opponent was not present in round 1, their score is 0
    resistance_points = opponent["ronde1"]["score"] if opponent["ronde1"]["tegenstander"] is not None else 0

    return resistance_points

# Calculate the resistance points for each player after round 1
for player in players_with_elo:
    player["weerstandspunten"] = calculate_resistance_points(player, players_with_elo)

def calculate_sonneborn_berger_score(player, players_with_elo):
    """
    Calculate the Sonneborn-Berger score for a player based on the scores of their opponents.
    """
    # If the player was not present in round 1, their Sonneborn-Berger score is 0
    if player["ronde1"]["tegenstander"] is None:
        return 0

    # Find the opponent's details
    opponent = next(p for p in players_with_elo if p["name"] == player["ronde1"]["tegenstander"])

    # The Sonneborn-Berger score is the score of the opponent multiplied by the player's score
    # If the opponent was not present in round 1, their score is 0
    sonneborn_berger_score = opponent["ronde1"]["score"] * player["ronde1"]["score"] if opponent["ronde1"]["tegenstander"] is not None else 0

    return sonneborn_berger_score

# Calculate the Sonneborn-Berger score for each player after round 1
for player in players_with_elo:
    player["sonneborn_berger_score"] = calculate_sonneborn_berger_score(player, players_with_elo)

# Sort the players by points, Sonneborn-Berger score, and Elo
sorted_players_after_round1 = sorted(players_with_elo, key=lambda x: (x['ronde1']['score'], x['sonneborn_berger_score'], x['elo']), reverse=True)

# Print the standings after round 1, including Sonneborn-Berger scores
print("\nStand na ronde 1:")
for player in sorted_players_after_round1:
    print(f"{player['name']}: {player['elo']:.2f} Elo, {player['ronde1']['score']} punten, {player['weerstandspunten']} weerstandspunten, {player['sonneborn_berger_score']} Sonneborn-Berger punten")

