\# Testing Strategy — Quick-Calc



\## Overview

This project applies a multi-layered testing strategy to ensure the reliability and correctness of the Quick-Calc calculator application. Testing focuses on validating core calculation logic and verifying that user interaction flows work as expected.



---



\## What Was Tested



\### Unit Testing

Unit tests were written for all core calculator operations:

\- Addition

\- Subtraction

\- Multiplication

\- Division

\- Clear function



Edge cases were also tested:

\- Division by zero

\- Negative numbers

\- Decimal numbers

\- Very large numbers



Unit tests ensure that individual functions behave correctly in isolation.



\### Integration Testing

Integration tests verify that the command-line interface works correctly with the calculator logic. These tests simulate real user interaction and confirm that input flows produce correct outputs.



---



\## What Was Not Tested

Non-functional aspects such as:

\- Performance under heavy load

\- Security vulnerabilities

\- Usability testing

\- Graphical user interface design



These were excluded because the assignment focuses on functional correctness and testing methodology.



---



\## Testing Pyramid

The test suite follows the Testing Pyramid principle:



\- \*\*Unit Tests (Majority):\*\* Most tests focus on individual functions for fast and reliable validation.

\- \*\*Integration Tests (Middle Layer):\*\* A smaller number of tests verify interaction between components.

\- \*\*UI Tests (Top Layer):\*\* Not implemented due to the simple CLI interface.



This structure ensures fast feedback and maintainable tests.



---



\## Black-Box vs White-Box Testing



\### Unit Tests — White-Box

Unit tests were written with knowledge of the internal code structure. Individual functions were directly tested to ensure correctness.



\### Integration Tests — Black-Box

Integration tests simulate user behavior without relying on internal implementation details. The system is tested from the user’s perspective.



---



\## Functional vs Non-Functional Testing



\### Functional Testing

The project focuses on functional testing:

\- Correctness of mathematical operations

\- Proper error handling

\- Accurate result display



\### Non-Functional Testing

Non-functional testing (performance, scalability, security) was not included as it falls outside the assignment scope.



---



\## Regression Testing

The test suite supports regression testing by automatically verifying existing functionality whenever new changes are introduced. Running the full test suite ensures that updates do not break previously working features.



---



\## Test Results Summary



| Test Name | Type | Status |

|-----------|------|--------|

| Calculator Unit Tests | Unit | Passed |

| CLI Integration Tests | Integration | Passed |

