import os
from decouple import config
from crewai import Crew, Process
from textwrap import dedent
from agents import ResearchCrewAgents
from tasks import ResearchCrewTasks



class ResearchCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = ResearchCrewAgents()
        self.tasks = ResearchCrewTasks()

    def run(self):
        # Initialize agents
        researcher = self.agents.researcher()
        analyst = self.agents.analyst()
        writer = self.agents.writer()

        # Initialize tasks with respective agents
        research_task = self.tasks.research_task(researcher, self.inputs)
        analysis_task = self.tasks.analysis_task(analyst, [research_task])
        writing_task = self.tasks.writing_task(writer, [analysis_task],self.inputs)

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential
        )

        # Execute the crew to carry out the research project
        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the Research Crew Setup")
    print("---------------------------------------")
    topic = input("Please enter the main topic of your research: ")
    detailed_questions = input("What specific questions or subtopics are you interested in exploring? ")

    inputs = f"Topic: {topic}\nDetailed Questions: {detailed_questions}"
    research_crew = ResearchCrew(inputs)
    result = research_crew.run()

    print("\n\n##############################")
    print("## Here are the results of your research project:")
    print("##############################\n")
    print(result)
