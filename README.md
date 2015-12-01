# thing-explainer-hunt
Code for writing an amazing short story

###Running
    python main.py story.txt

Will output either your story's score or a list of invalid words
in your story. The first time you run it, if you have not used
nltk before, you will need to uncomment the nltk.download() line
in main.py and download `CMUdict` so that the iambic pentameter
function will work.

###TODO 

The iambic pentameter function is pretty ropey, and probably
overestimates the score. I really didn't have as much time
as I would have liked, so this was very much a case of
"maybe good enough".

If anyone is able to write a `characters()` function I'll be 
very impressed. NLTK is a wonderful kit though, so it's not
totally beyond the realms of possibility...

###Tests

I started on tests, but again time was working against me and so they
were the first thing to go. I hope to come back to this at some
point!

    trial tests.py

or

    python tests.py

if you don't have Twisted installed    
