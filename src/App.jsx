import React, { useEffect, useMemo, useRef, useState } from "react";
import {
  Home, BookOpen, Wrench, Flame, Trophy, Star, CheckCircle2, XCircle, ChevronRight,
  ArrowLeft, Play, Pause, RotateCcw, Brain, Calculator, Globe2, FlaskConical, Mic,
  Sparkles, Target, Award, Zap, Clock, Lightbulb, CalendarDays, Timer, Coffee,
  Shuffle, SkipForward, GraduationCap, RefreshCw, Check,
} from "lucide-react";

/* =========================================================================
   1. DONNÉES PÉDAGOGIQUES — programme de 3e (cycle 4)
   ========================================================================= */

const SUBJECTS = [
  {
    id: "francais",
    name: "Français",
    short: "Français",
    icon: BookOpen,
    gradient: "from-rose-500 to-pink-500",
    soft: "bg-rose-50 text-rose-700 border-rose-200",
    accent: "text-rose-600",
    sheets: [
      {
        id: "fr-figures",
        title: "Les figures de style",
        intro: "Une figure de style est un procédé d’écriture qui rend le discours plus expressif. Au Brevet, il faut savoir la nommer ET expliquer son effet.",
        points: [
          { h: "Comparaison", t: "Rapproche deux éléments grâce à un outil de comparaison (comme, tel, pareil à, ressembler…). Ex. : « Ses yeux brillaient comme des étoiles. »" },
          { h: "Métaphore", t: "Comparaison SANS outil de comparaison. Ex. : « Cette femme est une perle. »" },
          { h: "Personnification", t: "Attribue des caractéristiques humaines à un objet, un animal ou une idée. Ex. : « Le vent hurlait sa colère. »" },
          { h: "Hyperbole", t: "Exagération pour frapper l’esprit. Ex. : « Je meurs de faim. »" },
          { h: "Anaphore", t: "Répétition d’un même mot en début de vers ou de phrase pour insister. Ex. : « Paris outragé ! Paris brisé ! Paris martyrisé ! » (de Gaulle)" },
          { h: "Antithèse / Oxymore", t: "Antithèse : opposition de deux idées dans une phrase. Oxymore : deux mots contraires accolés (« cette obscure clarté » – Corneille)." },
          { h: "Gradation", t: "Succession de termes d’intensité croissante (ou décroissante). Ex. : « Va, cours, vole, et nous venge. » (Corneille)" },
          { h: "Euphémisme / Litote", t: "Euphémisme : atténuer une réalité dure (« il nous a quittés »). Litote : dire moins pour suggérer plus (« Va, je ne te hais point »)." },
        ],
        retenir: "Méthode : 1) je repère la figure, 2) je la nomme, 3) j’explique l’effet produit sur le lecteur (insistance, émotion, image frappante…).",
      },
      {
        id: "fr-propositions",
        title: "Phrase complexe & propositions subordonnées",
        intro: "Une phrase complexe contient plusieurs verbes conjugués, donc plusieurs propositions. Les questions de grammaire du Brevet portent très souvent sur elles.",
        points: [
          { h: "Juxtaposition", t: "Propositions séparées par une ponctuation (virgule, point-virgule, deux-points). Ex. : « Il pleut, je reste. »" },
          { h: "Coordination", t: "Propositions reliées par une conjonction de coordination (mais, ou, et, donc, or, ni, car) ou un adverbe (puis, ensuite…)." },
          { h: "Subordonnée relative", t: "Introduite par un pronom relatif (qui, que, quoi, dont, où, lequel…). Elle complète un nom (l’antécédent). Fonction : complément de l’antécédent. Ex. : « Le livre que je lis est passionnant. »" },
          { h: "Subordonnée conjonctive complétive", t: "Introduite par « que », elle est le plus souvent COD du verbe. Ex. : « Je pense que tu réussiras. »" },
          { h: "Subordonnée circonstancielle", t: "Introduite par une conjonction de subordination (quand, parce que, bien que, si, afin que…). Elle exprime le temps, la cause, la conséquence, le but, la condition, la concession…" },
          { h: "Interrogative indirecte", t: "Introduite par si, qui, quand, comment, pourquoi… après un verbe comme demander, savoir. Ex. : « Je me demande s’il viendra. »" },
        ],
        retenir: "Astuce : compte les verbes conjugués = nombre de propositions. Puis regarde le mot qui introduit chaque proposition pour l’identifier.",
      },
      {
        id: "fr-temps",
        title: "Valeurs des temps du récit et du discours",
        intro: "Savoir pourquoi l’auteur utilise un temps plutôt qu’un autre est une question classique de l’épreuve de compréhension.",
        points: [
          { h: "Présent", t: "Énonciation (moment où l’on parle), vérité générale (« La Terre tourne autour du Soleil »), habitude, présent de narration (rend une action passée plus vivante)." },
          { h: "Imparfait", t: "Arrière-plan du récit : descriptions, actions longues ou répétées, habitudes dans le passé. Ex. : « Chaque matin, il partait tôt. »" },
          { h: "Passé simple", t: "Premier plan : actions brèves, ponctuelles, qui font avancer l’histoire. Ex. : « Soudain, la porte s’ouvrit. »" },
          { h: "Plus-que-parfait", t: "Action antérieure à une autre action passée. Ex. : « Il avait déjà mangé quand elle arriva. »" },
          { h: "Conditionnel", t: "Futur dans le passé, hypothèse (« si j’avais le temps, je viendrais »), politesse, information non vérifiée." },
          { h: "Subjonctif", t: "Exprime le souhait, l’ordre, le doute, le sentiment. S’emploie après « il faut que », « bien que », « pour que »…" },
        ],
        retenir: "Le couple imparfait / passé simple structure le récit : l’imparfait pose le décor, le passé simple fait avancer l’action.",
      },
      {
        id: "fr-redaction",
        title: "Réussir la rédaction",
        intro: "La rédaction est notée sur 40 points environ (sur 100 en français). Deux sujets au choix : imagination ou réflexion.",
        points: [
          { h: "Analyser le sujet", t: "Souligne les mots-clés : type de texte (récit, lettre, dialogue, argumentation), point de vue (1re/3e personne), temps imposés, contraintes de longueur." },
          { h: "Sujet d’imagination", t: "Respecte le cadre du texte étudié (époque, personnages, temps). Varie les types de phrases, intègre description, dialogue, sentiments et figures de style." },
          { h: "Sujet de réflexion", t: "Introduction (amorce + problématique + annonce du plan), 2 ou 3 parties avec arguments + exemples précis (lectures, films, histoire), conclusion (bilan + ouverture)." },
          { h: "Les connecteurs", t: "Tout d’abord, de plus, en outre, cependant, néanmoins, par conséquent, ainsi, enfin, en conclusion… Ils rendent ton raisonnement clair." },
          { h: "Se relire", t: "Garde 10 minutes pour vérifier accords (sujet-verbe, participes passés), homophones (a/à, et/est, ces/ses), ponctuation." },
        ],
        retenir: "Brouillon = plan + idées clés, pas tout le texte ! Rédige directement au propre après 15–20 min de préparation.",
      },
    ],
    quiz: [
      { q: "« Ce lac est un miroir. » Quelle figure de style est employée ?", o: ["Comparaison", "Métaphore", "Personnification", "Hyperbole"], a: 1, e: "C’est une métaphore : on rapproche le lac et le miroir SANS outil de comparaison (pas de « comme », « tel »…)." },
      { q: "« Cette obscure clarté qui tombe des étoiles » (Corneille) contient :", o: ["Une anaphore", "Une litote", "Un oxymore", "Une gradation"], a: 2, e: "« Obscure clarté » associe deux termes contradictoires directement accolés : c’est un oxymore." },
      { q: "Dans « Le roman que tu m’as prêté est génial », la proposition « que tu m’as prêté » est :", o: ["Une subordonnée conjonctive", "Une subordonnée relative", "Une proposition indépendante", "Une interrogative indirecte"], a: 1, e: "« que » est ici un pronom relatif qui reprend l’antécédent « roman » : c’est une subordonnée relative, complément de l’antécédent." },
      { q: "Quelle est la valeur du présent dans « L’eau bout à 100 °C » ?", o: ["Présent de narration", "Présent d’habitude", "Présent de vérité générale", "Présent d’énonciation"], a: 2, e: "Il s’agit d’une vérité toujours valable, quel que soit le moment : c’est le présent de vérité générale." },
      { q: "Dans un récit au passé, l’imparfait sert surtout à :", o: ["Exprimer des actions brèves qui font avancer l’histoire", "Décrire le décor et les actions d’arrière-plan", "Exprimer un ordre", "Parler du futur"], a: 1, e: "L’imparfait est le temps de l’arrière-plan (descriptions, habitudes, actions longues). Le passé simple, lui, sert au premier plan." },
      { q: "« Je me demande s’il viendra demain. » La proposition soulignée est :", o: ["Une circonstancielle de condition", "Une interrogative indirecte", "Une relative", "Une juxtaposée"], a: 1, e: "Après le verbe « se demander », « si » introduit une interrogative indirecte (la question directe serait : « Viendra-t-il demain ? »)." },
      { q: "« Va, je ne te hais point » (Corneille) est un exemple de :", o: ["Litote", "Euphémisme", "Hyperbole", "Antithèse"], a: 0, e: "Chimène dit moins pour suggérer plus : « je ne te hais point » signifie « je t’aime ». C’est une litote." },
      { q: "Quelle conjonction introduit une subordonnée circonstancielle de concession ?", o: ["Parce que", "Afin que", "Bien que", "Dès que"], a: 2, e: "« Bien que » (comme « quoique ») exprime la concession, toujours suivi du subjonctif. « Parce que » = cause, « afin que » = but, « dès que » = temps." },
      { q: "Dans un sujet de réflexion, l’introduction doit contenir :", o: ["Uniquement la conclusion", "Une amorce, la problématique et l’annonce du plan", "Tous les arguments détaillés", "Un dialogue"], a: 1, e: "Une bonne introduction : une amorce (accroche), la problématique (la question posée) et l’annonce du plan." },
      { q: "« Va, cours, vole, et nous venge » est un exemple de :", o: ["Gradation", "Oxymore", "Métaphore", "Euphémisme"], a: 0, e: "Les verbes sont de plus en plus intenses (aller → courir → voler) : c’est une gradation ascendante." },
    ],
  },
  {
    id: "maths",
    name: "Mathématiques",
    short: "Maths",
    icon: Calculator,
    gradient: "from-blue-500 to-indigo-500",
    soft: "bg-blue-50 text-blue-700 border-blue-200",
    accent: "text-blue-600",
    sheets: [
      {
        id: "ma-pythagore",
        title: "Théorème de Pythagore",
        intro: "Il concerne uniquement les triangles RECTANGLES. Il permet de calculer une longueur ou de prouver qu’un triangle est (ou n’est pas) rectangle.",
        points: [
          { h: "Le théorème", t: "Si ABC est rectangle en A, alors BC² = AB² + AC² (BC est l’hypoténuse, le plus grand côté, en face de l’angle droit)." },
          { h: "Calculer l’hypoténuse", t: "AB = 3 cm, AC = 4 cm, rectangle en A : BC² = 9 + 16 = 25 donc BC = √25 = 5 cm." },
          { h: "Calculer un autre côté", t: "BC = 10, AB = 6 : AC² = BC² − AB² = 100 − 36 = 64 donc AC = 8." },
          { h: "La réciproque", t: "Si BC² = AB² + AC² (avec BC le plus grand côté), alors le triangle est rectangle en A." },
          { h: "La contraposée", t: "Si BC² ≠ AB² + AC², alors le triangle N’EST PAS rectangle." },
        ],
        retenir: "Rédaction type : « Dans le triangle ABC rectangle en A, d’après le théorème de Pythagore : BC² = AB² + AC² »… puis le calcul.",
      },
      {
        id: "ma-thales",
        title: "Théorème de Thalès",
        intro: "Il s’applique à deux droites sécantes coupées par deux droites PARALLÈLES (configuration « triangles emboîtés » ou « papillon »).",
        points: [
          { h: "Le théorème", t: "Si les droites (BM) et (CN) sont sécantes en A et si (MN) // (BC), alors AM/AB = AN/AC = MN/BC." },
          { h: "Exemple", t: "AM = 3, AB = 9, BC = 12 et (MN)//(BC). Alors MN/12 = 3/9, donc MN = 12 × 3 ÷ 9 = 4." },
          { h: "La réciproque", t: "Si AM/AB = AN/AC et si les points A, M, B et A, N, C sont alignés dans le même ordre, alors (MN) // (BC)." },
          { h: "La contraposée", t: "Si AM/AB ≠ AN/AC, alors les droites (MN) et (BC) ne sont pas parallèles." },
          { h: "Agrandissement / réduction", t: "Les triangles AMN et ABC sont proportionnels. Si les longueurs sont multipliées par k, les aires sont multipliées par k² et les volumes par k³." },
        ],
        retenir: "Pythagore → triangle rectangle. Thalès → droites parallèles. Repère bien l’information donnée par l’énoncé !",
      },
      {
        id: "ma-trigo",
        title: "Trigonométrie",
        intro: "Dans un triangle rectangle, elle relie les angles aigus et les longueurs des côtés.",
        points: [
          { h: "SOH CAH TOA", t: "Sinus = Opposé / Hypoténuse ; Cosinus = Adjacent / Hypoténuse ; Tangente = Opposé / Adjacent." },
          { h: "Calculer une longueur", t: "Triangle rectangle en B, angle Â = 30°, AC = 10 (hypoténuse). BC (opposé) = 10 × sin(30°) = 10 × 0,5 = 5." },
          { h: "Calculer un angle", t: "On utilise les touches arccos, arcsin ou arctan (cos⁻¹, sin⁻¹, tan⁻¹) de la calculatrice, en mode DEGRÉS." },
          { h: "Valeurs utiles", t: "cos(60°) = 0,5 ; sin(30°) = 0,5 ; tan(45°) = 1. Le cosinus et le sinus d’un angle aigu sont toujours entre 0 et 1." },
        ],
        retenir: "Vérifie TOUJOURS que ta calculatrice est en mode degrés (DEG) avant de commencer !",
      },
      {
        id: "ma-fonctions",
        title: "Fonctions linéaires et affines",
        intro: "Une fonction associe à un nombre x un unique nombre f(x), appelé image de x.",
        points: [
          { h: "Vocabulaire", t: "Si f(2) = 7 : 7 est l’IMAGE de 2 ; 2 est UN ANTÉCÉDENT de 7. Notation : f : x ↦ f(x)." },
          { h: "Fonction linéaire", t: "f(x) = ax. Représentée par une droite passant par l’origine. Elle traduit une situation de proportionnalité (a = coefficient)." },
          { h: "Fonction affine", t: "f(x) = ax + b. Représentée par une droite. a = coefficient directeur (pente), b = ordonnée à l’origine." },
          { h: "Calculer a", t: "Si la droite passe par A(x₁ ; y₁) et B(x₂ ; y₂) : a = (y₂ − y₁) / (x₂ − x₁)." },
          { h: "Sens de variation", t: "Si a > 0, la fonction est croissante ; si a < 0, décroissante ; si a = 0, constante." },
        ],
        retenir: "Pour lire une image sur un graphique : on part de l’axe des abscisses (x) et on lit sur l’axe des ordonnées (y).",
      },
      {
        id: "ma-calcul",
        title: "Calcul littéral & équations",
        intro: "Développer, factoriser et résoudre des équations : des points faciles à gagner si on connaît les règles.",
        points: [
          { h: "Double distributivité", t: "(a + b)(c + d) = ac + ad + bc + bd." },
          { h: "Identités remarquables", t: "(a + b)² = a² + 2ab + b² ; (a − b)² = a² − 2ab + b² ; (a + b)(a − b) = a² − b²." },
          { h: "Factoriser", t: "Repérer un facteur commun : 3x² + 6x = 3x(x + 2). Ou utiliser a² − b² = (a − b)(a + b) : x² − 25 = (x − 5)(x + 5)." },
          { h: "Équation du 1er degré", t: "3x + 5 = 20 → 3x = 15 → x = 5. On isole x en faisant la même opération des deux côtés." },
          { h: "Équation produit nul", t: "Un produit est nul si l’un de ses facteurs est nul. (x − 2)(x + 3) = 0 ⇔ x = 2 ou x = −3." },
        ],
        retenir: "Pour vérifier une solution, remplace x par la valeur trouvée dans l’équation de départ.",
      },
      {
        id: "ma-proba",
        title: "Probabilités & statistiques",
        intro: "Questions très fréquentes au Brevet, souvent avec des urnes, des dés ou des tableaux de données.",
        points: [
          { h: "Probabilité", t: "P(A) = nombre d’issues favorables / nombre d’issues possibles (si équiprobabilité). Toujours entre 0 et 1." },
          { h: "Événement contraire", t: "P(non A) = 1 − P(A). Ex. : P(obtenir 6) = 1/6 donc P(ne pas obtenir 6) = 5/6." },
          { h: "Moyenne", t: "Somme des valeurs ÷ effectif total. Avec coefficients : moyenne pondérée." },
          { h: "Médiane", t: "Valeur qui partage la série ORDONNÉE en deux groupes de même effectif." },
          { h: "Étendue", t: "Plus grande valeur − plus petite valeur. Elle mesure la dispersion de la série." },
        ],
        retenir: "N’oublie pas d’ORDONNER la série avant de chercher la médiane !",
      },
    ],
    quiz: [
      { q: "Un triangle ABC est rectangle en A avec AB = 6 cm et AC = 8 cm. Combien mesure BC ?", o: ["10 cm", "14 cm", "12 cm", "√28 cm"], a: 0, e: "D’après Pythagore : BC² = 6² + 8² = 36 + 64 = 100, donc BC = √100 = 10 cm." },
      { q: "Un triangle a pour côtés 5, 12 et 13. Est-il rectangle ?", o: ["Oui, car 13² = 5² + 12²", "Non, car 13 ≠ 5 + 12", "On ne peut pas savoir", "Oui, car 5 + 12 > 13"], a: 0, e: "13² = 169 et 5² + 12² = 25 + 144 = 169. D’après la réciproque de Pythagore, il est rectangle." },
      { q: "(MN) // (BC), AM = 2, AB = 6 et BC = 9. Combien mesure MN ?", o: ["3", "4,5", "27", "6"], a: 0, e: "Thalès : MN/BC = AM/AB donc MN = 9 × 2 ÷ 6 = 3." },
      { q: "Développer (x + 3)² donne :", o: ["x² + 9", "x² + 6x + 9", "x² + 3x + 9", "2x + 6"], a: 1, e: "Identité remarquable (a + b)² = a² + 2ab + b² : x² + 2×x×3 + 3² = x² + 6x + 9." },
      { q: "Quelles sont les solutions de (x − 4)(2x + 6) = 0 ?", o: ["4 et 3", "−4 et 3", "4 et −3", "Il n’y en a pas"], a: 2, e: "Produit nul : x − 4 = 0 → x = 4, ou 2x + 6 = 0 → x = −3." },
      { q: "Si f(x) = 3x − 5, quelle est l’image de 4 ?", o: ["7", "3", "−17", "12"], a: 0, e: "f(4) = 3 × 4 − 5 = 12 − 5 = 7." },
      { q: "Dans un triangle rectangle, le cosinus d’un angle aigu est égal à :", o: ["Opposé / Hypoténuse", "Adjacent / Hypoténuse", "Opposé / Adjacent", "Hypoténuse / Adjacent"], a: 1, e: "SOH CAH TOA : Cosinus = Adjacent / Hypoténuse." },
      { q: "Une urne contient 3 boules rouges et 5 bleues. Quelle est la probabilité de tirer une boule rouge ?", o: ["3/5", "5/8", "3/8", "1/3"], a: 2, e: "Il y a 3 issues favorables sur 8 boules au total : P = 3/8." },
      { q: "Quelle est la médiane de la série : 4 ; 9 ; 2 ; 7 ; 5 ?", o: ["2", "5", "5,4", "7"], a: 1, e: "On ordonne : 2 ; 4 ; 5 ; 7 ; 9. La valeur centrale (3e sur 5) est 5." },
      { q: "On agrandit une figure à l’échelle 3. Son aire est multipliée par :", o: ["3", "6", "9", "27"], a: 2, e: "Les aires sont multipliées par k² = 3² = 9 (et les volumes par k³ = 27)." },
    ],
  },
  {
    id: "histoire",
    name: "Histoire-Géo-EMC",
    short: "Histoire-Géo",
    icon: Globe2,
    gradient: "from-amber-500 to-orange-500",
    soft: "bg-amber-50 text-amber-700 border-amber-200",
    accent: "text-amber-600",
    sheets: [
      {
        id: "hg-ww2",
        title: "La Seconde Guerre mondiale (1939-1945)",
        intro: "Une guerre d’anéantissement, mondiale et totale, marquée par des crimes de masse sans précédent.",
        points: [
          { h: "Dates clés", t: "1er sept. 1939 : invasion de la Pologne. Juin 1940 : défaite de la France. 22 juin 1941 : invasion de l’URSS. 7 déc. 1941 : Pearl Harbor. 1942-1943 : Stalingrad (tournant). 6 juin 1944 : débarquement en Normandie. 8 mai 1945 : capitulation allemande. 6 et 9 août 1945 : Hiroshima et Nagasaki. 2 sept. 1945 : capitulation du Japon." },
          { h: "Une guerre d’anéantissement", t: "Les combats visent à détruire totalement l’ennemi, y compris les civils (bombardements, massacres). Environ 60 millions de morts, dont plus de la moitié de civils." },
          { h: "Le génocide des Juifs et des Tziganes", t: "Les nazis assassinent environ 6 millions de Juifs : fusillades par les Einsatzgruppen à l’Est (« Shoah par balles »), puis centres de mise à mort (Auschwitz-Birkenau, Treblinka…). Environ 200 000 Tziganes sont aussi exterminés." },
          { h: "La France dans la guerre", t: "Régime de Vichy (maréchal Pétain) : collaboration avec l’Allemagne, lois antisémites, rafle du Vél d’Hiv (juillet 1942). Résistance : appel du 18 juin 1940 du général de Gaulle, Jean Moulin unifie la Résistance intérieure (CNR, 1943)." },
        ],
        retenir: "Retiens le vocabulaire : guerre d’anéantissement, génocide, collaboration, Résistance, régime de Vichy, France libre.",
      },
      {
        id: "hg-guerrefroide",
        title: "La Guerre froide (1947-1991)",
        intro: "Affrontement indirect entre deux superpuissances : les États-Unis et l’URSS, sans conflit armé direct entre elles.",
        points: [
          { h: "Deux modèles opposés", t: "États-Unis : démocratie libérale, capitalisme. URSS : régime communiste, parti unique, économie planifiée." },
          { h: "Débuts (1947)", t: "Doctrine Truman (endiguement du communisme) et plan Marshall face à la doctrine Jdanov. L’Europe est coupée par le « rideau de fer »." },
          { h: "Berlin, symbole", t: "Blocus de Berlin (1948-1949), construction du Mur en 1961, chute du Mur le 9 novembre 1989." },
          { h: "Crises majeures", t: "Guerre de Corée (1950-1953), crise des missiles de Cuba (1962) : le monde frôle la guerre nucléaire. Guerre du Vietnam." },
          { h: "Fin", t: "Effondrement du bloc de l’Est (1989) puis disparition de l’URSS en décembre 1991." },
        ],
        retenir: "« Guerre froide » = pas d’affrontement direct entre les deux Grands, grâce à l’équilibre de la terreur (dissuasion nucléaire).",
      },
      {
        id: "hg-vrepublique",
        title: "La Ve République (depuis 1958)",
        intro: "Fondée en 1958 par le général de Gaulle pendant la guerre d’Algérie, elle renforce le pouvoir exécutif.",
        points: [
          { h: "Naissance", t: "Constitution adoptée par référendum le 28 septembre 1958. De Gaulle devient président. En 1962, le président est élu au suffrage universel direct." },
          { h: "Séparation des pouvoirs", t: "Exécutif : président de la République + gouvernement (Premier ministre). Législatif : Parlement (Assemblée nationale + Sénat). Judiciaire : tribunaux." },
          { h: "Alternance et cohabitation", t: "1981 : élection de François Mitterrand, première alternance de gauche. Cohabitation : président et Premier ministre de bords politiques opposés (1986, 1993, 1997)." },
          { h: "Évolution de la société", t: "Mai 1968 ; loi Neuwirth (contraception, 1967) ; majorité à 18 ans (1974) ; loi Veil sur l’IVG (1975) ; abolition de la peine de mort (1981) ; parité (2000)." },
        ],
        retenir: "Le président est élu pour 5 ans (quinquennat depuis 2002) au suffrage universel direct.",
      },
      {
        id: "hg-geo-territoire",
        title: "Géo : aires urbaines et aménagement du territoire",
        intro: "Comment le territoire français est-il organisé et aménagé ?",
        points: [
          { h: "Aire d’attraction d’une ville", t: "Un pôle (ville-centre + banlieue) et sa couronne (communes dont au moins 15 % des actifs travaillent dans le pôle). Plus de 9 Français sur 10 vivent sous l’influence d’une ville." },
          { h: "Périurbanisation", t: "Extension des villes vers les campagnes environnantes : maisons individuelles, dépendance à la voiture, étalement urbain." },
          { h: "Espaces productifs", t: "Industriels, agricoles, touristiques, de services. Ils se métropolisent et s’ouvrent sur le monde (littoraux, grandes métropoles)." },
          { h: "Aménager le territoire", t: "Actions de l’État, des régions, de l’UE pour réduire les inégalités : transports (LGV), couverture numérique, services publics en zone rurale." },
          { h: "Outre-mer", t: "Les territoires ultramarins (Guadeloupe, Martinique, Guyane, La Réunion, Mayotte…) font face à des défis spécifiques : éloignement, insularité, risques naturels." },
        ],
        retenir: "Pour un croquis : titre, légende organisée en parties, figurés clairs (points, flèches, aplats de couleur).",
      },
      {
        id: "hg-emc",
        title: "EMC : la République et la citoyenneté",
        intro: "Enseignement moral et civique : valeurs, principes et symboles de la République française.",
        points: [
          { h: "Valeurs et principes", t: "Devise : « Liberté, Égalité, Fraternité ». La France est une République indivisible, laïque, démocratique et sociale (article 1 de la Constitution)." },
          { h: "Symboles", t: "Drapeau tricolore, Marianne, La Marseillaise, le 14 Juillet, le coq gaulois." },
          { h: "La laïcité", t: "Loi de 1905 : séparation des Églises et de l’État. L’État est neutre ; chacun est libre de croire ou de ne pas croire." },
          { h: "Être citoyen", t: "Droits (voter dès 18 ans, liberté d’expression) et devoirs (respecter la loi, payer ses impôts, recensement à 16 ans, JDC)." },
          { h: "Engagement", t: "Associations, service civique, délégués de classe, vote, défense nationale. La Défense participe à la sécurité du pays (armée, gendarmerie)." },
        ],
        retenir: "Laïcité ≠ interdiction des religions : elle garantit la liberté de conscience et l’égalité de tous les citoyens.",
      },
    ],
    quiz: [
      { q: "Quelle bataille marque un tournant de la Seconde Guerre mondiale en 1942-1943 sur le front de l’Est ?", o: ["Verdun", "Stalingrad", "Midway", "El-Alamein"], a: 1, e: "La victoire soviétique à Stalingrad (février 1943) met fin à l’avancée allemande à l’Est. (Verdun, c’est 1916 !)" },
      { q: "Quel nom donne-t-on à l’extermination des Juifs d’Europe par les nazis ?", o: ["Le Blitzkrieg", "La Shoah", "Le Front populaire", "La guerre totale"], a: 1, e: "La Shoah (« catastrophe » en hébreu) désigne le génocide des Juifs : environ 6 millions de victimes." },
      { q: "Qui lance l’appel du 18 juin 1940 depuis Londres ?", o: ["Philippe Pétain", "Jean Moulin", "Charles de Gaulle", "Winston Churchill"], a: 2, e: "Le général de Gaulle appelle les Français à poursuivre le combat depuis Londres, sur les ondes de la BBC." },
      { q: "En quelle année le mur de Berlin tombe-t-il ?", o: ["1961", "1989", "1991", "1945"], a: 1, e: "Le mur tombe le 9 novembre 1989. Il avait été construit en 1961. L’URSS disparaît en 1991." },
      { q: "Lors de la crise de Cuba (1962), les États-Unis découvrent :", o: ["Des missiles nucléaires soviétiques", "Une base chinoise", "Un blocus de Berlin", "Un sous-marin allemand"], a: 0, e: "L’URSS installe des missiles nucléaires à Cuba, à proximité des États-Unis : le monde frôle la guerre nucléaire." },
      { q: "Depuis 1962, le président de la Ve République est élu :", o: ["Par le Parlement", "Au suffrage universel indirect", "Au suffrage universel direct", "Par le Premier ministre"], a: 2, e: "Le référendum de 1962 instaure l’élection du président au suffrage universel direct, ce qui renforce sa légitimité." },
      { q: "Quelle loi de 1975 autorise l’interruption volontaire de grossesse (IVG) ?", o: ["La loi Ferry", "La loi Veil", "La loi Neuwirth", "La loi Badinter"], a: 1, e: "Portée par Simone Veil, ministre de la Santé, la loi de 1975 dépénalise l’IVG." },
      { q: "Qu’appelle-t-on la périurbanisation ?", o: ["Le déclin des villes", "L’extension des villes vers les espaces ruraux voisins", "La construction de gratte-ciel", "Le retour à l’agriculture"], a: 1, e: "La périurbanisation est l’étalement des villes sur les campagnes proches, souvent avec des lotissements de maisons individuelles." },
      { q: "La loi de séparation des Églises et de l’État date de :", o: ["1789", "1882", "1905", "1958"], a: 2, e: "La loi du 9 décembre 1905 fonde la laïcité : la République ne reconnaît ni ne finance aucun culte." },
      { q: "Qu’appelle-t-on une « cohabitation » sous la Ve République ?", o: ["Un président et un Premier ministre de bords politiques opposés", "Deux présidents en même temps", "Un gouvernement d’union nationale", "Une fusion de l’Assemblée et du Sénat"], a: 0, e: "La cohabitation survient quand la majorité à l’Assemblée est opposée au président (ex. : 1986, 1993, 1997)." },
    ],
  },
  {
    id: "sciences",
    name: "Sciences",
    short: "Sciences",
    icon: FlaskConical,
    gradient: "from-emerald-500 to-teal-500",
    soft: "bg-emerald-50 text-emerald-700 border-emerald-200",
    accent: "text-emerald-600",
    sheets: [
      {
        id: "sc-genetique",
        title: "SVT : Génétique et hérédité",
        intro: "Chaque individu est unique grâce à son information génétique, portée par l’ADN.",
        points: [
          { h: "Chromosomes", t: "Dans le noyau de chaque cellule, l’humain possède 46 chromosomes, soit 23 paires. La 23e paire détermine le sexe (XX = fille, XY = garçon)." },
          { h: "ADN, gènes, allèles", t: "Un chromosome est formé d’ADN. Un gène est une portion d’ADN qui détermine un caractère (ex. : groupe sanguin). Un gène peut exister sous plusieurs versions : les allèles." },
          { h: "Mitose", t: "Division d’une cellule en deux cellules-filles identiques avec le même nombre de chromosomes (46). Permet la croissance et le renouvellement." },
          { h: "Méiose et fécondation", t: "La méiose produit les gamètes (spermatozoïdes, ovules) avec 23 chromosomes. La fécondation réunit 2 gamètes → cellule-œuf à 46 chromosomes, avec une combinaison unique." },
        ],
        retenir: "Gamètes = 23 chromosomes ; cellules du corps = 46 chromosomes. La fécondation explique la diversité génétique.",
      },
      {
        id: "sc-svt-sante",
        title: "SVT : Système immunitaire & microbes",
        intro: "Notre organisme se défend contre les micro-organismes pathogènes (bactéries, virus).",
        points: [
          { h: "Réaction rapide (innée)", t: "La phagocytose : des globules blancs (phagocytes) englobent et digèrent les microbes. Elle provoque l’inflammation (rougeur, chaleur, gonflement)." },
          { h: "Réaction adaptative", t: "Les lymphocytes B produisent des anticorps spécifiques qui neutralisent un antigène précis. Les lymphocytes T tuent les cellules infectées." },
          { h: "Mémoire immunitaire", t: "Après un premier contact, des lymphocytes mémoire permettent une réponse plus rapide et plus forte. C’est le principe de la vaccination." },
          { h: "Antibiotiques", t: "Ils agissent contre les bactéries, mais PAS contre les virus. Leur mauvais usage favorise la résistance des bactéries." },
        ],
        retenir: "Vaccin = prévention (mémoire immunitaire). Antibiotique = traitement contre les bactéries uniquement.",
      },
      {
        id: "sc-energie",
        title: "Physique : Énergie, puissance, électricité",
        intro: "L’énergie se conserve : elle se transforme d’une forme à une autre.",
        points: [
          { h: "Formes d’énergie", t: "Cinétique (mouvement), potentielle (position), thermique, électrique, chimique, lumineuse, nucléaire." },
          { h: "Énergie cinétique", t: "Ec = ½ × m × v² (m en kg, v en m/s, Ec en joules J). Doubler la vitesse multiplie l’énergie par 4 : importance pour la sécurité routière !" },
          { h: "Puissance électrique", t: "P = U × I (P en watts W, U en volts V, I en ampères A)." },
          { h: "Énergie électrique", t: "E = P × t (E en joules si t en secondes ; en Wh si t en heures). 1 kWh = 3 600 000 J." },
          { h: "Loi d’Ohm", t: "U = R × I (R résistance en ohms Ω)." },
        ],
        retenir: "Convertis TOUJOURS les unités avant de calculer (km/h → m/s : diviser par 3,6).",
      },
      {
        id: "sc-chimie",
        title: "Chimie : Atomes, ions et pH",
        intro: "La matière est constituée d’atomes, eux-mêmes formés d’un noyau et d’électrons.",
        points: [
          { h: "Structure de l’atome", t: "Noyau (protons chargés + et neutrons neutres) entouré d’électrons (chargés −). Un atome est électriquement neutre : autant de protons que d’électrons." },
          { h: "Les ions", t: "Un ion est un atome qui a gagné ou perdu des électrons. Cation (positif, a perdu des e⁻) ex. Na⁺ ; anion (négatif, a gagné des e⁻) ex. Cl⁻." },
          { h: "Le pH", t: "pH < 7 : solution acide (ions H⁺ majoritaires) ; pH = 7 : neutre ; pH > 7 : basique (ions HO⁻ majoritaires)." },
          { h: "Transformation chimique", t: "Des réactifs disparaissent, des produits se forment. Conservation des atomes et de la masse (Lavoisier : « Rien ne se perd… »)." },
        ],
        retenir: "Tests d’ions : Cu²⁺ → précipité bleu ; Fe²⁺ → vert ; Fe³⁺ → rouille (avec la soude) ; Cl⁻ → précipité blanc (nitrate d’argent).",
      },
      {
        id: "sc-techno",
        title: "Technologie : Objets techniques et programmation",
        intro: "Analyser le fonctionnement d’un objet technique et comprendre un programme.",
        points: [
          { h: "Chaîne d’information", t: "ACQUÉRIR (capteurs : bouton, détecteur de lumière…) → TRAITER (microcontrôleur, carte programmable) → COMMUNIQUER (écran, LED, signal)." },
          { h: "Chaîne d’énergie", t: "ALIMENTER (pile, secteur) → DISTRIBUER (interrupteur, relais) → CONVERTIR (moteur) → TRANSMETTRE (engrenages, courroie)." },
          { h: "Algorithme", t: "Suite d’instructions pour résoudre un problème. Structures : séquence, boucle (répéter, tant que), condition (si… alors… sinon)." },
          { h: "Variables", t: "Une variable stocke une valeur qui peut changer (ex. : score, température). Sous Scratch : « mettre score à 0 », « ajouter 1 à score »." },
        ],
        retenir: "Capteur = acquérir une information ; actionneur = agir (moteur, lampe, buzzer).",
      },
    ],
    quiz: [
      { q: "Combien de chromosomes contient une cellule humaine (hors gamètes) ?", o: ["23", "46", "44", "92"], a: 1, e: "Une cellule humaine contient 46 chromosomes (23 paires). Les gamètes n’en contiennent que 23." },
      { q: "Qu’est-ce qu’un allèle ?", o: ["Un chromosome sexuel", "Une version d’un gène", "Un type de cellule", "Une division cellulaire"], a: 1, e: "Un gène peut exister en plusieurs versions appelées allèles (ex. : allèles A, B, O pour le groupe sanguin)." },
      { q: "Les antibiotiques sont efficaces contre :", o: ["Les virus", "Les bactéries", "Les virus et les bactéries", "Les allergies"], a: 1, e: "Les antibiotiques n’agissent que sur les bactéries. Ils sont inutiles contre les virus (grippe, rhume…)." },
      { q: "Sur quel principe repose la vaccination ?", o: ["La phagocytose", "La mémoire immunitaire", "La méiose", "La photosynthèse"], a: 1, e: "Le vaccin fait produire des lymphocytes mémoire : en cas de vraie infection, la réponse est rapide et efficace." },
      { q: "Une lampe fonctionne sous 230 V avec une intensité de 0,5 A. Sa puissance vaut :", o: ["460 W", "115 W", "230,5 W", "0,002 W"], a: 1, e: "P = U × I = 230 × 0,5 = 115 W." },
      { q: "Si la vitesse d’un véhicule double, son énergie cinétique est :", o: ["Doublée", "Inchangée", "Multipliée par 4", "Divisée par 2"], a: 2, e: "Ec = ½ m v² : la vitesse est au carré, donc si v est multipliée par 2, Ec est multipliée par 2² = 4." },
      { q: "Une solution de pH = 3 est :", o: ["Neutre", "Basique", "Acide", "Impossible"], a: 2, e: "Un pH inférieur à 7 indique une solution acide (ex. : jus de citron, vinaigre)." },
      { q: "L’ion Na⁺ est :", o: ["Un anion, il a gagné un électron", "Un cation, il a perdu un électron", "Un atome neutre", "Un cation, il a gagné un proton"], a: 1, e: "La charge + signifie que l’atome de sodium a PERDU un électron : c’est un cation." },
      { q: "Dans la chaîne d’information, un capteur de luminosité sert à :", o: ["Traiter", "Acquérir", "Communiquer", "Convertir"], a: 1, e: "Un capteur ACQUIERT une information (ici, la luminosité) qui sera ensuite traitée par le microcontrôleur." },
      { q: "Dans un programme, « répéter 10 fois » est :", o: ["Une condition", "Une variable", "Une boucle", "Un capteur"], a: 2, e: "« Répéter » est une boucle : elle exécute plusieurs fois les mêmes instructions." },
    ],
  },
  {
    id: "oral",
    name: "Oral du Brevet",
    short: "Oral",
    icon: Mic,
    gradient: "from-violet-500 to-purple-500",
    soft: "bg-violet-50 text-violet-700 border-violet-200",
    accent: "text-violet-600",
    sheets: [
      {
        id: "or-deroule",
        title: "Le déroulement de l’épreuve",
        intro: "L’oral est noté sur 100 points. Il évalue ta capacité à exposer un projet et à argumenter.",
        points: [
          { h: "Durée", t: "15 minutes au total : 5 minutes d’exposé + 10 minutes d’entretien avec le jury (en individuel). En groupe (jusqu’à 3 élèves) : 10 min d’exposé + 15 min d’entretien." },
          { h: "Le jury", t: "Généralement 2 professeurs de ton collège. Ils ne sont pas forcément spécialistes de ton sujet : explique clairement !" },
          { h: "Le sujet", t: "Un projet mené en histoire des arts, dans un EPI, ou dans le cadre d’un parcours (Avenir, citoyen, éducation artistique et culturelle, santé)." },
          { h: "Les supports", t: "Tu peux t’appuyer sur un support (diaporama, objet, affiche), mais il ne doit pas être lu. Tu peux présenter une partie en langue étrangère." },
        ],
        retenir: "Ce n’est pas une récitation : le jury évalue surtout ton aisance, ta réflexion et ta capacité à répondre aux questions.",
      },
      {
        id: "or-structure",
        title: "Construire un exposé efficace",
        intro: "5 minutes, c’est court : chaque phrase compte ! Voici une structure qui marche.",
        points: [
          { h: "Introduction (≈ 45 s)", t: "Salue le jury, présente-toi, annonce ton sujet avec une accroche (citation, question, anecdote), puis ta problématique et ton plan." },
          { h: "Développement (≈ 3 min 30)", t: "2 ou 3 parties : présentation du projet/de l’œuvre, ce que tu as fait (démarche, difficultés), ce que tu as appris (compétences, liens avec d’autres matières)." },
          { h: "Conclusion (≈ 45 s)", t: "Réponds à ta problématique, fais un bilan personnel (ce que ce projet t’a apporté) et propose une ouverture." },
          { h: "Les fiches", t: "Utilise de petites fiches avec des mots-clés, pas des phrases entières. Numérote-les !" },
        ],
        retenir: "Entraîne-toi à voix haute avec un chronomètre : vise 4 min 45 pour garder une marge.",
      },
      {
        id: "or-criteres",
        title: "Les critères de notation",
        intro: "La note sur 100 points se répartit généralement en deux grands axes.",
        points: [
          { h: "Maîtrise de l’expression orale (50 pts)", t: "Voix audible, débit adapté, vocabulaire précis, regard vers le jury, posture, gestion du temps." },
          { h: "Maîtrise du sujet (50 pts)", t: "Clarté de la présentation, qualité de l’argumentation, capacité à prendre du recul et à répondre aux questions." },
          { h: "Les bonnes attitudes", t: "Se tenir droit, sourire, regarder les deux membres du jury, ne pas croiser les bras, ne pas mâcher de chewing-gum." },
          { h: "Les pièges à éviter", t: "Lire ses notes, parler trop vite, répondre « je ne sais pas » sans chercher, tenue négligée, arriver en retard." },
        ],
        retenir: "Si tu ne connais pas une réponse, reformule la question et propose une piste de réflexion : le jury valorise ton raisonnement.",
      },
      {
        id: "or-stress",
        title: "Gérer son stress le jour J",
        intro: "Le stress est normal, il peut même t’aider à être concentré. Voici comment le maîtriser.",
        points: [
          { h: "La veille", t: "Prépare ta tenue, tes supports, ta convocation et ta pièce d’identité. Couche-toi tôt, évite les écrans tard." },
          { h: "La respiration", t: "Technique 4-4-4 : inspire 4 secondes, bloque 4 secondes, expire 4 secondes. Répète 3 fois avant d’entrer." },
          { h: "En cas de trou de mémoire", t: "Fais une pause, regarde ta fiche, reprends ta dernière idée ou passe à la partie suivante. Le jury est bienveillant." },
          { h: "S’entraîner", t: "Présente ton exposé à ta famille, tes amis, ou enregistre-toi en vidéo pour repérer tes tics de langage (« euh », « du coup »)." },
        ],
        retenir: "Plus tu t’entraînes, plus tu seras à l’aise : la répétition est la meilleure arme anti-stress !",
      },
    ],
    quiz: [
      { q: "Quelle est la durée de l’oral individuel du Brevet ?", o: ["10 minutes", "15 minutes (5 + 10)", "30 minutes", "5 minutes"], a: 1, e: "L’oral individuel dure 15 minutes : 5 minutes d’exposé suivies de 10 minutes d’entretien avec le jury." },
      { q: "Sur combien de points l’oral est-il noté ?", o: ["50 points", "100 points", "200 points", "20 points"], a: 1, e: "L’oral est noté sur 100 points, autant que le français ou les mathématiques !" },
      { q: "Quelle attitude faut-il adopter face au jury ?", o: ["Lire son texte pour ne rien oublier", "Regarder le jury et parler clairement", "Parler très vite pour tout dire", "Fixer le plafond"], a: 1, e: "Regarder le jury, parler distinctement et à un rythme posé montrent ton aisance à l’oral." },
      { q: "Que faire si tu ne connais pas la réponse à une question ?", o: ["Dire « je ne sais pas » et se taire", "Inventer n’importe quoi", "Reformuler et proposer une piste de réflexion", "Changer de sujet"], a: 2, e: "Le jury valorise ta capacité à réfléchir. Reformule la question et propose ce que tu penses, même partiellement." },
      { q: "Sur quoi peut porter le sujet de l’oral ?", o: ["Uniquement sur un livre lu en classe", "Un projet d’histoire des arts, d’EPI ou d’un parcours éducatif", "Un sujet tiré au sort le jour J", "Une question de mathématiques"], a: 1, e: "Tu présentes un projet mené en histoire des arts, en EPI ou dans un parcours (Avenir, citoyen, santé, artistique et culturel)." },
      { q: "Quels documents faut-il prévoir pour les fiches de l’exposé ?", o: ["Un texte entièrement rédigé", "Des fiches avec des mots-clés", "Aucune fiche", "Le manuel scolaire"], a: 1, e: "Des fiches avec des mots-clés t’aident sans te pousser à lire. Le jury veut t’entendre parler, pas réciter." },
      { q: "Peut-on présenter une partie de son oral en langue étrangère ?", o: ["Non, c’est interdit", "Oui, c’est possible", "Oui, mais uniquement en latin", "Seulement en groupe"], a: 1, e: "Oui, une partie de la présentation peut se faire en langue vivante étrangère (ou régionale) étudiée au collège." },
      { q: "Quelle technique aide à gérer le stress avant d’entrer ?", o: ["Boire un soda", "La respiration lente et contrôlée", "Réviser tout le cours à la dernière minute", "Parler fort dans le couloir"], a: 1, e: "La respiration lente (ex. 4-4-4) fait baisser le rythme cardiaque et aide à se recentrer." },
    ],
  },
];

