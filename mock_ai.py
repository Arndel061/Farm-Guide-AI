def get_remedy(prompt):
    if "yellowing leaves" in prompt.lower():
        return "The yellowing leaves may be due to nitrogen deficiency. Apply urea or compost manure."
    elif "insect holes" in prompt.lower():
        return "Use neem oil or ash water spray to control the insects."
    else:
        return "Please provide more details about the problem, like crop type and symptoms."
