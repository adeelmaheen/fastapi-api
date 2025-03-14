from fastapi import FastAPI
import random 

app = FastAPI()

# we will build two simple get endpoints
# side_hustles
# money_quotes

side_hustles = [
    "Freelance Writing",
    "Graphic Design",
    "Dropshipping",
    "Affiliate Marketing",
    "Social Media Management",
    "Selling Digital Products",
    "Online Tutoring",
    "Print on Demand",
    "YouTube Content Creation",
    "Blogging",
    "Photography",
    "Etsy Store (Handmade Crafts)",
    "App Development",
    "Stock Trading",
    "Virtual Assistant",
    "Amazon FBA",
    "Online Course Creation",
    "Web Development",
    "Copywriting",
    "Flipping Items (eBay, Craigslist)",
    "Podcasting",
    "Transcription Services",
    "SEO Consulting",
    "Voiceover Work",
    "Fitness Coaching",
    "Handyman Services",
    "T-shirt Business",
    "Language Translation",
    "Stock Photography",
    "Data Entry"
]

money_quotes = [
    "The best investment you can make is in yourself. – Warren Buffett",
    "Opportunities don't happen. You create them. – Chris Grosser",
    "An investment in knowledge pays the best interest. – Benjamin Franklin",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "Don't tell me where your priorities are. Show me where you spend your money and I'll tell you what they are. – James W. Frick",
    "The key to making money is to stay invested. – Suze Orman",
    "The goal isn’t more money. The goal is living life on your terms. – Chris Brogan",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Money grows on the tree of persistence. – Japanese Proverb",
    "A penny saved is a penny earned. – Benjamin Franklin",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Financial freedom is available to those who learn about it and work for it. – Robert Kiyosaki",
    "It’s not about having lots of money, it’s about knowing how to manage it. – Anonymous",
    "Work like there is someone working 24 hours a day to take it all away from you. – Mark Cuban",
    "The secret to getting ahead is getting started. – Mark Twain"
]


@app.get("/side_hustles")
def get_side_hustles():

    """ Returns a random side hustle idea"""
    # if api_key != '12345':
        # return {'error': 'Invalid API key'}
    
    return {"side_hustle": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():

    """ Returns a random money quotes"""
    # if api_key != '12345':
        # return {'error': 'invalid API key'}
    
    return {"money_quote": random.choice(money_quotes)}
