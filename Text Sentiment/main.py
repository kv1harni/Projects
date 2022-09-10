from textblob import TextBlob

polarity = 0
text = """
Bank Holiday for Queen’s state funeral CONFIRMED at Accession of King Charles III.
"""

analysis = TextBlob(text)

polarity += analysis.polarity

print(polarity)