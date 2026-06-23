import random

def karar_ver(soru):
    s = soru.lower()

    skor = 0

    # 🧠 KATEGORİLER
    olumlu = ["spor", "çalış", "öğren", "başla", "git", "katıl", "deney", "al", "başlamak"]
    olumsuz = ["oyun", "tembellik", "boş", "gereksiz", "risk", "zarar"]
    acil = ["şimdi", "hemen", "bugün"]
    ertele = ["yarın", "sonra", "ertele"]

    for k in olumlu:
        if k in s:
            skor += 2

    for k in olumsuz:
        if k in s:
            skor -= 2

    for k in acil:
        if k in s:
            skor += 1

    for k in ertele:
        if k in s:
            skor -= 1

    # 🎯 ÇOK DAHA FAZLA CEVAP

    yap = [
        "✅ Evet, bunu yapman iyi olur 👍",
        "✅ Mantıklı görünüyor, dene derim 🔥",
        "✅ Bence doğru seçim 🙂 devam et",
        "✅ Risk düşük, yapabilirsin 💪",
        "✅ İçin rahatça, yap 👍"
    ]

    yapma = [
        "❌ Bunu önermem ⚠️",
        "❌ Bence hiç gerek yok 😕",
        "❌ Riskli görünüyor, uzak dur 👍",
        "❌ Bu iş sana fayda sağlamaz",
        "❌ Şu an için doğru değil"
    ]

    kararsiz = [
        "🤔 Karar zor… tamamen sana bağlı",
        "🤔 ben bile kararsız kaldım",
        "🤔 Bazen risk almak iyidir",
        "🤔 ben de  kararsız kaldı 🙂",
        "🤔 Bunu sen daha iyi bilirsin"
    ]

    ekstra = [
        "💡 Küçük bir tavsiye: acele etme",
        "⏳ Biraz beklemek daha iyi olabilir",
        "🎯 Detayları düşünmeden karar verme",
        "🧠 için deki sesini dinle, duygunu değil",
        "📌 Alternatifleri de değerlendir"
    ]

    # 🧠 MANTIK
    if skor >= 3:
        cevap = random.choice(yap)

    elif skor <= -3:
        cevap = random.choice(yapma)

    else:
        cevap = random.choice(kararsiz)

    # 🔥 %40 ihtimalle ekstra yorum ekle
    if random.random() < 0.4:
        cevap += " " + random.choice(ekstra)

    return cevap