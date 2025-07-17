class Service:
    def __init__(self):
        """
        Initializes the Service.
        """
        pass
    
    def calculate_reading_time(self, text, words_per_minute=200):
        """
        Calculates the estimated reading time for a given text.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        words = text.split()
        word_count = len(words)
        
        if word_count == 0:
            return 0
        
        reading_time_minutes = word_count / words_per_minute
        return round(reading_time_minutes, 2)

    def count_words(self, text):
        """
        Counts the number of words in a given text.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        words = text.split()
        return len(words)


