def generate_game(n, source, auxiliary, target, state, count_steps):
    if n == 1:
        disk = state[source].pop()
        state[target].append(disk)
        count_steps[0] += 1
        print(f"Move disk from {source} to {target}: {disk}")
        print(f"Intermediate state: {state}\n")
    else:
        generate_game(n-1, source, target, auxiliary, state, count_steps)
        disk = state[source].pop()
        state[target].append(disk)
        count_steps[0] += 1
        print(f"Move disk from {source} to {target}: {disk}")
        print(f"Intermediate state: {state}\n")
        generate_game(n-1, auxiliary, source, target, state, count_steps)
    return state

def main():
    try:
        n = int(input("Please enter the number of disks: "))
        if n <= 0:
            raise ValueError("The number of disks must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    count_steps = [0]

    state = {
        "A": [i for i in range(n, 0, -1)],
        "B": [],
        "C": []
    }

    print("Initial state:", state, "\n")
    generate_game(len(state["A"]), "A", "B", "C", state, count_steps)
    print("Final state:", state)
    print(f"Total steps taken: {count_steps[0]}")

if __name__ == "__main__":
    while True:
        main()
        again = input("Would you like to try again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for playing!")
            break
