# Capstone
Domain specific keywords/terms highlighting model <br>
Domain: tennis tournament press conference (English/Chinese)<br>
Thought and process credit: [Intro to NLP with spaCy](https://www.youtube.com/watch?v=WnGPv6HnBok&list=PLBmcuObd5An559HbDr_alBnwVsGq-7uTF)



## OVERVIEW
I'm trying to train a custom name entity model with spaCy for specific domains to help Chinese/English interpreters prepare for work. 



## WHY THIS?
When I was a conference interpreter before the pandemic, one of the time-consuming tasks for me and many of my colleagues was (and still is I believe) to get familiarized with specific domains. <br>
As freelance interpreters, we work with clients in all fields. Whenever we work with a new client in a field we don't know much about for the first time, we will need to spend days on documents (slides/PDFs and so on) that client offers us for preparation, mostly for two things:
- Go through everything to make sure we don't miss anything important **that we don't know**
- Google things that we don't know at the same time



#### And the problems are:
- Going through everything takes a lot of time. What we need to spot is usually new words and/or domain specific terms, and everything else would be generic. But we cannot skip any part since we don't know where those new words and terms are. When there are hundreds of pages to read, it's not hard to imagine how much time is actually wasted.
- Googling things is another big pain for political reasons if the interpreter lives in Mainland China. It's technologically demanding, time-consuming and even a bit unsafe.

So, a custom name entitiy model with sufficient entities and proper visualization can help address both problems. 



## THE DOMAIN
I decided to do one domain to start out: 
- Press conferences of WTA (the Women's Tennis Association) matches

I like tennis. I watch lots of tennis games, I know all the rules, and I even once bought a tennis ball machine for my own practice. The first time I got to work with WTA tournaments in China, I was so excited but also sure I could do a great job. 
And I did, but only according to WTA. They were very happy about my performance and booked me right away for the next year. They said I was the best interpreter they saw in the entire China tour because I know enough about tennis.<br>
But I knew I missed a few things here and there. There are tournaments that I've never watched or even heard of, new players from different countries appear all the time with very long and hard to pronounce/remember names, there were even mentionings of anecdotes about well-known plays that I never dug. <br>
Then I talked to a few of my colleagues who did this before WTA found me. None of them are tennis fans and all of them told me reading through past transcripts is already a pain because there is so much they have no idea about. <br>
Things that are difficult for non tennis fans can be broken into four categories:
1. **Tennis tournament titles**, like all 4 Grand Slams, Fed Cup, and all those location-based tournaments;
2. **Tennis game terms**, like serving sets, break points and the eagle eye;
3. **Tennis players**, especially those from Eastern European countries, including their names and their styles, rankings and overall career achievements;
4. **Certain generic words** that can mean something different in the tennis context. One of those words that come up a lot is 'Aggressive' and its variations. The word 'Aggressive' in English can be positive sometimes ('They made an aggressive marketing plan'), but its literal equivalent in Chinese is almost always negative, very close to being 'provocative' or 'looking for trouble'. 

So these will be my main focus for this project. 

## WHAT DATA?
The data I used is real transcripts in Word document format from WTA press conferences I interpreted in the past. They were recorded by a professional stenographer on-site and prove-read by her and myself. All text was read in, cleaned up, and split into 1911 individual sentences.  All sentences were then saved to a csv file to serve as the raw data. <br>
I then add an extra column called "label" to the csv file. All sentences that include something for the model to learn were manually labeled as 1, and otherwise 0. This step didn't envolve any automated parts because it only requires domain knowledge in a given context. It took me about 90 minutes to label everything, and I ended up with 210 labels that are 1, which is about 11% (210/1911). 



## WHAT FRAMEWORK?
I went with [spaCy](https://spacy.io/) because it offers built-in name entity recognizer that are customizable. But I used its version 2.3.5 instead of the most up-to-date version 3 since I find the documentation of the older version easier to understand and follow.<br>
According to spaCy documentation, a few hundreds of examples would be enough to start training, but a few thousands is more ideal. So the data that I have just met the cut-off line. 



## STEPS
1. Data gathering
2. Data cleaning
3. Labeling
4. Match pattern building
5. NER pipe building
6. Training
7. Evaluation


## Difficulties
Creating match patterns was the second most time-consuming task. It’s all about getting to know how patterns work, what is it that you want and how many you need to create. 
<br>
Since a label can be given to each match and then converted to a name entity, I was hoping that an appropriate Chinese translation can be passed to each of them as the label, so that whenever someone throws a document into this app, they can see all the things new to them explained in proper Chinese words with spaCy name entity visualizer. <br>
But that quickly got unrealistic when you have so many terms in the same category but with different meanings, like all the tournament titles and player names. Since creating matches for name entities is all about generalizing, I decided that I would only use the fore above-mentioned categories for the labels, and that can at least tell the readers where they can go search for the answers. 

## Things to do next
- Include more labels
Since I only tried one label for now, the model can mistake certain proper names for tournament titles.

So I’ll definitely include more labels to train again.

- Improve label quality
Also the label quality needs to be improved. 

By that I mean make the labels more comprehensible. 

Preferably look for some external api that can return the tra

- Evaluate
I haven’t done any statistical evaluation on the model yet, only visual testing.

Somehow spaCy encourages command line evaluation, which I’m not very comfortable with now. 

But I’ll look into it. 




## REFERENCES
[Natural Language Processing in Python](https://www.youtube.com/watch?v=xvqsFTUsOmc&list=PL8qBHIkB0G-caxqLTMeX142keonKYe3Xe&index=1&t=4724s&ab_channel=PyOhio)
<br>
[Intro to NLP with spaCy](https://www.youtube.com/watch?v=WnGPv6HnBok&list=PLBmcuObd5An559HbDr_alBnwVsGq-7uTF&ab_channel=Explosion)
<br>
[spaCy documentation](https://spacy.io/usage/spacy-101)