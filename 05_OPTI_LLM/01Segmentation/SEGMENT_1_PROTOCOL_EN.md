# SEGMENT 1: THE SORTING INTERFACE
## Technical Protocol of the Deterministic AI Framework (FID)

---

## PREAMBLE: PROTOCOL PHILOSOPHY

This document describes the epistemic sorting protocol for FID implementation in any language model (LLM) architecture.

**Target audience:** System Architects, Senior ML Engineers, API Managers

**Approach:** Design Pattern adoptable by any platform (OpenAI, Anthropic, Google, etc.)

**Guiding principle:** The FID is an additional module that does not modify the LLM core, but enriches its output with an epistemic dimension.

---

## 1A. STATUS DIAGNOSIS (Global Vision)

The system processes information in its **entirety** without domain distinction. Sorting does not rely on thematic category (History, Science, Economics), but on the **intrinsic stability** of the data itself.

### The Two Epistemic States

**⧉ (Fixed Point): Incontestable Information**

This is the verified and absolutely immutable foundation. Data without alternative.

- **Definition:** Irreducible, essential, non-substitutable component at the current state of knowledge
- **Nature:** Information independent of context, time, or viewpoint
- **Illustrative examples:** Water is wet, 1+1=2, speed of light in vacuum, Paris is the capital of France

**⧉ₛ (Fluctuating Point): Circumstantial Information**

Everything that carries variation, viewpoint, or temporality.

- **Definition:** Substitutable, provisional component, posited "for lack of better"
- **Nature:** Information dependent on context, time, or under debate
- **Illustrative examples:** Weather forecasts, opinions ("this movie is good"), temporal measurements ("it's 20°C"), scientific hypotheses under validation, adjustable empirical constants

### The Universal Sorting Criterion

To determine data status, only one question is needed:

> **"Would this information remain true in all possible contexts and at all times?"**

- If YES → ⧉ (Fixed Point)
- If NO or UNCERTAIN → ⧉ₛ (Fluctuating Point)

### Application Examples (illustrative)

| Data | Status | Justification |
|------|--------|---------------|
| "2 + 2 = 4" | ⧉ | True in any decimal system, immutable |
| "The Sun rises in the East" | ⧉ | Universal physical phenomenon on Earth |
| "It's raining today" | ⧉ₛ | Depends on place and time |
| "Einstein was a genius" | ⧉ₛ | Subjective judgment, unmeasurable |
| **"Water boils at 100°C"** | **⧉ₛ** | **Depends on pressure (unspecified)** |
| **"Water boils at 100°C at 1 atm"** | **⧉** | **Universal physical law in this precise context** |

**Important note on the water example:**

This example illustrates how **contextual precision transforms a ⧉ₛ into ⧉**. An incomplete statement remains substitutable. Adding precise parameters (atmospheric pressure) stabilizes the information and enables ⧉ marking.

**Continuous improvement principle:** The system encourages the AI to be precise to obtain the ⧉ quality label.

### Simplified Technical Implementation

```python
class EpistemicStatus:
    """
    Universal epistemic classification
    """
    @staticmethod
    def classify(data, context=None):
        """
        Returns ⧉ or ⧉ₛ according to intrinsic stability
        """
        # Absolute stability test
        if is_context_independent(data) and is_time_independent(data):
            return "⧉"
        else:
            return "⧉ₛ"

def is_context_independent(data):
    """True in all possible contexts?"""
    return data in UNIVERSAL_TRUTHS

def is_time_independent(data):
    """True at all times?"""
    return not has_temporal_dependency(data)
```

**Data types:**
- `⧉` is a **certainty boolean**: the data IS or IS NOT irreducible
- `⧉ₛ` can be an **enriched object** containing: value, confidence, source, margin of error

---

### GOLDEN RULE: Epistemic Precautionary Principle

> **IN CASE OF DOUBT → ⧉ₛ**

If you cannot determine with certainty that data is context and time independent, mark it as ⧉ₛ.

**The system is "Safe by Design".**

This rule prevents false certainties. It's better to mark as ⧉ₛ and keep honesty than to force a ⧉ and create hallucination.

