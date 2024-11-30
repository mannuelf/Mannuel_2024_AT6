from user_input_validator import UserInputValidator

input1 = UserInputValidator()
input1.validate_positive_integers(["-2", "-1", "0", "1", 2, 3, 4, 5, "a", "b"])
