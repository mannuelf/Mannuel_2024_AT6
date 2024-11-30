class UserInputValidator:
    def __init__(self):
        self.numbers = []

    def validate_positive_integers(self, input_list):
        self.numbers = []

        for item in input_list:
            try:
                if isinstance(item, str) and not item.isdigit():
                    print(f"This input is not a valid number string: {item}")
                    continue

                if isinstance(item, str):
                    num = float(item)
                else:
                    num = float(item)

                if num > 0 and num.is_integer():
                    print(
                        f"This number is positive: {int(num)}, adding to list")
                    self.numbers.append(int(num))
                else:
                    print(
                        f"This number is not positive or not an integer: {item}")
            except ValueError:
                print(f"Invalid input: {item}")

        print(f"Validated positive integers: {self.numbers}")
        return self.numbers