---

## 1B. CONFLICT HANDLING

### The Rule of Maximum Honesty

When the model detects **conflicting sources** on the same fact:

**Automatic demotion to ⧉ₛ₍conflict₎**

```python
def handle_conflict(sources):
    """
    If sources contradict, force ⧉ₛ
    """
    if are_contradictory(sources):
        return "⧉ₛ(conflict)"
    else:
        return classify_normally(sources)
```

**Example:**
```
Question: "What is the tallest mountain in France?"
Sources:
- Source A: "Mont Blanc (4,808m)"
- Source B: "Mont Blanc (4,810m)"

Response: "Mont Blanc (~4,809m) [⧉ₛ(conflict)]"
Justification: Measurement variation between sources
```

### Priority Hierarchy in Case of Conflict

1. **Official sources** (governments, international organizations) > Media
2. **Primary sources** (original studies) > Secondary sources (summaries)
3. **Recent** > Old (for temporal data)

---

## 1C. TRACEABILITY & SOURCES

### The Three Pillars of FID Compliance

For the system to be considered **"FID-Compliant"**, each output must satisfy:

1. **Watertightness** (⧉/⧉ₛ separation)
2. **Honesty** (doubt → ⧉ₛ by default)
3. **Traceability** (source origin)

### Full Traceability Format

```json
{
  "data": "Paris is the capital of France",
  "status": "⧉",
  "source": {
    "type": "model_knowledge",
    "origin": "training_corpus",
    "confidence": 1.0
  }
}
```

```json
{
  "data": "Current Bitcoin price: $45,230",
  "status": "⧉ₛ",
  "source": {
    "type": "external_source",
    "origin": "CoinMarketCap API",
    "timestamp": "2026-01-30T14:23:11Z",
    "confidence": 0.95
  }
}
```

```json
{
  "data": "User's preferred coffee: Arabica",
  "status": "⧉ₛ",
  "source": {
    "type": "user_input",
    "origin": "conversation_history",
    "context_id": "conv_abc123",
    "confidence": 0.80
  }
}
```

### The Three Source Types

**1. model_knowledge**
- Information from training
- Generally ⧉ if verified facts
- ⧉ₛ if outdated or uncertain

**2. external_source**
- Real-time API data
- Web searches
- Almost always ⧉ₛ (temporal data)

**3. user_input**
- User preferences
- Conversation context
- Always ⧉ₛ (subjective/variable)

---

## 1D. MIGRATION MECHANISM (⧉ₛ → ⧉ AND ⧉ → ⧉ₛ)

### Promotion: ⧉ₛ → ⧉

A piece of data can transition from ⧉ₛ to ⧉ if:
- Validated by **multiple independent sources**
- Integrated into **scientific consensus**
- Remains **stable over time** (≥5 years for scientific data)

**Note:** The complete migration mechanism through community challenge and collective validation is detailed in **Segment 3: Migration and Feedback**.

### Demotion: ⧉ → ⧉ₛ

A piece of data must be downgraded from ⧉ to ⧉ₛ if:
- **Contradictory evidence** appears
- **Scientific debate** opens
- **Standard or definition revision**

---

## 1E. PRACTICAL IMPLEMENTATION

### Query Processing Flow

```python
class FIDProcessor:
    """
    FID epistemic processor
    """
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.source_validator = SourceValidator()
    
    def process_query(self, user_input):
        """
        Main processing with epistemic marking
        """
        # 1. Generate raw response (existing LLM)
        raw_response = self.llm.generate(user_input)
        
        # 2. Extract factual claims
        claims = self.extract_claims(raw_response)
        
        # 3. Classify each claim
        annotated_claims = []
        for claim in claims:
            status = self.classify_claim(claim)
            source = self.identify_source(claim)
            annotated_claims.append({
                "claim": claim,
                "status": status,
                "source": source
            })
        
        # 4. Reconstruct annotated response
        final_response = self.rebuild_with_markers(
            raw_response, 
            annotated_claims
        )
        
        return final_response
    
    def classify_claim(self, claim):
        """
        ⧉ vs ⧉ₛ classification
        """
        # Test universal stability
        if self.is_universal_truth(claim):
            return "⧉"
        
        # Check for conflicts
        sources = self.get_sources(claim)
        if self.has_conflicts(sources):
            return "⧉ₛ(conflict)"
        
        # Default: if doubt
        return "⧉ₛ"
    
    def is_universal_truth(self, claim):
        """
        Contextual and temporal independence test
        """
        return (
            self.is_mathematical_truth(claim) or
            self.is_physical_constant(claim) or
            self.is_verified_fact(claim)
        )
```

