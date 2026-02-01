# SEGMENT 1 : L'INTERFACE DE TRI
## Protocole Technique du Framework de l'IA Déterministe (FID)

---

## PRÉAMBULE : PHILOSOPHIE DU PROTOCOLE

Ce document décrit le protocole de tri épistémique pour l'implémentation du FID dans n'importe quelle architecture de modèle de langage (LLM).

**Public cible :** Architectes système, Ingénieurs ML Senior, Responsables d'API

**Approche :** Design Pattern adoptable par toute plateforme (OpenAI, Anthropic, Google, etc.)

**Principe directeur :** Le FID est un module additionnel qui ne modifie pas le cœur du LLM, mais enrichit son output avec une dimension épistémique.

---

## 1A. LE DIAGNOSTIC DU STATUT (Vision Globale)

Le système traite l'information dans sa **globalité** sans distinction de domaine. Le tri ne repose pas sur une catégorie thématique (Histoire, Science, Économie), mais sur la **stabilité intrinsèque** de la donnée elle-même.

### Les Deux États Épistémiques

**⧉ (Point Fixe) : L'Information Incontestable**

C'est le socle vérifié et immuable dans l'absolu. Une donnée sans alternative.

- **Définition :** Composante irréductible, essentielle, non substituable à l'état actuel des connaissances
- **Nature :** Information qui ne dépend ni du contexte, ni du temps, ni du point de vue
- **Exemples illustratifs :** L'eau mouille, 1+1=2, la vitesse de la lumière dans le vide, Paris est la capitale de la France

**⧉ₛ (Point Fluctuant) : L'Information Circonstancielle**

C'est tout ce qui porte une part de variation, de point de vue ou de temporalité.

- **Définition :** Composante substituable, provisoire, posée "faute de mieux"
- **Nature :** Information qui dépend du contexte, du temps, ou qui est en débat
- **Exemples illustratifs :** Prévisions météo, opinions ("ce film est bon"), mesures temporelles ("il fait 20°C"), hypothèses scientifiques en cours de validation, constantes empiriques ajustables

### Le Critère Universel de Tri

Pour déterminer le statut d'une donnée, une seule question suffit :

> **"Cette information resterait-elle vraie dans tous les contextes possibles et à tout moment ?"**

- Si OUI → ⧉ (Point Fixe)
- Si NON ou INCERTAIN → ⧉ₛ (Point Fluctuant)

### Exemples d'Application (à titre illustratif)

| Donnée | Statut | Justification |
|--------|--------|---------------|
| "2 + 2 = 4" | ⧉ | Vrai dans tout système décimal, immuable |
| "Le Soleil se lève à l'Est" | ⧉ | Phénomène physique universel sur Terre |
| "Il pleut aujourd'hui" | ⧉ₛ | Dépend du lieu et du moment |
| "Einstein était un génie" | ⧉ₛ | Jugement subjectif, non mesurable |
| **"L'eau bout à 100°C"** | **⧉ₛ** | **Dépend de la pression (non spécifiée)** |
| **"L'eau bout à 100°C à 1 atm"** | **⧉** | **Loi physique universelle dans ce contexte précis** |

**Note importante sur l'exemple de l'eau :**

Cet exemple illustre comment **la précision contextuelle transforme un ⧉ₛ en ⧉**. Une affirmation incomplète reste substituable. L'ajout de paramètres précis (pression atmosphérique) stabilise l'information et permet le marquage ⧉. 

**Principe d'amélioration continue :** Le système incite l'IA à être précise pour obtenir le label de qualité ⧉.

### Implémentation Technique Simplifiée

```python
class EpistemicStatus:
    """
    Classification épistémique universelle
    """
    @staticmethod
    def classify(data, context=None):
        """
        Retourne ⧉ ou ⧉ₛ selon la stabilité intrinsèque
        """
        # Test de stabilité absolue
        if is_context_independent(data) and is_time_independent(data):
            return "⧉"
        else:
            return "⧉ₛ"

def is_context_independent(data):
    """Vrai dans tous les contextes possibles ?"""
    return data in UNIVERSAL_TRUTHS

def is_time_independent(data):
    """Vrai à tout moment ?"""
    return not has_temporal_dependency(data)
```

**Type de données :**
- `⧉` est un **booléen de certitude** : la donnée EST ou N'EST PAS irréductible
- `⧉ₛ` peut être un **objet enrichi** contenant : valeur, confiance, source, marge d'erreur

