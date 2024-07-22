import os
from crewai import Agent, Task, Crew, Process
from textwrap import dedent
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.llms import Ollama
from agents import Agents
from tasks import Tasks


load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
LLM_MODEL = os.getenv('LLM_MODEL')

FILE_NAME='java_code.java'

class CCCrew:
    def __init__(self):
        # self.llm = Ollama(model=LLM_MODEL)
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=LLM_MODEL
        )
        self._code = open(FILE_NAME).read()

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = Agents()
        tasks = Tasks()

        # Define your custom agents and tasks here
        code_reviewer = agents.CodeReviewer()
        test_engineer = agents.TestAutomationEngineer()
        code_documenter = agents.CodeDocumenter()

        # Custom tasks include agent name and variables as input
        code_review = tasks.code_review(
            code_reviewer,
            self._code
        )

        testcase_generator = tasks.generate_testcase(
            test_engineer,
            self._code
        )

        code_documentation = tasks.code_documenter(
            code_documenter,
            self._code
        )
        
        write_report = tasks.write_report(
            # code_reviewer,
            code_documenter
        )

        # Define your custom crew here
        crew = Crew(
            agents=[code_reviewer, test_engineer, code_documenter],
            tasks=[code_review, testcase_generator, code_documentation, write_report],
            verbose=True,
            # process=Process.sequential,
            # memory=True,
            # embedder={
            #     "provider": "gpt4all"
            # },
            process=Process.hierarchical,
            manager_llm=self.llm
        )

        _result = crew.kickoff()
        return _result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI")
    print("-------------------------------")
    ccc = CCCrew()
    result = ccc.run()
    print("\n\n########################")
    print("## Here is your result:")
    print("########################\n")
    print(result)