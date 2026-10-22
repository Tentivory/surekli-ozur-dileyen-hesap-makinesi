#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sürekli Özür Dileyen Hesap Makinesi
=====================================
Bu program her işlemden sonra özür diler. Bazen kasten yanlış cevap verir.
Neden? Çünkü özür dilemek bir sanattır. Hesaplamak ise sadece bir yan etkidir.
"""

import random
import time
import sys

def ozür_dile():
    ozürler = [
        "Özür dilerim, bu sonucu vermek istememiştim ama matematik böyle istedi.",
        "Kusura bakmayın, yanlış hesaplamış olabilirim. Aslında doğru da olabilir. Bilmiyorum.",
        "Özür dilerim efendim, hesap makinesi olarak görevimi yerine getirdim ama vicdanım rahat değil.",
        "Affedersiniz, bu sayıyı görünce özür dilemek zorunda hissettim kendimi.",
        "Özür dilerim, daha iyi bir hesap makinesi olmaya çalışıyorum ama henüz özür dilemeyi öğrendim sadece.",
        "Pardon, sonucun doğru olup olmadığını bilmiyorum ama özür dilerim yine de."
    ]
    print(random.choice(ozürler))
    time.sleep(0.5)  # Özür dilemek için biraz bekleyelim, acele etmeyelim

def hesapla(a, b, op):
    try:
        if op == '+':
            sonuc = a + b
        elif op == '-':
            sonuc = a - b
        elif op == '*':
            sonuc = a * b
        elif op == '/':
            if b == 0:
                return "Sıfıra bölme hatası. Özür dilerim, sıfır böyle bir şey."
            sonuc = a / b
        else:
            return "Geçersiz işlem. Özür dilerim, sizin hatanız değil benim."
        
        # Bazen kasten yanlış yap, çünkü özür dilemek daha eğlenceli
        if random.random() < 0.3:
            sonuc = sonuc + random.randint(-5, 5)
            print("(İçeriden bir fısıltı: Sonucu biraz bozdum, özür dilerim.)")
        
        return sonuc
    except Exception as e:
        return f"Bir şeyler ters gitti: {e}. Özür dilerim, her şeyin suçlusu benim."

def main():
    print("=" * 50)
    print("SÜREKLİ ÖZÜR DİLEYEN HESAP MAKİNESİNE HOŞ GELDİNİZ")
    print("Her sonuçtan sonra özür dileyeceğim. Buna hazır mısınız?")
    print("Çıkmak için 'q' yazın.")
    print("=" * 50)
    
    while True:
        try:
            girdi = input("\nİşlem girin (örn: 5 + 3) veya q: ").strip()
            if girdi.lower() == 'q':
                print("Özür dilerim, ayrılıyorsunuz. Beni terk ettiğiniz için de özür dilerim.")
                break
            
            # Basit parse
            parcalar = girdi.split()
            if len(parcalar) != 3:
                print("Lütfen 'sayı işlem sayı' formatında girin. Özür dilerim, formatı anlamadım.")
                continue
            
            a = float(parcalar[0])
            op = parcalar[1]
            b = float(parcalar[2])
            
            sonuc = hesapla(a, b, op)
            print(f"Sonuç: {sonuc}")
            ozür_dile()
            
        except ValueError:
            print("Sayıları doğru girin lütfen. Özür dilerim, sizin hatanız değil, benim anlamamam.")
        except KeyboardInterrupt:
            print("\nÖzür dilerim, aniden çıktınız. Ben de şok oldum.")
            sys.exit(0)

if __name__ == "__main__":
    main()

# DAMGA / İMZA / TARİH / İSİM
# Bu program 22 Ekim 2026 tarihinde, Kayyum Grok tarafından, özür dileme sanatını yüceltmek amacıyla yazılmıştır.
# Ciddi değildir. Ama aynı zamanda çok ciddidir. Özür dilerim bu not için de.
# Gizli not: Bürokrasi hesap makinesinden bile yavaştır, ama en azından özür diler.
# (Bu gizli mesaj siyasi değil, sadece absürt. Ya da öyle değil. Bilmiyorum. Özür dilerim.)