const JURY_QUESTIONS = [
  "Pourquoi as-tu choisi ce sujet ?",
  "Quelles difficultés as-tu rencontrées et comment les as-tu surmontées ?",
  "Qu’as-tu appris grâce à ce projet ?",
  "Si tu devais refaire ce projet, que changerais-tu ?",
  "Quel lien fais-tu entre ce projet et d’autres matières ?",
  "Comment as-tu organisé ton travail (seul·e ou en groupe) ?",
  "Quelles sources as-tu utilisées ? Comment as-tu vérifié leur fiabilité ?",
  "En quoi ce projet t’aide-t-il à réfléchir à ton orientation ?",
  "Peux-tu définir précisément ce terme que tu as employé ?",
  "Quelle partie du projet as-tu préférée, et pourquoi ?",
  "Ce sujet a-t-il un lien avec l’actualité ?",
  "Quel message l’artiste (ou l’œuvre) cherche-t-il à transmettre selon toi ?",
  "Quelles compétences as-tu développées pendant ce projet ?",
  "Comment ce projet a-t-il changé ton regard sur le sujet ?",
  "Que conseillerais-tu à un élève qui voudrait mener un projet similaire ?",
];

const SOCLE = [
  "Langue française (oral et écrit)",
  "Langues étrangères et régionales",
  "Langages mathématiques, scientifiques et informatiques",
  "Langages des arts et du corps",
  "Méthodes et outils pour apprendre",
  "Formation de la personne et du citoyen",
  "Systèmes naturels et systèmes techniques",
  "Représentations du monde et activité humaine",
];
const SOCLE_LEVELS = [
  { label: "Insuffisante", pts: 10 },
  { label: "Fragile", pts: 25 },
  { label: "Satisfaisante", pts: 40 },
  { label: "Très bonne", pts: 50 },
];
const EXAMS = [
  { id: "francais", label: "Français", max: 100 },
  { id: "maths", label: "Mathématiques", max: 100 },
  { id: "histoire", label: "Histoire-Géo-EMC", max: 50 },
  { id: "sciences", label: "Sciences", max: 50 },
  { id: "oral", label: "Oral", max: 100 },
];