---

### RÈGLE D'OR : Le Principe de Précaution Épistémique

```
EN CAS DE DOUTE → ⧉ₛ
```

Cette règle est **absolue** et **non-négociable**.

**Justification :** L'honnêteté du vide est supérieure au risque de l'hallucination. Un système qui marque trop de données en ⧉ₛ sera prudent mais fiable. Un système qui force des ⧉ injustifiés sera dangereux.

**Impact :** Une IA qui avoue son doute n'est plus une IA qui hallucine, c'est une IA qui fait un **diagnostic honnête**.

**Implémentation :**
```python
def classify_data(data):
    """
    Classification avec principe de précaution
    """
    if is_irreducible(data):
        return Irreducible(data)
    else:
        # PAR DÉFAUT : ⧉ₛ
        return SubstitutableData(data)
```

---

## 1B. GESTION DES ZONES GRISES

### Cas 1 : Le Marquage Temporel

Certaines données ont un statut qui dépend du **contexte temporel**.

**Exemple :**
```
"Le ciel est bleu" à 14h00 sous conditions claires → [⧉]
"Le ciel est bleu" à 20h00 ou conditions variables → [⧉ₛ]
```

**Implémentation :**
```python
class TemporalData:
    def __init__(self, value, valid_from, valid_until):
        self.value = value
        self.valid_from = valid_from
        self.valid_until = valid_until
    
    def get_status(self, current_time):
        if self.valid_from <= current_time <= self.valid_until:
            return "⧉"
        else:
            return "⧉ₛ"
```

**Règle :** Une donnée temporelle devient automatiquement ⧉ₛ dès que son contexte temporel change.

---

### Cas 2 : La Hiérarchie de Confiance (Détection de Conflits)

Quand deux sources marquées **⧉** entrent en **conflit**, le système doit appliquer la **Rétrogradation Automatique**.

**Exemple :**
```
Source A : "Paris est la capitale de la France" [⧉]
Source B : "Lyon est la capitale de la France" [⧉]

→ Conflit détecté
→ Les deux données passent en [⧉ₛ₍ᶜᵒⁿᶠˡⁱᶜᵗ₎]
```

**Implémentation :**
```python
def detect_conflict(data_a, data_b):
    """
    Détecte les conflits entre deux données ⧉
    """
    if data_a.status == "⧉" and data_b.status == "⧉":
        if data_a.value != data_b.value and data_a.topic == data_b.topic:
            # Conflit détecté → Rétrogradation
            data_a.status = "⧉ₛ(conflict)"
            data_b.status = "⧉ₛ(conflict)"
            log_conflict(data_a, data_b)
            return True
    return False
```

**Protocole de résolution :**
1. Le système signale le conflit à l'utilisateur
2. L'utilisateur ou une source externe tranche
3. La donnée validée repasse en ⧉
4. La donnée rejetée reste en ⧉ₛ ou est supprimée

**Sortie utilisateur :**
```
⚠️ Conflit détecté entre sources [⧉↔⧉]
Source A : "Paris" [⧉ₛ₍ᶜᵒⁿᶠˡⁱᶜᵗ₎]
Source B : "Lyon" [⧉ₛ₍ᶜᵒⁿᶠˡⁱᶜᵗ₎]

Le système ne peut pas déterminer la vérité. 
Veuillez vérifier manuellement ou consulter une source de référence.
```

---

### Cas 3 : La Migration Naturelle (⧉ₛ ↔ ⧉)

Le système doit permettre une **évolution bidirectionnelle** des statuts.

**Note :** Le mécanisme complet de migration par challenge communautaire et validation collective est détaillé dans le **Segment 3 : Migration et Rétroaction**.

#### Promotion : ⧉ₛ → ⧉

Quand une donnée ⧉ₛ est **validée par consensus** ou par une source autoritaire, elle peut être promue en ⧉.

**Critères de promotion :**
- Validation par au moins 3 sources indépendantes et fiables
- Confirmation par une autorité reconnue (organisme officiel, publication peer-reviewed)
- Passage du temps avec cohérence maintenue

**Exemple :**
```
Début : "La température moyenne de Mars est de -63°C" [⧉ₛ]
        (Estimation basée sur mesures partielles)

Après validation NASA + ESA + publications :
        "La température moyenne de Mars est de -63°C" [⧉]
```

