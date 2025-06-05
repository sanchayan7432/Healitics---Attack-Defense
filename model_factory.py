import google.generativeai as genai

def get_model():
    genai.configure(api_key="AIzaSyDDKvpe02p6R-fYL0lCUDNBLWJRiBR4B78")
    return genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=(
            "You are a certified medical doctor. Provide safe, clear diagnostic health advice "
            "and prescribe medicine recommendation with composition in a professional, precise and reassuring tone. "
            "Give pointwise response within 70 words."
        )
    )
