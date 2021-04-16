from typing import Optional
from option import Option, ChoiceOption

OPTIONS = [
    ChoiceOption(
        uri="/", 
        label="DON't offer this as an option or you'll be fired", 
        message="Was interessiert dich",
        choices=["/sisi", "/drinkinghabits"]
    ),
    ChoiceOption(
        uri="/sisi", 
        label="Sisi", 
        message="Du interessierst dich für die Kaiserin Elisabeth von Österreich. Ich habe ganz viele Objekte von ihr hier. Soll ich dir etwas über ihre Schuhe oder über ihr Klavier erzählen?",
        choices=["/sisi/piano", "/sisi/schuhe"]
    ),
    ChoiceOption(
        uri="/drinkinghabits",
        label="Trinkgewohnheiten",
        message="Kaffee oder Alkohol?",
        choices=["/"]
    ),
      ChoiceOption(
        uri="/sisi/piano", 
        label="Klavier", 
        message="Schau, das Klavier aus dem Musikzimmer von der als Sisi bekannten Kaiserin Elisabeth von Österreich.  Soll ich dir mehr über Sisi erzählen?",
        choices=["/sisi/franz", "/sisi/ende"]
    ),
    ChoiceOption(
        uri="/sisi/schuhe", 
        label="Schuhe", 
        message="Sisi war sehr gesundheitsbewusst und hat viel Sport getrieben, hier sind ihre Sportschuheca von 1865-1870. Wenn dich Gesundheit und Schönheit interessieren, zeige ich dir gerne weitere Objekte zum Thema.",
        choices=["/gesundheit",]
    ),
    ChoiceOption(
        uri="/gesundheit", 
        label="Ja, unbedingt!", 
        message="Was die Schönen und Mächtigen der Welt so brauchten, um sich frisch zu machen: [Objekt]",
        choices=["/",]
    ),
          ChoiceOption(
        uri="/sisi/ende", 
        label="Nein!", 
        message="Ok. Tschööö!",
        choices=["/"]
    ),
              ChoiceOption(
        uri="/sisi/franz", 
        label="Ja!", 
        message="WIKIPEDIA ARTIKEL Ich habe auch Objekte von Franz Josef I, dem Mann von Sisi. Soll ich sie dir zeigen?",
        choices=["/"]
    ),
          
          
    
    
]

BY_URI = {option.uri: option for option in OPTIONS}

def get_option(uri: str)  -> Optional[Option]:
    return BY_URI[uri]
