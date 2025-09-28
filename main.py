from data import chord_lookup


def get_chords(key, nashville_numbers):
    if key not in chord_lookup:
        print(
            f"Key '{key}' not found. Available keys: {', '.join(chord_lookup.keys())}"
        )
        return
    if any(num < 1 or num > 7 for num in nashville_numbers):
        print("Nashville numbers must be between 1 and 7.")
        return

    chords = [chord_lookup[key][num - 1] for num in nashville_numbers]
    print(chords)


def main():
    print("Nashville Number Chord Lookup")

    key = input("Enter the key (e.g., C, G, F#, Bb): ").strip().capitalize()

    numbers_input = input("Enter Nashville numbers (e.g., 1 4 5 1): ").strip()

    # Convert string input to list of integers
    try:
        nashville_numbers = [int(num) for num in numbers_input.split()]
        get_chords(key, nashville_numbers)
    except ValueError:
        print("Please enter valid numbers separated by spaces.")


if __name__ == "__main__":
    main()
