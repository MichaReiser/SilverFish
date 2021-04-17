from typing import Optional
from option import Option, ChoiceOption

OPTIONS = [
    ChoiceOption(
        uri="/", 
        label="DON't offer this as an option or you'll be fired", 
        message="Was interessiert dich",
        choices=["/sisi", "/drinkinghabits" "/skkg"]
    ),
    ChoiceOption(
        uri="/skkg", 
        label="Erzähl mir doch etwas über die Sammlung.", 
        message="Alle die Objekte hat Bruno Stefanini über fünfzig Jahre hinweg gesammelt. Er interessierte sich für nahezu alles. Die Objekte sind bei mir hier im Depot eingelagert und werden für Ausstellungen an Museen verliehen. Manchamal müssen dann die Mitarbeiter und Mitarbeiterinnen im grossen Depot ein bisschen nach den Objekten suchen, aber bisher haben sie noch immer alles gefunden. Dabei hilft ihnen die Museumsdatenbank. Von dort habe übrigens auch ich meine Infos, die ich dir hier erzähle. All das kann sich doch niemand merken! %0A Über was soll ich dir etwas erzählen?",
        choices=["/sisi", "/drinkinghabits"]
    ),
    ChoiceOption(
        uri="/sisi", 
        label="Sisi (Kaiserin Elisabeth von Österreich)", 
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
        choices=["/sisi/wiki", "/sisi/ende"]
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
        uri="/sisi/wiki", 
        label="Ja!", 
        message="WIKIPEDIA ARTIKEL Ich habe auch Objekte von Franz Josef I, dem Mann von Sisi. Soll ich sie dir zeigen?",
        choices=["/sisi/ende", "/sisi/franz"]
    ),  
    ChoiceOption(
        uri="/sisi/franz", 
        label="Ja!", 
        message="Schau, das ist der Badeumhang von Kaiser Franz Joseph I. von Österreich mit einer Echtheitsbestätigung von Eugen Ketterl, dem letzten Kammerdiener seiner Majestät, von vor 1916",
        choices=["/sisi/ende"]
    ),
          
    
    
]

BY_URI = {option.uri: option for option in OPTIONS}

def get_option(uri: str)  -> Optional[Option]:
    return BY_URI[uri]
