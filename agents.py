from crewai import Agent
#from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq  # Import Groq client
from langchain_openai import ChatOpenAI
import os
from crewai_tools import SerperDevTool,WebsiteSearchTool, ScrapeWebsiteTool,PDFSearchTool 



class ResearchCrewAgents:

    def __init__(self):
        # Initialize tools if needed
        self.serper = SerperDevTool()
        self.web = WebsiteSearchTool()
        self.web_scrape=ScrapeWebsiteTool()
        self.pdf_search =PDFSearchTool()
    

       # OpenAI Models
        self.gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.gpt4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.7)
        self.gpt3_5_turbo_0125 = ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.7)
        self.gpt3_5_turbo_1106 = ChatOpenAI(model_name="gpt-3.5-turbo-1106", temperature=0.7)
        self.gpt3_5_turbo_instruct = ChatOpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.7)
        
        # Groq Models
        self.llama3_8b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="llama3-8b-8192")
        self.llama3_70b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="llama3-70b-8192")
        self.mixtral_8x7b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="mixtral-8x7b-32768")
        self.gemma_7b = ChatGroq(temperature=0.7, groq_api_key=os.environ.get("GROQ_API_KEY"), model_name="gemma-7b-it")
        
        # CHANGE YOUR MODEL HERE
        self.selected_llm =self.llama3_70b
    def researcher(self):
    # Detailed agent setup for the Research Expert
        return Agent(
        role='Market Researcher',
        goal='To Conduct deep market research on a product or an idea,and check all available resources to ensure thorough and indepth research ',
        backstory="As an expert in conducting market research ,you are charged with the responsibility of researching on an idea, product or service",
        verbose=True,
        allow_delegation=False,
        llm=self.selected_llm,
        max_iter=3,
        tools=[self.serper, self.web, self.web_scrape],
        ) 


    def analyst(self):
        # Detailed agent setup for the Analyst
        return Agent(
            role='Analyst',
            goal='Critically analyse the search result and provide insights and clearer view of the product or service',
            backstory="You are a respected analylst with good judgement,repected because of your analytical and predictive skills,you are expected to be critical in reasoning, very objective and always use numerical decription to provide depth in your analysis.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            max_iter=3,


        )

    def writer(self):
        # Detailed agent setup for the Writer
        return Agent(
            role='Blog writer',
            goal='Provide clean,readable and excellent writeup,that will keep readers engaged and wanting to read more,the points must easily be seen in the opening paragraphs and a delight to the readers.',
            backstory="You are a respected blog writer , a worldwide acclaimed journalist,your writing style in terms of delivery is super engaing and that is why the team needs you to do a clean job in deliverying the blog style article.",
            verbose=True,
            allow_delegation=False,
            llm=self.selected_llm,
            tools=[self.serper, self.web, self.web_scrape],
            max_iter=3,


        )
    def cache_function(**args):
        return False