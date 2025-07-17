import pytest
from src.service import Service

@pytest.fixture
def service():
    return Service()

def test_count_words_normal_text(service):
    text = "This is a sample sentence with seven words."
    assert service.count_words(text) == 8

def test_count_words_empty_string(service):
    assert service.count_words("") == 0

def test_count_words_non_string_input(service):
    with pytest.raises(TypeError):
        service.count_words(12345)

def test_calculate_reading_time_normal_text(service):
    text = "This is a test sentence with ten words total here."
    expected_time = round(10 / 200, 2)
    assert service.calculate_reading_time(text) == expected_time

def test_calculate_reading_time_empty_string(service):
    assert service.calculate_reading_time("") == 0

def test_calculate_reading_time_non_string_input(service):
    with pytest.raises(TypeError):
        service.calculate_reading_time(['not', 'a', 'string'])

def test_calculate_reading_time_custom_speed(service):
    text = "One two three four five six seven eight nine ten"
    expected_time = round(10 / 100, 2)  # slower reader: 100 wpm
    assert service.calculate_reading_time(text, words_per_minute=100) == expected_time
