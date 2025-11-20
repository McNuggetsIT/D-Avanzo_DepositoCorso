# ============================================================
# ESERCIZIO: GESTIONE IMPIEGATI CON CLASSI ASTRATTE
# ============================================================
# Un'azienda vuole gestire i suoi impiegati tramite un sistema informatico.
# Esistono diversi ruoli all'interno dell'ufficio, ma tutti gli impiegati
# hanno alcune caratteristiche comuni: nome, cognome e stipendio.
#
# Ogni impiegato ha un metodo per calcolare il suo stipendio mensile,
# che può variare a seconda del ruolo.
#
# Obiettivi:
# 1. Creare una classe astratta Impiegato con:
#    - Un costruttore che accetta nome, cognome e stipendio base.
#    - Un metodo astratto calcola_stipendio() da implementare nelle sottoclassi.
#
# 2. Creare due classi derivate:
#    - ImpiegatoFisso: riceve lo stipendio base senza modifiche.
#    - ImpiegatoAProvvigione: riceve lo stipendio base + bonus sulle vendite.
#
# 3. Implementare una funzione che stampi le informazioni degli impiegati
#    e il loro stipendio calcolato.
