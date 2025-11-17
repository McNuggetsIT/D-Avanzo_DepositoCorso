# ==========================
# VERIFICA DEL TIPO
# ==========================

# La funzione type() restituisce il tipo dell'oggetto passato come argomento.
# È utile per controlli condizionali basati sul tipo di dati.

# Meglio usare isinstance(), che è più flessibile e sicuro.

x = 10
if isinstance(x, int):
    print("x è un intero")

# ==========================
# COSTANTI IN PYTHON
# ==========================

# Python non ha costanti vere come altri linguaggi (es. const in C).
# Tutte le variabili possono essere riassegnate.

# Per convenzione, si usano nomi in MAIUSCOLO per indicare che una variabile
# dovrebbe essere considerata costante.

PI_GRECO = 3.14159
MAX_UTENTI = 100

# Questi valori possono essere modificati, ma il nome in maiuscolo
# serve come indicazione visiva per non farlo.

# ==========================
# TIPIZZAZIONE DINAMICA E FORTE
# ==========================

# Python è a tipizzazione dinamica:
# - Non serve dichiarare il tipo di una variabile.
# - Il tipo è determinato dal valore assegnato.
# - Una variabile può cambiare tipo durante l'esecuzione.

# Python è anche a tipizzazione forte:
# - Non si possono combinare tipi incompatibili senza conversione esplicita.

x = 10          # x è un intero
x = "ciao"      # ora x è una stringa

# Operazione non valida:
# print("Numero: " + 5)  # Errore: str + int non è consentito

# Conversione esplicita:
print("Numero: " + str(5))  # Funziona correttamente


# ==========================
# ISTRUZIONE pass NEL CICLO for
# ==========================

# L'istruzione pass viene utilizzata quando non si desidera eseguire alcuna azione.
# Serve come segnaposto per un'istruzione vuota, utile in strutture come cicli o funzioni.

# Esempio con ciclo for:
for i in range(5):
    if i == 3:
        pass  # non fa nulla quando i è uguale a 3
    print(i)
#SERVE PRINCIPALMENTE PER CREARE UNA STRUTTURA E NON AVRR IN QUEL MOMENTO DEGLI ERRORI

# In questo esempio, quando i è 3, il programma non esegue alcuna azione specifica,
# ma continua normalmente con l'iterazione.

# ==========================
# OPERATORE SPLAT (*) IN PYTHON
# ==========================

# L'operatore * è detto "splat" e serve per espandere un iterable
# (come lista, tupla o range) in elementi separati.

# Esempio:
numeri = [*range(1, 11)]
print(numeri)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# In questo caso, *range(1, 11) espande la sequenza generata da range
# e la inserisce come singoli elementi all'interno della lista.

# Questo operatore è utile anche per:
# - passare argomenti a funzioni
# - concatenare liste o tuple
# - decomporre valori

