#!/usr/bin/env python3
"""Open-Dispatch / Catchup main entry point.

Run web server:
  python main.py
Or run CLI commands:
  python main.py cli send --platforms twitter,bluesky --text "hello"
"""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        from cli import main as cli_main
        sys.argv.pop(1)
        sys.exit(cli_main())
    else:
        import uvicorn
        uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=True)

