import pandas as pd
text = """
Investigation by Journal/Publisher,13434
Notice - Limited or No Information,11054
Unreliable Results,8887
Concerns/Issues About Data,8143
Investigation by Third Party,7416
Concerns/Issues about Referencing/Attributions,6139
Concerns/Issues with Peer Review,5161
Breach of Policy by Author,4730
Fake Peer Review,4652
Paper Mill,3897
Concerns/Issues About Results,3877
Withdrawal,3773
Duplication of Image,3729
Randomly Generated Content,3440
Duplication of Article,3270
Euphemisms for Plagiarism,2881
Investigation by Company/Institution,2713
Plagiarism of Article,2459
Plagiarism of Text,2148
Misconduct by Author,1765
Error in Data,1686
Rogue Editor,1621
Falsification/Fabrication of Data,1611
Concerns/Issues About Image,1599
Original Data not Provided,1591
Unreliable Data,1472
Lack of IRB/IACUC Approval,1452
Misconduct - Official Investigation/Finding,1439
Author Unresponsive,1411
Concerns/Issues About Authorship,1394
Error in Results and/or Conclusions,1312
Error in Analyses,1219
Manipulation of Images,1117
Error in Methods,1056
Euphemisms for Duplication,928
Objections by Author(s),878
Retract and Replace,874
Results Not Reproducible,846
Notice - No/Limited Information,831
False/Forged Authorship,820
Error in Image,741
Objections by Third Party,734
Duplicate Publication through Error by Journal/Publisher,719
Error by Journal/Publisher,710
Copyright Claims,665
Error in Text,644
Ethical Violations by Author,641
Duplication of Data,627
Informed/Patient Consent - None/Withdrawn,611
Lack of Approval from Author,527
Withdrawn to Publish in Different Journal,494
Falsification/Fabrication of Image,490
Concerns/Issues about Third Party Involvement,472
Duplication of Text,449
Plagiarism of Image,418
Concerns/Issues about Human Subject Welfare,417
Conflict of Interest,391
Withdrawn (out of date),361
Lack of Approval from Third Party,340
Notice - Lack of,333
Taken from Dissertation/Thesis,313
Plagiarism of Data,310
Investigation by ORI,279
Lack of Approval from Company/Institution,256
Unreliable Image,196
Notice - Unable to Access via current resources,178
Error in Materials (General),176
False Affiliation,135
Doing the Right Thing,135
Cites Retracted Work,129
Contamination of Cell Lines/Tissues,118
Falsification/Fabrication of Results,111
Legal Reasons/Legal Threats,98
Miscommunication by Author,92
Bias Issues or Lack of Balance,87
Error in Cell Lines/Tissues,82
Publishing Ban,81
Complaints about Author,75
Criminal Proceedings,72
Contamination of Materials (General),63
Temporary Removal,51
Misconduct by Third Party,43
Transfer of Copyright/Ownership,41
Error by Third Party,40
Manipulation of Results,40
Ethical Violations by Third Party,29
Civil Proceedings,28
Salami Slicing,26
Objections by Company/Institution,26
Updated to Retraction,23
Euphemisms for Misconduct,22
Taken via Peer Review,20
Not Presented at Conference,20
Miscommunication by Journal/Publisher,18
Contamination of Reagents,18
Hoax Paper,15
Miscommunication by Third Party,12
Nonpayment of Fees/Refusal to Pay,10
Miscommunication by Company/Institution,10
Concerns/Issues about Animal Welfare,9
Misconduct by Company/Institution,8
Complaints about Third Party,7
No Further Action,7
Updated to Correction,4
Complaints about Company/Institution,4
Sabotage of Materials,1"""

reliability = ["Bias", "Randomly", "Error in Data", "Falsification/Fabrication", "Results", "Unreliable", "Concerns/Issues About Image", "Error in Image", "Error by Third Party", "Error in Analyses", "Error in Cell Lines/Tissues", "Error in Data", "Contamination", "Materials", "Error in Text", "Methods", "Cites Retracted", "Contamination", "Original Data not Provided", "Sabotage", "Concerns/Issues About Data", "Manipulation", "Peer Review", "Paper Mill", "Hoax Paper", "Retract and Replace", "Updated to Retraction", "False/Forged Authorship"]

# Create a dictionary to store the number of retractions by reason
retractions_by_reason = {}

def check_for_reliability(reason):
    if any(keyword in reason for keyword in reliability):
        return True
    return False

# Categorize each retraction by category
# Ensures that a retraction is only counted once in a category but allows for multiple categories

# Print all the reasons that were not categorized
printed_already = []
for line in text.split('\n'):
    reason = line.split(',')[0]
    reason = reason.strip()
    if check_for_reliability(reason):
        print(reason)
        printed_already.append(reason)

print("Not categorized:")

for line in text.split('\n'):
    reason = line.split(',')[0]
    reason = reason.strip()
    if reason not in printed_already:
        print(reason)
