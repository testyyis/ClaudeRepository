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
