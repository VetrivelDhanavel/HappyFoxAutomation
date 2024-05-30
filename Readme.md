## Overview
This repository contains an automation framework for testing web applications using Selenium WebDriver in Python. The framework follows the Page Object Model (POM) design pattern for better maintainability, reusability, and scalability of test automation scripts.

##Tools :
pytest 
python 
selenium


## Pytest :

Pytest is a powerful testing framework for Python that simplifies the process of writing and executing test cases. It provides a clean and readable syntax, along with various features for efficient testing.

 pip install pytest => install pytest
 pytest or pytest -m  or pytest testcase.py => run pytest tests 

# generate report   
    pip install pytest-html
    pytest --html=report.html
 # use allure report optional : 
    pip install allure-pytest
    pytest --alluredir=allure-results
     generate report  => allure serve allure-results

## Components
1. **config/**: Contains configuration files like `config.py` to store constants, URLs, and other configurations.
2. **pages/**: Contains page object classes representing web pages.
   - **base_page.py**: Base page class with common functionalities.
   - **login_page.py**: Page object for the login page.
   - **status_page.py**: Page object for the status page.
   - **priority_page.py**: Page object for the priority page.
3. **tests/**: Contains test case classes.
4. **utils/**: Contains utility modules like `driver.py` for driver setup.

## Page Object Model (POM)
- Each web page is represented by a separate page object class.
- Page object classes contain methods to interact with elements on their respective pages.
- Page objects encapsulate the details of the page, promoting reusability and maintainability.

## Test Cases
- Test case classes reside in the **tests/** directory.
- Each test case class focuses on testing a specific scenario.
- Test methods in each class follow the Arrange-Act-Assert pattern.

## Driver Setup
- Driver setup logic is encapsulated in the `utils/driver.py` module.
- Uses `webdriver_manager` for managing browser drivers.

## Configuration Management
- Configuration values such as URLs, credentials, etc., are stored in `config.py`.
- Separate configuration files can be created for different environments (e.g., `config.py`, `config_prod.py`).

## Reporting and Logging (Optional)
- Implement logging to capture detailed execution logs.
- Use reporting tools like Allure, HTMLTestRunner, or TestNG for generating comprehensive test reports.

## Exception Handling
- Implement proper exception handling mechanisms to handle errors gracefully.

## Setup and Teardown
- Use `setUp()` and `tearDown()` methods in test case classes for setup and teardown tasks like driver initialization and cleanup.

## Documentation
- Include inline comments and docstrings to explain the purpose and usage of classes and methods.

## Version Control
- Utilize version control systems like Git to manage code changes and collaborate with team members effectively.

## Best Practices
- Modularity: Each page and functionality is isolated, making the code easier to manage and extend.
- Reusability: Common actions are encapsulated in page objects and utilities.
- Maintainability: Configuration values are centralized, and the test case is clean and easy to read.
- Best Practices: Avoiding hardcoded values, using implicit waits, and ensuring single responsibility for classes and methods.

## Code Review Comments
1. **Single Responsibility Principle**: Divide the `TestcaseHappyFox` class into smaller, more manageable components with a single responsibility.
2. **Page Object Model**: Improve and standardize the POM implementation.
3. **Hardcoded Values**: Move credentials and URLs to a configuration file or environment variables.
4. **Use of Time Delays**: Avoid `time.sleep()` in favor of WebDriver's wait mechanisms.
5. **Exception Handling**: Implement proper exception handling for robust automation scripts.
6. **Inconsistent Coding Style**: Ensure consistent naming conventions and formatting throughout the codebase.

## Conclusion
This automation framework provides a structured approach to writing and organizing Selenium test scripts, ensuring better maintainability, scalability, and efficiency in web application testing. Contributions, feedback, and improvements are welcome.