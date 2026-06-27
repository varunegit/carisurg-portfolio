# AI Tiage Risk Register

| Risk Name | Category | Likelihood | Impact | Mitigation | Signal of Success |

| Incomplete Patient Information | AI-Technical | Medium | Medium - During busy periods, patients records may be incomplete before the AI generates a recommendation | High - Missing information can cause the AI to miscalculate the patient's severity and assign an incorrect triage level. | Less that 2% of AI assessments are completed with missing required clinical information during audits |
| Clinical Guideline Drift | AI-Technical | Medium - Hospital triage guidelines can change while the AI continues using outdated decision patterns | High - AI recommendations may no longer align with current clinical practices, increasing the risk of incorrect triage decisions. | The AI team will review the model after every guideline change | Updated model is validated and redeployed within 15 days of a guideline revision. |
