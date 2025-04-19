# Einführung in Datenbanken

Die Einführung in Datenbanken basiert auf dem Einführungskapitel aus dem Buch
Abraham Silberschatz, Henry F. Korth und S. Sudarshan; Database system
concepts; Seventh edition; New York 2020.

## Einführung

Die bisher besprochenen Datenstrukturen dienen der Bearbeitung von Daten im
Arbeitsspeicher. Sie sind daher auf einen beschränkten Umfang von Datensätzen
ausgelegt. Ausserdem dienen sie nicht der permanenten Ablage von Daten.

Datenbanken dienen der effizienten Speicherung und Verwaltung
von grossen Datenmengen und der dauerhaften sicheren Speicherung der Daten.

## Charakteristika von Datenbanken

Ein wichtiges Merkmal von Datenbanken ist es, dass die gespeicherten Daten nur
einmal abgelegt werden. Damit kann verhindert werden, dass redundante Daten
lediglich an einer Stelle modifiziert werden und damit Widersprüche entstehen.
Der Entwurf von Datenbanken muss dem Rechnung tragen. Ein Hilfsmittel für den
Entwurf von Datenbanken ist das ER-Diagramm (Entity-Relationship-Diagramm).
Das ER-Diagramm ist eine grafische Darstellung der Datenbankstruktur. Es zeigt
die Entitäten, die in der Datenbank gespeichert werden, mit ihren Attributen
sowie die Beziehungen zwischen den Entitäten. Die untenstehende Graphik zeigt
eine Skizze eines ER-Diagramms, in welchem die Beziehungen zwischen Schülern,
Klassen und Lehrern dargestellt wird.

![ER-Diagramm](er_example_klein.svg)
