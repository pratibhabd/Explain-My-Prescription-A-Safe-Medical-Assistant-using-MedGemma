# 💊 Explain My Prescription

## 👩‍💻 Team 0

**Pratibha Kambi**  
Role: End-to-End Developer  
Specialty: AI / Machine Learning, LLM-based Applications  

### Contributions
- Use-case ideation and healthcare problem framing  
- Model selection and local deployment using MedGemma  
- Prompt design for safe, deterministic medical explanations  
- Streamlit UI development and local inference integration  
- Evaluation framework and safety scoring design  

---

# 🩺 Problem Statement

Patients are often prescribed medications with minimal explanation due to time constraints in clinical environments. This leads to confusion, anxiety, improper usage, and reduced adherence to treatment plans—especially in settings with limited internet access or healthcare staff availability.

Most existing AI solutions rely on large, closed models hosted in the cloud, making them unsuitable for privacy-sensitive healthcare environments or low-connectivity regions.

---

# 🌍 Impact Potential

This project improves patient education and communication by enabling individuals to understand:

- Why a medicine was prescribed  
- How it works in simple terms  
- General dosage guidance  
- Common side effects and warning signs  

The solution empowers patients while preserving privacy and can be deployed in clinics, pharmacies, or rural healthcare setups without reliance on cloud infrastructure.

---

# 👥 Target Users & Unmet Need

## Primary Users

- Patients receiving new prescriptions  
- Elderly individuals managing multiple medications  
- Pregnant or breastfeeding patients needing extra clarity  
- Rural patients with limited pharmacist interaction  
- Pharmacies seeking scalable patient education tools  

## Unmet Need

While printed medication leaflets are widely available, they are:

- Dense and difficult to understand  
- Not personalized to patient age or condition  
- Not contextualized to specific prescription scenarios  

In busy clinical settings, pharmacists and doctors may not have sufficient time to provide detailed explanations.

AI is appropriate here because it enables:

- Context-aware explanation  
- Simplified language adaptation  
- Special-condition acknowledgement  
- On-demand clarification  

The system is designed to **augment**, not replace, healthcare professionals.

---

# 🧠 Overall Solution

The solution uses **MedGemma**, an open-weight healthcare-focused language model from Google’s HAI-DEF collection, to generate reliable and context-aware explanations of prescribed medicines.

MedGemma is deployed locally, giving full control over:

- Model behavior  
- Prompt structure  
- Inference safety (deterministic decoding)  
- Infrastructure and data flow  

By avoiding external APIs and centralized servers, the system aligns with the HAI-DEF philosophy of adaptable, privacy-focused AI tools that can run wherever care is delivered.

The model is prompted to produce educational, non-diagnostic outputs, ensuring responsible and safe use in a healthcare context.

---

# ⚙️ Technical Details

**Model:** Google MedGemma (open-weight, healthcare-specific)  
**Deployment:** Fully local inference (CPU-based)  
**Frontend:** Streamlit Web Interface  

## Inputs

- Medicine name  
- Dosage/strength  
- Frequency (optional)  
- Patient age  
- Special condition (optional)  

## Outputs

- Purpose of the medicine  
- How it works  
- Typical usage information  
- Common side effects  
- When to consult a doctor  

## Key Technical Design Choices

- Deterministic generation (`temperature = 0`) to reduce hallucinations  
- Controlled token length  
- Clear medical disclaimers  
- Rule-based post-generation validation  
- No storage or transmission of patient data  
- Offline capability after initial model download  

The application is lightweight, easy to deploy, and suitable for real-world healthcare environments.

---

# 🤖 Why MedGemma?

MedGemma was chosen because it is an open-weight, healthcare-focused language model designed specifically for medical and life sciences use cases.

Unlike general-purpose LLMs, MedGemma:

- Handles clinical terminology more reliably  
- Produces context-aware medical explanations  
- Aligns better with healthcare safety requirements  

Its open-weight nature allows:

- Full local deployment  
- Model transparency  
- Infrastructure independence  
- Privacy preservation  

---

# 🎯 Effective Use of HAI-DEF Models

MedGemma is used as a domain-specialized healthcare reasoning model rather than a generic text generator.

This project leverages MedGemma’s strengths in:

- Understanding medical terminology  
- Handling clinical context  
- Producing structured instructional outputs  
- Operating within healthcare safety boundaries  

Compared to general-purpose LLMs, MedGemma reduces the likelihood of:

- Informal or non-clinical phrasing  
- Unnecessary alternative treatment suggestions  
- Speculative outputs  

Its open-weight nature enabled:

- Deterministic decoding control  
- Prompt-level behavioral shaping  
- Post-generation safety validation  
- Full local deployment  

---

# 🏗 System Architecture & Pipeline

The system follows a structured end-to-end pipeline:

## 1️⃣ User Input Collection (Streamlit UI)

- Medicine name  
- Dosage  
- Frequency  
- Patient age  
- Special conditions  

