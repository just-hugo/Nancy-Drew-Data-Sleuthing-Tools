# Murder Rates API day 1 postmortem

## What I Did

-Installed the CDE (FBI Crime Data Explorer) app locally
-Used Python to hit the FBI API after signing up for an API key and researching some API parameters (ORI, count,etc)
-Used Python to hit the BJS API
-Expored an open source FBI Crime Data API Wrapper repo
-Used Python and a variety of libraries (csv, json, beautifulsoup, lxml, ast) to attempt to extract data from the API payloads

## What went well (Gains)

Was able to work through initial technical problems and several layers of documentation to get set up and resolve all the quirks of getting started (python envs, cloning/working with git repos, setting up local dev server)
Worked with several new libraries without major issues (outside of the problems of working with data)
Was able to successfully hit a couple of endpoints, returning payloads with data to parse.

## What couldve gone better (Setbacks)

Got sidetracked several times with things that ultimately weren't that useful (the cde local app server, finicky git stuff), sinking some of my most productive hours into things that didn't achieve my goal (even if they in themselves were rewarding learning experiences)

## Challenges

The payloads returned by both the FBI API and the BJS API have been difficult to work with. I'm unsure if the issue is formatting inherent in the payload or if there is a gap in my knowledge/something that I am doing incorrectly in trying to work with them. I'm unable to extract any useful data from them.

## Outstanding Questions

Am I misusing the libraries or is there some quirk to the data?
It seems like I am missing some understanding of the data I'm getting and how to work with it.

## Next Steps

Post to stack overflow
Deep dive into working with json data
Deep dive into how API data works, is formatted, working with API payloads
Work through the Coding For Journalists section on APIs and databases

# Murder Rates API day 2 postmortem

## What I Did

[Strings, Unicode, and Bytes in Python 3: Everything You Always Wanted to Know](https://medium.com/better-programming/strings-unicode-and-bytes-in-python-3-everything-you-always-wanted-to-know-27dc02ff2686)

Read up on data types in Python 3

Researched how to handle API responses and how to save API responses in JSON format

[How do I write JSON data to a file?](https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file)

[Python: Saving API result into json file?](https://stackoverflow.com/questions/50262879/python-saving-api-result-into-json-file)

[How to write the response in a file with JSON format using python?](https://stackoverflow.com/questions/52893297/how-to-write-the-response-in-a-file-with-json-format-using-python)

## What went well (Gains)

Was able to identify relatively quckly that I had missed a crucial step in handling the response, which was causing the data to have weird, difficult-to-understand formatting and be difficult to work with. 

## What couldve gone better (Setbacks)

## Challenges

I feel like I have to "Yes, and," a lot of concepts instead of thoroughly understanding them — even though I have a decent high level idea of the solutions from SO that I applied, I'm still not 100% sure what's going on under the hood, which means that I'll need to do this a few more times before it really sinks in.

## Outstanding Questions

## Next Steps

Now that I have a basic model for how the response data works, I need to do more exploratory testing of the endpoints available through the FBI API, in order to figure out which ones are needed for the demographic per capita calculations for this project

Then I need to do the same thing with the BJS endpoint

Then I need to extract the data from the relevant endpoints 

Then I need to transform it using per capita calculations

Then I need to clean up/refactor the project directory to create a streamlined program to hit the APIs and return the statistics I want to display

Then I need to figure out how to display that data on a front end

# Murder Rates API day 3 and 4 postmortem

## What I Did

While inspecting data returned from the FBI API, I discovered that much of the data was incomplete, returning numbers that clearly were not reflective of the overall murder rate each year. 

While there is probably complete information buried somewhere in one of their endpoints, I decided to backburner my exploration of how to work with their endpoints in order to explore the CDC's Wonder API, which contains more robust information and does not rely on law enforcement reporting for their sources. 

I plan to return to the FBI API in order to have multiple datasets to work with, but have pivoted in the immediate term to the CDC API, which is both more complex to work with and more robust in the degree of information available. 

The CDC API requires quite a bit of setup to get working. I spent a bit of time getting the POST request parameters working based on CDC documentation as well as an old Reddit thread where other people were figuring out some of the kinks involved.

Most of my time has been spent writing up documentation on the query parameters for the endpoint I want to work with, but the end result will (hopefully) make it easier to work with in the future. 

## What went well (Gains)

Though the CDC API is complex, I was able to break it down into manageable parts and understand what it needs to return data inside an afternoon. This involved both understanding the setup for the POST request in Python and analyzing the query parameter structure and naming conventions. 

## What couldve gone better (Setbacks)

Structuring the query parameters is tedious and time-consuming and involves a lot of cross-referencing and reading to understand each parameter's name-code and function. 

## Challenges

Understanding the cryptic nature of the API took time

Formatting API queries is eating a lot of time

## Outstanding Questions

How to streamline the query-writing process? 

## Next Steps

# Murder Rates API week 2 postmortem

## What I Did

Spent time annotating each parameter in the D76 example query, to make sure I understood how it worked and to provide documentation for future use. I then formatted the header data I grabbed from the user portal as a query parameter set and was able to successfully get a 200.

## What went well (Gains)

I quickly got the hang of how query parameters correlate to the user portal and overall got a solid understanding how how the database works.

## What couldve gone better (Setbacks)

The time it took to annotate the sample query was quite extensive, and overall both annotating the sample query and formatting the header data into parameters was tedious. 

## Challenges

The response body is formatted in such a way that when you use multipl Sort By options, pulling the data out becomes much more complicated (though doable). 

The easiest solution is to perform multiple calls, each with a single Sort By parameter, then extract the data and operate on it to show useful intersections.

## Outstanding Questions

## Next Steps

Write a script to take header form data and format it into query parameters.

Write a script for each API call needed to get all the data. 

Extract the data from each call.