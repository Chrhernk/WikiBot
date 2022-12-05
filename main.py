#comments ! << using this (#) Symbol, we can make comments in python
# In this, We'll be makign a research assistant, using class and Object.

#We will be using these libraries!
# Wikipedia
import wikipedia
#this imports our tts system
import pyttsx3
#getting our engine set up
engine = pyttsx3.init()

# Creating a function that will display info about the assistant
def display_intro():
    print(":: Introduction ::")
    print("This program will help you as a research assistant.")
    print("It will help, by researching topics for you!")
    print("\n")
    print("When you input a topic, the program will go out and research it for you!")
    print("It will also write a small report for you!")
    print("\n\n")
def display_title():
    print("\n")
    print("[]" * 25)
    print("Hello! I am Clover! Your research assistant!")
    engine.say("Hello! I am Clover, Your research assistant!")
    print("[]" * 25)
    print("\n")
    engine.runAndWait()
#creating our function to collect user's topic
def get_topic():
    #ask our user for a topic
    topic = input("Please input your topic for me to research for you!: ")
    #return the topic 
    return topic
#creating our exit statement
def exit_statement():
    #collecting the input
    answer = input (" \n If you would like to go again, input [Again], if not, input [Exit] \n ")
    #depending on the input, it runs a different section!
    if (answer == "Again"):
        main()
    elif (answer == "Exit"):
        exit()
    else:
        print("That is not an option!")
        exit_statement()
#Next up will be our main function, used to call our other functions.
#This is our Driver function.
def main():
    #calling our title function
    display_title()
    #calling the display Intro function
    display_intro()
    #call our get topic function
    topic = get_topic()
    #next, we set the subject for our bot to research
    ResearchSubject = topic
    #tell the user that we're researching the topic!
    print("I am now researching the topic " +ResearchSubject+" for you!")
    engine.say(" I am now researching the topic " + ResearchSubject + " for you!")
    engine.runAndWait()
    #call the Wiki function that we imported for our AI
    #passing in ResearchSubject as our argument
    wikipedia_page = wikipedia.page(ResearchSubject)
    #and getting the page as the retunr value
    print("\n")
    Title = wikipedia_page.title
    print("Title: " + wikipedia_page.title)
    engine.say("The title of the article is " + Title + ".")
    engine.runAndWait()
    print("\n")
    #next, printing the summary of the wiki page
    print("\n")
    print ("Summary: "+ wikipedia_page.summary)
    engine.say("The summary of the page is as follows " + wikipedia_page.summary + ".")
    engine.runAndWait()
    #now printing the contents of the page
    print("\n")
    print("Content: "+ wikipedia_page.content)
    engine.say("The Content of the page is as follows " + wikipedia_page.content + " .")
    engine.runAndWait()
    #now we print the refrences
    #print the URL of the wiki for refrences
    print("\n")
    print("References: ")
    print("URL: " + wikipedia_page.url)
    #create a list var to hold refrences
    references = wikipedia_page.references
    #print them line by line
    for reference in references:
        print(reference)
    #printing the links to the pages
    print("\n")
    print("Links: ")
    #creating a list Var for Links
    links = wikipedia_page.links
    #now printing them line by line
    for link in links:
        print(link)
    #Tell the user that the topic has been researched
    print("\n")
    print("[]" * 25)
    print("I have finished researching the topic")
    print("[]" * 25)
    print("\n")
    #make a loop back to the begining if they want
    #let them exit if they want
    exit_statement()
#Creating our entry point, which calls the pain function
#It checks if theres a main, and if so, goes there first
if __name__ == "__main__":
    #call the main function
    main()