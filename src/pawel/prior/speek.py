import pyttsx3


def speak_sentence(sentence):
    engine = pyttsx3.init()
    engine.say(sentence)
    engine.runAndWait()


def speak_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            speak_sentence(line.strip())


if __name__ == "__main__":
    choice = input(
        "Enter '1' to speak a sentence or '2' to read from a file: ")
    if choice == '1':
        sentence = input("Enter a sentence to speak: ")
        speak_sentence(sentence)
    elif choice == '2':
        file_path = input("Enter the path to the file: ")
        speak_from_file(file_path)
    else:
        print("Invalid choice.")
