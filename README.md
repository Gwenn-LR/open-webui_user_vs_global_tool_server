# Description

This repository is only a reference to demonstrate an issue with `Open WebUI` while setting up Global Tool Servers. It appears that while User Tool Servers and Global Tool Servers are supposed to function the same way once the latter does not show information about the answer, while the former does.

EDIT :
After some debug, I've found the difference in the JSON response from the `Open-WebUI` backend lacks the field `sources`, so this repository might be overkill but it correspond to my minimal reproductible project and can be usefull for other issues or others developpers. Therefore, I'll keep it that way for now.

# Setup

> ```bash
> docker volume create open-webui
> docker compose up
> docker exec -ti open-webui_user_vs_global_tool_server-ollama-1 ollama pull mistral:7b
> ```

# Reproduce

One the stack is created and setup, other configurations will be done in the `Open WebUI` interface :
- Setup the admin account.
- Create the Global Tool Server.
![alt text](<assets/Global Tool Servers.png>)
- Add it to the Model associated to `mistral:7b`
![alt text](<assets/Setup model.png>)
- Toggle it in the current chat.
![alt text](<assets/Toogle tool.png>)
- Prompt somethink like "Based on the generate_code tool, return the generated code without any other information.".
![alt text](<assets/Global Tool Servers answer.png>)
- Create a new chat (Global Tool Server is deactivated y default)
- Create a User Tool Server
![alt text](<assets/User Tool Servers.png>)
- Prompt the same text.
![alt text](<assets/User Tool Servers answer.png>)

We can see that there is a bubble with information, that was not there with Global Tool Server. This bubble seems to correspond to the `Open-WebUI` backend JSON key `sources` that is not present when using a Global Tool Server vs User Tool Server.

`Open-WebUI` backend response with Globale Tool Server:
![alt text](<assets/Global Tool Servers answer JSON.png>)

`Open-WebUI` backend response with User Tool Server:
![alt text](<assets/User Tool Servers answer JSON.png>)