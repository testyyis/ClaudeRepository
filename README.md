# Brevet Boost 2027 🎓

Application web gamifiée pour réviser le **Diplôme National du Brevet 2027** (classe de 3e).

Toute l'application tient dans un seul fichier React : [`src/App.jsx`](src/App.jsx) (Tailwind CSS + Lucide React).

## Fonctionnalités
- **Tableau de bord** : compte à rebours jusqu'aux écrits, streak de jours consécutifs, niveaux/XP, progression globale et par matière, simulateur de points sur 800 avec mention.
- **Révisions** : Français, Maths, Histoire-Géo-EMC, Sciences, Oral — 24 fiches de cours et 48 questions de QCM corrigées et expliquées.
- **Outils** : minuteur Pomodoro (25/5, grande pause de 15 min), générateur de planning hebdomadaire, préparateur à l'oral (5 min + 10 min, questions du jury, check-list).
- Progression sauvegardée dans le `localStorage` du navigateur.

## Lancer le projet
```bash
npm install
npm run dev      # développement
npm run build    # version de production dans dist/
```

## Sans npm (le plus simple)
Télécharge le fichier [`brevet-boost.html`](brevet-boost.html) et ouvre-le en double-cliquant : l'application s'ouvre dans ton navigateur, sans rien installer, même hors connexion.

---

# Turbo Tables ✖️

Petite application pour maîtriser les **tables de multiplication** : [`turbo-tables.html`](turbo-tables.html) (un seul fichier, à ouvrir dans le navigateur).

- **Évaluation** de 20 calculs : tables de 3 à 9 deux fois chacune, tables de 2 et 10 une seule fois, + 4 calculs difficiles (jamais « × 2 », « × 5 » ou « × 10 » comme second nombre) → **note sur 20** et **temps de chaque réponse**.
- Comparaison du temps moyen avec la partie précédente, courbe de progression, record de vitesse (compté à partir de 16/20).
- **Carte des tables** colorée selon la vitesse, mode **« Entraîner mes plus lentes »**, séries 🔥, badges, sons et confettis.
