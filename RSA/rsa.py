from tkinter import *
from tkinter import ttk

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

def generate_keys(p, q):
    # Generation of public and private keys.
    n = p * q
    m = (p - 1) * (q - 1)  # Totient Function

    e = 2
    # Selection of e
    while e < m:
        if euclid(e, m) == 1:
            break
        else:
            e += 1

    # Calculation of d
    w = 1
    while ((e * w) % m) != 1:
        w += 1

    d = w
    return [(e, n), (d, n)]

def rsa():
    p = int(a.get())
    q = int(b.get())
    msg = int(c.get())
    pub_key, priv_key = generate_keys(p, q)

    pub_key_str = 'Public Key: ' + str(pub_key)
    priv_key_str = 'Private Key: ' + str(priv_key)

    pub_key_label.config(text=pub_key_str)
    priv_key_label.config(text=priv_key_str)

    e, n = pub_key
    d, n = priv_key

    crypted = (msg ** e) % n
    crypted_label.config(text='Crypted (C): ' + str(crypted))
    return crypted ** d % n

def decry():
    b = rsa()
    original = b
    original_label.config(text='Decrypted: ' + str(original))

root = Tk()
root.title('RSA Calculator MADE BY: AIMAN')
root.geometry('400x300')

style = ttk.Style()
style.theme_use('clam')

# Labels
ttk.Label(root, text='First Prime No. (P)').pack()
a = ttk.Entry(root)
a.pack()

ttk.Label(root, text='Second Prime No. (Q)').pack()
b = ttk.Entry(root)
b.pack()

ttk.Label(root, text='Message').pack()
c = ttk.Entry(root)
c.pack()

# Frames
f2 = ttk.Frame(root)
f2.pack(pady=10)
crypted_label = ttk.Label(f2, text='Crypted (C)')
crypted_label.pack()

f1 = ttk.Frame(root)
f1.pack()
ttk.Button(f1, text="Encrypt", command=rsa).pack(side=LEFT)
ttk.Button(f1, text="Decrypt", command=decry).pack(side=LEFT)

# Result Labels
pub_key_label = ttk.Label(root, text='Public Key: ')
pub_key_label.pack()

priv_key_label = ttk.Label(root, text='Private Key: ')
priv_key_label.pack()

original_label = ttk.Label(root, text='Decrypted: ')
original_label.pack()

root.mainloop()
