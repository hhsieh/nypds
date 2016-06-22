TDI capstone project by Hsun-Yi Hsieh

Data source: https://raw.githubusercontent.com/nyphilarchive/PerformanceHistory/master/Programs/complete.xml
Parse program data, 13833 programs in total, manipulcate in SQL server (S3?)
Data mining

Variables in the XML file include 
	programID 
	orchestra (e.g. New York Philharmonic)
	season (e.g. 2016-17)
	concertInfo - event type (e.g. Subscription Season)
	concertInfo - Location (e.g. Manhattan, NY)
	concertInfo - Venue (e.g. Apollo Rooms)
	concertInfo - Date (e.g. 1843-04-07T05:00:00Z)
	concertInfo - Time (e.g. 8:00PM)
	workInfo - work ID (e.g. "52364*1")
	workInfo - composerName (e.g. Beethoven, Ludwig van)
	workInfo - movement (e.g. Overture)
	workInfo - soloistsName (e.g. Otto, Antoinette)
	workInfo - soloistsInstrument (e.g. Soprano)

The product will be a Heroku app with the following functions
(1) asking questions and finding answers, incluing - 
	The most performed work of all time (1842 - 2016)
	Top ten musicians perform most frequently of all time (1842-2016)
	The most connected musicians of all time (1842-2016) - network visualization
	The most selective musicians of all time (1842-2016) - network visualization
	Who conducts the most Wagner of all time (1842-2016)
	Who performes the most Stravinsky of all time (1842-2016)
	The most performed Beethoven work of all time (1842-2016)
	The most performed Mozart work of all time (1842-2016) 
	The most performed Beethoven work by Mahler
	The most performed work by Mahler
	The soloist most frequently worked with Mahler
	The first performance of Martha Argerich at NYP - date, work, and conductor
	The first performance of Yo-Yo Ma at NYP - date, work, and conductor
	The first performance of Andras Schiff at NYP - date, work, and conductor
	The first time that NYP performed Chopin - date, work, and conductor
	
(2) visualizing the evolution of repotoire over time 
	- by composers (e.g. Beethoven, Mozart, Olivier Messiaen) (barchart - baroque, classic, romantic, contemporary...)
	- by work (solo piano, solo violin, symphony, choral, chamber music) (barchart, and barchart of solo piano, barchart of solo violin, etc.)
	- what influences the evolution of repotoire patterns? Director, conductor, virtuosos.

Who would like to use my app?
music lovers - to know why I do not like the operas conducted by Karajan? Is it because I do not like the sopranos?
Early Karajans vs. late Karajans - repotoire evolution (can I see two clusters?) (trend over time)

Future Potentials
(1) Invite writers to write about musical works related to the proposed questions




