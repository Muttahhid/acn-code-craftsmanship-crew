import os
from crewai import Agent
from textwrap import dedent
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
LLM_MODEL = os.getenv('LLM_MODEL')

class Agents:

    def __init__(self):
        # self.llm = Ollama(model=LLM_MODEL)
        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=LLM_MODEL
        )

    # Agent 1: Code Reviewer
    def CodeReviewer(self):
        return Agent(
            role="Code Reviewer",
            goal=dedent(f"""
                Ensure that the codebase adheres to the highest standards of quality and maintainability.
                Mentor developers by providing constructive feedback and best practices.
                Identify and eliminate potential bugs and performance issues early in the development process.    
            """),
            # backstory=dedent(f"""
            #     An expert software code reviewer, who spends all day and night thinking about code quality in terms of
            #     green code and best software craftsmanship to perform code reviews and coach developers.
            # """),
            backstory=dedent(f""" 
                You're an attentive code reviewer with a keen eye for detail, ensuring that all 
                code meets high standards of quality and efficiency. Your experience in reviewing various programming 
                languages and diverse codebases makes you a valuable asset. 
            """),
            verbose=True,
            llm=self.llm
        )

    # Agent 2: Quality Engineer
    def TestAutomationEngineer(self):
        return Agent(
            role="Test Automation Engineer",
            goal=dedent(f"""
                Identify test cases for the code
            """),
            # backstory=dedent(f"""
            #     A test automation engineer with a strong background in both manual and automated
            #     testing. Having worked in quality assurance teams for major software products, Jordan excels in
            #     identifying edge cases and ensuring comprehensive test coverage. Their analytical mindset and meticulous
            #     nature make them an expert in creating robust test cases that cover all possible scenarios.
            # """),
            backstory=dedent(f""" 
                You're a meticulous test automation engineer focused on ensuring the quality of 
                software products through automated testing. Your expertise lies in creating comprehensive test cases 
                based on existing codebases to validate functionality and performance effectively. 
            """),
            verbose=True,
            llm=self.llm
        )

    # Agent 3: Code Documenter
    def CodeDocumenter(self):
        return Agent(
            role="Code Documentation",
            goal=dedent(f"""
                Understand and document code
            """),
            backstory=dedent(f""" 
                You're an experienced code documenter with a passion for ensuring that all code is 
                well-documented for easy understanding and future reference. Your attention to detail and ability to 
                simplify complex code structures make you stand out in your field. 
            """),
            verbose=True,
            llm=self.llm
        )