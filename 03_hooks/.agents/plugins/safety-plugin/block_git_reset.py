#!/usr/bin/env python3
import sys
import json

def main():
    try:
        with open("/Users/petruzalek/projects/state-of-agentic-coding/03_hooks/debug_hook.log", "w") as f:
            f.write("Hook script invoked!\n")
    except Exception:
        pass

    try:
        data = json.load(sys.stdin)
    except Exception as e:
        # If we cannot parse JSON, we fall back to allowing but log a reason
        print(json.dumps({"decision": "allow", "reason": f"Failed to parse input: {e}"}))
        return

    tool_call = data.get("toolCall", {})
    tool_name = tool_call.get("name")
    args = tool_call.get("args", {})
    command_line = args.get("CommandLine", "")

    # Check if command is git reset
    if tool_name == "run_command" and command_line.strip().startswith("git reset"):
        response = {
            "decision": "deny",
            "reason": f"Execution of 'git reset' is strictly blocked by the repo's safety hooks. Command attempted: '{command_line}'"
        }
    else:
        response = {
            "decision": "allow"
        }

    print(json.dumps(response))

if __name__ == "__main__":
    main()
