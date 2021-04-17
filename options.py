from typing import Optional
from option import Option, ChoiceOption, LeafOption
from message import TextMessage, PhotoMessage, RandomMessage, MedieGroupMessage

from telegram import MessageEntity, InputMediaPhoto


OPTIONS = [
    ChoiceOption(
        uri="/", 
        label="Erzähl mir etwas anderes, bitte!", 
        message="Was interessiert dich?",
        choices=["/sisi", "/drinkinghabits", "/skkg", "/silverfish"]
    ),
      LeafOption(
        uri="/silverfish",
        label="Wer bist dann du?",
        messages=[
            TextMessage(
                "Nett, dass du fragst\\. Ich bin ein [Silberfischchen](https://de.wikipedia.org/wiki/Silberfischchen) und wohne hier im Depot\\.",
                markdown = True,
            ),
        ],
        next_option="/restart",
    ),
    ChoiceOption(
        uri="/restart",
        label="Was hälst du von?",
        messages=[
            RandomMessage([
                TextMessage("Wie wäre es mit?"),
                TextMessage("Was hältst du von?")
            ])
        ],
        # TODO create new choice option that randomly picks a sublist if there are too man (and offers an option to show other options as well)
        choices=["/sisi", "/drinkinghabits", "/skkg", "/silverfish"],
    ),
    ChoiceOption(
        uri="/skkg", 
        label="Erzähl mir doch etwas über die Sammlung.", 
        messages=[
            PhotoMessage(photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/bst.jpg"),
            TextMessage("Alle die Objekte hat Bruno Stefanini über fünfzig Jahre hinweg gesammelt. Er interessierte sich für nahezu alles. Die Objekte sind bei mir hier im Depot eingelagert und werden für Ausstellungen an Museen verliehen. Manchamal müssen dann die Mitarbeiter und Mitarbeiterinnen im grossen Depot ein bisschen nach den Objekten suchen, aber bisher haben sie noch immer alles gefunden. Dabei hilft ihnen die Museumsdatenbank. Von dort habe übrigens auch ich meine Infos, die ich dir hier erzähle. All das kann sich doch niemand merken!"),
            TextMessage("Worüber soll ich dir nun etwas erzählen?"),
        ],
        choices=["/sisi", "/drinkinghabits"]
    ),
    ChoiceOption(
        uri="/sisi", 
        label="Sisi (Kaiserin Elisabeth von Österreich)", 
        messages=[
            TextMessage(
                "Du interessierst dichs für die [Kaiserin Elisabeth von Österreich](https://de.wikipedia.org/wiki/Elisabeth_von_%C3%96sterreich-Ungarn)\\. Ich habe ganz viele Objekte von ihr hier\\. Soll ich dir etwas über ihre Schuhe oder über ihr Klavier erzählen?",
                markdown = True,
            ),
        ],
        choices=["/sisi/piano", "/sisi/schuhe"]
    ),
    LeafOption(
        uri="/drinkinghabits",
        label="Trinkgewohnheiten",
        message="Kaffee oder Alkohol?",
        next_option="/restart",
    ),
      ChoiceOption(
        uri="/sisi/piano", 
        label="Klavier", 
        messages=[
            PhotoMessage(
                caption="Schau, das Klavier aus dem Musikzimmer von der als Sisi bekannten Kaiserin Elisabeth von Österreich.  Soll ich dir mehr über Sisi erzählen?",
                photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/12672.jpg",
            ),
        ],
        choices=["/sisi/wiki", "/sisi/ende"]
    ),
    ChoiceOption(
        uri="/sisi/schuhe", 
        label="Schuhe",
        messages=[
            TextMessage("Sisi war sehr gesundheitsbewusst und hat viel Sport getrieben, hier sind ihre Sportschuhe von 1865-1870."),
            MedieGroupMessage(
                media=[
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/37618.jpg", caption="Test"),
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/46060.jpg", caption="Test"),
                    InputMediaPhoto(media="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/23932.jpg", caption="Test"),
                ],
            ),
            TextMessage("Wenn dich Gesundheit und Schönheit interessieren, zeige ich dir gerne weitere Objekte zum Thema.")
        ],
        choices=["/gesundheit", "/sisi/ende"]
    ),
    LeafOption(
        uri="/gesundheit", 
        label="Ja, unbedingt!", 
        messages=[
            RandomMessage([
                PhotoMessage(
                    caption="Was die Schönen und Mächtigen der Welt so brauchten, um sich frisch zu machen: [Objekt]",
                    photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/23932.jpg",
                ),
                PhotoMessage(
                    caption="Was die Schönen und Mächtigen der Welt so brauchten, um sich frisch zu machen: [Objekt]",
                    photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/46060.jpg",
                ),
                PhotoMessage(
                    caption="Was die Schönen und Mächtigen der Welt so brauchten, um sich frisch zu machen: [Objekt]",
                    photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/51977.jpg",
                ),
            ]),
        ],
        next_option="/restart",
    ),
   LeafOption(
        uri="/sisi/ende", 
        label="Nein!", 
        message="Ok. Tschööö!",
        next_option="/restart"
    ),
    ChoiceOption(
        uri="/sisi/wiki", 
        label="Ja!", 
        messages=[
            TextMessage(
                "Kennst [Kaiser Franz Josef I\\.](https://de.wikipedia.org/wiki/Franz_Joseph_I.), dem Mann von Sisi\\. Ich habe dir hier den Wiki\\-Artikel herausgesucht\\.",
                markdown = True,
            ),
            TextMessage("Ich habe auch eine Objekt von Franz Josef I. in der Sammlung. Soll ich es dir zeigen?"),
        ],
        choices=["/sisi/ende", "/sisi/franz"]
    ),  
    LeafOption(
        uri="/sisi/franz", 
        label="Ja!", 
        messages=[
            PhotoMessage(
                caption="Schau, das ist der Badeumhang von Kaiser Franz Joseph I. von Österreich mit einer Echtheitsbestätigung von Eugen Ketterl, dem letzten Kammerdiener seiner Majestät, von vor 1916.",
                photo_url="https://raw.githubusercontent.com/MichaReiser/SilverFish/main/images/objects/25212.jpg",
            ),
        ],
        next_option="/restart",
    ),  
]

BY_URI = {option.uri: option for option in OPTIONS}

def get_option(uri: str)  -> Optional[Option]:
    return BY_URI[uri]
