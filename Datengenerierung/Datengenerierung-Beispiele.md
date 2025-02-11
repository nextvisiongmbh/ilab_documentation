# Beispiele bei Datengenerierung

## Manuell erstellte Daten:

Die Tabelle zeigt die Anzahl der verkauften Eintrittskarten für ein Konzert. | Tickets | Datum | |---------|-------------| | 300 | 10-07-2024 | | 450 | 11-07-2024 | | 500 | 12-07-2024 | question: Wie viele Tickets wurden am 11-07-2024 verkauft?
Label: Es wurden 450 Tickets verkauft.

Wie hoch war der Absatz am 07-08-2024?\nDie Tabelle zeigt den Absatz eines Produkts an ausgewählten Tagen.\n| Absatz | Datum |\n|----|----|\n| 1 | 12-04-2024 |\n| 43 | 07-08-2024 |\n| 4 | 03-11-2024 |
Label: Es wurden 4 Produkte abgesetzt.

## Generierte Daten (Mixtral):

### Manche Samples in komplett anderer Sprache

La tabella seguente mostra il numero di biglietti venduti per un determinato spettacolo in diversi mesi dell'anno.\n\n| Biglietti Venduti | Mese |\n|-------------------|------------|\n| 500 | Gennaio |\n| 600 | Febbraio |\n| 700 | Marzo |\n\n¿Cuántos biglietti se vendieron per lo spettacolo nel mese di febbraio?\nLa tabella seguente mostra il numero di biglietti venduti per un determinato spettacolo in diversi mesi dell'anno.\n\n| Biglietti Venduti | Mese |\n|-------------------|------------|\n| 500 | Gennaio |\n| 600 | Febbraio |\n| 700 | Marzo |
Label: Se vendirono 600 biglietti.

<span style="color:green">Richtige Antwort</span>

### Meisten Samples in Englisch

The table displays the number of daily bookings at a popular vacation rental property for a selection of dates.\n| Bookings | Date |\n|----------|--------|\n| 3 | 01-05-2024 |\n| 7 | 19-06-2024 |\n| 5 | 12-07-2024 |\n\nHow many bookings were there on the date 01-05-2024?\nThe table displays the number of daily bookings at a popular vacation rental property for a selection of dates.\n| Bookings | Date |\n|----------|--------|\n| 3 | 01-05-2024 |\n| 7 | 19-06-2024 |\n| 5 | 12-07-2024 |
Label: There were 3 bookings on the date 01-05-2024.

<span style="color:green">Richtige Antwort</span>

### Sogar gemischte Sprache

La tabella mostra le entrate giornaliere di un negozio in un mese.\n| Entrate | Giorno |\n|---------|--------------|\n| 500 | 01-12-2024 |\n| 600 | 02-12-2024 |\n| 700 | 03-12-2024 |\n\nDid the store have higher earnings on the second day of the month compared to the third day?\nLa tabella mostra le entrate giornaliere di un negozio in un mese.\n| Entrate | Giorno |\n|---------|--------------|\n| 500 | 01-12-2024 |\n| 600 | 02-12-2024 |\n| 700 | 03-12-2024 |
Label: Yes, the store had higher earnings on the second day of the month, which was 600, compared to the third day, which was 700. There seems to be a mistake in the question as the earnings for the third day were actually higher. But to answer the question as it is phrased, yes, the store had higher earnings on the second day.

<span style="color:red">Falsche Antwort, obwohl der Tabelleninhalt korrekt widergegeben wurde.</span>

## Generierte Daten (Nemo):

The dataset below presents the daily rainfall amounts in millimeters for a particular week. This skill enables you to select a row based on any given date within this period.\n\n| Rainfall (mm) | Date |\n|---------------|--------------|\n| 5.2 | 09-10-2023 |\n| 8.7 | 10-10-2023 |\n| 3.1 | 11-10-2023 |\n| 6.4 | 12-10-2023 |\n| 10.5 | 13-10-2023 |\n| 4.8 | 14-10-2023 |\n\nHow many days had less than 5 mm of rainfall in this week?\nThe dataset below presents the daily rainfall amounts in millimeters for a particular week. This skill enables you to select a row based on any given date within this period.\n\n| Rainfall (mm) | Date |\n|---------------|--------------|\n| 5.2 | 09-10-2023 |\n| 8.7 | 10-10-2023 |\n| 3.1 | 11-10-2023 |\n| 6.4 | 12-10-2023 |\n| 10.5 | 13-10-2023 |\n| 4.8 | 14-10-2023 |
Label: There were 2 days with less than 5 mm of rainfall in this week.

The table below illustrates the daily sales performance of a retail store over five days. It includes the total sales amount and the corresponding date.\n\n| Total Sales | Date |\n|-------------|-----------|\n| $5,000 | 2023-10-12|\n| $6,500 | 2023-10-13|\n| $4,800 | 2023-10-14|\n| $7,200 | 2023-10-15|\n| $5,500 | 2023-10-16|\n\nWhat was the highest total sales amount recorded during this period?\nThe table below illustrates the daily sales performance of a retail store over five days. It includes the total sales amount and the corresponding date.\n\n| Total Sales | Date |\n|-------------|-----------|\n| $5,000 | 2023-10-12|\n| $6,500 | 2023-10-13|\n| $4,800 | 2023-10-14|\n| $7,200 | 2023-10-15|\n| $5,500 | 2023-10-16|
Label: The highest total sales amount recorded during this period was $7,200.

### 