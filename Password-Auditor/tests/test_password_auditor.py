from main import check_password


# Test 1: Weak password
def test_weak_password():
    score, strength, feedback = check_password("hello")

    assert score <= 2
    assert strength == "Weak"
    assert len(feedback) > 0


# Test 2: Moderate password
def test_moderate_password():
    score, strength, feedback = check_password("Hello123")

    assert score == 3
    assert strength == "Moderate"


# Test 3: Strong password
def test_strong_password():
    score, strength, feedback = check_password("BlueSky!2026Secure")

    assert score == 6
    assert strength == "Strong"
    assert len(feedback) == 0


# Test 4: Common password
def test_common_password():
    score, strength, feedback = check_password("password123")

    assert score == -1
    assert strength == "Weak"
    assert any("too common" in item.lower() for item in feedback)


# Test 5: Missing uppercase letters
def test_missing_uppercase():
    score, strength, feedback = check_password("helloworld123!")

    assert any("uppercase letter" in item.lower() for item in feedback)


# Test 6: Missing numbers
def test_missing_number():
    score, strength, feedback = check_password("HelloWorld!")

    assert any("at least one number" in item.lower() for item in feedback)


# Test 7: Missing special characters
def test_missing_special_character():
    score, strength, feedback = check_password("HelloWorld123")

    assert any("special character" in item.lower() for item in feedback)


# Test 8: Repeated characters
def test_repeated_characters():
    score, strength, feedback = check_password("Aaaaaaaaaaa123!")

    assert any("repeated characters" in item.lower() for item in feedback)


# Test 9: Sequential characters
def test_sequential_characters():
    score, strength, feedback = check_password("abcdef!2026")

    assert any("sequential characters" in item.lower() for item in feedback)


# Test 10: Missing lowercase letters
def test_missing_lowercase():
    score, strength, feedback = check_password("HELLOWORLD123!")

    assert any("lowercase letter" in item.lower() for item in feedback)