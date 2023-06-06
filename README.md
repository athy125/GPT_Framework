## Prompt Testing Framework for Evaluating OpenAI GPT-3 Prompts

This repository contains a Python testing framework specifically designed for evaluating prompts for OpenAI's GPT-3 language model. The framework allows you to automate the testing process, ensuring that prompts meet the desired requirements in terms of functionality and performance.

### Features

- Allows you to define test cases consisting of prompts and their expected outputs.
- Utilizes OpenAI's GPT-3 API to generate responses for each prompt.
- Compares the generated output with the expected output to determine test pass/fail status.
- Provides a summary of testing results, including the total number of tests, passed tests, and failed tests.

### Usage

1. Set up your OpenAI API credentials by replacing `'YOUR_API_KEY'` with your actual API key in the code.

2. Define your test cases using the `add_test_case` method, providing the prompt and the expected output.

3. Run the tests using the `run_tests` method, which executes each test case and compares the generated output with the expected output.

4. View the testing summary using the `display_results` method, which displays the total number of tests, passed tests, and failed tests. If any tests fail, the failed test numbers are also shown.

### Example

```python
framework = PromptTestingFramework()
framework.add_test_case("What is the capital of France?", "Paris")
framework.add_test_case("Who wrote the novel 'Pride and Prejudice'?", "Jane Austen")
framework.add_test_case("Solve for x: 2x + 5 = 15", "x = 5")

framework.run_tests()
framework.display_results()
```

This example sets up three test cases, evaluates them using the OpenAI GPT-3 engine, and displays the testing summary.

### Contribution

Contributions to this repository are welcome. Feel free to suggest improvements, report issues, or submit pull requests to enhance the functionality or performance of the prompt testing framework.

---

Feel free to customize this description as needed to provide additional details or specifications for your specific repository.
