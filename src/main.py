from service import Service

class Main:
    def __init__(self):
        self._service = Service()
        
    def run(self):
        text = input("Enter your text: ")

        word_count = self._service.count_words(text)
        reading_time = self._service.calculate_reading_time(text)

        print(f"\nWord count: {word_count}")
        print(f"Estimated reading time: {reading_time} minutes")

if __name__ == "__main__":
    main = Main()
    main.run()


