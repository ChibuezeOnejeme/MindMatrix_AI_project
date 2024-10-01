from crewai import Task

from crewai import Task

class ResearchCrewTasks:

    def research_task(self, agent, inputs):
      return Task(
          agent=agent,
          description=f" Based {inputs} conduct a thorough research checking the best respectable resources online,ensure they speak to numbers and they are verifiable",
          expected_output=f"Clean presented research report on the market subject matter"

      )


    def analysis_task(self, agent, context):
      return Task(
        agent=agent,
        context=context,
        description=f"Evaluate the following report: {context}. Based on the results,and anlysis critically .",
        expected_output=f"provide a robust critically analysed result for the  next agent"
   
    )


    def writing_task(self, agent, context, inputs):
        return Task(
            agent=agent,
            context=context,
            description=f"Answer the users inquiry their request topics: {inputs} Given the following the requested{context}, using web search, web scraping ,craft the best report and deliver meaning and understanding that is easily digestible",
            expected_output=f"write a stellar blog style report that is engaging ,smooth and very understandable.",
        )