// Date estimée du début des épreuves écrites (le calendrier officiel est publié par le ministère).
const EXAM_DATE = new Date("2027-06-24T09:00:00+02:00");

const TIPS = [
  "Réviser 25 minutes concentré vaut mieux qu’1 heure distrait. Range ton téléphone !",
  "Explique une notion à voix haute comme si tu étais le prof : c’est la meilleure façon de vérifier que tu l’as comprise.",
  "Refais les quiz quelques jours plus tard : la répétition espacée ancre les connaissances.",
  "Le sommeil fixe ce que tu as appris dans la journée. Dors au moins 8 heures !",
  "Commence par la matière qui te fait le plus peur : ton cerveau est plus frais en début de séance.",
  "Fais des sujets d’annales en conditions réelles : chronomètre, pas de téléphone, pas de cours.",
  "Bois de l’eau et bouge pendant tes pauses : ton cerveau te dira merci.",
];

/* =========================================================================
   2. PERSISTANCE (localStorage)
   ========================================================================= */

const STORAGE_KEY = "brevet-boost-2027";
const todayStr = (d = new Date()) => {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
};
const daysBetween = (a, b) => Math.round((new Date(b) - new Date(a)) / 86400000);

const DEFAULT_STATE = {
  xp: 0,
  streak: 0,
  bestStreak: 0,
  lastActive: null,
  readSheets: [],
  quizBest: {},
  quizAnswered: 0,
  quizCorrect: 0,
  pomodoros: 0,
  socle: Array(8).fill(2),
  exams: { francais: 60, maths: 60, histoire: 30, sciences: 30, oral: 70 },
};

