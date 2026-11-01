from e2b import Sandbox
from dotenv import load_dotenv

load_dotenv()
def test_code_generation(html_code: str):
    sandbox = Sandbox.create(
        network={
            "allow_public_traffic": True
        }
    )

    html = html_code

    sandbox.files.write("/home/user/index.html", html)

    sandbox.commands.run(
        "python -m http.server 8080 --directory /home/user",
        background=True
    )

    url = f"https://{sandbox.get_host(8080)}"

    return url