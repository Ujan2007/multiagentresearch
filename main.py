from agents.search_agent import get_search_agent
from agents.reader_agent import get_content
from agents.writer_agent import write_research

question = input("What would you like to dive into today?")

#getting the urls
sharedmemory = get_search_agent(question)

#getting the analysis info
sharedmemory = get_content(sharedmemory)

#finalanalysis
research = write_research(sharedmemory)

print(research)
    



