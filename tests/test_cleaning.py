from src.preprocessing.cleaning import clean_text
#test_clean_text_lowercase_text()
#remove_html
#remove_urls
#remove_emils_addresses
#normalize_whitespaces

def test_clean_text_lowercase_text():
    result = clean_text("Hello World")

    assert result == "hello world"

def test_clean_text_remove_html():
    result = clean_text("<p>Hello</p> <a>World</a>")

    assert result == "hello world"

def test_clean_text_remove_urls():
    result = clean_text("Click on this linkL: https://www.example.com")

    assert "https://www.example.com" not in result

def test_clean_text_remove_emils_addresses():
    result = clean_text("This is my email: example@gmail.com")

    assert "example@gmail.com" not in result

def test_clean_text_normalize_whitespaces():
    result = clean_text("Hello world              \n\n  this is         a         test")

    assert result == "hello world this is a test"