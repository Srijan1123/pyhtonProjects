print("\n------Simple voting system------")



# let's put 10 voters infornamtion here
voters = [
    {"voter_id": 1, "name": "Sita", "age": 25, "location": "Kathmandu", "ward": 1, "voted": False},
    {"voter_id": 2, "name": "Ram", "age": 30, "location": "Lalitpur", "ward": 2, "voted": False},
    {"voter_id": 3, "name": "Gita", "age": 22, "location": "Bhaktapur", "ward": 3, "voted": False},
    {"voter_id": 4, "name": "Hari", "age": 27, "location": "Kathmandu", "ward": 4, "voted": False},
    {"voter_id": 5, "name": "Mina", "age": 24, "location": "Lalitpur", "ward": 5, "voted": False},
    {"voter_id": 6, "name": "Krishna", "age": 29, "location": "Bhaktapur", "ward": 6, "voted": False},
    {"voter_id": 7, "name": "Radha", "age": 28, "location": "Kathmandu", "ward": 7, "voted": False},
    {"voter_id": 8, "name": "Shyam", "age": 26, "location": "Lalitpur", "ward": 8, "voted": False},
    {"voter_id": 9, "name": "Laxmi", "age": 23, "location": "Bhaktapur", "ward": 9, "voted": False},
    {"voter_id": 10, "name": "Harihar", "age": 31, "location": "Kathmandu", "ward": 10, "voted": False}
]

#let's put party and contender(name)
parties = {
    "UML": ["Alice", "Bob", "Charlie"],
    "CONGRESS": ["David", "Emma", "Frank"],
    "RRSP": ["George", "Helen", "Ian"]
}

#  Initialize votes
votes = {
    "UML": {"Alice": 0, "Bob": 0, "Charlie": 0},
    "CONGRESS": {"David": 0, "Emma": 0, "Frank": 0},
    "RRSP": {"George": 0, "Helen": 0, "Ian": 0}
}

# let's show Voting process
print("Welcome to the Python Voting System!\n")
voted_count = 0

while voted_count < len(voters):
    print("\nList of Voters:")
    for voter in voters:
        status = "Voted" if voter["voted"] else "Not Voted"
        print(f'ID: {voter["voter_id"]}, Name: {voter["name"]}, Status: {status}')

    try:
        voter_id = int(input("\nEnter your Voter ID to vote: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        continue

    # let's find the voter
    voter = next((v for v in voters if v["voter_id"] == voter_id), None)
    if not voter:
        print("Voter ID not found!")
        continue
    if voter["voted"]:
        print("You have already voted!")
        continue

    #let's  Choose  the Party
    print("\nParties:")
    for i, party in enumerate(parties.keys(), 1):
        print(f"{i}. {party}")
    try:
        party_choice = int(input("Select a party by number: "))
        party_name = list(parties.keys())[party_choice - 1]
    except (ValueError, IndexError):
        print("Invalid party choice!")
        continue

    # let's Choose Contender whom to vote
    contenders = parties[party_name]
    print(f"\nContenders in {party_name}:")
    for i, contender in enumerate(contenders, 1):
        print(f"{i}. {contender}")
    try:
        contender_choice = int(input("Select a contender by number: "))
        contender_name = contenders[contender_choice - 1]
    except (ValueError, IndexError):
        print("Invalid contender choice!")
        continue

    #  now let's Record vote
    votes[party_name][contender_name] += 1
    voter["voted"] = True
    voted_count += 1
    print(f"\nThank you {voter['name']}! Your vote has been recorded for {contender_name} ({party_name}).")

# let's Check if all 10 voted
if voted_count < 10:
    print("\nVoting not valid! Less than 10 voters voted.")
else:
    # Step 6: let's Show results
    print("\nVoting Complete! Here are the results:\n")
    for party, contenders in votes.items():
        print(f"Party: {party}")
        for contender, count in contenders.items():
            print(f"  {contender}: {count} votes")
        winner = max(contenders, key=contenders.get)
        print(f"  Winner in {party}: {winner} with {contenders[winner]} votes\n")

    # let's diplay the Overall winner
    overall_winner = None
    max_votes = 0
    for party, contenders in votes.items():
        for contender, count in contenders.items():
            if count > max_votes:
                max_votes = count
                overall_winner = f"{contender} ({party})"
    print(f"Overall Winner: {overall_winner} with {max_votes} votes")
