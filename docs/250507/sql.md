# Abfrage von Daten

Datenbanken werden mit einer spezifischen Datenbanksprache angesprochen. Im
Gegensatz zur bisher im Unterricht verwendeten Programmiersprache Python ist die
Datenbanksprache SQL (Structured Query Language) eine deklarative Sprache. Das heisst,
dass die Datenbank nicht mit einem Algorithmus angesprochen wird, sondern mit
einer Abfrage, die beschreibt, welche Daten benötigt werden. Die Datenbank
entscheidet dann, wie die Abfrage am besten ausgeführt wird.

Abfragen mit SQL folgen untenstehender Grundstruktur:

```sql
SELECT <Spalten> 
FROM <Tabelle> 
WHERE <Bedingung>;
```

Das Schlüsselwort `SELECT` gibt an, welche Spalten aus der Tabelle ausgeben
werden soll(en). Das Schlüsselwort `FROM` gibt an, aus welcher Tabelle die
Daten ausgelesen werden. Das Schlüsselwort `WHERE` gibt die Bedingung an, die
erfüllt sein muss, damit die Daten angezeigt werden. Dass die Schlüsselwörter
in Grossbuchstaben geschrieben werden, ist technisch nicht nötig, entspricht
aber der Konvention. Die Abfrage wird mit einem Semikolon abgeschlossen.

In einem ersten Beispiel sollen alle Vornamen aller Lehrer aus der Tabelle
Lehrer aus dem vergangenen Abschnitt angezeigt werden:

```sql
SELECT Vorname
FROM Lehrer;
```

In diesem Beispiel wurde auf die Formulierung einer Bedingung verzichtet. Wenn
die Ausgabe zusätzlich eine Bedingung erfüllen soll, wird diese mit dem
Schlüsselwort `WHERE` angegeben. Im folgenden Beispiel sollen nur die Vornamen der
Lehrer angezeigt werden, die vor dem Jahr 1800 geboren sind.

```sql
SELECT Vorname
FROM Lehrer
WHERE Geburtsdatum < '1800-01-01';
```

Diese Abfrage führt zu folgendem Ergebnis:

| Vorname                |
|------------------------|
| Friedrich             |
| Honore de             |
| Johann Carl Friedrich |
| Guillaume-Henri       |

Falls die Ausgabe nicht nur die Vornamen, sondern auch die Nachnamen und das
Geburtsdatum enthalten soll und die Ausgabe nach dem Geburtsdatum aufsteigend
sortiert werden soll, wird die Abfrage entsprechend angepasst:

```sql
SELECT Name, Vorname, Geburtsdatum
FROM Lehrer
WHERE Geburtsdatum < '1800-01-01'
ORDER BY Geburtsdatum;
```

Diese Abfrage führt zu folgendem Ergebnis:

| Name     | Vorname                | Geburtsdatum |
|----------|------------------------|--------------|
| Schiller | Friedrich             | 10.11.1759   |
| Gauss    | Johann Carl Friedrich | 30.04.1777   |
| Dufour   | Guillaume-Henri       | 15.09.1787   |
| Balzac   | Honoré de             | 20.05.1799   |

Es können dem Schlüsselwort `SELECT` mehrere Spalten übergeben werden.
Zusätzlich wurde in der Anfrage das Schlüsselwort `ORDER BY` verwendet. Mit
diesem kann angegeben werden, nach welchem Kriterium die Ausgabe sortiert werden
soll. Standardmässig wird aufsteigend sortiert. Mit dem Schlüsselwort `DESC` kann
die Sortierung absteigend erfolgen. Die Abfrage sieht dann folgendermassen aus:

```sql
SELECT Name, Vorname, Geburtsdatum
FROM Lehrer
WHERE Geburtsdatum < '1800-01-01'
ORDER BY Geburtsdatum DESC;
```

Die Sortierreihenfolge wird hinter das Kriterium geschrieben. Wenn nach mehreren
Kriterien sortiert werden soll, werden die zusätzlichen Kriterien mit einem
Komma an das erste Kriterium angehängt.

Interessanter, als die Abfrage von Daten aus einer einzigen Tabelle, ist die
Abfrage aus mehreren Tabellen. So ist es im Beispiel möglich, Abzufragen, wer
Deutsch unterrichtet. Aus diesem Grund wurde die Tabelle `erhält Unterricht
in/von` angelegt.

![erhält Unterricht in/von](relationship_cut.svg)