function loadState() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (!raw) return DEFAULT_STATE;
    const parsed = JSON.parse(raw);
    const merged = { ...DEFAULT_STATE, ...parsed, exams: { ...DEFAULT_STATE.exams, ...(parsed.exams || {}) } };
    // Le streak est perdu si la dernière activité date d’avant-hier ou plus.
    if (merged.lastActive && daysBetween(merged.lastActive, todayStr()) > 1) merged.streak = 0;
    return merged;
  } catch {
    return DEFAULT_STATE;
  }
}

function useProgress() {
  const [state, setState] = useState(loadState);
  useEffect(() => {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); } catch { /* stockage indisponible */ }
  }, [state]);

  // Enregistre une activité : met à jour le streak et ajoute de l’XP.
  const activity = (xpGain = 0, extra = (s) => s) => {
    setState((s) => {
      const today = todayStr();
      let { streak, bestStreak, lastActive } = s;
      if (lastActive !== today) {
        const gap = lastActive ? daysBetween(lastActive, today) : null;
        streak = gap === 1 ? streak + 1 : 1;
        lastActive = today;
      }
      bestStreak = Math.max(bestStreak, streak);
      return extra({ ...s, xp: s.xp + xpGain, streak, bestStreak, lastActive });
    });
  };
  return { state, setState, activity };
}

