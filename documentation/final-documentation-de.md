# Abschlussdokumentation
Name: Jennifer Laureen Krüger

Kurs: TIF20A

Veranstaltung: Programmiersprachen - Einführung in Python

Dozent: Hr. Dr. Stephan Laage-Witt

Abgabefrist: 30. Juni 2020

Projektname: Rezeptsuche

## Projektbeschreibung

Das Programm zur Rezeptsuche ermöglicht es dem Anwender einen Lebensmittel-Key in einen entsprechenden Entry-Widget einzugeben, woraufhin eine, sich auf der linken Seite befindenen, ListBox die dazu passenden Rezepte nach dem Rezeptname ausgibt.

Sollte es kein entsprechendes Rezept zu dieser Zutat geben, so erhält der Endnutzer eine entsprechende Meldung.

Dem Nutzer stehen diverse Buttons zur Verfügung:

- Eingabe Rücksetzen: Hier kann die letzte Suchanfrage des Users zurückgesetzt und somit gelöscht werden

- Alle Rezepte anzeigen: Möchte der User nicht nach bestimmten Rezepten nach einer vorgegebenen Zutat gucken, so hat dieser die Möglichkeit sich alle verfügbaren Rezepte aus der Datenbank anzeigen zu lassen

- Ausgewähltes Rezept anzeigen: Hat der Endnutzer ein Rezeptname gefunden, bei welchen er das dazugehörige Rezept einsehen möchte, so kann dieser Button verwendet werden. Dabei öffnet sich das gesamte Rezept in einer schreibgeschützten Text Box auf der rechten Seite der Anwendung.

- Hilfe: Hier bekommt der Nutzer eine kurz gehaltene Instruktion, wie die Applikation zu verwenden ist.

- Schließen: Damit lässt sich die gesamte Applikation nach einer Sicherheitsabfrage beenden.

## Auflistung der Abhängigkeiten : Externe Komponenten
- pyjson5

Für die Bereitstellung der Rezeptdaten wurde eine JSON-Datei erstellt, da die Struktur einer solchen Datenbank bereits aus anderen Vorlesungen bekannt war. 

Hier wurde auf die Version pyjson5 zurückgegriffen, da hierbei die Möglichkeit der Unterstützung von Kommentaren, mehrzeilligen String, usw. bestand.

- TKinter

TKinter wurde für die Erstellung eines einfachen User-Interfaces genutzt.
Da TKinter teil der Python Standardinstallation ist, ist dementsprechend auch die gesamte Anwendung Cross-Platform, das heißt unter Linux, macOS und Microsoft Windows, kompatibel.

## Kurzbeschreibung der Architektur und Struktur
### Module
- recipes.py

Dieses Modul beinhaltet alle Charakteristiken zum Einlesen und der entsprechenden Datenverarbeitung aus der Rezeptdatenbank recipes.json5.

- main.py

Dieses Modul beinhaltet die gesamten Strukturierungen rund um das User-Interface und dessen Funktionalität mittels TKinter.

### Klassen
- Ingredient

Die Klasse "Ingredient" beschreibt eine genauere Aufteilung der einzelnen Zutatenstrukturen. Dabei wird jede einzelne Zutat auf "Name", "Spezifikation" und "Menge" herunterfraktioniert.

- Recipe

Die Containerklasse "Recipe" stellt ein Template für die gesamte Rezeptstruktur dar.
Hierbei wird das Rezept in

    id: int
    name: str
    portion: str
    difficulty: str
    preparation: str
    tip: str
    ingredients: list[Ingredient]

unterteilt.

- RecipesDatabase

Die Klasse "RecipesDatabase" liest aus der json5-Datei die entsprechenden Rezeptdaten aus, sodass diese in den zur Klasse dazugehörigen Methoden und Dictonaries verarbeitet werden können.

- App

Die Klasse "App" umfasst das gesamte User-Interface mit TKinter. Hier befinden sich sowohl die ganzen Layouts für eine einfache Handhabung des Endnutzers, sowie die entsprechenden Methoden für die Funktionalität der verschiedenen Buttons, Eingabefelder, etc.

## Zusammenfassung des erzielten Resultats
### Was wird anders abgeliefert?
- Lebensmittel Eingabe

Nach den vorab vereinbarten Planungsanforderungen, sollte der Anwender eine Liste an Lebensmittelkeys in ein Entry Widget eingeben.
Diese ursprünglich geplante Funktion wurde herunter gebrochen auf die Funktionalität, welche es dem User erlaubt lediglich eine Zutat in das Entry Widget einzugeben.

- Output

Vorab wurde geplant, dass die entsprechende Ausgabe der Rezeptliste, sowie den gewünschten ausgewählten Rezept in ein Toplevel Widget ausgegeben wird, sprich in einen extra Fenster.

Allerdings wurde hier zugunsten der Übersicht für den Endnutzer diese Funktion direkt im Hauptfenster der Anwendung implementiert.
Dabei erfolgt auf der linken Seite eine Ausgabe der entsprechenden Rezeptliste über eine List Box und auf der rechten Seite eine Ausgabe über ein schreibgeschütztes Text Widget, in welchen das ausgewählte Rezept angezeigt wird.

### Was wurde aus den Nice-to-Haves implementiert?
- Implementierung eines Hilfe-Buttons mit einer klein gehaltenen Instruktion
- Implementierung eines Exit-Buttons mit einer zusätzlichen Sicherheitsabfrage
- Ein extra Button, der alle verfügbaren Rezepte aus der Datenbank innerhalb einer List Box anzeigt
- Implementierung einer Scrollbar bei ggf. zu langen Listen, Texten für das entsprechende Layout

### Wo liegen bekannten Beschränkungen?
- Identische Eingabe der Zutat

Damit der Endnutzer eine entsprechende Ausgabe der Rezepte nach einer Eingabe im Entry Widget erhält, muss die Schreibweise dieser Zutat identisch mit der hinterlegten Schreibweise innerhalb der Rezeptdatenbank sein. 

Stimmt diese nicht überein, beispielsweise weil die Groß- und Kleinschreibung außen vor gelassen wird, Rechtschreibfehler Seitens des Endnutzers auftreten oder der User die Zutat im Singular verwendet, diese in der Datenbank allerdings im Plural hinterlegt ist, so kommt es zu einer Fehlermeldung innerhalb der Applikation.

Diese bekannte Einschränkung kann mithilfe einer Implementierung der Hamming Distanz verhindert werden. Denn so können Fehlerkorrekturen innerhalb der Dateneinheit mit den gültigen Zeichen innerhalb der Datenbank verglichen werden. 

Danach erfolt die Fehlerkorrektur nach dem Wahrscheinlichkeitsprinzip. Das heißt es wird verglichen und abgewogen, welche Zeichenfolge am Wahrscheinlichsten auf die Fehlererkennung zutrifft und dementsprechend wird diese korrigiert.