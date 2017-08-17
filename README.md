# Real Data Competition

This folder contains my solutions to the HackerRank's Real Data 2016 competition - https://www.hackerrank.com/real-data-contest-april-2016
I was able to secure top 20% with these solutions - https://www.hackerrank.com/results/real-data-contest-april-2016/susravan

### Twitter Hashtag Segmentation - TwitterHashtagSegmentation.py
Given a hashtag (Single word), the function returns the constituent words
Example - "wearethepeople" returns "we are the people"
It's practical applications range from getting the intent of the hashtag to discerning the sentiment of the tweet.
The program uses "google 20k word list.txt" which contains 20,000 commonly occuring English words. 

### Image Unsampling - ImageUnsampling.py
Given a downsampled image, return it's upsampled image

Input:
0,0,200 0,0,10 10,0,0
90,90,50 90,90,10 255,255,255
100,100,88 80,80,80 15,75,255

Output:
0,0,200 100,100,100 0,0,10 5,5,5 10,0,0 50,50,50
90,90,50 90,90,50 90,90,10 90,90,10 255,255,255 0,0,10
100,100,88 100,100,88 80,80,80 80,80,80 15,75,255 15,75,255 
100,100,88 100,100,88 80,80,80 80,80,80 15,75,255 15,75,255 
100,100,88 100,100,88 80,80,80 80,80,80 15,75,255 15,75,255
90,90,50 90,90,50 90,90,10 90,90,10 255,255,255 0,0,10

### Language Detection - LanguageDetection.py
Given a snippet from English, Spanish, German, French with atleast one word with more than three characters, the function returns the language of the snippet
Note: Words that are less than length three are ignored to increase the classifcation accuracy.