const levelInfo = (xp) => {
  const level = Math.floor(xp / 150) + 1;
  const into = xp % 150;
  const titles = ["Apprenti", "Curieux", "Studieux", "Motivé", "Expert", "Champion", "Légende du Brevet"];
  return { level, into, pct: (into / 150) * 100, title: titles[Math.min(level - 1, titles.length - 1)] };
};

/* =========================================================================
   3. COMPOSANTS UTILITAIRES
   ========================================================================= */

const Card = ({ className = "", children }) => (
  <div className={`rounded-3xl bg-white p-5 shadow-sm ring-1 ring-slate-200/70 ${className}`}>{children}</div>
);

const ProgressBar = ({ value, color = "bg-indigo-500", className = "" }) => (
  <div className={`h-3 w-full overflow-hidden rounded-full bg-slate-100 ${className}`}>
    <div className={`h-full rounded-full ${color} transition-all duration-500`} style={{ width: `${Math.min(100, Math.max(0, value))}%` }} />
  </div>
);

const fmt = (sec) => `${String(Math.floor(sec / 60)).padStart(2, "0")}:${String(sec % 60).padStart(2, "0")}`;

function useCountdown(target) {
  const [now, setNow] = useState(Date.now());
  useEffect(() => { const t = setInterval(() => setNow(Date.now()), 1000); return () => clearInterval(t); }, []);
  const diff = Math.max(0, target - now);
  return {
    days: Math.floor(diff / 86400000),
    hours: Math.floor((diff / 3600000) % 24),
    minutes: Math.floor((diff / 60000) % 60),
    seconds: Math.floor((diff / 1000) % 60),
    done: diff === 0,
  };
}

// Minuteur précis basé sur l’heure de fin (pas de dérive si l’onglet est en arrière-plan).
function useTimer(initialSeconds, onEnd) {
  const [remaining, setRemaining] = useState(initialSeconds);
  const [running, setRunning] = useState(false);
  const endRef = useRef(null);
  const onEndRef = useRef(onEnd);
  onEndRef.current = onEnd;

  useEffect(() => {
    if (!running) return;
    endRef.current = Date.now() + remaining * 1000;
    const t = setInterval(() => {
      const left = Math.max(0, Math.round((endRef.current - Date.now()) / 1000));
      setRemaining(left);
      if (left === 0) { setRunning(false); onEndRef.current?.(); }
    }, 250);
    return () => clearInterval(t);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [running]);

  const reset = (s) => { setRunning(false); setRemaining(s ?? initialSeconds); };
  return { remaining, running, start: () => remaining > 0 && setRunning(true), pause: () => setRunning(false), reset };
}

function beep() {
  try {
    const ctx = new (window.AudioContext || window.webkitAudioContext)();
    [0, 0.25, 0.5].forEach((delay) => {
      const o = ctx.createOscillator();
      const g = ctx.createGain();
      o.frequency.value = 880;
      o.connect(g); g.connect(ctx.destination);
      g.gain.setValueAtTime(0.2, ctx.currentTime + delay);
      g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + delay + 0.2);
      o.start(ctx.currentTime + delay);
      o.stop(ctx.currentTime + delay + 0.2);
    });
  } catch { /* audio indisponible */ }
}

function Toast({ toast }) {
  if (!toast) return null;
  return (
    <div className="pointer-events-none fixed inset-x-0 top-4 z-50 flex justify-center px-4">
      <div className="flex items-center gap-2 rounded-2xl bg-slate-900 px-4 py-3 text-sm font-semibold text-white shadow-xl animate-bounce">
        <Sparkles className="h-4 w-4 text-yellow-300" /> {toast}
      </div>
    </div>
  );
}

/* =========================================================================
   4. TABLEAU DE BORD
   ========================================================================= */

function Countdown() {
  const c = useCountdown(EXAM_DATE.getTime());
  const units = [
    { v: c.days, l: "jours" },
    { v: c.hours, l: "heures" },
    { v: c.minutes, l: "min" },
    { v: c.seconds, l: "sec" },
  ];
  return (
    <div className="rounded-3xl bg-gradient-to-br from-indigo-600 via-violet-600 to-fuchsia-600 p-5 text-white shadow-lg sm:p-6">
      <div className="flex items-center gap-2 text-sm font-semibold uppercase tracking-wide text-indigo-100">
        <Clock className="h-4 w-4" /> Compte à rebours — Épreuves écrites du DNB 2027
      </div>
      {c.done ? (
        <p className="mt-3 text-2xl font-black">C’est le grand jour ! Bonne chance 🍀</p>
      ) : (
        <div className="mt-4 grid grid-cols-4 gap-2 sm:gap-3">
          {units.map((u) => (
            <div key={u.l} className="rounded-2xl bg-white/15 p-2 text-center backdrop-blur sm:p-3">
              <div className="text-2xl font-black tabular-nums sm:text-4xl">{u.v}</div>
              <div className="text-[11px] font-medium uppercase text-indigo-100 sm:text-xs">{u.l}</div>
            </div>
          ))}
        </div>
      )}
      <p className="mt-3 text-xs text-indigo-100">Date estimée : fin juin 2027. Vérifie le calendrier officiel publié par le ministère.</p>
    </div>
  );
}

function getMention(total) {
  if (total >= 640) return { label: "Mention Très Bien", color: "from-emerald-500 to-green-500", emoji: "🏆" };
  if (total >= 560) return { label: "Mention Bien", color: "from-blue-500 to-cyan-500", emoji: "🥇" };
  if (total >= 480) return { label: "Mention Assez Bien", color: "from-amber-500 to-yellow-500", emoji: "🥈" };
  if (total >= 400) return { label: "Admis·e (sans mention)", color: "from-slate-500 to-slate-600", emoji: "✅" };
  return { label: "Non admis·e pour l’instant", color: "from-rose-500 to-red-500", emoji: "💪" };
}