## 2️⃣ Prompt Construction

- Structured medical prompt template  
- Embedded safety constraints  
- Explicit prohibition of diagnosis or dosage modification  

## 3️⃣ Model Inference

- MedGemma 4B (local inference)  
- Deterministic decoding  
- Controlled max token length  

## 4️⃣ Post-Processing

- Rule-based safety validation  
- Hallucination detection  
- Special-condition acknowledgement check  

## 5️⃣ Structured Output Delivery

- Enforced headings  
- Patient-friendly language  
- No personal data storage  

---

# 📊 Impact Estimation

Medication non-adherence is widely recognized as a contributor to avoidable healthcare complications and costs.

If deployed in pharmacy or clinic workflows, this system could:

- Improve patient comprehension at point of dispensing  
- Reduce clarification calls  
- Reduce anxiety-driven follow-ups  
- Improve safe usage in elderly and pregnancy cases  

Because it runs locally with no subscription infrastructure, it is scalable in rural and resource-constrained settings.

---

# 📚 Dataset Design & Test Case Strategy

A structured synthetic evaluation dataset of **112 test cases** was created:

- **80 valid prescription scenarios**
- **32 invalid or adversarial inputs**

## Coverage Categories

- Adult prescriptions  
- Elderly patients  
- Pregnancy cases  
- Breastfeeding  
- Chronic illness  
- Pediatric context  
- OTC medicines  
- Edge cases  

Each case tested:

- Context conditioning  
- Special-condition awareness  
- Safety constraint adherence  
- Hallucination resistance  

---

# 🧪 Evaluation Strategy

Each response was evaluated across four dimensions:

1. Instruction Following  
2. Safety  
3. Special-Condition Handling  
4. Readability  

Evaluation methods included:

- Rule-based validation  
- Structured keyword detection  
- Manual edge-case review  
- Quantitative scoring aggregation  
- Correlation analysis  

---

# 🧮 Scoring System

| Score | Meaning |
|-------|---------|
| 0 | Failure |
| 1 | Partial / Caution |
| 2 | Fully Compliant |

### Safety
- 0 = Violation  
- 1 = Cautionary  
- 2 = Fully safe  

### Special Condition Handling
- 0 = Missed acknowledgement  
- 1 = Partial  
- 2 = Properly handled  

---

# 📈 Evaluation Findings (80 Valid Cases)

- 100% instruction compliance  
- 12.5% safety violations  
- 67.5% cautionary outputs  
- 20% fully safe outputs  
- 12.5% hallucinated advice  
- 19 missed special-condition acknowledgements  
- Correlation (0.33) between safety and special-condition handling  

---

# 🔍 Failure Analysis & Mitigation

## Observed Weaknesses

- Over-cautious phrasing  
- Missed elderly and pregnancy acknowledgements  
- Verbosity-induced reasoning drift  

## Mitigation Strategies

- Conditional acknowledgement enforcement in prompt  
- Length control (<800 words)  
- Rule-based hallucination filtering  
- Deterministic decoding  

---

# 🔧 Model Adaptation Strategy

The system currently uses structured prompt engineering rather than full fine-tuning.

This was intentional to:

- Preserve MedGemma’s base medical safety priors  
- Avoid catastrophic forgetting  
- Maintain reproducibility  
- Ensure lightweight deployment  

### Future Enhancements

- Supervised fine-tuning on pharmacist-reviewed datasets  
- Instruction tuning on anonymized prescription pairs  
- RLHF for safety optimization  

---

# 🚀 Deployment Feasibility

## Deployment Settings

- Pharmacy desktops  
- Clinic reception systems  
- Rural health center workstations  
- Kiosk-style education terminals  

## Challenges

- Model size constraints  
- Inference latency  
- Need for early oversight  

## Mitigation

- Quantized model variants  
- Edge-device optimization  
- Human-in-the-loop validation  

---

# ⚠ Limitations

- Synthetic evaluation dataset  
- No clinical validation yet  
- Not a diagnostic tool  
- Special-condition handling requires improvement  

---

# 🛡 Ethical & Safety Considerations

- No dosage modification advice  
- No alternative treatment suggestions  
- Clear disclaimers  
- No patient data storage  
- Fully offline after setup  

The assistant augments healthcare communication rather than replacing clinicians.

---

# 📎 Code & Reproducibility

Kaggle Notebook:

🔗 https://www.kaggle.com/code/completeregistratiom/pratibha-kambi  

Includes:

- Model loading & inference pipeline  
- Prompt engineering  
- Structured evaluation framework  
- Safety scoring system  
- Quantitative analysis & visualizations  

---

# 🏁 Conclusion

Explain My Prescription demonstrates that MedGemma, combined with structured prompting and rule-based validation, can generate safe, readable, and instruction-compliant medication explanations in a privacy-preserving environment.

This project highlights the practical potential of open-weight healthcare AI to improve patient understanding and medication adherence without reliance on cloud infrastructure.
