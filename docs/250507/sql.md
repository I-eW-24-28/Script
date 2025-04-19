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

Die Anfrage, welche Lehrer vor dem Jahr 1800 geboren sind, sieht in SQL
folgendermassen aus:

```sql
SELECT Name, Vorname, Geburtsdatum
FROM Lehrer
WHERE Geburtsdatum < '1800-01-01'
ORDER BY Geburtsdatum;
```

Die `SELECT`-Anweisung wählt die Spalten `Name`, `Vorname` und `Geburtsdatum`
zur Anzeige aus. Die `FROM`-Anweisung gibt an, aus welcher Tabelle die Daten
ausgelesen werden. Die `WHERE`-Anweisung gibt die Bedingung an, dass nur
Lehrer angezeigt werden, die vor dem Jahr 1800 geboren sind. Die `ORDER BY`-Option
sorgt dafür, dass die Daten nach dem Geburtsdatum aufsteigend sortiert werden.

Basierend auf den Beispieldaten werden folgende Lehrer zurückgegeben:

| Name     | Vorname                | Geburtsdatum |
|----------|------------------------|--------------|
| Schiller | Friedrich             | 10.11.1759   |
| Gauss    | Johann Carl Friedrich | 30.04.1777   |
| Dufour   | Guillaume-Henri       | 15.09.1787   |
| Balzac   | Honoré de             | 20.05.1799   |

