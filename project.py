import random


def read_vocab_from_file(file_path):
    vocab = {}
    with open(file_path, 'r') as file:
        for line in file:
            english, spanish = line.strip().split(',')
            vocab[english.strip()] = spanish.strip()
    return vocab

def get_random_words(vocab, num_words):
    words = random.sample(list(vocab.keys()), num_words)
    return words

def calculate_score(total_questions, correct_answers):
    return correct_answers / total_questions * 100

def main():
    file_path = "/workspaces/55799578/project/spanish_vocab.txt"
    vocab = read_vocab_from_file(file_path)

    print("Welcome to the Spanish vocabulary learning game!")
    print("Type 'exit' to quit the program.")

    total_score = 0
    while True:
        level = input("Select a level (1, 2, or 3) or type 'exit' to quit: ").strip().lower()

        if level == 'exit':
            print("Thank you for using the program. Adiós!")
            break

        if level not in ['1', '2', '3']:
            print("Invalid level. Please select 1, 2, or 3.")
            continue

        num_words = 5 if level == '1' else (10 if level == '2' else 15)
        words = get_random_words(vocab, num_words)

        print(f"Level {level} - You will be tested on {num_words} words.")
        score = 0
        for word in words:
            answer = input(f"What is the Spanish equivalent of '{word}'? ").strip().lower()

            if answer == 'exit':
                print("Thank you for using the program. Adiós!")
                break

            if answer == vocab[word].lower():
                print("Correct! ✔️")
                score += 1
            else:
                print(f"Wrong. The correct answer is '{vocab[word]}'. ❌")

        total_score += score
        print(f"Level {level} completed. Your score for this level: {score}/{num_words}")
        print(f"Total score: {total_score}/{num_words * (int(level))}")
        print(f"Overall accuracy: {calculate_score(num_words * (int(level)), total_score)}%")

if __name__ == "__main__":
    main()