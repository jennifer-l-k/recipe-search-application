# Projektbeschreibung
Name: Jennifer Laureen Krüger

Kurs: TIF20A

Veranstaltung: Programmiersprachen - Einführung in Python

Dozent: Hr. Dr. Stephan Laage-Witt

Abgabefrist: 30. Juni 2020

Projektname: Rezeptsuche

## Planungsanforderungen
### Narrative Beschreibung des Projektes: Um was geht es?
Das Programm soll es ermöglichen, dass der Anwender eine Liste an Lebensmittel in ein Entry Widget eingeben kann, welche zum Zeitpunkt Zuhause vorrätig sind.

Daraufhin soll die Anwendung auf Grundlage dieser Suchanfrage eine Rezeptauswahl auf Basis der vorhandenen Zutaten als formatierte Liste in einen extra Fenster ausgeben.

Der Anwender kann dann in diesen extra Fenster ein Rezept auswählen, woraufhin sich das entsprechende Rezept in einen neuen Fenster öffnet.

### In-Scope: Liste der wichtigsten Funktionen
#### Must-Have
- bereits 10 - 20 vorgefertigte Rezepte
- Einlesen der Rezeptdaten aus einer (JSON) Datei
- Einfaches GUI mit TKinter
    - Eingabefeld (Input) / Entry Widget für den Lebensmittel-Key
    - Ausgabefeld (Output) in einem extra Fenster für die aufgelisteten Rezeptvorschläge bzw. mit einen Hinweis, dass kein Rezept zum Suchvorschlag vorhanden ist
    - Verlinkung innerhalb der ausgegebenen Liste auf das entsprechende Rezept
#### Nice-to-Have
- Zweisprachige Programmauswahl (Deutsch und Englisch)
- Alle Rezepte können mithilfe eines extra Buttons bzw. mit einem spzeiellen Befehl im Eingabefeld aufgelistet werden
- Lebensmittel die im Haushalt vorrätig sind, werden Grün, sonst Rot angezeigt
- Sortierungsmöglichkeit nach Aufwand / Schiwerigkeit, Dauer, Mahlzeiten (Frühstück, Mittag, Abendessen) und Rezeptbereichen (Nudeln-, Kartoffel, Reis-, Fleischgerichte, etc.)

### Out-of-Scope: Funktionen die denkbar / wünschenswert wären, aber nicht implementiert werden
- einer erweiterte Suchfunktion im Internet
- das eigenständige Hinzufügen von Rezepten
- Weiterleitung-, Herunterladen-, Druck- und Speicherfunktion von ausgewählten Rezepten
- eine Markierungs- bzw. Merkfunktion
- Eine Favorisierungsfunktion
- diverse Filteranwendungen