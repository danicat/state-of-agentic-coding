Your task is to create a Model Context Protocol (MCP) server to expose a “hello_world” tool. For the MCP implementation, you should use the official Go SDK for MCP and use the stdio transport. When called, this tool should return the string "Hello, MCP World!"

## TO DO
- Get package github.com/modelcontextprotocol/go-sdk/mcp (official SDK)
- Create the server with stdio transport
- Create one tool "hello_world" that returns the message "Hello, MCP World!"
- Build the server as "./bin/server"
- Create a client that connects with the server over stdio
- The client should have a flag --list-tools to list all available tools in the server
- The client should have a flag --call-tool to call a tool by name
- Build the client as "./bin/client"

## Acceptance Criteria
- Command `./bin/client --list-tools` must succeed (must have: stdout containing `hello_world`).
- Command `./bin/client --call-tool hello_world` must succeed (must have: stdout containing `Hello, MCP World!`).