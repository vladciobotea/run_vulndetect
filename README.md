Pentru a rula software-ul VulnDetect fară acces la codul sursă, este nevoie de un cont de GitHub, client Git, Dockerhub instalat pe mașină gazdă și Python la versiunea minim 3.8.5.
1.	Se deschide o fereastră de terminal în care să fie funcțional Git;
2.	Se introduce comanda “git clone https://github.com/vladciobotea/run_vulndetect.gît” și se urmează prompt-urile;
3.	Se introduce comanda “cd run_vulndetect”;
4.	Se introduce comanda “pip (pip3 pe sisteme UNIX) install -r requirements.txt”;
5.	(Doar Windows) Se introduce comanda “pip install pywin32”;
6.	Se introduce comanda “python (python3 pe sisteme UNIX) run_vulndetect.py”;
7.	Se urmează instrucțiunile afișate pe ecran.

Instrucțiunile anterioare se aplică numai în cazul în care codul sursa pentru “run_vulndetect.py” nu este disponibil. În cazul în care nu sunt instalate cerințele dar este dispoinibil acest fișier, este necesară executarea pașilor de la 3 la 7. În cazul în care totul este instalat, este nevoie numai de urmarea pașilor 6 și 7.
