from language_tool_python import LanguageTool

# Initialize the LanguageTool instance
def check_auth(text):
    tool = LanguageTool('en-US')
    # Check the grammar
    matches = tool.check(text)

    # Print the grammar errors and suggested replacements
    # if len(matches) > 0:
    #     print("Grammar errors found:")
    #     for match in matches:
    #         print("Error:", match.ruleId)
    #         print("Suggested replacement:", match.replacements)
    # else:
    #     print("No grammar errors found.")
    # # Count the number of errors
    error_count = len(matches)

    # Calculate the percentage of errors
    total_words = len(text.split())
    error_percentage = (error_count / total_words) * 100

    if error_percentage >= 10.0:
        return 0
    else:
        return 1

# print(check_auth("Maharashtra chief minister Eknath Shinde has appealed to the masses to cooperate for the restoration of peace after violence in Kolhapur district on Tuesday. Normalcy returned late in the afternoon and evening as there was regular traffic, though vehicles were fewer, around Shivaji Chowk and the KMC main building nearby. Almost 90% of shops, trade and business establishments remained shut."))