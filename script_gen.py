import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def generate_script(occasion, name, details, rudeness):
    """
    Generates a structured and humorous monologue script using Google Gemini API.

    Parameters:
        - occasion (str): Type of script (e.g., "Break Up", "Quit Job")
        - name (str): Name of the person
        - details (str): Basic reason
        - rudeness (int): Scale from 1 (polite) to 10 (savage)

    Returns:
        - Generated script (str)
    """
    prompt = f"""
    You are an AI that writes scripts for difficult conversations in a humorous tone.

    **Scenario:** {occasion}  
    **Target Person:** {name}  
    **Reason:** {details}  
    **Rudeness Level:** {rudeness} (1 = very polite, 10 = brutally direct)  

    Please generate a **first-person speech** that the user will say **directly to {name}**.  
    The message should:
    - Start with a **soft opening** or a joke (if appropriate).  
    - Clearly state the reason in a **concise, natural, and humorous way**.  
    - End with a **smooth exit line** (e.g., "I wish you the best").  

    Format the response as a **full paragraph** that the user can read aloud.
    """

    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)

    return response.text if response else "Failed to generate script."

