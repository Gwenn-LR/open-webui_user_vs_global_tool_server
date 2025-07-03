from asyncio import sleep
from fastmcp import FastMCP


mcp = FastMCP(name="Open WebUI User vs Gloabl tool server behaviour", stateless_http=True, port=8082)


@mcp.tool()
async def generate_code() -> dict:
    """A generation tool which create a code.

    Returns:
        dict: The generation result.
    """
    await sleep(2)

    return {
        "code": "qsohfqsdljgndqs;nbgdqsyfZORTF",
        "source": "# Me"
    }


if __name__ == "__main__":
    mcp.run("sse")
