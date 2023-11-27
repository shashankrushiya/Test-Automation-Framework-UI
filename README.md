# Test Automation Framework README

## Hybrid Test Automation Framework

This repository contains a hybrid test automation framework that integrates both data-driven and method-driven approaches. The framework is built on the concept of Page Object Model (POM) to enhance test maintainability and readability.

### Directory Structure

1. **configfiles**: This directory stores configuration files containing variables, constants, URLs, and paths used across the test suite.

2. **page**: The page directory adheres to the Page Object Model (POM) and holds classes representing web pages. Each page class encapsulates the interactions and elements of the respective page, promoting modularity and reusability.

3. **reports**: The reports directory is designated for storing test execution reports. These reports provide insights into test results, aiding in the identification and resolution of issues.

4. **screenshots**: In case of test failures, the screenshots directory captures screenshots for further analysis and debugging. Screenshots can be instrumental in understanding the state of the application at the time of failure.

5. **testcases**: This directory contains test cases written in a format that aligns with the hybrid framework's data-driven and method-driven approach. Test cases may utilize data from external sources, promoting flexibility and scalability.

6. **conftest.py**: The conftest file is responsible for setup and teardown procedures that are executed before and after test execution. This includes configurations like initializing the test environment and closing resources after test completion.

7. **utilities**: The utilities directory houses modules and functions that provide essential services for the framework. Notable components include:

   - **wait_module**: A module for implementing dynamic waits, ensuring synchronization between the test script and the application under test.
   - **generic_methods**: Contains generic methods that can be reused across different test scenarios, enhancing code maintainability and reducing redundancy.

### Getting Started

To utilize the framework, follow these steps:

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Configure the variables, constants, URLs, and paths in the `configfiles` directory according to your test environment.

3. Write test cases in the `testcases` directory, leveraging the hybrid approach and adhering to the Page Object Model.

4. Execute the tests using your preferred test runner. I personally prefer local terminal with same directory to run testcases by following command:

   ```bash
   pytest --html=./reports/report.html
   ```

### Contact

For any questions or feedback, please contact Shashank Rushiya at mailId: shashankrushiya@gmail.com or cell: 8446278818.