# Love Cars

This program was set up in order to analyse information provided on a Google Sheet called Love_Cars_2023. This dataset was originally imported from Kaggle. This program allows the user to pull information from the spreadsheet and finding out information such as the maximum cost of a car in this dataset, the total car sales, entering a car model and receiving information about the same car such as cost, customer rating, transmission type and so much more!
On opening this program the user is presented with a number of questions they can find out the answer to and they can select which questiom they would like to begin with. The user will be able to get the answers to all questions if they wish. 
The information displayed to the user is easily understood and organised in its format.
- (IMAGE OF PROJECT WHEN COMPLETE)

## Planning of Project
- I began to plan my project initially by brainstorming as to what type of project I would like to create using Python and I have a big interest in the data science and data anaylsis side of Python so I decided I would analyse a spreadsheet using Python. 
- I sourced my spreadsheet from <a href ='https://www.kaggle.com/'>Kaggle</a> as it has a vast range of datasheet that could be manipulated.
- I chose the <a href ='https://www.kaggle.com/datasets/anoopjohny/2023-cars-dataset'> 2023 Cars Dataset></a> as I do have an interets in cars and I believed I could make good use of this dataset. 
- Once I had the dataset chose I then imported the data set to Googlesheets.
- From here I laid out a plan for my project using <a href='https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_phrase_&km_CPC_CampaignId=1490375424&km_CPC_AdGroupID=55688907097&km_CPC_Keyword=lucid%20%2B%20app&km_CPC_MatchType=p&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433234813&km_CPC_TargetID=kwd-1642964025971&km_CPC_Country=1007880&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=Cj0KCQjwz8emBhDrARIsANNJjS6RwYy24zCQFCUOUgdm1xU7kGdINpTk-hPq88aJ0ZzMZM6RDxpHdEwaAkQ2EALw_wcB'>Lucid App</a> as can be seen. I found this very helpful as it served like a checklist to me as I progressed through my project to ensure I was doing all I needed to do. 

![LucidAppPlan](assets/readme_images/lucid_image.png)

## Contents of Project
- Data Cleaning
- Making Data Accessible
- Functions
- User Options and Instructions
- Libraries Imported

### Data Cleaning
- I had two options to choose from in relation to cleaning of the data in order to make it easier to manipluate and to give users the most accurate results also. I had spoken to my tutor about using the drop_duplicates() function imported through the Pandas library. I did attempt to do this however, unfortuantely it was taking too much time so I have added this as a feature I would like to extend onto when I do have more time. While attempting to do this I also found out that Codeanywhere could not iterate through more than approximately 100 lines without throws an error so in order to reduce these I used the functionality within Googlesheets to remove duplicates and to ensure the total dataset was less than 100 lines. 

### Making Data Accessible
- Following on from advice of my tutor I decided to make a blueprint as such for each of the columns and the header row of my datasheet in order to make all of the data easier to access in the functions that would be wrote within the project. This helped immensley as data could be easily pulled in different functions as they were declared at a Global Scope meaning they could be used anywhere within thr project.

### Functions 
- There were a number of functions I had thought of that would be possible for this project as I could see its potential for vast manipulation. 
    * 
