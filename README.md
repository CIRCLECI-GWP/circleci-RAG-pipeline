# Tools and prerequisites
To build your LLM and set up automated testing, you’ll need the following frameworks and tools:

-   [CircleCI](https://circleci.com/signup/) – A configuration-as-code CI/CD platform that allows users to run and orchestrate cloud-based pipelines across machines.
    
-   [LangChain](https://docs.langchain.com/docs/) – An open-source framework for developing language model-powered applications. It provides prompt templates, models, document loaders, text splitters, and [many other tools for interacting with models](https://docs.langchain.com/docs/category/components).
    
-   [LangSmith](https://docs.smith.langchain.com/) – A tool created to more efficiently debug language model applications by showing the trace of LLM calls, as well as inputs and outputs for certain prompts. This allows you to view the test results and metadata for all LLM calls in a single dashboard.
    
-   [ChromaDB](https://docs.trychroma.com/) – An open-source embedding database/vector store, which tokenizes inputs (in our case, text) and stores them in an n-dimensional vector space. Chunks of text similar to new inputs can be returned using a modified K-nearest-neighbor algorithm in the vector space.



# Directory structure
 - The rag/ directory contains an example LLM-powered application and unit test suite spread across multiple Python scripts.
	 - These scripts rely on a .env file with API keys to OpenAI and Langchain, as well as other environment variables. An example is provided, but you need to populate it with your own variables.
 -   The tools/ directory contains a script for setting up the environment to run the ML workflow and testing it locally.
    
 -   Finally, the .circleci/ directory contains the CircleCI config.yml that defines the CircleCI pipelines that call the ML scripts.


# Set up environment
 -  Fork the example repository and clone your forked version locally.
    
 -  Install your virtual environment using `source ./tools/install-venv.sh`
    
	 - This will enter a Python [virtual environment](https://docs.python.org/3/library/venv.html) and make sure all of the necessary packages in requirements.txt are installed. After running the command, you should see a new venv/ directory and your command line prompt should be prepended with `(venv)` to indicate you are in the virtual environment.
	 - You can leave the virtual environment any time with the `deactivate` command. After executing this command, `(venv)` should no longer be prepended to your prompt, which is how you know you are no longer in the virtual environment.
	 - **Note: You must [source](https://ss64.com/bash/source.html) the script rather than executing. If not, a new process will be spawned, the child process will enter the virtual environment by setting its environment variables, then it will exit, leaving your original shell process without the right environment variables.**
    

 -  Create a .env file by running `cp .env.example .env`, then set the necessary environment variables in it. This will include:
	 - **OpenAI API key**: Go to [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys), set up a paid account, and create a new secret key. This key should be stored in the `OPENAI_API_KEY` environment variable in your .env file.
	 - **LangChain API key**: Go to [https://smith.langchain.com/](https://smith.langchain.com/), create an account, and create an API key by clicking on the API Keys button on the bottom left of the page and following the instructions. This key should be stored in the `LANGCHAIN_API_KEY` environment variable in your .env file.


# Run the application
## Start the server
    flask --app rag/app run &  # spin up the Flask server

## Interact with the server

    curl -X POST -H "Content-Type: application/json" -d '{"message": "What is LangSmith?"}' http://localhost:5000

Ask the application different questions by changing the `message` field in the curl command.

## Stop the server

    fg [job no. of server]
    Ctrl-C

# Where to go from here
More detailed tutorials showing how to test and run this application are available here:

 - TODO: link 1
 - TODO: link 2

