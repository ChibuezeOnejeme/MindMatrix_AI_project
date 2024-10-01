## Project MINDMATRIX INTELLIGENT RESEARCH AGENTS

### Objective:

This project is to create AI agents that is capable of utilizing Large language Models(LLM) to perform assigned tasks in this case a marketing research role for a ,using tools provided eg SerperDevTool,WebsiteSearchTool, ScrapeWebsiteTool,PDFSearchTool  and these tools was from imported crewai_tools library.And these agents work as a team, there is one fro core research,another one for analysis and the final agent to pencil it down in writing in form of a summarized blog post.
There are additional parameters handed over to the agents eg goal and back story for them to fully understand the mission and the project goal/output.




### Key Steps:

1. **Install Required Tools:**

   - Ensure you have VS Code, GIT,and Poetry installed on your computer. Follow a guide to set up these tools if needed.

2. **Clone GitHub Repository:**

   - Copy the GitHub repository link and use the command `git clone <repository link>` to clone the project.
   - Move into the project folder using `cd <folder name>`.

3. **Install Dependencies:**

   - Run `poetry install --no-root` to install project dependencies.

4. **Set Up API Keys:**

   - Add API keys for Groq, and Serper in the Streamlit_app.py file.
   - Alternatively, create a `.env` file with API keys and place it in the specified directory.
   - Remember to add your Api keys to `gitignore file` to avoid your API keys being exposed

5. **Run the Application:**

   - Execute `streamlit run mindmatrix.py` to start the application.
   - Enter search topics or queries to test the application functionality.

6. **Customize Language Models:**

   - Modify the `agents.py` file to change the large language model being used.
   - Update the selected model in the code to switch between available options.

### Worthy of Noting:

- Ensure that you have a dummy OpenAI API keys exposed see what i did in mindmatrix.py file else it might throw an error.



