from .code_generation import code_generation
from .testing import test_code_generation

def main():
    output = code_generation("i am an aiml engineer and i am working in a ibm and my name is rishabh soni and i want to create a portfolio with stunning ui and i want to create hosted website")

    url_generation = test_code_generation(output)
    print(f"Portfolio website generated code: {output}")

    print(f"Portfolio website generated and hosted at: {url_generation}")


if __name__ == "__main__":
    main()