from crewai import Task
from textwrap import dedent


class Tasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a promotion!"

    def code_review(self, agent, _code):
        return Task(
            # description=dedent(
            #     f"""
            #     Review code submissions {_code} for adherence to coding standards and best practices.
            #     Provide detailed feedback and suggest improvements.
            #     Collaborate with developers to explain and discuss feedback.
            #     Conduct regular code audit sessions to maintain codebase health.
            #     Start by reviewing code submissions thoroughly and assess them against established coding standards. Provide constructive feedback on areas that require improvement and suggest specific ways to enhance the code quality. When reviewing, ensure your feedback is clear, constructive, and encourages learning and growth. Engage in discussions to address any concerns or questions the developers may have about the feedback provided.
            #
            #     In code audit sessions, focus on identifying potential issues, inefficiencies, or vulnerabilities in the codebase. Work closely with the development team to prioritize and address any outstanding issues promptly. Maintain accurate records of code review findings and improvements suggested for future reference. By upholding coding standards and best practices, you contribute to the overall quality and efficiency of the codebase.
            #     """
            # ),
            description=dedent(
                f"""              
                Your task is to review the following code snippet and provide feedback on its structure, efficiency, readability, and any potential improvements that can be made.
                ```
                {_code}
                ```
                While reviewing, pay close attention to variable naming conventions, code logic, indentation, comments for clarity, and adherence to best practices. Provide constructive feedback to help the developer enhance their code quality effectively.
                Remember, your feedback should be informative, encouraging, and focused on helping the developer grow their skills. Your insights can significantly impact the coding practices and overall performance of the developer.
                For example, when reviewing code, you should look for opportunities to optimize algorithms, suggest alternative functions for better performance, and recommend clearer variable names for enhanced readability.
                """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                Detailed code review reports with actionable feedback to improved code quality and reduced technical debt.
                """
            ),
            output_file="./reports/PR.md"

        )

    def generate_testcase(self, agent, _code):
        return Task(
            # description=dedent(
            #     f"""
            #     Create and maintain a comprehensive suite of test cases for new and existing features.
            #     Automate test cases using suitable frameworks and tools.
            #     Perform manual testing when necessary to cover complex scenarios.
            #     Code : {_code}
            #     """
            # ),
            description=dedent(
                f"""              
                I need you to generate test cases based on the following code snippets:
                {_code} 
                Please create test cases that thoroughly cover the functionality of these code snippets. 
                Ensure that the test cases are logical, cover edge cases, and validate the expected outputs for 
                different input scenarios. Your goal is to assess the correctness and robustness of the given 
                functions through your test cases. 
                 
                Generate test cases that cover a wide range of scenarios to ensure thorough testing of the provided 
                code snippets. Aim to validate both normal and boundary conditions to enhance the reliability of the 
                functions under test. """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                Generate test cases that cover a wide range of scenarios to ensure thorough testing of the provided 
                code snippets. Aim to validate both normal and boundary conditions to enhance the reliability of the 
                functions under test.
                """
            ),
            output_file="./reports/TestCases.md"

        )

    def code_documenter(self, agent, _code):
        return Task(
            description=dedent(
                f"""              
                Your task is to analyze and understand the code below in order to provide a comprehensive and detailed 
                documentation of the code. This includes explaining the purpose of the code, breaking down complex 
                functions or algorithms into simpler explanations, and providing examples where necessary to clarify 
                the code's functionality.

                {_code} 
                
                You will need to document and explain each line of code and each method or function.

                For example, when documenting a function, you would start with a brief description of what the 
                function does, followed by its input parameters, expected outputs, and any side effects. You might 
                also provide code snippets to demonstrate how the function is used in different scenarios. """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                Organize the documentation in a clear and logical manner, use proper formatting and 
                language conventions, and anticipate potential questions or areas where developers might need further 
                clarification. 
                """
            ),
            output_file="./reports/Documentation.md"

        )
    
    def write_report(self, agent):
        return Task(
            description=dedent(
                f"""
                    Gather all information from the different agents.
                    Write a detailed report with all information gathered.

                    Make sure to use the most recent data as possible and generate a detailed report organized by these sections:
                    - Code quality
                    - Performance quality
                    - Green code quality
                    - Code correction suggestion with line of code (actual and what it should be)
                    - Test cases identified by agents
                    - Detailed Code documentations identified by agents
                """
            ),
            agent=agent,
            expected_output=dedent(
                f"""
                    Report in markdown format with appropriate headings and sections. The report should be well-organized and easy to read for quick reference.
            """
            ),
            output_file="./reports/CodeReport.md"
        )
