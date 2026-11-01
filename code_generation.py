
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def code_generation(topic: str):

    parser = StrOutputParser()

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        temperature=0
    )

    chain = llm | parser

    result = chain.invoke(
        f"""
        Build a professional, modern portfolio website for a {topic}.

        Requirements:
        - Return complete HTML5 code.
        - Include CSS inside <style>.
        - Include JavaScript inside <script>.
        - Make the website responsive.
        - Use modern UI design.
        - Return only HTML code.
        - No Markdown code fences.
        - No explanations.
        """
    )

    return result.strip()