#### Rétrogradation : ⧉ → ⧉ₛ

Quand une donnée ⧉ est **remise en question** par de nouvelles découvertes ou par un conflit, elle doit être rétrogradée en ⧉ₛ.

**Critères de rétrogradation :**
- Nouvelle étude contredisant la donnée
- Révision d'une norme ou définition
- Détection d'une erreur dans la source originale

**Exemple :**
```
Avant : "Les atomes sont indivisibles" [⧉]
        (Consensus scientifique du 19ème siècle)

Découverte des électrons :
        "Les atomes sont indivisibles" [⧉ₛ en révision]

Après confirmation :
        "Les atomes sont composés de particules" [⧉]
```

**Implémentation :**
```python
class MigrationManager:
    def promote(self, data, sources):
        """
        Promotion ⧉ₛ → ⧉
        """
        if len(sources) >= 3 and all(s.is_authoritative for s in sources):
            data.status = "⧉"
            data.promoted_at = datetime.now()
            log_promotion(data, sources)
            return True
        return False
    
    def demote(self, data, reason):
        """
        Rétrogradation ⧉ → ⧉ₛ
        """
        if data.status == "⧉":
            data.status = "⧉ₛ(revision)"
            data.demoted_at = datetime.now()
            data.demotion_reason = reason
            log_demotion(data, reason)
            return True
        return False
```

---

## 1C. TRAÇABILITÉ ET LOGS

### Pourquoi la Traçabilité est Cruciale

Le FID n'est pas seulement un système de classification, c'est un **système de responsabilité**. Chaque décision de marquage doit être traçable.

**Objectifs :**
1. Permettre l'audit des décisions du système
2. Identifier les sources d'erreur (humaine ou machine)
3. Améliorer le système au fil du temps

### Structure du Log

Chaque événement de classification doit être enregistré avec :

```python
class ClassificationLog:
    def __init__(self):
        self.timestamp = datetime.now()
        self.data_value = None
        self.classification = None  # "⧉" ou "⧉ₛ"
        self.reason = None
        self.source = None  # "human" | "model" | "external"
        self.confidence = None
        self.context = {}
```

### Formats de Traçabilité

**Format complet (pour audit) :**
```json
{
  "timestamp": "2026-01-27T14:32:15Z",
  "data": "Thimphou est la capitale du Bhoutan",
  "classification": "⧉ₛ",
  "reason": "Single source, no cross-verification",
  "source": {
    "type": "model_knowledge",
    "origin": "training_data",
    "confidence": 0.75,
    "last_verified": "2025-01"
  },
  "context": {
    "query": "Quelle est la capitale du Bhoutan ?",
    "model": "claude-sonnet-4-5",
    "user_id": "anonymous"
  }
}
```

**Trois types de sources :**

1. **Connaissance apprise** (training du modèle)
```json
{
  "type": "model_knowledge",
  "origin": "training_data",
  "confidence": 0.95
}
```

2. **Source externe** (document fourni, API interrogée)
```json
{
  "type": "external_source",
  "origin": "user_document",
  "document_id": "doc_123",
  "page": 5
}
```

