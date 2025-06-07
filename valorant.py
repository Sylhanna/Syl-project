import random

# Define agents by role
agents_by_role = {
    "Duelist": ["Jett", "Phoenix", "Reyna", "Raze", "Yoru", "Neon", "Iso"],
    "Initiator": ["Sova", "Breach", "Skye", "KAY/O", "Fade", "Gekko"],
    "Controller": ["Brimstone", "Omen", "Viper", "Astra", "Harbor", "Clove"],
    "Sentinel": ["Sage", "Cypher", "Killjoy", "Chamber", "Deadlock"],
}

def create_random_team():
    team = []
    role_counts = {role: 0 for role in agents_by_role}
    available_agents = {role: agents.copy() for role, agents in agents_by_role.items()}

    while len(team) < 5:
        # For Duelist, max 2; for other roles, max 5 (since only Duelist is restricted)
        valid_roles = []
        for role in agents_by_role:
            if role == "Duelist":
                if role_counts[role] < 2 and available_agents[role]:
                    valid_roles.append(role)
            else:
                if available_agents[role]:
                    valid_roles.append(role)
        if not valid_roles:
            break

        role = random.choice(valid_roles)
        agent = random.choice(available_agents[role])
        team.append((agent, role))
        role_counts[role] += 1
        available_agents[role].remove(agent)

    return team

if __name__ == "__main__":
    team = create_random_team()
    print("Random Valorant Team:")
    for agent, role in team:
        print(f"{agent} ({role})")