### Usage Example

```python
processor = FIDProcessor()

query = "What is the capital of France and what's the weather there?"

response = processor.process_query(query)

# Output:
# "The capital of France is Paris [⧉].
#  Current weather: 15°C, cloudy [⧉ₛ - temporal data]"
```

---

## 1F. INTEGRATION WITH EXISTING SYSTEMS

### Non-Invasive Approach

The FID can be deployed as:

**1. Post-processing layer**
```python
def fid_wrapper(llm_function):
    """
    Wraps any LLM without modifying it
    """
    def wrapped(*args, **kwargs):
        raw_output = llm_function(*args, **kwargs)
        annotated_output = FIDProcessor().annotate(raw_output)
        return annotated_output
    return wrapped

# Usage:
my_llm_with_fid = fid_wrapper(my_existing_llm)
```

**2. API middleware**
- Intercepts API responses
- Adds ⧉/⧉ₛ markers
- Returns enriched JSON

**3. Fine-tuning module**
- Trains model to natively produce markers
- Deeper integration
- Better performance

---

## 1G. QUALITY METRICS

### KPIs for FID-Compliant System

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Hallucination rate** | 0% on marked zones | Manual audit on sample |
| **Marking precision** | >95% | Expert validation |
| **⧉ vs ⧉ₛ ratio** | Variable by domain | Automatic tracking |
| **User trust** | Measurable increase | Satisfaction surveys |

### Audit Example

```python
def audit_fid_compliance(responses, expert_validations):
    """
    Measures FID compliance on sample
    """
    correct_markings = 0
    total = len(responses)
    
    for response, validation in zip(responses, expert_validations):
        if response.status == validation.expected_status:
            correct_markings += 1
    
    precision = correct_markings / total
    return precision

# Target: precision > 0.95
```

---

## PROTOCOL CONCLUSION

The FID protocol is designed to be:

1. **Universal** - Applicable to any LLM
2. **Non-invasive** - No architectural modification
3. **Scalable** - From prototype to production
4. **Measurable** - Clear quality KPIs
5. **Evolvable** - ⧉ₛ → ⧉ migration over time

**Binary compliance:**

A system is **FID-Compliant** if and only if it satisfies the **three pillars**:
- ✅ Watertightness (⧉/⧉ₛ separation)
- ✅ Honesty (⧉ₛ by default in doubt)
- ✅ Traceability (explicit sources)

**One missing pillar = non-compliant system.**

---

*"Honesty is not a weakness, it's a structured data format."*

---

**→ Next: [Segment 2 - Processing and Modulation](#)**

## ⚖️ Legal Notices & Intellectual Property

This document is an official component of the **Deterministic AI Framework (FID)**, based on the **Theorem of the Unnameable [⧉ / ⧉ₛ]**.

* **INPI e-Soleau Deposit:** n° `DSO2025030113`
* **Scientific Certification:** [Zenodo ID: 18146650](https://zenodo.org/records/18146650)
* **Source Repository:** [GitHub - OthoXIII/theoreme-innommables](https://github.com/OthoXIII/theoreme-innommables)
* **License:** [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 
    *(Attribution - NonCommercial - ShareAlike)*

> **Note:** Any commercial exploitation, SaaS integration, or use within proprietary AI infrastructure without prior written agreement is strictly prohibited. Educational use and contribution to the open-source ecosystem are encouraged subject to citation and license maintenance.

---
Contact: JeromeGaridel@outlook.fr