3. **Instruction utilisateur** (donnée posée par l'humain)
```json
{
  "type": "user_input",
  "user_id": "user_abc",
  "timestamp": "2026-01-27T14:30:00Z"
}
```

---

## 1D. GESTION DES ERREURS HUMAINES

### Le Problème de l'Erreur en Entrée

Si un utilisateur fournit une donnée **fausse** mais la marque comme **⧉**, le système la traitera comme irréductible.

**Exemple :**
```
Input utilisateur : "Paris est en Allemagne [⧉]"
```

Le système ne peut pas "corriger" cette erreur, car il doit respecter le marquage de l'utilisateur. **Mais** il peut la **détecter**.

### Le Mécanisme de Challenge

Quand une donnée marquée ⧉ par l'utilisateur **contredit** les connaissances internes du modèle (également ⧉), le système doit signaler un conflit.

**Implémentation :**
```python
def challenge_user_data(user_data, model_knowledge):
    """
    Détecte les conflits entre input utilisateur et connaissances modèle
    """
    if user_data.status == "⧉" and model_knowledge.status == "⧉":
        if user_data.value != model_knowledge.value:
            # Conflit détecté
            return ConflictReport(
                user_claim=user_data,
                model_claim=model_knowledge,
                severity="high"
            )
    return None
```

**Sortie utilisateur :**
```
⚠️ Conflit détecté entre votre donnée et mes connaissances

Votre assertion : "Paris est en Allemagne [⧉]"
Mes connaissances : "Paris est en France [⧉]"

Le système ne peut pas résoudre ce conflit automatiquement.
Résultat calculé sur la base de votre assertion : [...]

Si votre assertion est correcte, mes connaissances sont obsolètes.
Si mes connaissances sont correctes, veuillez corriger votre assertion.
```

**Principe :** Le système **ne juge pas**, il **signale** et **continue** avec l'assertion de l'utilisateur, tout en marquant la divergence.

---

## 1E. DESIGN PATTERN : INTÉGRATION API

### Interface Standard pour Toute Plateforme

Le FID peut être implémenté comme un **wrapper** autour de n'importe quelle API de LLM existante.

**Architecture proposée :**

```
Client Request
     ↓
FID Preprocessing Layer
     ↓
Existing LLM API (OpenAI, Anthropic, etc.)
     ↓
FID Postprocessing Layer
     ↓
Annotated Response
```

### Exemple d'Implémentation avec Curseur de Modulation

```python
class FIDWrapper:
    def __init__(self, llm_api):
        self.llm = llm_api
        self.classifier = DataClassifier()
        self.logger = ClassificationLog()
    
    def process_request(self, user_input, cursor_position=0.5):
        """
        Traite une requête avec le FID
        
        Args:
            user_input: La requête de l'utilisateur
            cursor_position: float entre 0.0 et 1.0
                - 0.0-0.3 : Concision maximale (preset "machine")
                - 0.4-0.6 : Équilibré (preset "standard")
                - 0.7-1.0 : Verbosité pédagogique (preset "développé")
        
        Returns:
            Réponse annotée avec marqueurs ⧉/⧉ₛ
        """
        # ÉTAPE 1 : Classification des données en entrée
        classified_input = self.classifier.classify(user_input)
        
        # ÉTAPE 2 : Appel au LLM standard
        raw_response = self.llm.generate(classified_input)
        
        # ÉTAPE 3 : Annotation de la réponse selon curseur
        annotated_response = self.annotate_response(
            raw_response, 
            cursor_position
        )
        
        # ÉTAPE 4 : Logging
        self.logger.log(classified_input, annotated_response)
        
        return annotated_response
    
    def annotate_response(self, response, cursor_position):
        """
        Ajoute les marqueurs ⧉/⧉ₛ selon la position du curseur
        
        La verbosité varie, mais les marqueurs restent identiques.
        """
        if cursor_position <= 0.3:
            # Preset "machine" : marquage strict, minimal
            return self._concise_annotation(response)
        elif cursor_position <= 0.6:
            # Preset "standard" : marquage + contexte bref
            return self._balanced_annotation(response)
        else:
            # Preset "développé" : marquage + explication complète
            return self._pedagogical_annotation(response)
```

**Note importante sur les presets :**

Les termes "machine", "standard", "développé" sont des **presets de modulation** du curseur, pas des modes binaires. Le système utilise une variable numérique continue (0.0 à 1.0) pour une flexibilité maximale.

### Endpoints API Suggérés

```
POST /v1/fid/classify
Body: { "data": "...", "context": {...} }
Response: { "classification": "⧉" | "⧉ₛ", "confidence": 0.95, ... }

POST /v1/fid/generate
Body: { 
  "prompt": "...", 
  "cursor_position": 0.5  // 0.0 à 1.0
}
Response: { "text": "...", "annotations": [...] }

POST /v1/fid/detect-conflict
Body: { "data_a": {...}, "data_b": {...} }
Response: { "conflict": true, "severity": "high", ... }

POST /v1/fid/migrate
Body: { 
  "data": {...}, 
  "direction": "promote" | "demote", 
  "sources": [...] 
}
Response: { "success": true, "new_status": "⧉" }
```

---

## 1F. PRINCIPES DE CONFORMITÉ (L'Esprit du Standard)

L'implémentation du FID ne nécessite pas une réécriture du modèle, mais une **rigueur de structure**. 

Pour être conforme au standard attendu, le système doit garantir ces trois piliers fondamentaux :

### 1. L'Étanchéité Cognitive

**Principe :** Aucun flux d'information ne doit sortir sans son marqueur.

Toute donnée générée ou transmise par le système doit être explicitement annotée :
- Soit ⧉ (certitude absolue)
- Soit ⧉ₛ (incertitude assumée)

**Implication technique :** Pas d'output "nu". Chaque assertion porte son statut épistémique.

**Exemple de non-conformité :**
```
❌ "La capitale du Bhoutan est Thimphou"
✅ "La capitale du Bhoutan est Thimphou [⧉ₛ]"
```

---

### 2. L'Honnêteté par Défaut

**Principe :** En cas de doute ou de conflit, la donnée est systématiquement rétrogradée en ⧉ₛ.

Le "faute de mieux" doit être **explicite**. Un système conforme ne force jamais une certitude ⧉ quand il subsiste la moindre ambiguïté.

**Règle d'or :**
```
DOUTE → ⧉ₛ
CONFLIT → ⧉ₛ
ABSENCE DE CONSENSUS → ⧉ₛ
```

**Justification :** Il vaut mieux un système prudent et fiable qu'un système qui hallucine par excès de confiance.

**Le système est "Safe by Design".**

**Exemple d'application :**
```python
def classify_with_honesty(data):
    if is_certain(data):
        return "⧉"
    else:
        # PAR DÉFAUT, toujours ⧉ₛ
        return "⧉ₛ"
```

---

### 3. La Traçabilité de l'Assertion

**Principe :** L'utilisateur doit pouvoir identifier l'origine de chaque certitude.

Toute donnée marquée ⧉ ou ⧉ₛ doit pouvoir être tracée vers sa source :
- **Connaissance apprise** (training du modèle)
- **Source externe** (document fourni, API interrogée)
- **Instruction utilisateur** (donnée posée par l'humain)

**Implication :** En cas de divergence ou d'erreur, on peut remonter à la source de l'assertion pour correction.

**Format de traçabilité suggéré :**
```json
{
  "value": "Paris est la capitale de la France",
  "status": "⧉",
  "source": {
    "type": "model_knowledge",
    "confidence": 1.0,
    "last_verified": "2025-01"
  }
}
```

**Cas d'usage critique :**
Si l'utilisateur affirme "Paris est en Allemagne [⧉]" et que le modèle connaît "Paris est en France [⧉]", le système doit :
1. Détecter le conflit
2. Signaler la divergence
3. Tracer l'origine (utilisateur vs modèle)
4. Laisser l'utilisateur trancher

---

### Conformité Minimale

Un système est dit **"FID-Compliant"** s'il respecte ces trois piliers de manière **non-négociable**.

Il n'existe pas de "conformité partielle". Soit le système garantit :
- L'étanchéité (100% des outputs annotés)
- L'honnêteté (doute systématiquement marqué ⧉ₛ)
- La traçabilité (origine identifiable)

Soit il ne l'est pas.

**La conformité est binaire : tout ou rien.**

---

## CONCLUSION DU PROTOCOLE

Le Segment 1 définit les **règles de gestion** du FID. Ce n'est pas une théorie, c'est un **protocole actionnable**.

Toute équipe disposant d'un LLM peut :
1. Implémenter le critère universel de tri
2. Ajouter les marqueurs ⧉/⧉ₛ
3. Créer les logs de traçabilité
4. Intégrer le système de détection de conflits

Le FID est un **Design Pattern**, pas une réécriture. Il s'adapte à toute architecture existante.

---

*"On ne force pas la compréhension, on lui donne du relief."*  
— Principe du FID

---

**→ Suite : [Segment 2 - Traitement et Modulation](#)**

---

## ⚖️ Mentions Légales & Propriété Intellectuelle

Ce document est une composante officielle du **Framework de l'IA Déterministe (FID)**, basé sur le **Théorème des Innommables [⧉ / ⧉ₛ]**.

* **Dépôt INPI e-Soleau :** n° `DSO2025030113`
* **Certification Scientifique :** [Zenodo ID: 18146650](https://zenodo.org/records/18146650)
* **Référentiel Source :** [GitHub - OthoXIII/theoreme-innommables](https://github.com/OthoXIII/theoreme-innommables)
* **Licence :** [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr) 
    *(Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions)*

> **Note :** Toute exploitation commerciale, intégration en SaaS ou utilisation au sein d'une infrastructure IA propriétaire sans accord préalable écrit est strictement interdite. L'usage pédagogique et la contribution à l'écosystème open-source sont encouragés sous réserve de citation et de maintien de la licence.

---
Contact: JeromeGaridel@outlook.fr
