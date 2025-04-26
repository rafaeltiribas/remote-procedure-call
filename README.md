# Remote Procedure Call (RPC) with RPyC

This project implements a basic remote procedure call (RPC) system using the Python library **RPyC**.

## Project Structure

```
rpc-trabalho/
├── client/
│   └── client.py          # Client-side implementation
├── server/
│   └── server.py          # Server-side implementation
├── tests/
│   └── test_connection.py # Basic connection test
├── README.md              # Instructions
├── RELATORIO.md           # Detailed project report (in Portuguese)
├── requirements.txt       # Project dependencies
└── .gitignore             # Git ignored files
```

## Requirements

- Python 3.8+
- RPyC library

Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

First, start the server:

```bash
python server/server.py
```

Then, in another terminal, run the client:

```bash
python client/client.py
```

Make sure the server is running before starting the client.

## Notes

- The project was built as part of an academic assignment.
- Detailed explanations, task division, and results are available in the `RELATORIO.md` file (in Portuguese).
- If running on different machines, ensure proper network configurations and firewall permissions.
```
