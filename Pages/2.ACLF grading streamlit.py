# ACLF Classification Script

def classify_aclf(bilirubin, creatinine, crrt, circulation, inr, he_grade, respiratory):
    # Determine organ failures
    liver_failure = bilirubin > 205
    kidney_failure = creatinine > 175 or crrt == "yes"
    circulation_failure = circulation == "yes"
    coagulation_failure = inr > 2.5
    brain_failure = he_grade >= 3
    respiratory_failure = respiratory == "yes"

    # Count failing organs
    total_failing = sum([liver_failure, kidney_failure, circulation_failure,
                         coagulation_failure, brain_failure, respiratory_failure])

    # Classification logic
    if total_failing == 0:
        return "ACLF-0"
    elif total_failing == 1:
        # Check for brain and kidney
        if kidney_failure:
            return "ACLF-1"
        elif brain_failure:
            if 133 <= creatinine <= 175:
                return "ACLF-1"
            elif creatinine < 133:
                return "ACLF-0"
        else:  # Any single organ failure not being kidney or brain
            if 133 <= creatinine <= 175:
                return "ACLF-1"
            elif creatinine < 133 and he_grade == 0:
                return "ACLF-0"
            elif he_grade > 0:
                return "ACLF-1"
    elif total_failing == 2:
        return "ACLF-2"
    else:
        return "ACLF-3"

# Example of running the classification
result = classify_aclf(bilirubin=100, creatinine=43, crrt="no", circulation="no", inr=3.0, he_grade=0, respiratory="no")
print("ACLF Classification:", result)
