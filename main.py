import openai

# Set up OpenAI API credentials
openai.api_key = 'YOUR_API_KEY'


class PromptTestingFramework:
    def __init__(self):
        self.test_cases = []
        self.passed_tests = []
        self.failed_tests = []

    def add_test_case(self, prompt, expected_output):
        self.test_cases.append((prompt, expected_output))

    def run_tests(self):
        for i, (prompt, expected_output) in enumerate(self.test_cases):
            print(f"Running test #{i + 1}")
            print("Prompt:")
            print(prompt)
            output = self.generate_output(prompt)
            print("Expected Output:")
            print(expected_output)
            print("Actual Output:")
            print(output)
            if output == expected_output:
                self.passed_tests.append(i + 1)
                print("Test Passed\n")
            else:
                self.failed_tests.append(i + 1)
                print("Test Failed\n")

    def generate_output(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].text.strip()

    def display_results(self):
        print("Testing Summary:")
        total_tests = len(self.test_cases)
        passed_tests = len(self.passed_tests)
        failed_tests = len(self.failed_tests)
        print(f"Total tests: {total_tests}")
        print(f"Passed tests: {passed_tests}")
        print(f"Failed tests: {failed_tests}")
        if failed_tests:
            print("Failed Test Numbers:", self.failed_tests)


# Example usage
framework = PromptTestingFramework()
framework.add_test_case("What is the capital of France?", "Paris")
framework.add_test_case("Who wrote the novel 'Pride and Prejudice'?", "Jane Austen")
framework.add_test_case("Solve for x: 2x + 5 = 15", "x = 5")

framework.run_tests()
framework.display_results()


