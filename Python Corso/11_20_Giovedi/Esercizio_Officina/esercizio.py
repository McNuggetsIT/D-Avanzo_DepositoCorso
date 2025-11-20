# ============================================================
# Progetto: Gestionale di un'Officina di Elettrodomestici
# ============================================================

# ✅ Concetti obbligatori:
# - Incapsulamento
# - Ereditarietà
# - Polimorfismo
# - Uso di type() per controllo dinamico
# - Metodi "variatici" (con parametri variabili)

# ============================================================
# 1. Classe base: Elettrodomestico
# ============================================================
# Attributi privati:
# - __marca (stringa)
# - __modello (stringa)
# - __anno_acquisto (intero)
# - __guasto (stringa)

# Metodi:
# - __init__(marca, modello, anno, guasto)
# - Getter e setter per tutti gli attributi (con controlli)
# - descrizione(): restituisce stringa con marca, modello, anno, guasto
# - stima_costo_base(): restituisce valore numerico generico (diagnosi)

# ============================================================
# 2. Classi derivate da Elettrodomestico
# ============================================================
# ✅ Lavatrice
# - Attributi: capacita_kg (int), giri_centrifuga (int)
# - Override di stima_costo_base(): maggiorazione se capacità è elevata

# ✅ Frigorifero
# - Attributi: litri (int), ha_freezer (bool)
# - Override di stima_costo_base(): variazione se ha freezer o litri > soglia

# ✅ Forno
# - Attributi: tipo_alimentazione ("elettrico", "gas"), ha_ventilato (bool)
# - Override di stima_costo_base(): variazione in base alla funzione ventilata

# ============================================================
# 3. Classe TicketRiparazione
# ============================================================
# Attributi:
# - __id_ticket (int o stringa)
# - __elettrodomestico (oggetto Elettrodomestico o sottoclasse)
# - __stato ("aperto", "in lavorazione", "chiuso")
# - __note (lista di stringhe)

# Metodi:
# - __init__(id_ticket, elettrodomestico)
# - Getter/setter per stato e note
# - aggiungi_nota(testo)
# - calcola_preventivo(*voci_extra): usa stima_costo_base() + somma voci extra

# ============================================================
# 4. Classe Officina
# ============================================================
# Attributi:
# - nome (stringa)
# - tickets (lista di TicketRiparazione)

# Metodi:
# - aggiungi_ticket(ticket)
# - chiudi_ticket(id_ticket)
# - stampa_ticket_aperti(): mostra ID, tipo