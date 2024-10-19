import streamlit as st

def replace_terms(full_term):
    """
    Replace specific terms and suffixes with their full forms.
    
    :param full_term: A string containing the term.
    :return: The term with replacements applied.
    """
    replacements = {
        "-KG": " KILOGRAMS",
        "-LB": " POUNDS",
        "HORIZONTAL CG": "Horizontal Center of Gravity",
        "-MM": " MILLIMETERS",
        "-IN": " INCHES",
        "-PSI": " pounds per square inch",
        "-GPM": " Gallons Per Minute",
        "-LPM": " Liters Per Minute",
        "-QTY": " QUANTITY"
    }
    
    for key, value in replacements.items():
        full_term = full_term.replace(key, value)
    
    return full_term

def generate_abbreviations(full_term):
    """
    Generate alternate abbreviations or variations for any given term.
    
    :param full_term: A string representing the term (e.g., "Horizontal Center of Gravity").
    :return: A list of variations (abbreviations).
    """
    # First replace any special terms or suffixes
    full_term = replace_terms(full_term)
    
    # Split the full term into words
    words = full_term.split()
    
    # List to store the variations
    variations = []
    
    # 1. Full form
    variations.append(full_term)
    
    # Filter out common words like "of", "the", etc.
    filtered_words = [word for word in words if word.lower() not in ['of', 'the', 'and']]
    
    # 2. Initial abbreviations (e.g., "HCG")
    initials = ''.join([word[0].upper() for word in filtered_words])
    variations.append(initials)
    
    # 3. Mixed abbreviations:
    # "Horizontal CG", "H Center of Gravity", "H C Gravity", "H C G"
    if len(filtered_words) > 1:
        # Variation: "Horizontal CG"
        variations.append(f"{filtered_words[0]} {initials[1:]}")
        
        # Variation: "H Center of Gravity"
        if len(filtered_words) > 2:
            variations.append(f"{initials[0]} {filtered_words[1]} {filtered_words[2]}")
        
        # Variation: "H C Gravity"
        for i in range(1, len(filtered_words)):
            partial_abbr = ' '.join([word[0].upper() for word in filtered_words[:i]]) + ' ' + ' '.join(filtered_words[i:])
            variations.append(partial_abbr)
        
        # Variation: "H C G" (only initials)
        variations.append(' '.join([word[0].upper() for word in filtered_words]))
    
    return variations


# Streamlit App
st.title("Term Abbreviation Generator")

st.write("Enter a term to generate its abbreviations and variations:")

# Create a form with a submit button
with st.form(key='term_form'):
    # User input for the term
    term_input = st.text_input("Input Term", value="")
    
    # Submit button
    submit_button = st.form_submit_button(label="Submit")

# Check if the form is submitted
if submit_button and term_input:
    st.write(f"Original term: {term_input}")
    
    # Generate abbreviations
    abbreviations = generate_abbreviations(term_input)
    
    st.write("Generated abbreviations/variations:")
    
    # Display abbreviations
    for abbr in abbreviations:
        st.write(f"- {abbr}")