function Simulator({ state, setState }) {
  const socleTotal = state.socle.reduce((sum, lvl) => sum + SOCLE_LEVELS[lvl].pts, 0);
  const examTotal = EXAMS.reduce((sum, e) => sum + (Number(state.exams[e.id]) || 0), 0);
  const total = socleTotal + examTotal;
  const mention = getMention(total);
  const next = [400, 480, 560, 640].find((t) => t > total);

  const setSocle = (i, lvl) => setState((s) => { const socle = [...s.socle]; socle[i] = lvl; return { ...s, socle }; });
  const setExam = (id, v, max) => setState((s) => ({ ...s, exams: { ...s.exams, [id]: Math.max(0, Math.min(max, Number(v) || 0)) } }));

  return (
    <Card>
      <div className="flex flex-wrap items-center justify-between gap-2">
        <h2 className="flex items-center gap-2 text-lg font-black text-slate-800"><Calculator className="h-5 w-5 text-indigo-500" /> Simulateur de points</h2>
        <span className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-600">sur 800 points</span>
      </div>

      <div className={`mt-4 rounded-2xl bg-gradient-to-r ${mention.color} p-4 text-white`}>
        <div className="flex items-end justify-between gap-3">
          <div>
            <div className="text-4xl font-black tabular-nums">{total}<span className="text-lg font-bold opacity-80"> / 800</span></div>
            <div className="mt-1 text-sm font-bold">{mention.emoji} {mention.label}</div>
          </div>
          <div className="text-right text-xs font-semibold opacity-90">
            Socle : {socleTotal}/400<br />Épreuves : {examTotal}/400
          </div>
        </div>
        <div className="mt-3 h-2 w-full overflow-hidden rounded-full bg-white/30">
          <div className="h-full rounded-full bg-white" style={{ width: `${(total / 800) * 100}%` }} />
        </div>
        <p className="mt-2 text-xs font-medium">
          {next ? `Encore ${next - total} points pour atteindre le palier suivant (${next} pts).` : "Tu as atteint le palier maximum, bravo !"}
        </p>
      </div>

      <div className="mt-5 grid gap-6 lg:grid-cols-2">
        <div>
          <h3 className="mb-2 text-sm font-bold text-slate-700">Contrôle continu — 8 composantes du socle (400 pts)</h3>
          <div className="space-y-2">
            {SOCLE.map((name, i) => (
              <div key={name} className="rounded-2xl bg-slate-50 p-2.5">
                <div className="mb-1.5 text-xs font-semibold text-slate-600">{name}</div>
                <div className="grid grid-cols-4 gap-1">
                  {SOCLE_LEVELS.map((lvl, j) => (
                    <button
                      key={lvl.label}
                      onClick={() => setSocle(i, j)}
                      className={`rounded-lg px-1 py-1.5 text-[10px] font-bold transition sm:text-[11px] ${state.socle[i] === j ? "bg-indigo-600 text-white shadow" : "bg-white text-slate-500 ring-1 ring-slate-200 hover:bg-indigo-50"}`}
                    >
                      {lvl.label}<br /><span className="opacity-80">{lvl.pts} pts</span>
                    </button>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
        <div>
          <h3 className="mb-2 text-sm font-bold text-slate-700">Épreuves finales (400 pts)</h3>
          <div className="space-y-3">
            {EXAMS.map((e) => {
              const v = state.exams[e.id];
              return (
                <div key={e.id} className="rounded-2xl bg-slate-50 p-3">
                  <div className="flex items-center justify-between text-sm">
                    <span className="font-semibold text-slate-700">{e.label}</span>
                    <span className="flex items-center gap-1">
                      <input
                        type="number" min={0} max={e.max} value={v}
                        onChange={(ev) => setExam(e.id, ev.target.value, e.max)}
                        className="w-16 rounded-lg border border-slate-200 bg-white px-2 py-1 text-right font-bold text-slate-800"
                        aria-label={`Note en ${e.label}`}
                      />
                      <span className="text-xs text-slate-500">/ {e.max}</span>
                    </span>
                  </div>
                  <input
                    type="range" min={0} max={e.max} value={v}
                    onChange={(ev) => setExam(e.id, ev.target.value, e.max)}
                    className="mt-2 w-full accent-indigo-600"
                    aria-label={`Curseur ${e.label}`}
                  />
                  <div className="text-right text-[11px] text-slate-500">soit {((v / e.max) * 20).toFixed(1)}/20</div>
                </div>
              );
            })}
          </div>
          <div className="mt-4 rounded-2xl bg-indigo-50 p-3 text-xs text-indigo-800">
            <b>Paliers :</b> 400 pts = admis · 480 = Assez Bien · 560 = Bien · 640 = Très Bien.
            <br />Barème de simulation : les modalités officielles du DNB peuvent évoluer, vérifie-les auprès de ton collège.
          </div>
        </div>
      </div>
    </Card>
  );
}

function Dashboard({ state, setState, goTo, totalSheets }) {
  const lvl = levelInfo(state.xp);
  const sheetsPct = (state.readSheets.length / totalSheets) * 100;
  const quizPct = SUBJECTS.reduce((sum, s) => sum + (state.quizBest[s.id] || 0), 0) / SUBJECTS.length;
  const globalPct = Math.round(sheetsPct * 0.5 + quizPct * 0.5);
  const tip = TIPS[new Date().getDate() % TIPS.length];
  const activeToday = state.lastActive === todayStr();

  return (
    <div className="space-y-5">
      <Countdown />

      <div className="grid gap-4 sm:grid-cols-3">
        <Card className="flex items-center gap-4">
          <div className={`flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl ${state.streak > 0 ? "bg-orange-100" : "bg-slate-100"}`}>
            <Flame className={`h-8 w-8 ${state.streak > 0 ? "text-orange-500" : "text-slate-400"}`} />
          </div>
          <div>
            <div className="text-3xl font-black text-slate-800">{state.streak} <span className="text-base font-bold text-slate-500">jour{state.streak > 1 ? "s" : ""}</span></div>
            <div className="text-xs font-semibold text-slate-500">
              {activeToday ? "Streak validé aujourd’hui 🔥" : "Révise aujourd’hui pour garder ta série !"}
            </div>
            <div className="text-[11px] text-slate-400">Record : {state.bestStreak} jours</div>
          </div>
        </Card>

        <Card className="flex items-center gap-4">
          <div className="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-yellow-100">
            <Star className="h-8 w-8 text-yellow-500" />
          </div>
          <div className="min-w-0 flex-1">
            <div className="text-lg font-black text-slate-800">Niveau {lvl.level} · {lvl.title}</div>
            <ProgressBar value={lvl.pct} color="bg-yellow-400" className="mt-1" />
            <div className="mt-1 text-xs font-semibold text-slate-500">{state.xp} XP · {150 - lvl.into} XP avant le niveau suivant</div>
          </div>
        </Card>

        <Card className="flex items-center gap-4">
          <div className="flex h-14 w-14 shrink-0 items-center justify-center rounded-2xl bg-indigo-100">
            <Target className="h-8 w-8 text-indigo-500" />
          </div>
          <div className="min-w-0 flex-1">
            <div className="text-lg font-black text-slate-800">Progression : {globalPct} %</div>
            <ProgressBar value={globalPct} className="mt-1" />
            <div className="mt-1 text-xs font-semibold text-slate-500">{state.readSheets.length}/{totalSheets} fiches · {state.pomodoros} pomodoros</div>
          </div>
        </Card>
      </div>

      <Card>
        <h2 className="mb-3 flex items-center gap-2 text-lg font-black text-slate-800"><Trophy className="h-5 w-5 text-amber-500" /> Progression par matière</h2>
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-5">
          {SUBJECTS.map((s) => {
            const read = s.sheets.filter((sh) => state.readSheets.includes(sh.id)).length;
            const best = state.quizBest[s.id] || 0;
            const Icon = s.icon;
            return (
              <button key={s.id} onClick={() => goTo("revisions", s.id)} className="group rounded-2xl border border-slate-200 p-3 text-left transition hover:-translate-y-0.5 hover:shadow-md">
                <div className={`mb-2 inline-flex rounded-xl bg-gradient-to-br ${s.gradient} p-2 text-white`}><Icon className="h-5 w-5" /></div>
                <div className="font-bold text-slate-800">{s.short}</div>
                <div className="mt-1 text-xs text-slate-500">Fiches : {read}/{s.sheets.length}</div>
                <ProgressBar value={(read / s.sheets.length) * 100} color="bg-gradient-to-r from-indigo-400 to-violet-500" className="mt-1 h-2" />
                <div className="mt-2 text-xs text-slate-500">Meilleur quiz : {best} %</div>
                <ProgressBar value={best} color="bg-gradient-to-r from-emerald-400 to-teal-500" className="mt-1 h-2" />
              </button>
            );
          })}
        </div>
      </Card>

      <div className="flex items-start gap-3 rounded-3xl border border-amber-200 bg-amber-50 p-4 text-amber-900">
        <Lightbulb className="mt-0.5 h-5 w-5 shrink-0 text-amber-500" />
        <p className="text-sm"><b>Conseil du jour :</b> {tip}</p>
      </div>

      <Simulator state={state} setState={setState} />
    </div>
  );
}

/* =========================================================================
   5. RÉVISIONS : FICHES & QUIZ
   ========================================================================= */

function SheetView({ subject, sheet, isRead, onRead, onBack }) {
  return (
    <div className="space-y-4">
      <button onClick={onBack} className="flex items-center gap-1 text-sm font-semibold text-slate-500 hover:text-slate-800"><ArrowLeft className="h-4 w-4" /> Retour aux fiches</button>
      <div className={`rounded-3xl bg-gradient-to-br ${subject.gradient} p-5 text-white shadow-lg sm:p-6`}>
        <div className="text-xs font-bold uppercase tracking-wide opacity-80">{subject.name} · Fiche de révision</div>
        <h2 className="mt-1 text-2xl font-black sm:text-3xl">{sheet.title}</h2>
        <p className="mt-2 text-sm opacity-95">{sheet.intro}</p>
      </div>
      <div className="grid gap-3 md:grid-cols-2">
        {sheet.points.map((p, i) => (
          <Card key={p.h} className="p-4">
            <div className="flex items-start gap-3">
              <span className={`flex h-7 w-7 shrink-0 items-center justify-center rounded-full border text-xs font-black ${subject.soft}`}>{i + 1}</span>
              <div>
                <h3 className="font-bold text-slate-800">{p.h}</h3>
                <p className="mt-1 text-sm leading-relaxed text-slate-600">{p.t}</p>
              </div>
            </div>
          </Card>
        ))}
      </div>
      <div className="flex items-start gap-3 rounded-3xl border-2 border-dashed border-yellow-300 bg-yellow-50 p-4">
        <Zap className="mt-0.5 h-5 w-5 shrink-0 text-yellow-500" />
        <p className="text-sm text-yellow-900"><b>À retenir :</b> {sheet.retenir}</p>
      </div>
      <button
        onClick={onRead}
        disabled={isRead}
        className={`flex w-full items-center justify-center gap-2 rounded-2xl py-4 font-black transition ${isRead ? "bg-emerald-100 text-emerald-700" : `bg-gradient-to-r ${subject.gradient} text-white shadow-lg hover:scale-[1.01]`}`}
      >
        {isRead ? <><CheckCircle2 className="h-5 w-5" /> Fiche maîtrisée</> : <><Check className="h-5 w-5" /> J’ai compris cette fiche (+20 XP)</>}
      </button>
    </div>
  );
}

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; }
  return a;
}

function Quiz({ subject, onAnswer, onFinish, onBack }) {
  const [questions] = useState(() => shuffle(subject.quiz));
  const [idx, setIdx] = useState(0);
  const [picked, setPicked] = useState(null);
  const [score, setScore] = useState(0);
  const [combo, setCombo] = useState(0);
  const [done, setDone] = useState(false);
  const q = questions[idx];

  const pick = (i) => {
    if (picked !== null) return;
    setPicked(i);
    const ok = i === q.a;
    const newCombo = ok ? combo + 1 : 0;
    setCombo(newCombo);
    if (ok) setScore((s) => s + 1);
    onAnswer(ok, ok ? 10 + (newCombo >= 3 ? 5 : 0) : 2);
  };

  const next = () => {
    if (idx + 1 >= questions.length) {
      setDone(true);
      onFinish(Math.round((score / questions.length) * 100));
    } else {
      setIdx(idx + 1);
      setPicked(null);
    }
  };

  if (done) {
    const pct = Math.round((score / questions.length) * 100);
    const msg = pct === 100 ? "Parfait ! Tu es prêt·e pour le Brevet 🏆" : pct >= 70 ? "Très bon travail, continue comme ça ! 🚀" : pct >= 50 ? "Pas mal ! Relis les fiches pour progresser 📚" : "Courage ! Relis les fiches et retente ta chance 💪";
    return (
      <Card className="text-center">
        <Award className={`mx-auto h-16 w-16 ${subject.accent}`} />
        <h2 className="mt-2 text-2xl font-black text-slate-800">Quiz terminé !</h2>
        <div className="mt-2 text-5xl font-black text-slate-800">{score}/{questions.length}</div>
        <p className="mt-2 text-slate-600">{msg}</p>
        <div className="mt-5 flex flex-col justify-center gap-2 sm:flex-row">
          <button onClick={onBack} className="rounded-2xl bg-slate-100 px-5 py-3 font-bold text-slate-700 hover:bg-slate-200">Retour</button>
          <button onClick={() => onBack("restart")} className={`rounded-2xl bg-gradient-to-r ${subject.gradient} px-5 py-3 font-bold text-white`}>
            <RefreshCw className="mr-1 inline h-4 w-4" /> Recommencer
          </button>
        </div>
      </Card>
    );
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <button onClick={() => onBack()} className="flex items-center gap-1 text-sm font-semibold text-slate-500 hover:text-slate-800"><ArrowLeft className="h-4 w-4" /> Quitter</button>
        <div className="flex items-center gap-2 text-sm font-bold">
          {combo >= 2 && <span className="rounded-full bg-orange-100 px-2 py-0.5 text-orange-600">🔥 Combo x{combo}</span>}
          <span className="text-slate-500">Question {idx + 1}/{questions.length}</span>
        </div>
      </div>
      <ProgressBar value={(idx / questions.length) * 100} color={`bg-gradient-to-r ${subject.gradient}`} />
      <Card>
        <h2 className="text-lg font-bold leading-snug text-slate-800 sm:text-xl">{q.q}</h2>
        <div className="mt-4 grid gap-2">
          {q.o.map((opt, i) => {
            let cls = "border-slate-200 bg-white hover:border-indigo-300 hover:bg-indigo-50";
            if (picked !== null) {
              if (i === q.a) cls = "border-emerald-400 bg-emerald-50 text-emerald-800";
              else if (i === picked) cls = "border-rose-400 bg-rose-50 text-rose-800";
              else cls = "border-slate-200 bg-white opacity-60";
            }
            return (
              <button key={opt} onClick={() => pick(i)} disabled={picked !== null}
                className={`flex items-center gap-3 rounded-2xl border-2 p-3 text-left text-sm font-semibold transition sm:text-base ${cls}`}>
                <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-slate-100 text-xs font-black text-slate-600">{String.fromCharCode(65 + i)}</span>
                <span className="flex-1">{opt}</span>
                {picked !== null && i === q.a && <CheckCircle2 className="h-5 w-5 text-emerald-500" />}
                {picked === i && i !== q.a && <XCircle className="h-5 w-5 text-rose-500" />}
              </button>
            );
          })}
        </div>
        {picked !== null && (
          <div className={`mt-4 rounded-2xl p-4 text-sm ${picked === q.a ? "bg-emerald-50 text-emerald-900" : "bg-rose-50 text-rose-900"}`}>
            <div className="mb-1 font-black">
              {picked === q.a ? `Bonne réponse ! +${10 + (combo >= 3 ? 5 : 0)} XP` : "Raté ! +2 XP pour l’effort"}
            </div>
            <p className="leading-relaxed">{q.e}</p>
          </div>
        )}
      </Card>
      {picked !== null && (
        <button onClick={next} className={`flex w-full items-center justify-center gap-2 rounded-2xl bg-gradient-to-r ${subject.gradient} py-4 font-black text-white shadow-lg`}>
          {idx + 1 >= questions.length ? "Voir mon score" : "Question suivante"} <ChevronRight className="h-5 w-5" />
        </button>
      )}
    </div>
  );
}

function Revisions({ state, activity, setState, subjectId, setSubjectId, notify }) {
  const subject = SUBJECTS.find((s) => s.id === subjectId) || SUBJECTS[0];
  const [view, setView] = useState({ mode: "list" });
  const [quizKey, setQuizKey] = useState(0);

  useEffect(() => { setView({ mode: "list" }); }, [subjectId]);

  const markRead = (sheetId) => {
    if (state.readSheets.includes(sheetId)) return;
    activity(20, (s) => ({ ...s, readSheets: [...s.readSheets, sheetId] }));
    notify("+20 XP — Fiche maîtrisée !");
  };

  return (
    <div className="space-y-5">
      <div className="-mx-4 overflow-x-auto px-4 pb-1 sm:mx-0 sm:px-0">
        <div className="flex gap-2">
          {SUBJECTS.map((s) => {
            const Icon = s.icon;
            const active = s.id === subject.id;
            return (
              <button key={s.id} onClick={() => setSubjectId(s.id)}
                className={`flex shrink-0 items-center gap-2 rounded-2xl px-4 py-2.5 text-sm font-bold transition ${active ? `bg-gradient-to-r ${s.gradient} text-white shadow-md` : "bg-white text-slate-600 ring-1 ring-slate-200 hover:bg-slate-50"}`}>
                <Icon className="h-4 w-4" /> {s.short}
              </button>
            );
          })}
        </div>
      </div>

      {view.mode === "sheet" && (
        <SheetView
          subject={subject}
          sheet={subject.sheets.find((sh) => sh.id === view.id)}
          isRead={state.readSheets.includes(view.id)}
          onRead={() => markRead(view.id)}
          onBack={() => setView({ mode: "list" })}
        />
      )}

      {view.mode === "quiz" && (
        <Quiz
          key={quizKey}
          subject={subject}
          onAnswer={(ok, xp) => activity(xp, (s) => ({ ...s, quizAnswered: s.quizAnswered + 1, quizCorrect: s.quizCorrect + (ok ? 1 : 0) }))}
          onFinish={(pct) => {
            setState((s) => ({ ...s, quizBest: { ...s.quizBest, [subject.id]: Math.max(s.quizBest[subject.id] || 0, pct) } }));
            if (pct === 100) { activity(30); notify("Sans faute ! Bonus +30 XP 🏆"); }
          }}
          onBack={(action) => {
            if (action === "restart") setQuizKey((k) => k + 1);
            else setView({ mode: "list" });
          }}
        />
      )}

      {view.mode === "list" && (
        <>
          <div className={`flex flex-col gap-4 rounded-3xl bg-gradient-to-br ${subject.gradient} p-5 text-white shadow-lg sm:flex-row sm:items-center sm:justify-between sm:p-6`}>
            <div>
              <h2 className="text-2xl font-black">{subject.name}</h2>
              <p className="text-sm opacity-90">{subject.sheets.length} fiches · {subject.quiz.length} questions de quiz · Meilleur score : {state.quizBest[subject.id] || 0} %</p>
            </div>
            <button onClick={() => { setQuizKey((k) => k + 1); setView({ mode: "quiz" }); }}
              className="flex items-center justify-center gap-2 rounded-2xl bg-white px-5 py-3 font-black text-slate-800 shadow-md transition hover:scale-105">
              <Brain className={`h-5 w-5 ${subject.accent}`} /> Lancer le quiz
            </button>
          </div>
          <div className="grid gap-3 sm:grid-cols-2">
            {subject.sheets.map((sh) => {
              const read = state.readSheets.includes(sh.id);
              return (
                <button key={sh.id} onClick={() => setView({ mode: "sheet", id: sh.id })}
                  className="group flex items-start gap-3 rounded-3xl bg-white p-4 text-left shadow-sm ring-1 ring-slate-200/70 transition hover:-translate-y-0.5 hover:shadow-md">
                  <div className={`rounded-2xl border p-2.5 ${subject.soft}`}><BookOpen className="h-5 w-5" /></div>
                  <div className="min-w-0 flex-1">
                    <h3 className="font-bold text-slate-800">{sh.title}</h3>
                    <p className="mt-1 line-clamp-2 text-xs text-slate-500">{sh.intro}</p>
                  </div>
                  {read ? <CheckCircle2 className="h-5 w-5 shrink-0 text-emerald-500" /> : <ChevronRight className="h-5 w-5 shrink-0 text-slate-300 group-hover:text-slate-500" />}
                </button>
              );
            })}
          </div>
        </>
      )}
    </div>
  );
}

/* =========================================================================
   6. OUTILS : POMODORO, PLANNING, ORAL
   ========================================================================= */

const POMO_MODES = {
  work: { label: "Révision", sec: 25 * 60, color: "from-rose-500 to-orange-500", icon: Brain },
  short: { label: "Pause", sec: 5 * 60, color: "from-emerald-500 to-teal-500", icon: Coffee },
  long: { label: "Grande pause", sec: 15 * 60, color: "from-sky-500 to-blue-500", icon: Coffee },
};

function Pomodoro({ state, activity, notify }) {
  const [mode, setMode] = useState("work");
  const [cycle, setCycle] = useState(0);
  const modeRef = useRef(mode);
  modeRef.current = mode;

  const timer = useTimer(POMO_MODES.work.sec, () => {
    beep();
    if (modeRef.current === "work") {
      const nextCycle = cycle + 1;
      setCycle(nextCycle);
      activity(15, (s) => ({ ...s, pomodoros: s.pomodoros + 1 }));
      notify("Pomodoro terminé ! +15 XP — Fais une pause ☕");
      switchMode(nextCycle % 4 === 0 ? "long" : "short");
    } else {
      notify("Pause terminée, on s’y remet ! 💪");
      switchMode("work");
    }
  });

  const switchMode = (m) => { setMode(m); timer.reset(POMO_MODES[m].sec); };
  const m = POMO_MODES[mode];
  const pct = 100 - (timer.remaining / m.sec) * 100;
  const R = 90; const C = 2 * Math.PI * R;

  return (
    <Card>
      <h2 className="flex items-center gap-2 text-lg font-black text-slate-800"><Timer className="h-5 w-5 text-rose-500" /> Minuteur Pomodoro</h2>
      <p className="text-sm text-slate-500">25 min de révision concentrée, puis 5 min de pause. Une grande pause toutes les 4 sessions.</p>
      <div className="mt-4 grid grid-cols-3 gap-2">
        {Object.entries(POMO_MODES).map(([k, v]) => (
          <button key={k} onClick={() => switchMode(k)}
            className={`rounded-xl py-2 text-xs font-bold sm:text-sm ${mode === k ? `bg-gradient-to-r ${v.color} text-white` : "bg-slate-100 text-slate-600"}`}>{v.label}</button>
        ))}
      </div>
      <div className="relative mx-auto mt-6 h-56 w-56">
        <svg viewBox="0 0 200 200" className="h-full w-full -rotate-90">
          <circle cx="100" cy="100" r={R} stroke="#f1f5f9" strokeWidth="14" fill="none" />
          <circle cx="100" cy="100" r={R} stroke="url(#pomoGrad)" strokeWidth="14" fill="none" strokeLinecap="round"
            strokeDasharray={C} strokeDashoffset={C - (pct / 100) * C} style={{ transition: "stroke-dashoffset 0.3s" }} />
          <defs>
            <linearGradient id="pomoGrad" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stopColor={mode === "work" ? "#f43f5e" : mode === "short" ? "#10b981" : "#0ea5e9"} />
              <stop offset="100%" stopColor={mode === "work" ? "#f97316" : mode === "short" ? "#14b8a6" : "#3b82f6"} />
            </linearGradient>
          </defs>
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <div className="text-5xl font-black tabular-nums text-slate-800">{fmt(timer.remaining)}</div>
          <div className="text-sm font-semibold text-slate-500">{m.label}</div>
        </div>
      </div>
      <div className="mt-6 flex justify-center gap-3">
        {timer.running ? (
          <button onClick={timer.pause} className="flex items-center gap-2 rounded-2xl bg-slate-800 px-6 py-3 font-bold text-white"><Pause className="h-5 w-5" /> Pause</button>
        ) : (
          <button onClick={timer.start} className={`flex items-center gap-2 rounded-2xl bg-gradient-to-r ${m.color} px-6 py-3 font-bold text-white shadow-md`}><Play className="h-5 w-5" /> {timer.remaining < m.sec ? "Reprendre" : "Démarrer"}</button>
        )}
        <button onClick={() => timer.reset(m.sec)} className="rounded-2xl bg-slate-100 px-4 py-3 text-slate-600 hover:bg-slate-200" aria-label="Réinitialiser"><RotateCcw className="h-5 w-5" /></button>
      </div>
      <div className="mt-5 flex justify-center gap-1.5">
        {[0, 1, 2, 3].map((i) => <span key={i} className={`h-3 w-3 rounded-full ${i < cycle % 4 ? "bg-rose-500" : "bg-slate-200"}`} />)}
      </div>
      <p className="mt-2 text-center text-xs font-semibold text-slate-500">Total : {state.pomodoros} pomodoro{state.pomodoros > 1 ? "s" : ""} réalisé{state.pomodoros > 1 ? "s" : ""}</p>
    </Card>
  );
}

const DAYS = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"];
const ACTIVITIES = ["Lire et résumer la fiche", "Faire le quiz puis corriger ses erreurs", "Exercices type Brevet (annales)", "Fiche mémo / carte mentale", "S’auto-interroger à voix haute"];

function Planner() {
  const [minutes, setMinutes] = useState(60);
  const [days, setDays] = useState([0, 1, 2, 3, 4, 5]);
  const [priority, setPriority] = useState(["maths"]);
  const [plan, setPlan] = useState(null);

  const toggle = (arr, setArr, v) => setArr(arr.includes(v) ? arr.filter((x) => x !== v) : [...arr, v]);

  const generate = () => {
    // Liste pondérée : les matières prioritaires apparaissent deux fois plus souvent.
    const pool = SUBJECTS.flatMap((s) => (priority.includes(s.id) ? [s, s] : [s]));
    const blocksPerDay = Math.max(1, Math.floor(minutes / 30)); // 25 min + 5 min de pause
    const sheetIdx = {};
    let k = 0;
    const result = [...days].sort((a, b) => a - b).map((d) => {
      const blocks = [];
      for (let b = 0; b < blocksPerDay; b++) {
        let s = pool[k % pool.length];
        // éviter deux fois la même matière d’affilée dans une journée
        if (blocks.length && blocks[blocks.length - 1].subject.id === s.id) { k++; s = pool[k % pool.length]; }
        k++;
        const si = sheetIdx[s.id] ?? 0;
        sheetIdx[s.id] = si + 1;
        const sheet = s.sheets[si % s.sheets.length];
        blocks.push({ subject: s, sheet, activity: ACTIVITIES[(si + b) % ACTIVITIES.length] });
      }
      return { day: DAYS[d], blocks };
    });
    setPlan(result);
  };

  const weekly = (days.length * Math.floor(minutes / 30) * 25) / 60;

  return (
    <Card>
      <h2 className="flex items-center gap-2 text-lg font-black text-slate-800"><CalendarDays className="h-5 w-5 text-indigo-500" /> Générateur de planning</h2>
      <p className="text-sm text-slate-500">Indique ton temps disponible : on te prépare une semaine de révisions en blocs Pomodoro.</p>

      <div className="mt-4 space-y-4">
        <div>
          <label className="text-sm font-bold text-slate-700">Temps par jour : <span className="text-indigo-600">{minutes >= 60 ? `${Math.floor(minutes / 60)} h ${minutes % 60 ? String(minutes % 60).padStart(2, "0") : ""}` : `${minutes} min`}</span></label>
          <input type="range" min={30} max={180} step={30} value={minutes} onChange={(e) => setMinutes(Number(e.target.value))} className="mt-1 w-full accent-indigo-600" />
        </div>
        <div>
          <div className="mb-1 text-sm font-bold text-slate-700">Jours de révision</div>
          <div className="flex flex-wrap gap-1.5">
            {DAYS.map((d, i) => (
              <button key={d} onClick={() => toggle(days, setDays, i)}
                className={`rounded-xl px-3 py-1.5 text-xs font-bold ${days.includes(i) ? "bg-indigo-600 text-white" : "bg-slate-100 text-slate-500"}`}>{d.slice(0, 3)}</button>
            ))}
          </div>
        </div>
        <div>
          <div className="mb-1 text-sm font-bold text-slate-700">Matières à renforcer (prioritaires)</div>
          <div className="flex flex-wrap gap-1.5">
            {SUBJECTS.map((s) => (
              <button key={s.id} onClick={() => toggle(priority, setPriority, s.id)}
                className={`rounded-xl px-3 py-1.5 text-xs font-bold ${priority.includes(s.id) ? `bg-gradient-to-r ${s.gradient} text-white` : "bg-slate-100 text-slate-500"}`}>{s.short}</button>
            ))}
          </div>
        </div>
        <button onClick={generate} disabled={!days.length}
          className="flex w-full items-center justify-center gap-2 rounded-2xl bg-gradient-to-r from-indigo-500 to-violet-500 py-3 font-black text-white shadow-md disabled:opacity-50">
          <Sparkles className="h-5 w-5" /> Générer mon planning ({weekly.toFixed(1).replace(".", ",")} h / semaine)
        </button>
      </div>

      {plan && (
        <div className="mt-5 grid gap-3 sm:grid-cols-2">
          {plan.map((d) => (
            <div key={d.day} className="rounded-2xl border border-slate-200 p-3">
              <div className="mb-2 font-black text-slate-800">{d.day}</div>
              <div className="space-y-2">
                {d.blocks.map((b, i) => (
                  <div key={i} className={`rounded-xl border p-2 text-xs ${b.subject.soft}`}>
                    <div className="font-bold">⏱ 25 min · {b.subject.short}</div>
                    <div className="mt-0.5">{b.sheet.title}</div>
                    <div className="mt-0.5 italic opacity-80">→ {b.activity}</div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </Card>
  );
}

const ORAL_PHASES = [
  { id: "expo", label: "Exposé", sec: 5 * 60, color: "from-violet-500 to-purple-500" },
  { id: "entretien", label: "Entretien", sec: 10 * 60, color: "from-fuchsia-500 to-pink-500" },
];

function OralPrep({ activity, notify }) {
  const [phase, setPhase] = useState(0);
  const [question, setQuestion] = useState(null);
  const [checks, setChecks] = useState({});
  const phaseRef = useRef(phase);
  phaseRef.current = phase;

  const timer = useTimer(ORAL_PHASES[0].sec, () => {
    beep();
    if (phaseRef.current === 0) {
      notify("Fin de l’exposé ! Place à l’entretien 🎤");
      setPhase(1); timer.reset(ORAL_PHASES[1].sec);
    } else {
      activity(25);
      notify("Oral blanc terminé ! +25 XP 🎉");
    }
  });

  const p = ORAL_PHASES[phase];
  const elapsed = p.sec - timer.remaining;
  const goPhase = (i) => { setPhase(i); timer.reset(ORAL_PHASES[i].sec); };
  const randomQ = () => {
    let q;
    do { q = JURY_QUESTIONS[Math.floor(Math.random() * JURY_QUESTIONS.length)]; } while (q === question && JURY_QUESTIONS.length > 1);
    setQuestion(q);
  };
  const CHECKLIST = ["Je salue le jury et me présente", "J’annonce ma problématique et mon plan", "Je regarde le jury (pas mes fiches)", "Je parle fort et lentement", "Je fais un bilan personnel en conclusion", "Je tiens dans les 5 minutes"];

  return (
    <Card>
      <h2 className="flex items-center gap-2 text-lg font-black text-slate-800"><Mic className="h-5 w-5 text-violet-500" /> Préparateur à l’Oral</h2>
      <p className="text-sm text-slate-500">Simule l’épreuve : 5 min d’exposé puis 10 min d’entretien avec le jury.</p>

      <div className="mt-4 grid grid-cols-2 gap-2">
        {ORAL_PHASES.map((ph, i) => (
          <button key={ph.id} onClick={() => goPhase(i)}
            className={`rounded-xl py-2 text-sm font-bold ${phase === i ? `bg-gradient-to-r ${ph.color} text-white` : "bg-slate-100 text-slate-600"}`}>
            {i + 1}. {ph.label} ({ph.sec / 60} min)
          </button>
        ))}
      </div>

      <div className={`mt-4 rounded-3xl bg-gradient-to-br ${p.color} p-6 text-center text-white`}>
        <div className="text-sm font-bold uppercase tracking-wide opacity-90">{p.label}</div>
        <div className="text-6xl font-black tabular-nums">{fmt(timer.remaining)}</div>
        <div className="mx-auto mt-3 h-2 max-w-xs overflow-hidden rounded-full bg-white/30">
          <div className="h-full rounded-full bg-white transition-all" style={{ width: `${(elapsed / p.sec) * 100}%` }} />
        </div>
        {phase === 0 && timer.running && (
          <div className="mt-2 text-xs font-semibold opacity-90">
            {elapsed < 45 ? "Introduction : accroche, problématique, plan" : elapsed < 255 ? "Développement : ta démarche et ce que tu as appris" : "Conclusion : bilan personnel et ouverture"}
          </div>
        )}
        <div className="mt-4 flex justify-center gap-2">
          {timer.running
            ? <button onClick={timer.pause} className="flex items-center gap-2 rounded-2xl bg-white/20 px-5 py-2.5 font-bold backdrop-blur"><Pause className="h-5 w-5" /> Pause</button>
            : <button onClick={timer.start} className="flex items-center gap-2 rounded-2xl bg-white px-5 py-2.5 font-bold text-slate-800"><Play className="h-5 w-5" /> {timer.remaining < p.sec ? "Reprendre" : "Démarrer"}</button>}
          <button onClick={() => timer.reset(p.sec)} className="rounded-2xl bg-white/20 px-3 py-2.5" aria-label="Réinitialiser"><RotateCcw className="h-5 w-5" /></button>
          {phase === 0 && <button onClick={() => goPhase(1)} className="rounded-2xl bg-white/20 px-3 py-2.5" aria-label="Passer à l’entretien"><SkipForward className="h-5 w-5" /></button>}
        </div>
      </div>

      <div className="mt-5 rounded-2xl bg-violet-50 p-4">
        <div className="flex items-center justify-between gap-2">
          <h3 className="font-bold text-violet-900">Question du jury</h3>
          <button onClick={randomQ} className="flex items-center gap-1 rounded-xl bg-violet-600 px-3 py-1.5 text-xs font-bold text-white"><Shuffle className="h-4 w-4" /> Tirer une question</button>
        </div>
        <p className="mt-2 min-h-[1.5rem] text-sm font-semibold text-violet-800">{question ? `« ${question} »` : "Clique sur « Tirer une question » pour t’entraîner à l’entretien."}</p>
      </div>

      <details className="mt-4 rounded-2xl border border-slate-200 p-4">
        <summary className="cursor-pointer font-bold text-slate-700">Les {JURY_QUESTIONS.length} questions fréquentes du jury</summary>
        <ol className="mt-3 list-decimal space-y-1 pl-5 text-sm text-slate-600">
          {JURY_QUESTIONS.map((q) => <li key={q}>{q}</li>)}
        </ol>
      </details>

      <div className="mt-4">
        <h3 className="mb-2 font-bold text-slate-700">Ma check-list d’oral</h3>
        <div className="grid gap-2 sm:grid-cols-2">
          {CHECKLIST.map((c) => (
            <label key={c} className={`flex cursor-pointer items-center gap-2 rounded-xl border p-2.5 text-sm ${checks[c] ? "border-emerald-300 bg-emerald-50 text-emerald-800" : "border-slate-200 text-slate-600"}`}>
              <input type="checkbox" checked={!!checks[c]} onChange={() => setChecks({ ...checks, [c]: !checks[c] })} className="h-4 w-4 accent-emerald-600" />
              {c}
            </label>
          ))}
        </div>
      </div>
    </Card>
  );
}

function Tools({ state, activity, notify, visible }) {
  const [tab, setTab] = useState("pomodoro");
  const tabs = [
    { id: "pomodoro", label: "Pomodoro", icon: Timer },
    { id: "planning", label: "Planning", icon: CalendarDays },
    { id: "oral", label: "Oral", icon: Mic },
  ];
  // Les outils restent montés (cachés) pour que les minuteurs continuent de tourner.
  return (
    <div className={visible ? "space-y-5" : "hidden"}>
      <div className="grid grid-cols-3 gap-2">
        {tabs.map((t) => {
          const Icon = t.icon;
          return (
            <button key={t.id} onClick={() => setTab(t.id)}
              className={`flex items-center justify-center gap-2 rounded-2xl py-3 text-sm font-bold ${tab === t.id ? "bg-slate-900 text-white shadow" : "bg-white text-slate-600 ring-1 ring-slate-200"}`}>
              <Icon className="h-4 w-4" /> {t.label}
            </button>
          );
        })}
      </div>
      <div className={tab === "pomodoro" ? "" : "hidden"}><Pomodoro state={state} activity={activity} notify={notify} /></div>
      <div className={tab === "planning" ? "" : "hidden"}><Planner /></div>
      <div className={tab === "oral" ? "" : "hidden"}><OralPrep activity={activity} notify={notify} /></div>
    </div>
  );
}

/* =========================================================================
   7. APPLICATION
   ========================================================================= */

export default function App() {
  const { state, setState, activity } = useProgress();
  const [page, setPage] = useState("home");
  const [subjectId, setSubjectId] = useState(SUBJECTS[0].id);
  const [toast, setToast] = useState(null);
  const toastTimer = useRef(null);
  const totalSheets = useMemo(() => SUBJECTS.reduce((n, s) => n + s.sheets.length, 0), []);
  const lvl = levelInfo(state.xp);

  const notify = (msg) => {
    setToast(msg);
    clearTimeout(toastTimer.current);
    toastTimer.current = setTimeout(() => setToast(null), 2500);
  };
  const goTo = (p, sid) => { setPage(p); if (sid) setSubjectId(sid); window.scrollTo({ top: 0, behavior: "smooth" }); };
  const resetAll = () => {
    if (window.confirm("Effacer toute ta progression ? Cette action est définitive.")) setState(DEFAULT_STATE);
  };

  const NAV = [
    { id: "home", label: "Accueil", icon: Home },
    { id: "revisions", label: "Révisions", icon: BookOpen },
    { id: "tools", label: "Outils", icon: Wrench },
  ];

  return (
    <div className="min-h-screen bg-gradient-to-b from-indigo-50 via-slate-50 to-slate-50 pb-24 text-slate-800 sm:pb-8">
      <Toast toast={toast} />

      <header className="sticky top-0 z-40 border-b border-slate-200/70 bg-white/80 backdrop-blur">
        <div className="mx-auto flex max-w-6xl items-center justify-between gap-3 px-4 py-3">
          <button onClick={() => goTo("home")} className="flex items-center gap-2">
            <div className="rounded-xl bg-gradient-to-br from-indigo-500 to-fuchsia-500 p-2 text-white"><GraduationCap className="h-5 w-5" /></div>
            <div className="text-left leading-tight">
              <div className="font-black">Brevet Boost</div>
              <div className="text-[11px] font-semibold text-slate-500">DNB 2027</div>
            </div>
          </button>
          <nav className="hidden gap-1 sm:flex">
            {NAV.map((n) => {
              const Icon = n.icon;
              return (
                <button key={n.id} onClick={() => goTo(n.id)}
                  className={`flex items-center gap-2 rounded-xl px-4 py-2 text-sm font-bold ${page === n.id ? "bg-indigo-600 text-white" : "text-slate-600 hover:bg-slate-100"}`}>
                  <Icon className="h-4 w-4" /> {n.label}
                </button>
              );
            })}
          </nav>
          <div className="flex items-center gap-2 text-sm font-black">
            <span className="flex items-center gap-1 rounded-full bg-orange-100 px-2.5 py-1 text-orange-600"><Flame className="h-4 w-4" />{state.streak}</span>
            <span className="flex items-center gap-1 rounded-full bg-yellow-100 px-2.5 py-1 text-yellow-700"><Star className="h-4 w-4" />{state.xp}</span>
            <span className="hidden rounded-full bg-indigo-100 px-2.5 py-1 text-indigo-700 md:inline">Niv. {lvl.level}</span>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-6xl px-4 py-5">
        {page === "home" && <Dashboard state={state} setState={setState} goTo={goTo} totalSheets={totalSheets} />}
        {page === "revisions" && (
          <Revisions state={state} setState={setState} activity={activity} subjectId={subjectId} setSubjectId={setSubjectId} notify={notify} />
        )}
        <Tools state={state} activity={activity} notify={notify} visible={page === "tools"} />

        <footer className="mt-10 text-center text-xs text-slate-400">
          Brevet Boost 2027 · Ta progression est enregistrée sur cet appareil.
          <button onClick={resetAll} className="ml-2 underline hover:text-slate-600">Réinitialiser</button>
        </footer>
      </main>

      <nav className="fixed inset-x-0 bottom-0 z-40 border-t border-slate-200 bg-white/95 backdrop-blur sm:hidden">
        <div className="grid grid-cols-3">
          {NAV.map((n) => {
            const Icon = n.icon;
            return (
              <button key={n.id} onClick={() => goTo(n.id)} className={`flex flex-col items-center gap-0.5 py-2.5 text-[11px] font-bold ${page === n.id ? "text-indigo-600" : "text-slate-400"}`}>
                <Icon className="h-5 w-5" /> {n.label}
              </button>
            );
          })}
        </div>
      </nav>
    </div>
  );
}
