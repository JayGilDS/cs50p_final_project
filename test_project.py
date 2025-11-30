import pytest
from project import read_vocab_from_file, get_random_words, calculate_score

def test_read_vocab_from_file():
    file_path = "/workspaces/55799578/project/spanish_vocab.txt"
    vocab = read_vocab_from_file(file_path)

    assert len(vocab) > 0, "The vocabulary dictionary should not be empty."
    assert isinstance(vocab, dict), "The vocabulary should be a dictionary."

def test_get_random_words():
    vocab = {
        "apple": "manzana",
        "banana": "plátano",
        "cat": "gato",
        "dog": "perro",
        "hello": "hola",
        "goodbye": "adiós",
    }

    num_words = 3
    words = get_random_words(vocab, num_words)

    assert len(words) == num_words, f"Expected {num_words} words, but got {len(words)}."

    for word in words:
        assert word in vocab, f"Random word '{word}' not found in the vocabulary."

def test_calculate_score():
    total_questions = 20
    correct_answers = 15

    score = calculate_score(total_questions, correct_answers)
    expected_score = (correct_answers / total_questions) * 100

    assert score == expected_score, f"Expected score: {expected_score}, but got {score}."

if __name__ == "__main__":
    pytest.main()