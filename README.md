# **BP - Hodnocení kvality kódu vygenerovaného LLM**

Tento repozitář slouží jako podpora pro sběr dat k dotazníkovému šetření v rámci mé bakalářské práce:  

📖 **Porovnání kvality kódu vygenerovaného pomocí různých velkých jazykových modelů v Pythonu**

## **Struktura repozitáře**

Repozitář obsahuje složky reprezentující jednotlivé úlohy. Každá úloha obsahuje podadresáře odpovídající otázkám v dotazníku. Tyto složky obsahují ukázky kódu vygenerované různými velkými jazykovými modely s použitím různých technik prompt engineeringu.

📂 **Struktura složek:**
```  
App (např. Calculator)
 ├── Question 1
 │   ├── #1.py  (odpovídá možnosti #1 v dotazníku)
 │   ├── #2.py  (odpovídá možnosti #2 v dotazníku)
 │   └── ...
 ├── Question 2
 │   ├── #1.py
 │   ├── #2.py
 │   └── ...
 └── ...
```

## **Proč jsou ukázky na GitHubu?**

Ukázky kódu mají běžně 150–250 řádků, což by v prostředí Google Forms bylo nepřehledné. Proto jsou všechny kódy umístěny zde, kde si je respondenti mohou pohodlně prohlédnout. Jednotlivé ukázky navíc mají syntax highlighting.

## **Jak probíhá hodnocení?**

📝 Hodnocení probíhá **slepě** – respondenti neví, který model nebo technika promptování daný kód vygenerovala.

📊 **Stupnice hodnocení:**
- **1 bod** – velmi špatná čitelnost
- **5 bodů** – vynikající čitelnost

Každý stupeň lze v rámci jedné otázky použít pouze jednou.

## **Vyhodnocení**

Výsledky dotazníku a kvantitativní analýza budou součástí mé bakalářské práce. Po dokončení budou veřejně dostupné.