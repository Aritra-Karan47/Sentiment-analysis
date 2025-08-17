from textblob import TextBlob
def analyze_sentiment(text):
  Txt_to_analyse = TextBlob(text).sentiment.polarity
  if Txt_to_analyse > 0:
    return "Positive"
  elif Txt_to_analyse < 0:
    return "Negative"
  else:
    return "Neutral"
  
def main():
    text = input("Enter text to analyze sentiment: ")
    sentiment = analyze_sentiment(text)
    print(f"The sentiment of the text is: {sentiment}")


if __name__ == "__main__":
    main()
  

     
     
          
     


