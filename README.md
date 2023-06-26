# Chatbot

* With the recent release of the GPT 3.5 series API by OpenAI, we can do much more than just chit-chatting. One very productive use case for businesses and your personal use is QA (Question Answering). what if we want to build a little chatbot that only use your own custome data. build a ask me anything chatbot that answer all your question about datascience, ai, machine learning, deeplearning based on the content from naver 지식in webstie in this area

### 1. Data Collect

* For this project, i will collect data from  https://kin.naver.com/. Unfortunately, this website doesn't not provide public API, so i decided to use python (beautifulSoup) to scrape title of post, content of post, date, comment based on the search topic "data science", "bigdata", "AI", "machine learning", "data analyst".

* ## 2. EDA

* * Count of posts by year for each topic
  * WordCould
 
    ## 3. Build Chatbot

    * we can augment a large language model such as gpt-3.5-turbo that is underlying the chatGPT with our own Naver 지식인 data. this is also called in context learning where we insert context into the inputs prompt and that way we can take advantage of the large language models reasoning capabilities to generate answers to our questions. one simple way to do this with chatGPT
    *  To pass on large context data like our comments data, we need to use a package called Lama index
    *  We will need to create the context file which is in our case just a large text file combining all the text from the Naver 지식인 posts and the comments that we have retrieved.
    *  After done, we will hand on building chatbot with the workflow:
       ** 1. Build an index of your document data with LlamaIndex
       ** 2. Query the index with natural language
       ** 3. LlamaIndex will retrieve the relevant parts and pass them to the GPT prompt
       ** 4. Ask GPT with the relevant context and construct a response
  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c08e27d4-274e-4d81-b026-0e3cbbe50510/Untitled.png)
