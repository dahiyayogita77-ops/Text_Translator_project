# Human-Friendly Text Translator using Deep Translator
# By: Yogita Dahiya

from deep_translator import GoogleTranslator

def main():
    print("\n Welcome to the Text Translator!")
    print("This tool lets you translate text from one language to another.")
    print("---------------------------------------------------------------\n")

    while True:
        try:
            # Ask user for text to translate
            text = input(" What text would you like to translate? (type 'exit' to quit): ").strip()
            if text.lower() == 'exit':
                print("\n Thanks for using the translator. Goodbye!\n")
                break

            # Ask for source language
            src_lang = input("️ Which language is this text in? (e.g., 'en' for English): ").strip().lower()

            # Ask for destination language
            dest_lang = input(" What language do you want to translate it to? (e.g., 'hi' for Hindi): ").strip().lower()

            # Perform translation
            translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)

            # Show result
            print(f"\n Translated from '{src_lang}' to '{dest_lang}':\n {translated}\n")

        except Exception as e:
            print(f"\n Oops! Something went wrong: {e}\nPlease try again.\n")

# Run the program
if __name__ == "__main__":
    main()
