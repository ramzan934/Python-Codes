from collections import Counter

print("===== WORD FREQUENCY COUNTER =====")

try:
    file_name = input("Enter text file name (e.g., sample.txt): ").strip()

    with open(file_name, "r") as file:
        text = file.read()

    # Clean and split text
    words = text.lower().replace("\n", " ").replace(".", "").replace(",", "").split()

    # Count words
    word_count = Counter(words)

    print("\nWord Frequencies:")
    for word, freq in word_count.most_common():
        print(f"{word} : {freq}")

except FileNotFoundError:
    print("File not found. Please check the file name.")
except Exception as e:
    print("Error:", e)

