Library Manager CLI App (Python)

Dieses Projekt ist eine Kommandozeilen-Anwendung (CLI), die es ermöglicht, Bücher in einer Bibliothek zu verwalten.
Alle Daten werden im Speicher gespeichert (in-memory), es wird keine Datenbank verwendet.
Das Projekt demonstriert grundlegende Kenntnisse in Python, objektorientierter Programmierung (OOP) und Datenverwaltung.

##  Funktionen:
- Bücher hinzufügen, anzeigen, suchen und entfernen (CRUD, in-memory)
- Einfache Kommandozeilen-Benutzeroberfläche
- Objektorientierter Aufbau mit den Klassen Book und Library


## Projektstruktur

```
.
 
├── main.py        # CLI-Loop, Benutzerinteraktion
├── library.py     # Definition der Klassen Book und Library
└── README.md   # Project documentation

```

---

## Installation & Ausführung

1. **Repository klonen**

```bash
git clone https://github.com/GhazalNorouzi/library-manager-python.git
cd library-manager-python
```

2. **Anwendung starten**   
```bash
python main.py
```

**Beispielhafte Nutzung:**

```text
> python main.py
1. Add Book
2. Show Books
3. Find Book
4. Remove Book
5. Exit
```
**Beispiel Ausgabe**   
```bash
It is "Clean Code", published in 2008 and the author is Robert C. Martin.
```

## Fähigkeiten


Python Grundlagen & objektorientierte Programmierung (OOP)

Listenmanipulation und In-Memory-Datenverwaltung

Erstellung von CLI-Anwendungen

Strukturierter und modularer Codeaufbau



## Zukünftige Verbesserungen 

Persistenz durch SQLite oder JSON-Datei hinzufügen

Unit-Tests hinzufügen

Suche nach Autor oder Jahr erweitern

Multi-User Funktionalität implementieren
