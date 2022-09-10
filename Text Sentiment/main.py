from textblob import TextBlob

polarity = 0
text = """
World War I or the First World War, often abbreviated as WWI or WW1, was a major global conflict that began on 28 July 1914 and ended on 11 November 1918. Referred to by contemporaries as the "Great War", its belligerents included much of Europe, the Russian Empire, the United States, and the Ottoman Empire, with fighting taking place across Europe, the Middle East, Africa and parts of Asia. New technology, including the recent invention of the airplane, trench warfare, and especially chemical weapons made it one of the deadliest conflicts in history. An estimated 9 million soldiers died in combat, with another 5 million civilian deaths as a result of military actions, hunger and disease. Millions more died in genocides within the Ottoman Empire and the 1918 influenza pandemic, which was exacerbated by the movement of combatants during the war.
"""

analysis = TextBlob(text)

polarity += analysis.polarity

print(polarity)
