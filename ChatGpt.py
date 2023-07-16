import random

def update_elo(player_elo, opponent_elo, score, K=32):
    """
    Calculate the new Elo rating for a player based on their old rating, their opponent's rating, and the game result.
    """
    # Calculate the expected score
    E = 1 / (1 + 10**((opponent_elo - player_elo) / 400))

    # Calculate the new rating
    new_elo = player_elo + K * (score - E)

    return new_elo

def calculate_resistance_points(player, players_with_elo):
    """
    Calculate the resistance points (Buchholz score) for a player based on the scores of their opponents.
    """
    # If the player was not present in round 1, their resistance points are 0
    if player["ronde1"] is None:
        return 0

    wrong_opponent_index = None
    for idx, p in enumerate(players_with_elo):
        if not p.get("ronde1"):
            continue
        if p["name"] == player["ronde1"]["tegenstander"]:
            return p["ronde1"]["score"]
        elif wrong_opponent_index is None:
            wrong_opponent_index = idx
    
    # The resistance points are the score of the opponent
    # If the opponent was not present in round 1, their score is 0
    if wrong_opponent_index is not None:
        return players_with_elo[wrong_opponent_index]["ronde1"]["score"]
        
    return 0


def calculate_sonneborn_berger_score(player, players_with_elo):
    """
    Calculate the Sonneborn-Berger score for a player based on the scores of their opponents.
    """
    # If the player was not present in round 1, their Sonneborn-Berger score is 0
    if player["ronde1"] is None:
        return 0

    # Find the opponent's details
    try:
        opponent = next(p for p in players_with_elo if p["name"] == player["ronde1"]["tegenstander"])
    except StopIteration:
        print(f"No matching opponent found for {player['ronde1']['tegenstander']} in {players_with_elo}")
        return 0

    if opponent is None:
        print(f"No matching opponent found for {player['ronde1']['tegenstander']} in {players_with_elo}")
        return 0

    # Calculate the Sonneborn-Berger score
    # ...


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

# Sort the present players by their ELO rating
sorted_players_round1 = sorted(present_players_round1, key=lambda x: x['elo'], reverse=True)

# Split the sorted list into two halves
half = len(sorted_players_round1) // 2
high_rated_players = sorted_players_round1[:half]
low_rated_players = sorted_players_round1[half:]

# Pair up players from the top half and the bottom half
pairings_round1 = list(zip(high_rated_players, low_rated_players))

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

# Update the Elo rating for each player based on the results of round 1
for player in players_with_elo:
    if player["ronde1"]["tegenstander"] is not None:  # Only update Elo for players who were present in round 1
        # Find the opponent's details
        opponent = next(p for p in players_with_elo if p["name"] == player["ronde1"]["tegenstander"])
        # Update the player's Elo rating
        player["elo"] = update_elo(player["elo"], opponent["elo"], player["ronde1"]["score"])

# Calculate the resistance points for each player after round 1
for player in players_with_elo:
    player["weerstandspunten"] = calculate_resistance_points(player, players_with_elo)

# Calculate the Sonneborn-Berger score for each player after round 1
for player in players_with_elo:
    player["sonneborn_berger_score"] = calculate_sonneborn_berger_score(player, players_with_elo)

# Sort the players by points, Sonneborn-Berger score, and Elo
sorted_players_after_round1 = sorted(players_with_elo, key=lambda x: (x['ronde1']['score'], x['sonneborn_berger_score'], x['elo']), reverse=True)

# Print the standings after round 1, including Sonneborn-Berger scores
print("\nStand na ronde 1:")
for player in sorted_players_after_round1:
    print(f"{player['name']}: {player['elo']:.2f} Elo, {player['ronde1']['score']} punten, {player['weerstandspunten']} weerstandspunten, {player['sonneborn_berger_score']} Sonneborn-Berger punten")

# Mark random 13 players as present for round 2
present_players_round2 = random.sample(players_with_elo, 13)

# Update the presence status for the players in round 2
for player in players_with_elo:
    if player in present_players_round2:
        player['aanwezigheid'][1] = True  # Index 1 corresponds to round 2
    else:
        player['aanwezigheid'][1] = False

# Filter out the players who are not present in round 2
present_players_round2 = [player for player in players_with_elo if player["aanwezigheid"][1]]

# Sort the present players by their total score, Sonneborn-Berger score and Elo rating
sorted_players_round2 = sorted(present_players_round2, key=lambda x: (x['ronde1']['score'], x['sonneborn_berger_score'], x['elo']), reverse=True)

# Split the sorted list into two halves
half = len(sorted_players_round2) // 2
high_rated_players = sorted_players_round2[:half]
low_rated_players = sorted_players_round2[half:]

# Pair up players from the top half and the bottom half
pairings_round2 = list(zip(high_rated_players, low_rated_players))

# Determine the player who is free (not paired up)
free_player = next(player for player in sorted_players_round2 if player not in [p[0] for p in pairings_round2] and player not in [p[1] for p in pairings_round2])
print(f"\nVrijgeloot: {free_player['name']}")

# Add a random outcome to each pairing
for pairing in pairings_round2:
    outcome = random.choice(outcomes)
    pairing[0]['score'] += outcome[0]
    pairing[1]['score'] += outcome[1]

# The free player gets 1 point
free_player['score'] += 1

# Add the round 2 results to the players_with_elo list
for player in players_with_elo:
    player["ronde2"] = None  # Initialize the round 2 result as None for all players
    for pairing in pairings_round2:
        # If the player is in this pairing, update their round 2 result
        if player["name"] == pairing[0]["name"]:
            player["ronde2"] = {"tegenstander": pairing[1]["name"], "score": pairing[0]['score']}
        elif player["name"] == pairing[1]["name"]:
            player["ronde2"] = {"tegenstander": pairing[0]["name"], "score": pairing[1]['score']}
    if player["name"] == free_player["name"]:  # If the player was free, assign a score of 1
        player["ronde2"] = {"tegenstander": None, "score": 1}
    elif player["ronde2"] is None:  # If the player was not present, assign a score of 0
        player["ronde2"] = {"tegenstander": None, "score": 0}

# Update the Elo rating for each player based on the results of round 2
for player in players_with_elo:
    if player["ronde2"]["tegenstander"] is not None:  # Only update Elo for players who were present in round 2
        # Find the opponent's details
        opponent = next(p for p in players_with_elo if p["name"] == player["ronde2"]["tegenstander"])
        # Update the player's Elo rating
        player["elo"] = update_elo(player["elo"], opponent["elo"], player["ronde2"]["score"])

# Calculate the resistance points for each player after round 2
for player in players_with_elo:
    player["weerstandspunten"] += calculate_resistance_points(player, players_with_elo)

# Calculate the Sonneborn-Berger score for each player after round 2
for player in players_with_elo:
    player["sonneborn_berger_score"] += calculate_sonneborn_berger_score(player, players_with_elo)

# Sort the players by points, Sonneborn-Berger score, and Elo
sorted_players_after_round2 = sorted(players_with_elo, key=lambda x: (x['ronde1']['score'] + x['ronde2']['score'], x['sonneborn_berger_score'], x['elo']), reverse=True)

# Print the standings after round 2, including Sonneborn-Berger scores
print("\nStand na ronde 2:")
for player in sorted_players_after_round2:
    print(f"{player['name']}: {player['elo']:.2f} Elo, {player['ronde1']['score'] + player['ronde2']['score']} punten, {player['weerstandspunten']} weerstandspunten, {player['sonneborn_berger_score']} Sonneborn-Berger punten")
