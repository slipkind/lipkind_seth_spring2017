
# Seth Lipkind - Midterm

# Question 1 
############################################################################################################################

# Enron Analysis 1
- Parse through each of the 4 key players and see how many emails they sent to people
- Key players were gotten from http://www.nytimes.com/2006/01/29/business/businessspecial3/10-enron-players-where-they-landed-after-the-fall.html?module=ArrowsNav&contentCollection=undefined&action=keypress&region=FixedLeft&pgtype=article
- I selected: Kenneth Lay, Jeffrey K. Skilling, Greg Whalley, and Vincent J. Kaminski
- I searched through their sent folder and counted the number of times they sent an email to someone
- For some strings, they emailed many people, so I had to split at the comma and remove any leading empty spaces
- CONCLUSION:
   - Vincent Kaminski was the most suspicious, as he sent over 1000 emails to his aol email address.  Definitely should look at those

# Enron Analysis 2
- Parse through each of the Kaminski emails he sent, and find how many attachments were sent
- The emails with the most attachments should be inspected
- CONCLUSION:
    - Emails 2272 and 1190 should be inspected since they each have at least 26 mentions of a .doc file

# Enron Analysis 3
- Parse through each of the Kaminski sent, and find which day had the most emails
- The day with the most emails should be investigated
- CONCLUSION:
    - The day that should be investigated is: 1/11/2000

# Question 2
############################################################################################################################

# First analysis of Articles:
- This analysis was to see which article had the most words on the first 20 pages of the articles api on 03/03/2017
- Each page had responses which contained documents
- Each document had a headline and a word count
- Using the two keys above, I was able to create a dictionary that was later sorted based on word count
- CONCLUSION:
    - "Inside Sara Berman's closet has the most words of any article written from the first 20 pages as of 03/03/2017

# Second Analysis of Articles API:
- There were 190 articles printed in the first 20 pages of the articles api on 03/03/2017
- Of that list: 70 were from the 'Associated Press', 62 were from 'Reuters', 56 were from 'The New York Times', 1 was from 'CNBC', and 1 was from 'Internation New York Times'
- This shows that the New York Times does not print as often as either the Associated Press (1st) or Reuters (2nd)
- CONCLUSION:
    - The New York Times writes only the third most articles, indicting either there is more staff at Associated Press and Reuters, or The New York Times does not bring in as much money as the first two elements

# Third Analysis of Articles API:
- This analysis was to see which section had the most articles written about it
- There was a total of 20 sections that had articles written about them
- The most commonly written about sections were: "U.S.", "World", and "Business Day"
- CONCLUSION:
    - "Most readers care more about the U.S. and World News than they do about all other news.

# First Archive Analysis
- First analysis of the archive files was to show zipfs law with stopwords
- Conclusion:
    - The graph that is saved as: zipfs_archives_2010-2017_withstopwords.png confirms that zipfs law still holds true.  After doing a log-log plot it shows that the most common word is used about twice as frequently as the next word and so on, until the end where all words are used once.

# Second Archive Analysis
- Second analysis of the archive files was to show zipfs law without stopwords
- Conclusion:
    - The graph that is saved as: zipfs_archives_no_stopwords_2010-2017.png confirms that zipfs law still holds true.  After doing a log-log plot it shows that the most common word is used about twice as frequently as the next word and so on, until the end where all words are used once.

# Third Archive Analysis
- Third analysis of the archive files was to count the number contributions each author made to see who deserves a raise
- This analysis required looking at all archives from 2010-present and looking at all of the contributors in the byline
- After getting the list of contributors, counting how many instances of their names was next.
- CONCLUSION:
    - Paul Krugman had his name against the most stories (665), so he is going to get a raise
